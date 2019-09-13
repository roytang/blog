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

from utils import loadurlmap, MDSearcher, URLResolver
urlmap = loadurlmap(False)

def import_plurks():
    resolver = URLResolver()
    searcher = MDSearcher(resolver=resolver)
    importdir = Path("D:\\temp\\plurk-roytang-backup\\data\\plurks")
    matched = []
    unmatched = []
    for jsfile in importdir.glob("**/*.js"):
        #print(jsfile)
        with jsfile.open() as f:
            rawjs = f.read()
            splitidx = rawjs.find("=")
            rawjs = rawjs[splitidx+1:-1]
            plurks = json.loads(rawjs)
            for plurk in plurks:
                d = datetime.strptime(plurk['posted'], "%a, %d %b %Y %H:%M:%S %Z")
                monthstr = d.strftime("%Y-%m-%d")
                info = searcher.find_by_day_and_text(monthstr, plurk['content_raw'])
                if info is not None:
                    matched.append((plurk, info))
                else:
                    unmatched.append(plurk)
    #print(json.dumps(unmatched, indent=2))
    print(len(matched))
    print(len(unmatched))
    resolver.save_cache()

import_plurks()
