from pathlib import Path
import sys, frontmatter
import json

template = """- hashtag: %s
  description: Retro review from May 2023
  media: games
  title: '%s'
  date: 1990-01-01"""

tocfile = Path("d:\\temp\\toc.json")
with tocfile.open(encoding='UTF-8') as f:
    listdata = json.loads(f.read())
    for item in listdata:
        idx = item['text'].find(".")
        if idx > 0:
            title = item['text'][idx+2:].replace("'", "\'")
            outtext = template % (item['href'][1:], title)
            print(outtext)
