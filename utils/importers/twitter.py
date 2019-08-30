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
        response = urllib.request.urlopen(url)
        urlcache[url] = response.geturl()
        return response.geturl(), True
    except:
        e = sys.exc_info()[0]
        print("Error: " + url)
        print(e)
        urlcache[url] = url
        return url, False

countbysource = {}
replies = 0
retweets = 0
withmedia = 0

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

def process_tweet(d1):
    orig_tweet_url = "https://twitter.com/%s/statuses/%s/" % (TWITTER_USERNAME, d1['id_str'])

    # detect content syndicated from elsewhere
    # instagram, tumblr, roytang.net
    if tweet_source.find("IFTTT") >= 0 or tweet_source.find("Tumblr") >= 0:
        # print(d1["full_text"])

        for u in d1.get('entities', {}).get("urls", []):
            url = u["expanded_url"]
            url, no_errors = get_final_url(url)
            url = url.replace("www.instagram.com", "instagram.com")
            url = urldefrag(url)[0]
            if url in urlmap:
                u = urlmap[url]
                source_path = Path(u['source_path'])
                full_path = contentdir / source_path
                add_syndication(full_path, orig_tweet_url, "twitter")
                return

            if url.find("://roytang.net") >= 0:
                link_url = urlparse(url)
                u = urlmap.get(link_url.path, None)
                if u is not None:
                    source_path = Path(u['source_path'])
                    full_path = contentdir / source_path
                    add_syndication(full_path, orig_tweet_url, "twitter")
                    return
                else:
                    print("######## Unmatched roytang url: %s" % (url))
            
            # print("######## URL = %s" % (url))



with Path(SOURCE_FILE).open(encoding='utf-8') as f:
    d = json.load(f)
    idx = 0
    for d1 in d:
        tweet_source = d1["source"]
        if tweet_source not in countbysource:
            countbysource[tweet_source] = 1
        else:
            countbysource[tweet_source] = countbysource[tweet_source] + 1

        for prop in ["in_reply_to_status_id_str", "in_reply_to_screen_name"]:
            if prop in d1:
                replies = replies + 1

        # handle retweet
        content = d1["full_text"]
        if content.startswith("RT @"):
            retweets = retweets + 1

        process_tweet(d1)


        # post = frontmatter.Post(d1["full_text"])
        # post['date'] = d1["created_at"]
        # post['source'] = 'twitter'
        # post['id'] = d1["id_str"]

        # tags = []
        # for ht in d1["entities"]["hashtags"]:
        #     tags.append(ht["text"])
        # if len(tags) > 0:
        #     post['tags'] = tags

        # media = []
        # if "extended_entities" in d1:
        #     for m in d1["extended_entities"]["media"]:
        #         media.append(m["media_url_https"])
        # post['media'] = media

        # if len(media) > 0:
        #     withmedia = withmedia + 1

        # # replies
        # post["reply"] = False
        # for prop in ["in_reply_to_status_id_str", "in_reply_to_screen_name"]:
        #     if prop in d1:
        #         post[prop] = d1[prop]
        #         post["reply"] = True
        #         replies = replies + 1

        # # handle retweet
        # post["retweet"] = False
        # if content.startswith("RT @"):
        #     post["retweet"] = True
        #     colon_idx = content.find(":")
        #     retweeted_screen_name = content[4:colon_idx]
        #     mdlink = "[@%s](https://twitter.com/%s/)" % (retweeted_screen_name, retweeted_screen_name)
        #     # blockquote the content
        #     rt_content = content[colon_idx+1:]
        #     content = "RT @%s" % (retweeted_screen_name) # the 'entities' code below should turn this into a link
        #     content = content + '\n\n> ' + rt_content
        #     retweets = retweets + 1

        # if "entities" in d1:
        #     # replace mentions with link
        #     for m in d1["entities"]["user_mentions"]:
        #         screen_name = m["screen_name"]
        #         # replace with markdown link
        #         mdlink = "[@%s](https://twitter.com/%s/)" % (screen_name, screen_name)
        #         content = content.replace("@"+screen_name, mdlink)
        #     # clean urls
        #     # for u in d1["entities"]["urls"]:
        #     #     url = u["url"]
        #     #     expanded_url = u["expanded_url"]
        #     #     expanded_url, no_errors = get_final_url(expanded_url)

        #     #     if expanded_url.startswith("https://twitter.com/") and expanded_url.find("/status/") > 0 and no_errors:
        #     #         # handle QTs by creating a markdown embed
        #     #         qtid = expanded_url[expanded_url.find("/status/")+8:]
        #     #         # remove ? query params if it exists
        #     #         if qtid.find("?") > 0:
        #     #             qtid = qtid.split("?")[0]
        #     #         if qtid.endswith("/"):
        #     #             qtid = qtid[:-1]
        #     #         # finally, make sure the qtid is a numeric string
        #     #         if not is_number(qtid):
        #     #             content = content.replace(url, expanded_url)
        #     #         else:
        #     #             mdembed = "{{< tweet %s >}}" % qtid
        #     #             content = content.replace(url, mdembed)
        #     #     else:
        #     #         content = content.replace(url, expanded_url)

        # post.content = content
        # # newfile = frontmatter.dumps(post)
        # # with open(OUTPUT_DIR + d1["id_str"] + ".md", "w", encoding='utf-8') as w:
        # #     w.write(newfile)

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
print("total: %s" % (idx))