sourcefolder = "D:\\temp\\ireadcomicbooks"

import xmltodict
import frontmatter
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from urllib.error import HTTPError
import urllib
import shutil
import os
import json
import urllib.request
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import utils

class MyParser(HTMLParser):
    def __init__(self, output_list=None):
        HTMLParser.__init__(self)
        if output_list is None:
            self.output_list = []
        else:
            self.output_list = output_list
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.output_list.append(dict(attrs).get('href'))

blogdir = Path(os.environ['HUGO_BLOG_OUTDIR'])
urlmapfile = blogdir / "urlmap.json"

sourcedir = Path(sourcefolder)
postsfile = sourcedir / "posts.xml"
mediadir = sourcedir / "media"

cwd = Path.cwd()
contentdir = cwd / "content"

def get_final_url(url):
    try:
        response = urllib.request.urlopen(url)
        return response.geturl()
    except:
        print("Error: " + url)
        return url

import hashlib
def get_file_hash(path):
    with open(path, "rb") as f:
        file_hash = hashlib.md5()
        chunk = f.read(8192)
        file_hash.update(chunk)
    return file_hash.hexdigest()

def create_photo_post(p, content = None):
    if content is None:
        content = p.get('photo-caption', '')

    id = p["@id"]
    post = utils.PostBuilder(id, content)
    d = datetime.strptime(p["@date-gmt"], "%Y-%m-%d %H:%M:%S %Z")
    post.date = d
    post.add_syndication("tumblr", p["@url-with-slug"])
    post.kind = "photos"

    tags = p.get("tag", [])
    if not isinstance(tags, list):
        tags = [tags]
    tags.append("ireadcomicbooks")
    if len(tags) > 0:
        post.tags = tags

    post.source = "tumblr"

    # find photos
    filehashes = []

    for imgfile in mediadir.glob(id + "*.*"):
        filehash = get_file_hash(imgfile)
        if filehash in filehashes:
            # duplicate of already processed image, ignore
            continue
        filehashes.append(filehash)
        post.media.append("file://" + str(imgfile))

    return post

def get_repost_source(url):
    try:
        with urllib.request.urlopen(url) as fp:
            mybytes = fp.read()
            mystr = mybytes.decode("utf8")
            soup = BeautifulSoup(mystr, "html.parser")

            # use reblog-link
            links = soup.findAll("a",{"class": "reblog-link"})
            for link in links:
                # use the first one
                return {
                    "type": "tumblr",
                    "name": link.text.strip(),
                    "url": link['href']
                }


            # look for "roytang reblogged this from"
            lis = soup.findAll("li", {"class": "tumblelog_roytang"})
            for li in lis:
                anchors = li.findAll("a", {"class", "source_tumblelog"})
                for anchor in anchors:
                    return {
                        "type": "tumblr",
                        "name": anchor.text.strip(),
                        "url": anchor['href']
                    }

                

            # try the content_source first
            divs = soup.findAll("div", {"class": "content_source"})
            for div in divs:
                a = div.a
                return {
                    "type": "tumblr",
                    "name": a.text.replace("Source:", "").strip(),
                    "url": a['href']
                }
            
            # next we try quotes_source
            divs = soup.findAll("div", {"class": "cont"})
            # we get the very last p
            lastp = None
            for div in divs:
                for para in div.findAll("p"):
                    if para.text.find("(via ") >= 0:
                        lastp = para
            if lastp is not None:
                a = lastp.a
                return {
                    "type": "tumblr",
                    "name": a.text.strip(),
                    "url": a['href']
                }

    except HTTPError as e:
        print("Error fetching the URL")
        print(e)
        return False # bad practice!
            
    # default!
    print("##### Couldnt find source, using default %s" % (url))
    return {
        "type": "tumblr",
        "name": "tumlbr",
        "url": url
    }


def create_post(p, kind, content, params):
    post = frontmatter.Post(content)
    d = datetime.strptime(p["@date-gmt"], "%Y-%m-%d %H:%M:%S %Z")
    post['date'] = d
    post['syndicated'] = [
        {
            "type": "tumblr",
            "url": p["@url-with-slug"]
        }
    ]
    if p["@is_reblog"] == 'true':
        kind = "reposts"
        # ugh this is going to slow us down
        repost_source = get_repost_source(p["@url-with-slug"])
        if not repost_source:
            return # exception getting the url, let's just fail
        post['repost_source'] = repost_source

    tags = p.get("tag", [])
    if not isinstance(tags, list):
        tags = [tags]
    if "tags" in params:
        for t in params["tags"]:
            if t not in tags:
                tags.append(t)

    if len(tags) > 0:
        post["tags"] = tags

    post["source"] = "tumblr"
    id = p["@id"]
    for param in params:
        if param != "tags":
            post[param] = params[param]
    outdir = contentdir / kind / d.strftime("%Y") / d.strftime("%m")
    if not outdir.exists():
        outdir.mkdir(parents=True)
    outfile = outdir / ( id + ".md" )
    newfile = frontmatter.dumps(post)
    with outfile.open("w", encoding="UTF-8") as w:
        w.write(newfile)

def add_syndication(mdfile, url, stype):
    #print(str(mdfile))
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

urlmap = utils.loadurlmap()

countbytype = {}
reblogscount = 0
instagramcount = 0
roytangcount = 0
unprocessed = 0

def import_post(post):

    global countbytype
    global reblogscount
    global instagramcount
    global roytangcount
    global unprocessed
    global urlmap

    ptype = post['@type']
    purl = post["@url"]
    purlslug = post["@url-with-slug"]
    if purl in urlmap or purlslug in urlmap:
        # already syndicated, no need to process
        return

    # if post["@id"] != "182463223840":
    #     return

    # print(ptype)
    
    if post['@is_reblog'] == 'true':
        reblogscount = reblogscount + 1
        print()
        repost_source = get_repost_source(purlslug)
        if repost_source["url"] in urlmap:
            um = urlmap[repost_source["url"]]
            utils.add_syndication(utils.urlmap_to_mdfile(um), purl, "tumblr")
        else:
            pb = create_photo_post(post)
            pb.kind = "reposts"
            pb.params["repost_source"] = repost_source
            pb.params["album"] = "comicbooks"
            pb.save()

    if ptype == 'regular':
        body = post.get('regular-body', '')
        body = BeautifulSoup(body, "html.parser").text
        pb = create_photo_post(post, body)
        if len(pb.media) > 0:
            pb.params["album"] = "comicbooks"
            pb.save()
            return
        print(purlslug)
        print(body)

    if ptype == 'photo':
        pb = create_photo_post(post)
        pb.params["album"] = "comicbooks"
        pb.save()
        return


    unprocessed = unprocessed + 1
    if ptype not in countbytype:
        countbytype[ptype] = 1
    else:
        countbytype[ptype] = countbytype[ptype] + 1

with postsfile.open(encoding="UTF-8") as fd:
    doc = xmltodict.parse(fd.read())
    posts = doc['tumblr']['posts']['post']
    for post in posts:
        import_post(post)


print("total posts: " + str(len(posts)))
print("total reblogs: " + str(reblogscount))
print("total instagram: " + str(instagramcount))
print("total roytang.net: " + str(roytangcount))
print("total unprocessed: " + str(unprocessed))
print(countbytype)
