sourcefile = "d://temp//disqus.xml"
base_url = "http://roytang.net"

import xmltodict
import frontmatter
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

with open(sourcefile, encoding="UTF-8") as fd:
    doc = xmltodict.parse(fd.read())

    threads = {} # map of dsq:id to thread object
    for thread in doc["disqus"]["thread"]:
        threads[thread["@dsq:id"]] = thread

    cwd = Path.cwd() 
    # navigate to ./content/post
    p = cwd / "content" / "comment"
    
    for post in doc["disqus"]["post"]:
        print(post)
        postid = post["@dsq:id"]
        threadid = post["thread"]["@dsq:id"]
        thread = threads[threadid]

        fm = frontmatter.Post(post["message"])
        fm['source'] = 'disqus'

        datestr = post["createdAt"]
        date = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%SZ')
        fm['date'] = date

        # create the year folder if it doesnt exist
        yearfldr = p / str(date.year)
        if not yearfldr.exists():
            yearfldr.mkdir()

        # same for month 
        month = str(date.month)
        if len(month) == 1:
            month = "0" + month
        monthfldr = yearfldr / month
        if not monthfldr.exists():
            monthfldr.mkdir()


        url = urlparse(thread['link'])
        u = url.path
        u = u.replace("/blog/", "/") # handle older blog links

        fm['parent_page'] = { 'urlpath' : u, 'title': thread['title'] }
        fm['author'] = { 'name': post['author']['name'], 'anonymous': post['author']['isAnonymous'], 'username': post['author'].get('username', '')}

        newfile = frontmatter.dumps(fm)
        outfile = monthfldr / ("disqus-" + postid + ".md")
        with outfile.open("w", encoding='utf-8') as w:
            w.write(newfile)        