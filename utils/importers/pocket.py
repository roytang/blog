sourcefile = "D:\\temp\\ril_export.html"
base_url = "http://roytang.net"

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
from slugify import slugify

source = Path(sourcefile)

cwd = Path.cwd()
contentdir = cwd / "content"

from bs4 import BeautifulSoup

def create_post(d, link_text, link_url, overwrite=True):
    post = frontmatter.Post("")
    title = link_text
    post['title'] = title
    slug = slugify(title)
    post['slug'] = slug
    post['date'] = d

    post["source"] = "pocket"
    post['link'] = {
        "url": link_url,
        "text": link_text,
        "source": "pocket",
        "source_url": "https://getpocket.com"
    }
    id = post['slug']
    kind = "links"

    outdir = contentdir / kind / d.strftime("%Y") / d.strftime("%m")
    if not outdir.exists():
        outdir.mkdir(parents=True)
    outfile = outdir / ( id + ".md" )

    if outfile.exists() and not overwrite():
        return

    newfile = frontmatter.dumps(post)
    with outfile.open("w", encoding="UTF-8") as w:
        w.write(newfile)

import requests

def get_final_url(url):
    try:
        response = urllib.request.urlopen(url)
        return response.geturl()
    except:
        return url

def get_link_title(url):
    try:
        url = get_final_url(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html.parser")
            titles = soup.findAll("title")
            for title in titles:
                return title.text.strip()
        else:
            print("#### Received status code %s for url %s" % (r.status_code, url))

    except Exception as e:
        print("#### Error fetching the URL: %s" % (url))
        print(e)

    # default
    return url            

def import_file():
    count = 0
    with source.open(encoding="UTF-8") as fd:
        soup = BeautifulSoup(fd.read(), "html.parser")
        rows = soup.find_all('a')
        for row in rows:
            link_text = row.text
            d = datetime.utcfromtimestamp(int(row['time_added']))
            link_url = row['href']

            tags = row["tags"].split(",")
            if 'ifttt' in tags:
                continue
            
            if link_url.startswith("https://ifttt.com/missing_link"):
                continue

            if link_url == link_text:
                link_text = get_link_title(link_url)


            create_post(d, link_text, link_url)

            count = count + 1

    print(count)