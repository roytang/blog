URL_CACHE_FILE = "d:\\temp\\twitter\\urlcache.json"

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
import html

def load_map_from_json(filename):
    cachefile = Path(filename)
    cache = {}
    if cachefile.exists():
        with cachefile.open(encoding="UTF-8") as f:
            cache = json.loads(f.read())
    return cache

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

import string
printable = set(string.printable)
markdown_link = re.compile("\[([^\]]+)\]\((http[s]?://[^)]+)\)")
def clean_string(str):
    # clean string for matching purposes
    str = html.unescape(str)
    # remove hashes for some silly plurk reason
    str = str.replace("#", "")
    # remove markdown links
    str = markdown_link.sub(r'\g<1>', str)
    str = "".join(list(filter(lambda x: x in printable, str)))
    return str[0:100]

class MDSearcher:

    def __init__(self, kind=None, resolver=None):
        # index all the mdfiles
        cwd = Path.cwd()
        searchdir = cwd / "content"
        if kind is not None:
            searchdir = searchdir / kind
        self.resolver = resolver
        self.filelist = []
        self.filesbymonth = {}
        self.filesbyday = {}
        print("## MDSearcher: Building search index")
        for mdfile in searchdir.glob("**/*.md"):
            try:
                mdpost = frontmatter.load(mdfile)
            except:
                print("Error parsing file %s" % (str(mdfile)))
                continue
            date = mdpost.get('date', datetime.now())
            info = {
                "date": date.strftime("%Y-%m-%d %H:%M:%S"),
                "text": mdpost.content,
                "matchtext": clean_string(mdpost.content),
                "file": str(mdfile)
            }
            self.filelist.append(info)
            datestr = date.strftime("%Y-%m")
            self.filesbymonth[datestr] = self.filesbymonth.get(datestr, [])
            self.filesbymonth[datestr].append(info)
            datestr = date.strftime("%Y-%m-%d")
            self.filesbyday[datestr] = self.filesbyday.get(datestr, [])
            self.filesbyday[datestr].append(info)
        print("## MDSearcher: Done building search index")

    def find_by_day_and_text(self, datestr, text):
        if self.resolver is not None:
            text = self.resolver.replace_urls(text)
        text = clean_string(text)
        daymatches = self.filesbyday.get(datestr, [])
        for m in daymatches:
            if text.startswith(m['matchtext']):
                return m
            if m['matchtext'].startswith(text):
                return m
        return None

    def find_by_month_and_text(self, datestr, text):
        if self.resolver is not None:
            text = self.resolver.replace_urls(text)
        text = clean_string(text)
        matches = self.filesbymonth.get(datestr, [])
        for m in matches:
            if len(m['matchtext']) > 10 and text.startswith(m['matchtext']):
                return m
            if len(text) > 10 and m['matchtext'].startswith(text):
                return m
        return None

class URLResolver:

    def __init__(self):
        self.urlcache = load_map_from_json(URL_CACHE_FILE)

    def replace_urls(self, str):
        raw_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
        for raw_url in raw_urls:
            final_url, no_errors = self.get_final_url(raw_url)
            if no_errors and raw_url != final_url:
                str = str.replace(raw_url, final_url)
        return str

    def get_final_url(self, url, usecache=True):
        if usecache and url in self.urlcache:
            if self.urlcache[url].endswith("imgur.com/removed.png"):
                # rewrite the cache so we don't use this imgur 404:
                self.urlcache[url] = url
                return url, True
            # print(self.urlcache[url])
            return self.urlcache[url], True

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            response = requests.get(url, headers=headers)
            self.urlcache[url] = response.url
            return response.url, True
        except HTTPError as e:
            print("Error: " + url)
            print(str(e.getcode()) + "::" + e.reason)
            self.urlcache[url] = url
            return url, False
        except:
            e = sys.exc_info()[0]
            print("Error: " + url)
            self.urlcache[url] = url
            print(e)
            return url, False

    def save_cache(self):
        with Path(URL_CACHE_FILE).open("w", encoding="UTF-8") as f:
            f.write(json.dumps(self.urlcache, indent=2))

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

# print(clean_string("[@NoGunsNoKilling](https://twitter.com/NoGunsNoKilling/) what is that Batman figure on the left, looks neat"))
#MDSearcher()