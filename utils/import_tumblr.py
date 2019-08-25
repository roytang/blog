sourcefolder = "D:\\temp\\tumblr"
base_url = "http://roytang.net"

import xmltodict
import frontmatter
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

sourcedir = Path(sourcefolder)
postsfile = sourcedir / "posts.xml"

countbytype = {}
reblogscount = 0
instagramcount = 0
roytangcount = 0

with postsfile.open(encoding="UTF-8") as fd:
    doc = xmltodict.parse(fd.read())
    posts = doc['tumblr']['posts']['post']
    for post in posts:
        ptype = post['@type']
        print(post['@date-gmt'] + '::' + post['@type'])
        if ptype not in countbytype:
            countbytype[ptype] = 1
        else:
            countbytype[ptype] = countbytype[ptype] + 1

        if ptype == 'regular':
            if 'regular-title' in post:
                print(post['regular-title'])

        if post['@is_reblog'] == 'true':
            reblogscount = reblogscount + 1

        if ptype == 'photo':
            if 'photo-link-url' in post and post['photo-link-url'].startswith("https://www.instagram.com/"):
                instagramcount = instagramcount + 1
            if 'photo-caption' in post:
                print(post['photo-caption'])

        if ptype == 'link':
            if 'link-url' in post and post['link-url'].find("://roytang.net") >= 0:
                roytangcount = roytangcount+1
            else:
                if 'link-url' in post:
                    print('link: ' + post['link-url'])
        
        if ptype == 'quote':
            print(post['quote-text'])
        


print("total posts: " + str(len(posts)))
print("total reblogs: " + str(reblogscount))
print("total instagram: " + str(instagramcount))
print("total roytang.net: " + str(roytangcount))
print(countbytype)
