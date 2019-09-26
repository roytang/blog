URL_CACHE_FILE = "d:\\temp\\urlcache.json"

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
from datetime import datetime, timedelta
import re
import html

cwd = Path(os.environ['HUGO_BLOG_SRCDIR'])
contentdir = cwd / "content"

def urlmap_to_mdfile(info):
    return contentdir / info["source_path"]

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
                urlmap[clean_string(title)] = u1
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
    if str is None or len(str) == 0:
        return str
    # clean string for matching purposes
    str = html.unescape(str)
    # remove markdown links
    str = markdown_link.sub(r'\g<1>', str)
    # remove hashes for some silly plurk reason
    str = str.replace("#", "")
    # remove nonalpha
    str = re.sub(r'\W+', '', str)
    str = "".join(list(filter(lambda x: x in printable, str)))
    return str[0:100]


excluded_kinds = ["archm", "archy", "links", "replies", "reposts"]
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
            excluded = False
            for k in excluded_kinds:
                if str(mdfile).find("\\%s\\" % k) >= 0:
                    excluded = True
                    break
            if excluded:
                continue
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

    def get_daymatch(self, datestr, text):
        daymatches = self.filesbyday.get(datestr, [])
        for m in daymatches:
            matchtext = clean_string(m["matchtext"])
            if len(matchtext) > 10 and text.startswith(matchtext):
                return m
            if len(text) > 10 and matchtext.startswith(text):
                return m
        return None

    def find_by_day_and_text(self, datestr, text):
        if self.resolver is not None:
            text = self.resolver.replace_urls(text)
        text = clean_string(text)
        date = datetime.strptime(datestr, "%Y-%m-%d")
        m = self.get_daymatch(datestr, text)
        # if not found, try +/- one day to account for tz shiz
        if m is None:
            dateplus = date + timedelta(days=1)
            dateplus = dateplus.strftime("%Y-%m-%d")
            m = self.get_daymatch(dateplus, text)
        if m is None:
            dateminus = date + timedelta(days=-1)
            dateminus = dateminus.strftime("%Y-%m-%d")
            m = self.get_daymatch(dateminus, text)
        return m

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

def add_syndication(mdfile, url, stype, source=None):
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
        if not source is None and post.get("source") is None:
            post["source"] = source
        newfile = frontmatter.dumps(post)
        with mdfile.open("w", encoding="UTF-8") as w:
            w.write(newfile)

# print(clean_string("[@NoGunsNoKilling](https://twitter.com/NoGunsNoKilling/) what is that Batman figure on the left, looks neat"))
#MDSearcher()

def get_content(content, resolver):
    raw_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    for raw_url in raw_urls:
        expanded_url, no_errors = resolver.get_final_url(raw_url)
        if expanded_url.find("www.youtube.com") >= 0:
            # convert youtube links to embeds
            link_url = urlparse(expanded_url)
            qps = parse_qs(link_url.query)
            content = content.replace(raw_url, "{{< youtube %s >}}" % (qps["v"][0]))
        content = content.replace(raw_url, expanded_url)

    return content

class PostBuilder():

    @staticmethod
    def from_mdfile(mdfile):
        id = mdfile.stem
        mdpost = frontmatter.load(mdfile)
        date = mdpost.get('date', datetime.now())
        info = {
            "date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "text": mdpost.content,
            "matchtext": clean_string(mdpost.content),
            "file": str(mdfile)
        }
        post = PostBuilder(id, content=mdpost.content, source=mdpost.get("source", ""))
        post.kind = "gibberish" # require the caller to replace it, not easy to extract from the file (we can, pero katamad)
        post.title = mdpost.get("title")
        post.date = mdpost.get("date")
        post.tags = mdpost.get("tags")
        for syn in mdpost.get('syndicated', []):
            post.add_syndication(syn['type'], syn['url'])
        return post

    def __init__(self, id, content="", source=""):
        self.params = {}
        self.id = id # id is also the slug
        self.post = frontmatter.Post(content)
        self.kind = "notes" # reasonable default
        self.title = None # reasonable default
        self.date = datetime.now() # reasonable default
        self.source = source
        self.media = []
        self.tags = []

    def add_syndication(self, stype, url):
        if self.post.get('syndicated') is None:
            self.post['syndicated'] = []
        self.post['syndicated'].append({
            "type": stype,
            "url": url
        })

    # follow link shorteners
    # extract embeds via:
    # - youtube
    # - imgur
    def resolve_links(self, resolver):
        content = self.post.content
        raw_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
        for raw_url in raw_urls:
            expanded_url, no_errors = resolver.get_final_url(raw_url)
            if expanded_url.find("www.youtube.com") >= 0:
                # convert youtube links to embeds
                link_url = urlparse(expanded_url)
                qps = parse_qs(link_url.query)
                content = content.replace(raw_url, "{{< youtube %s >}}" % (qps["v"][0]))
            elif expanded_url.find("imgur.com") >= 0 or expanded_url.endswith(".jpg"):
                self.media.append(expanded_url)
                # leave the image url for context
                #content = content.replace(raw_url, "")
            else:
                content = content.replace(raw_url, expanded_url)

        self.post.content = content

    def save(self):
        for param in self.params:
            self.post[param] = self.params[param]
        self.post["date"] = self.date
        self.post["source"] = self.source

        parsed_tags = re.findall(r"\s#(\w+)", " " + self.post.content)
        for tag in parsed_tags:
            if tag not in self.tags:
                self.tags.append(tag.lower())

        self.post["tags"] = self.tags
        if self.title is not None:
            self.post["title"] = self.title
        outdir = contentdir / self.kind / self.date.strftime("%Y") / self.date.strftime("%m") / self.id
        if not outdir.exists():
            outdir.mkdir(parents=True)

        outfile = outdir / ( "index.md" )
        newfile = frontmatter.dumps(self.post)
        with outfile.open("w", encoding="UTF-8") as w:
            w.write(newfile)
        # copy over any media from the reply as well
        for m in self.media:
            filename = m[m.rfind("/")+1:]
            download_to = outdir / filename
            if m.startswith("file://"):
                filepath = Path(m.replace("file://", ""))
                shutil.copy(str(filepath), str(download_to))    
            else:
                print("Downloading %s" % (m))
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(m, str(download_to))

    def get_source_path(self):
        return contentdir / self.kind / self.date.strftime("%Y") / self.date.strftime("%m") / self.id / "index.md"

class CommentBuilder():

    def __init__(self, source_path):
        if type(source_path).__name__ == "str":
            source_path = Path(source_path)
        self.source_path = source_path


    def add_comment(self, id, date, author, source, content, url=None, overwrite=False):
        datestr = date.strftime('%Y%m%dT%H%M%S')
        newfile = self.source_path.parent / ( "comment-%s-%s.json" % (datestr, id) )

        if newfile.exists() and not overwrite:
            return

        comment = {
            "id": id,
            "name": author['name'],
            "url": author.get('url', ''),
            "text": content, 
            "date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "photo": author.get('photo', ''),
            "source_url": url,
            "mention_url": url,
            "source": source
        }

        # save the comment into newdir
        with Path(newfile).open("w", encoding="UTF-8") as f:
            f.write(json.dumps(comment))

def add_to_listmap(map, key, value):
    if key in map:
        map[key].append(value)
    else:
        map[key] = [value]