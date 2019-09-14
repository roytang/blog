from pathlib import Path
import urllib.request
import xmltodict
from importers.pocket import create_post
from datetime import datetime
import html

remote_url = "https://getpocket.com/users/hungryroy/feed/all"

# imports a feed into a local xml, so it can be parsed by JS without CORS issues
# (I realize I could just generate the links page directly via md here, but I didn't want to add a feedparser dependency)
def import_feed():
    mystr = ""
    with urllib.request.urlopen(remote_url) as fp:
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

    items = xmltodict.parse(mystr)['rss']['channel']['item']
    for a in items:
        # print(html.unescape(a['title']))
        link_text = html.unescape(a['title'])
        link_url = a['link']
        d = datetime.strptime(a['pubDate'], "%a, %d %b %Y %H:%M:%S %z")

        create_post(d, link_text, link_url, overwrite=False)

import_feed()