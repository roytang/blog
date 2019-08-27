sourcefolder = "D:\\temp\\"
base_url = "http://roytang.net"

import xmltodict
import frontmatter
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import urllib
import shutil
import os
import json
from slugify import slugify

from html.parser import HTMLParser

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
postsfile = sourcedir / "goodreads.xml"

cwd = Path.cwd()
contentdir = cwd / "content"

from bs4 import BeautifulSoup

def create_post(title, author, url, d, params):
    post = frontmatter.Post("")
    post['title'] = 'Book Review: %s by %s' % (title, author)
    slug = slugify(title)
    if title.find(":") > 0:
        title_parts = title.split(":")
        slug = slugify(title_parts[0])
    post['slug'] = slug
    post['date'] = d
    post['syndicated'] = [
        {
            "type": "goodreads",
            "url": "https://www.goodreads.com" + url
        }
    ]

    post["tags"] = ['books']
    post["source"] = "goodreads"
    id = post['slug']
    kind = "post"

    outdir = contentdir / kind / d.strftime("%Y") / d.strftime("%m")
    if not outdir.exists():
        outdir.mkdir(parents=True)
    outfile = outdir / ( id + ".md" )
    newfile = frontmatter.dumps(post)
    with outfile.open("w", encoding="UTF-8") as w:
        w.write(newfile)

with postsfile.open(encoding="UTF-8") as fd:
    soup = BeautifulSoup(fd.read(), "html.parser")
    rows = soup.find_all('tr')
    print(len(rows))
    for row in rows:
        has_review = False
        for cell in row.find_all('td'):
            if 'title' in cell['class']:
                title = cell.a['title']
                for c in cell.a.findChildren():
                    title = title.replace(" " + c.text, "")
                book_url = cell.a['href']
            if 'actions' in cell['class']:
                if cell.text.find("view (with text)") > 0:
                    has_review = True
            if 'cover' in cell['class']:
                cover_src = cell.img['src']
            if 'author' in cell['class']:
                author = cell.a.text
                author_url = cell.a['href']
            if 'comments' in cell['class']:
                review_url = cell.a['href']
            if 'date_read' in cell['class']:
                date_read = cell.span.text
        if has_review:
            print("\n\n----------")
            date_read = datetime.strptime(date_read, "%b %d, %Y")
            print(title)
            print(cover_src)
            print(book_url)
            print(author)
            print(author_url)
            print(review_url)
            print(date_read)
            create_post(title, author, review_url, date_read, {})


