SOURCE_FILE = "D:\\temp\\twitter\\tweet.js"
TWITTER_USERNAME = 'roytang'
auto_tags = ["mtg"]
syndicated_sources = ["IFTTT", "Tumblr", "instagram.com", "Mailchimp", "Twitter Web", "TweetDeck", "mtgstorm"]
debug_id = None
# debug_id = "11143081155" 

import frontmatter
import json
import requests
import urllib.request
from urllib.parse import urlparse, parse_qs, urldefrag
from urllib.error import HTTPError
import sys
from pathlib import Path
import os, shutil
import inspect
from datetime import datetime
import re
from utils import loadurlmap, load_map_from_json, URLResolver, PostBuilder

cwd = Path.cwd()
contentdir = cwd / "content"
blogdir = Path(os.environ['HUGO_BLOG_OUTDIR'])
mediadir = Path("D:\\temp\\roy_mtg-twitter\\tweet_media")

retweetscache = load_map_from_json("d:\\temp\\twitter\\retweets.json")

resolver = URLResolver()

def loadurlmap(cleanupdupes=False):
    blogdir = Path(os.environ['HUGO_BLOG_OUTDIR'])
    urlmapfile = blogdir / "urlmap.json"
    urlmap = {}
    urlmapdupes = {}
    with urlmapfile.open(encoding="UTF-8") as f:
        tempurlmap = json.loads(f.read())
        for u in tempurlmap:
            u1 = tempurlmap[u]
            if "syndicated" in u1:
                for s in u1['syndicated']:
                    if 'url' in s:
                        su = s['url']
                        if su in urlmap:
                            # we expect syndicated urls to be unique, 
                            # so if it's already in the map,
                            # it must be a dupe
                            # (This is really just to clean up my own mess!)
                            if su not in urlmapdupes:
                                urlmapdupes[su] = [u1, urlmap[su]]
                            else:
                                urlmapdupes[su].append(u1)
                        else:
                            urlmap[su] = u1
            urlmap[u] = u1
            title = u1.get("title", "").strip()
            if len(title) > 0:
                urlmap[title] = u1
    if cleanupdupes:
        # clean up any found dupes by syndicated url
        for su in urlmapdupes:
            dupes = urlmapdupes[su]
            canonical = None
            for_deletion = []
            for d in dupes:
                if d["source_path"].startswith("post") or d["source_path"].startswith("links") or len(d['syndicated']) > 2:
                    if canonical is not None:
                        print("\n\r##### WTH. More than one canonical urls were detected for %s" % (su))
                        print(json.dumps(dupes, indent=4))
                    canonical = d
                else:
                    for_deletion.append(d)

            if canonical is None:
                print("##### Dupes were detected for %s but no canonical url found!" % (su))
                print(dupes)
            else:
                urlmap[su] = canonical
                for d in for_deletion:
                    source_path = Path(d['source_path'])
                    full_path = contentdir / source_path
                    if full_path.exists():
                        os.remove(str(full_path))
    return urlmap

urlmap = loadurlmap(False)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def add_syndication(mdfile, url, stype):
    with mdfile.open(encoding="UTF-8") as f:
        try:
            post = frontmatter.load(f)
        except:
            print("Error parsing file")
            return

        if post.get('syndicated') == None:
            post['syndicated'] = []
        else:
            for s in post['syndicated']:
                if s["type"] == stype and s["url"] == url:
                    # dont add a duplicate!
                    return

        post['syndicated'].append({
            'type': stype,
            'url': url
        })
        newfile = frontmatter.dumps(post)
        with mdfile.open("w", encoding="UTF-8") as w:
            w.write(newfile)
    
def get_content(t):
    content  = t['full_text']
    if "entities" in t:
        # get raw urls in the text
        raw_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
        # replace mentions with link
        for m in t["entities"]["user_mentions"]:
            screen_name = m["screen_name"]
            # replace with markdown link
            mdlink = "[@%s](https://twitter.com/%s/)" % (screen_name, screen_name)
            content = content.replace("@"+screen_name, mdlink)
        processed_urls = []
        # clean urls
        for u in t["entities"]["urls"]:
            url = u["url"]
            processed_urls.append(url)
            expanded_url = u["expanded_url"]
            processed_urls.append(expanded_url)
            # print("##### A URL!!! %s" % expanded_url)
            expanded_url, no_errors = resolver.get_final_url(expanded_url)
            processed_urls.append(expanded_url)
            content = content.replace(url, expanded_url)

        # find urls that were not in the entities
        for raw_url in raw_urls:
            if raw_url not in processed_urls:
                expanded_url, no_errors = resolver.get_final_url(raw_url)
                content = content.replace(raw_url, expanded_url)

    return content

def create_post(t):
    id = t['id_str']
    d = datetime.strptime(t['created_at'], "%a %b %d %H:%M:%S %z %Y")

    content = get_content(t)
    post = frontmatter.Post(content)
    post['date'] = d
    post['syndicated'] = [
        {
            "type": "twitter",
            "url": "https://twitter.com/%s/statuses/%s/" % (TWITTER_USERNAME, t['id'])
        }
    ]

    kind = "notes"
    if "in_reply_to_status_id_str" in t and "in_reply_to_screen_name" in t:
        kind = "replies"
        post["reply_to"] = {
            "type": "twitter",
            "url": "https://twitter.com/%s/statuses/%s/" % (t['in_reply_to_screen_name'], t['in_reply_to_status_id_str']),
            "name": t["in_reply_to_screen_name"],
            "label": "%s's tweet" % (t["in_reply_to_screen_name"]) 
        }
    elif t["full_text"].startswith("RT @"):
        rc = retweetscache.get(id)
        if rc is None:
            # RTed status is inaccessible, we'll just render it as an ordinary note
            pass
        else:
            if "retweeted_user" in rc:
                kind = "reposts"
                post['repost_source'] = {
                    "type": "twitter",
                    "name": rc["retweeted_user"],
                    "url": "https://twitter.com/%s/statuses/%s/" % (rc['retweeted_user'], rc['retweeted_id'])
                }        
                # dont process reposts for now
                # return False
            else:
                # 785744070027030528 fails this
                # RTed status is inaccessible, we'll just render it as an ordinary note
                pass

    # else:
    #     # dont process others for now
    #     return False

    media = []
    for m in t.get("extended_entities", {}).get("media", []):
        media.append(m["media_url_https"])
    if len(media) > 0:
        if kind != "reposts" and kind != "replies":
            kind = "photos" 
        
        # dont process media for now
        # return False

    tags = []
    for tag in t.get('entites', {}).get('hashtags', []):
        tags.append(tag['text'].lower())

    parsed_tags = re.findall(r"\s#(\w+)", " " + content)
    for tag in parsed_tags:
        if tag not in tags:
            tags.append(tag.lower())

    for tag in auto_tags:
        if tag not in tags:
            tags.append(tag)
    if len(tags) > 0:
        post["tags"] = tags

    post["source"] = "twitter"
    outdir = contentdir / kind / d.strftime("%Y") / d.strftime("%m")
    if len(media) > 0:
        outdir = outdir / (id)

    if not outdir.exists():
        outdir.mkdir(parents=True)

    if len(media) > 0:
        outfile = outdir / ( "index.md" )
        # find photos
        for imgfile in mediadir.glob(id + "*.*"):
            to_file = outdir / imgfile.name
            shutil.copy(str(imgfile), str(to_file))    
    else:
        outfile = outdir / ( id + ".md" )

    newfile = frontmatter.dumps(post)
    with outfile.open("w", encoding="UTF-8") as w:
        w.write(newfile)
    return True

def process_syn_url(d1, raw_url, url):
    orig_tweet_url = "https://twitter.com/%s/statuses/%s/" % (TWITTER_USERNAME, d1['id_str'])

    url, no_errors = resolver.get_final_url(url)
    if not no_errors:
        print(d1["full_text"])

    url = url.replace("www.instagram.com", "instagram.com")
    url = url.replace("/roytang0400", "")
    url = urldefrag(url)[0]
    if url.find("instagram.com") >= 0 and url.find("?") >= 0:
        # remove utm and other misc query params from insta urls
        url = url.split("?")[0]
    if url in urlmap:
        u = urlmap[url]
        source_path = Path(u['source_path'])
        full_path = contentdir / source_path
        add_syndication(full_path, orig_tweet_url, "twitter")
        return True

    if url.find("://roytang.net") >= 0 or url.find("://mtgstorm.com") >= 0:
        link_url = urlparse(url)
        u = urlmap.get(link_url.path, None)
        if u is None:
            # try matching by title
            title_search_term = d1["full_text"]
            title_search_term = title_search_term.replace("New blog post: ", "")
            title_search_term = title_search_term.replace("New post: ", "")
            title_search_term = title_search_term.replace(raw_url, "")
            title_search_term = title_search_term.strip()
            u = urlmap.get(title_search_term, None)
        if u is not None:
            source_path = Path(u['source_path'])
            full_path = contentdir / source_path
            add_syndication(full_path, orig_tweet_url, "twitter")
            return True
        else:
            print("######## Unmatched roytang url: %s" % (url))
            print(d1["full_text"])
            return True

    return False

def process_tweet(d1):

    orig_tweet_url = "https://twitter.com/%s/statuses/%s/" % (TWITTER_USERNAME, d1['id_str'])

    if orig_tweet_url in urlmap:
        og = urlmap.get(orig_tweet_url)
        if og['source_path'].startswith('post\\') or og['source_path'].startswith('photos\\'):
            # no need to process further any tweets that are already mapped to a post
            return True

    tweet_source = d1["source"]
    # print("#### %s: %s" % (tweet_source, orig_tweet_url))
    # detect content syndicated from elsewhere
    # instagram, tumblr, roytang.net
    for s in syndicated_sources:
        if tweet_source.find(s) >= 0:
            for u in d1.get('entities', {}).get("urls", []):
                raw_url = u["url"]
                url = u["expanded_url"]
                if process_syn_url(d1, raw_url, url):
                    return True
                # print("######## URL = %s" % (url))

            # also process raw urls
            raw_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', d1["full_text"])
            for raw_url in raw_urls:
                if process_syn_url(d1, raw_url, raw_url):
                    return True
            break

    return create_post(d1)

def import_all():
    countbysource = {}
    replies = 0
    retweets = 0
    withmedia = 0
    raw = 0

    with Path(SOURCE_FILE).open(encoding='utf-8') as f:
        d = json.load(f)
        idx = 0
        for d1 in d:
            if debug_id is not None and d1["id_str"] != debug_id:
                continue

            if process_tweet(d1):
                continue

            tweet_source = d1["source"]
            if tweet_source not in countbysource:
                countbysource[tweet_source] = 1
            else:
                countbysource[tweet_source] = countbysource[tweet_source] + 1

            is_reply = False
            if "in_reply_to_status_id_str" in d1 and "in_reply_to_screen_name" in d1:
                replies = replies + 1
                is_reply = True

            # handle retweet
            is_retweet = False
            content = d1["full_text"]
            if content.startswith("RT @"):
                retweets = retweets + 1
                is_retweet = True

            media = []
            if "extended_entities" in d1:
                for m in d1["extended_entities"]["media"]:
                    media.append(m["media_url_https"])

            if len(media) > 0:
                withmedia = withmedia + 1

            if not is_reply and not is_retweet and len(media) == 0:
                raw = raw + 1

            idx = idx + 1
            # if idx > 100:
            #     break

    # save the url cache for future use
    resolver.save_cache()

    for source in countbysource:
        print("countbysource: %s = %s" % (source, countbysource[source]))
    print("replies: %s" % (replies))
    print("retweets: %s" % (retweets))
    print("withmedia: %s" % (withmedia))
    print("raw: %s" % (raw))
    print("total: %s" % (idx))

def thread_replies():
    with Path(SOURCE_FILE).open(encoding='utf-8') as f:
        d = json.load(f)
        idx = 0
        # process in reverse order so tweet sequences are in order
        d = reversed(d)
        for d1 in d:
            is_reply = False
            if "in_reply_to_status_id_str" in d1 and "in_reply_to_screen_name" in d1:
                is_reply = True
            if not is_reply:
                continue
            id_str = d1['id_str']
            # if id_str != "602009895437737984" and id_str != "602009747294924802":
            #     continue
            orig_tweet_url = "https://twitter.com/%s/statuses/%s/" % (TWITTER_USERNAME, id_str)
            # dont bother if already syndicated
            if orig_tweet_url in urlmap:
                continue
            date = datetime.strptime(d1['created_at'], "%a %b %d %H:%M:%S %z %Y")
            # process replies to myself
            if d1["in_reply_to_screen_name"] == TWITTER_USERNAME:
                replied_to_url = "https://twitter.com/%s/statuses/%s/" % (d1['in_reply_to_screen_name'], d1['in_reply_to_status_id_str'])
                info = urlmap[replied_to_url]
                source_path = Path(info['source_path'])
                full_path = contentdir / source_path
                # welp, we might as well move them to bundles
                if full_path.name == "index.md":
                    parentdir = full_path.parent
                else:
                    parentdir = full_path.parent / full_path.stem
                    if not parentdir.exists():
                        parentdir.mkdir(parents=True)
                    oldfile = full_path
                    full_path = parentdir / "index.md"
                    shutil.move(str(oldfile), str(full_path))
                    # also update the urlmap!
                    urlmap[replied_to_url]['source_path'] = str(full_path.relative_to(contentdir))
                # append the reply to the original post, and add it as a syndication as well
                with full_path.open(encoding="UTF-8") as f:
                    try:
                        post = frontmatter.load(f)
                    except:
                        print("Error parsing file")
                        return
                    post['syndicated'].append({
                        'type': 'twitter',
                        'url': orig_tweet_url
                    })
                    content = get_content(d1)
                    post.content = post.content + "\n\r" + content
                    newfile = frontmatter.dumps(post)
                    with full_path.open("w", encoding="UTF-8") as w:
                        w.write(newfile)
                # copy over any media from the reply as well
                media = []
                for m in d1.get("extended_entities", {}).get("media", []):
                    media.append(m["media_url_https"])
                for imgfile in mediadir.glob(d1["id_str"] + "*.*"):
                    to_file = parentdir / imgfile.name
                    shutil.copy(str(imgfile), str(to_file))    
                # delete any existing file created for this reply
                oldfile = contentdir / "replies" / date.strftime("%Y") / date.strftime("%m") / (id_str + ".md")
                if oldfile.exists():
                    os.remove(str(oldfile))
                oldfolder = contentdir / "replies" / date.strftime("%Y") / date.strftime("%m") / (id_str)
                if oldfolder.exists():
                    shutil.rmtree(str(oldfolder))
                # replace this entry in the urlmap! this is so that succeeding replies can find the correct root tweet to attach to
                urlmap[orig_tweet_url] = info
            else:
                continue

            idx = idx + 1
        print(idx)

from utils import urlmap_to_mdfile

def cleanup_videos():
    with Path(SOURCE_FILE).open(encoding='utf-8') as f:
        d = json.load(f)
        idx = 0
        for d1 in d:
            orig_tweet_url = "https://twitter.com/%s/statuses/%s/" % (TWITTER_USERNAME, d1["id_str"])
            info = urlmap.get(orig_tweet_url)
            if info is None:
                continue
            for m in d1.get("extended_entities", {}).get("media", []):
                if "video_info" in m:
                    videos = []
                    lowest_bitrate = 1000000000000
                    lowest_video = ""
                    for vi in m["video_info"]["variants"]:
                        if 'bitrate' in vi:
                            videos.append(vi["url"])
                            bitrate = int(vi['bitrate'])
                            if bitrate < lowest_bitrate:
                                lowest_video = vi["url"]
                                lowest_bitrate = bitrate
                    
                    mdfile = urlmap_to_mdfile(info)
                    if str(mdfile).find("\\photos\\") >= 0:
                        print(mdfile)
                        # move it to notes, since it's not a photo
                        p = PostBuilder.from_mdfile(mdfile)
                        p.kind = "notes"
                        p.save() 
                        # delete the old files
                        container = mdfile.parent
                        for f in container.iterdir():
                            os.remove(str(f))
                        container.rmdir()
                    continue
                    # delete all the video files except for the one with the lowest bitrate
                    for v in videos:
                        if v == lowest_video:
                            continue
                        name = Path(v).name
                        if name.find("?") >= 0:
                            name = name.split("?")[0]
                        vfilename = d1["id_str"] + "-" + name
                        vfile = container / vfilename
                        print(vfile)
                        os.remove(str(vfile))
                    

# thread_replies()
# import_all()

cleanup_videos()
