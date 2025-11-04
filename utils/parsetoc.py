from pathlib import Path
import sys, frontmatter
import json

"""
JS to extract the JSON:

var nodes = document.querySelectorAll("details li a");
var outlist = [];
for (let i=0; i<nodes.length; i++) { outlist.push({ "href": nodes[i].getAttribute("href"), "text": nodes[i].innerText }); } 

outlist;

* Make sure the TOC is open and visible when run!

"""

template = """- hashtag: %s
  description: ''
  media: tv
  rating: 0.0
  title: '%s'"""

tocfile = Path("d:\\temp\\toc.json")
with tocfile.open(encoding='UTF-8') as f:
    listdata = json.loads(f.read())
    for item in listdata:
        title = item['text']
        year = "0"
        if title.endswith(")"):
            lastidx = title.rindex("(")
            year = title[lastidx+1:-1]
            title = title[0:lastidx-1]
        outtext = template % (item['href'][1:], title)
        print(outtext)
