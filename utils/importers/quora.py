
# to get this json, open your quora profile and scroll down to the end until all the answers are visible
# then use the js console:
# let list = document.querySelectorAll(".answer_permalink");
# let output = []
# list.forEach((item) => { output.push( { 'url': item.getAttribute('href'), 'label': item.innerText }) });
# then dump the output variable into a file
sourcefile = "D:\\temp\\quora.json"

# need a second temporary file, so that re-running the post-creation script doesnt have to re-scrape the pages
tempfile = "D:\\temp\\quora_temp.json"

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

def scrape_data():
    with source.open(encoding="UTF-8") as fd:
        qlist = json.loads(fd.read())
        all = []
        for l in qlist:
            full_url = "https://www.quora.com%s" % (l['url'])
            print(full_url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
                'Accept-Language': 'en-US,en;q=0.5'
            }
            r = requests.get(full_url, headers=headers)
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, "html.parser")
                titles = soup.findAll("span", {"class": "ui_content_title"})
                parsed = {}
                for t in titles:
                    parsed['title'] = t.text
                    break
                divs = soup.findAll("div", {"class": "ExpandedAnswer"})
                for div in divs:
                    spans = div.findAll("span", {"class": "ui_qtext_rendered_qtext"})
                    for span in spans:
                        parsed['answer_text'] = str(span)
                        break

                divs = soup.findAll("div", {"class": "OriginallyAnsweredBanner"})
                for div in divs:
                    spans = div.findAll("span", {"class": "ui_qtext_rendered_qtext"})
                    for span in spans:
                        parsed['original_answer_text'] = str(span)
                        break
                
                parsed['date'] = l['label'].replace("Answered ", "")
                parsed['url'] = l['url']
                all.append(parsed)
            else:
                print("#### Received status code %s for url %s" % (r.status_code, full_url))

        print(len(qlist))

        with Path(tempfile).open("w", encoding="UTF-8") as out:
            out.write(json.dumps(all))


def create_posts():

    with Path(tempfile).open(encoding="UTF-8") as f:
        rows = json.loads(f.read())
        for row in rows:
            d = datetime.strptime(row['date'].replace(",", ""), '%b %d %Y')
            title = row.get('original_answer_text', row.get('title'))
            url = row.get('url')
            answer_text = row.get('answer_text')
            create_post(d, title, url, answer_text)

def create_post(d, title, url, answer_text, overwrite=True):

    url = "https://www.quora.com%s" % (url)   

    caption = "Someone on [quora]() asked:\n\r"
    caption = caption + ("> [%s](%s)\n\r" % (title, url))
    caption = caption + answer_text
    post = frontmatter.Post(caption)
    slug = slugify(title[0:30])
    post['slug'] = slug
    post['date'] = d

    post["source"] = "quora"
    post["syndicated"] = [{
        'type': 'quora',
        'url': url
    }]
    id = post['slug']
    post['tags'] = ['answers']
    kind = "notes"

    outdir = contentdir / kind / d.strftime("%Y") / d.strftime("%m")
    if not outdir.exists():
        outdir.mkdir(parents=True)
    outfile = outdir / ( id + ".md" )

    if outfile.exists() and not overwrite:
        return

    newfile = frontmatter.dumps(post)
    with outfile.open("w", encoding="UTF-8") as w:
        w.write(newfile)

create_posts()