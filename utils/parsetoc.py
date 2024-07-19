from pathlib import Path
import sys, frontmatter
import json

"""
JS to extract the JSON:

var nodes = document.querySelectorAll("details li a");
var outlist = [];
for (let i=0; i<nodes.length; i++) { outlist.push({ "href": nodes[i].getAttribute("href"), "text": nodes[i].innerText }); } 


"""

template = """- hashtag: %s
  description: ''
  media: comics
  title: '%s'
  issues: 0
  year: 0`"""

tocfile = Path("d:\\temp\\toc.json")
with tocfile.open(encoding='UTF-8') as f:
    listdata = json.loads(f.read())
    for item in listdata:
        title = item['text']
        outtext = template % (item['href'][1:], title)
        print(outtext)
