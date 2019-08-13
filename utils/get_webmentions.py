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

token = os.environ['WEBMENTION_TOKEN']
endpoint = "https://webmention.io/api/mentions.jf2?token=%s" % (token)

cwd = Path.cwd() 
p = cwd / "content" / "post"
cf = cwd / "content" / "comment"

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

        fm = frontmatter.Post(content)
        fm['source'] = 'webmention'
        datestr = link['wm-received']
        date = date = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%SZ')
        fm['date'] = date
        # create the year folder if it doesnt exist
        yearfldr = cf / str(date.year)
        if not yearfldr.exists():
            yearfldr.mkdir()
        # same for month 
        month = str(date.month)
        if len(month) == 1:
            month = "0" + month
        monthfldr = yearfldr / month
        if not monthfldr.exists():
            monthfldr.mkdir()
    
        url = urlparse(link["wm-target"])
        u = url.path
        # also fetch the title
        n = requests.get(link["wm-target"])
        al = n.text
        # this is a bit hacky, but should work as long as the theme implements microformats
        startstr = 'class="p-name">'
        startidx = al.find(startstr) + len(startstr)
        title = al[startidx : al.find('</', startidx)]
    
        fm['parent_page'] = { 'urlpath' : u, 'title': title }
        fm['author'] = link['author']
        fm['webmention_type'] = link['wm-property']
    
        newfile = frontmatter.dumps(fm)
        newfilename = "webmention-%s.md" % ( link['wm-id'] )
        outfile = monthfldr / newfilename
        with outfile.open("w", encoding='utf-8') as w:
            w.write(newfile)                                
    