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

from utils import loadurlmap, MDSearcher, URLResolver, add_syndication, get_content, PostBuilder
urlmap = loadurlmap(False)

def import_plurks():
    resolver = URLResolver()
    searcher = MDSearcher(resolver=resolver)
    importdir = Path("D:\\temp\\plurk-roytang-backup\\data\\plurks")
    matched = []
    unmatched = []
    for jsfile in importdir.glob("**/*.js"):
        with jsfile.open() as f:
            rawjs = f.read()
            splitidx = rawjs.find("=")
            rawjs = rawjs[splitidx+1:-1]
            plurks = json.loads(rawjs)
            for plurk in plurks:
                # if plurk["base_id"] != "9ah6mc":
                #     continue
                plurk_url = "https://plurk.com/p/%s" % plurk["base_id"]
                if plurk_url in urlmap:
                    # no need to do anything, already syndicated
                    continue
                plurk["plurk_url"] = plurk_url
                d = datetime.strptime(plurk['posted'], "%a, %d %b %Y %H:%M:%S %Z")
                datestr = d.strftime("%Y-%m-%d")
                info = searcher.find_by_day_and_text(datestr, plurk['content_raw'])
                if info is None:
                    datestr = d.strftime("%Y-%m")
                    info = searcher.find_by_month_and_text(datestr, plurk['content_raw'])
                if info is not None:
                    matched.append((plurk, info))
                else:
                    post = PostBuilder(plurk["base_id"], source="plurk", content=plurk["content_raw"])
                    post.date = d
                    post.add_syndication("plurk", plurk_url)
                    post.resolve_links(resolver)
                    post.save()
    # print(json.dumps(matched, indent=2))
    for match in matched:
        plurk = match[0]
        info = match[1]
        add_syndication(Path(info["file"]), plurk["plurk_url"], "plurk")
    # print(json.dumps(unmatched, indent=2))
    print(len(matched))
    print(len(unmatched))
    resolver.save_cache()

    # with Path("D:\\temp\\plurk-unmatched.json").open("w", encoding="UTF-8") as f:
    #     f.write(json.dumps(unmatched, indent=2))

def import_plurk_comments():
    importdir = Path("D:\\temp\\plurk-roytang-backup\\data\\responses")
    matched = []
    unmatched = []
    for jsfile in importdir.glob("**/*.js"):
        parent_id = jsfile.stem
        print(parent_id)
        parent_url = "https://plurk.com/p/%s" % (parent_id)
        if parent_url in urlmap:
            with jsfile.open() as f:
                rawjs = f.read()
                splitidx = rawjs.find("=")
                rawjs = rawjs[splitidx+1:-1]
                reacts = json.loads(rawjs)
                for react in reacts:
                    #print(react)
                    pass
        else:
            print("### ERROR: Missing parent file for %s" % str(jsfile))

import_plurks()
