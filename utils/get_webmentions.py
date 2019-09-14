# pulls webmentions in as comments
# todo: make this as webhook in the flask app 

from pathlib import Path
import frontmatter
import io
import slugify
from datetime import datetime
from urllib.parse import urlparse
import os
import requests
import json

token = os.environ['WEBMENTION_TOKEN']
endpoint = "https://webmention.io/api/mentions.jf2?token=%s" % (token)
print(endpoint)

cwd = Path.cwd() 
p = cwd / "content" / "post"
cf = cwd / "content" / "comment"

blogdir = Path(os.environ['HUGO_BLOG_OUTDIR'])
urlmapfile = blogdir / "urlmap.json"
urlmap = {}
with urlmapfile.open(encoding="UTF-8") as f:
    urlmap = json.loads(f.read())

import urllib.request, json 
with urllib.request.urlopen(endpoint) as url:
    data = json.loads(url.read().decode())
    for link in data['children']:
        # print(link)

        content = ""
        if link['wm-property'] == 'like-of':
            content = "[%s](%s) liked this [on twitter](%s)" % (link['author']['name'], link['author']['url'], link['url'])
        if link['wm-property'] == 'repost-of':
            content = "[%s](%s) shared this [on twitter](%s)" % (link['author']['name'], link['author']['url'], link['url'])
        if link['wm-property'] == 'mention-of':
            content = "[%s](%s) mentioned [%s](%s)" % (link['wm-source'], link['wm-source'], link['wm-target'], link['wm-target'])

        datestr = link['wm-received']
        date = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%SZ')
        url = urlparse(link["wm-target"])
        info = urlmap.get(url.path)
        if info is None:
            print("##### Path not found, map manually %s" % url.path)
            continue
        parentmd = cwd / "content" / info["source_path"]
        if parentmd.name != "index.md":
            # migrate the post to a page bundle
            newdir = parentmd.parent / parentmd.stem
            if not newdir.exists():
                newdir.mkdir(parents=True)
            if parentmd.exists():
                newfile = newdir / "index.md"
                os.rename(str(parentmd), str(newfile))
        else:
            newdir = parentmd.parent

        id = "webmention-%s" % (link["wm-id"])
        datestr = date.strftime('%Y%m%dT%H%M%S')
        wtype = link['wm-property']
        if wtype == 'like-of':
            newfile = newdir / ( "like-%s-%s.json" % (datestr, id) )
        elif wtype == 'repost-of':
            newfile = newdir / ( "repost-%s-%s.json" % (datestr, id) )
        elif wtype == 'mention-of':
            newfile = newdir / ( "mention-%s-%s.json" % (datestr, id) )
        else:
            newfile = newdir / ( "comment-%s-%s.json" % (datestr, id) )

        comment = {
            "id": id,
            "name": link['author']['name'],
            "url": link['author'].get('url', ''),
            "text": link.get("content", {}).get("text", ""), 
            "date": date.strftime("%Y-%m-%d %H:%M:%S"),
            "photo": link['author'].get('photo', ''),
            "source_url": link["wm-source"],
            "mention_url": link["url"],
            "source": "webmention"
        }

        # save the comment into newdir
        if not newfile.exists():
            with Path(newfile).open("w", encoding="UTF-8") as f:
                f.write(json.dumps(comment))
    