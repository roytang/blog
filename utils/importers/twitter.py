SOURCE_FILE = "D:\\temp\\twitter\\tweet.js"
OUTPUT_DIR = "D:\\repos\\blog\\content\\aside\\"
TWITTER_USERNAME = 'roytang'

import frontmatter
import json
import requests
import urllib.request
from urllib.parse import urlparse, parse_qs, urldefrag
from urllib.error import HTTPError
import sys
from pathlib import Path
import os
import inspect
from datetime import datetime

urlcachefile = Path("d:\\temp\\twitter\\urlcache.json")
urlcache = {}
if urlcachefile.exists():
    with urlcachefile.open(encoding="UTF-8") as f:
        urlcache = json.loads(f.read())

blogdir = Path(os.environ['HUGO_BLOG_OUTDIR'])
urlmapfile = blogdir / "urlmap.json"
urlmap = {}
with urlmapfile.open(encoding="UTF-8") as f:
    tempurlmap = json.loads(f.read())
    for u in tempurlmap:
        u1 = tempurlmap[u]
        if "syndicated" in u1:
            for s in u1['syndicated']:
                if 'url' in s:
                    su = s['url']
                    urlmap[su] = u1
        urlmap[u] = u1

cwd = Path.cwd()
contentdir = cwd / "content"

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_final_url(url):
    global urlcache
    if url in urlcache:
        return urlcache[url], True

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        req = urllib.request.Request(url, headers=headers)

        response = urllib.request.urlopen(req)
        urlcache[url] = response.geturl()
        return response.geturl(), True
    except HTTPError as e:
        print("Error: " + url)
        print(str(e.getcode()) + "::" + e.reason)
        urlcache[url] = url
        return url, False
    except:
        e = sys.exc_info()[0]
        print("Error: " + url)
        urlcache[url] = url
        print(e)
        return url, False


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
        # replace mentions with link
        for m in t["entities"]["user_mentions"]:
            screen_name = m["screen_name"]
            # replace with markdown link
            mdlink = "[@%s](https://twitter.com/%s/)" % (screen_name, screen_name)
            content = content.replace("@"+screen_name, mdlink)
        # clean urls
        for u in t["entities"]["urls"]:
            url = u["url"]
            expanded_url = u["expanded_url"]
            # print("##### A URL!!! %s" % expanded_url)
            expanded_url, no_errors = get_final_url(expanded_url)
            content = content.replace(url, expanded_url)

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
            "url": "https://twitter.com/roytang/statuses/%s/" % (t['id'])
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
        kind = "reposts"
        # dont process reposts for now
        return False
    # else:
    #     # dont process others for now
    #     return False

    media = []
    for m in t.get("extended_entities", {}).get("media", []):
        media.append(m["media_url_https"])
    if len(media) > 0:
        if kind != "reposts":
            kind = "photos" 
        # dont process media for now
        return False

    # if p["@is_reblog"] == 'true':
    #     kind = "reposts"
    #     # ugh this is going to slow us down
    #     repost_source = get_repost_source(p["@url-with-slug"])
    #     if not repost_source:
    #         return # exception getting the url, let's just fail
    #     post['repost_source'] = repost_source

    tags = []
    for tag in t.get('entites', {}).get('hashtags', []):
        tags.append(tag['text'])
    if len(tags) > 0:
        post["tags"] = tags

    post["source"] = "twitter"
    outdir = contentdir / kind / d.strftime("%Y") / d.strftime("%m")
    if not outdir.exists():
        outdir.mkdir(parents=True)
    outfile = outdir / ( id + ".md" )
    newfile = frontmatter.dumps(post)
    with outfile.open("w", encoding="UTF-8") as w:
        w.write(newfile)
    return True

def process_tweet(d1):
    orig_tweet_url = "https://twitter.com/%s/statuses/%s/" % (TWITTER_USERNAME, d1['id_str'])
    tweet_source = d1["source"]

    # detect content syndicated from elsewhere
    # instagram, tumblr, roytang.net
    if tweet_source.find("IFTTT") >= 0 or tweet_source.find("Tumblr") >= 0 or tweet_source.find("instagram.com") > 0:
        # print(d1["full_text"])

        for u in d1.get('entities', {}).get("urls", []):
            url = u["expanded_url"]
            url, no_errors = get_final_url(url)

            if not no_errors:
                print(d1["full_text"])

            url = url.replace("www.instagram.com", "instagram.com")
            url = urldefrag(url)[0]
            if url in urlmap:
                u = urlmap[url]
                source_path = Path(u['source_path'])
                full_path = contentdir / source_path
                add_syndication(full_path, orig_tweet_url, "twitter")
                return True

            if url.find("://roytang.net") >= 0:
                link_url = urlparse(url)
                u = urlmap.get(link_url.path, None)
                if u is not None:
                    source_path = Path(u['source_path'])
                    full_path = contentdir / source_path
                    add_syndication(full_path, orig_tweet_url, "twitter")
                    return True
                else:
                    print("######## Unmatched roytang url: %s" % (url))
                    return True
            
            # print("######## URL = %s" % (url))

    return create_post(d1)

countbysource = {}
replies = 0
retweets = 0
withmedia = 0
raw = 0

with Path(SOURCE_FILE).open(encoding='utf-8') as f:
    d = json.load(f)
    idx = 0
    for d1 in d:
        # print(d1["id"])
        # if d1["id_str"] != "1145894355170779137":
        #     continue

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
with urlcachefile.open("w", encoding="UTF-8") as f:
    f.write(json.dumps(urlcache))

for source in countbysource:
    print("countbysource: %s = %s" % (source, countbysource[source]))
print("replies: %s" % (replies))
print("retweets: %s" % (retweets))
print("withmedia: %s" % (withmedia))
print("raw: %s" % (raw))
print("total: %s" % (idx))