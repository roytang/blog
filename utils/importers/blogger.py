from pathlib import Path
import inspect
from datetime import datetime
import re
import xmltodict
import json

from utils import loadurlmap, add_syndication, get_content, add_to_listmap, urlmap_to_mdfile, clean_string
from utils import MDSearcher, URLResolver, PostBuilder, CommentBuilder
urlmap = loadurlmap(False)

def import_blogger(importfilepath):
    # resolver = URLResolver()
    # searcher = MDSearcher(resolver=resolver)
    attachments_map = {}
    post_count = 0
    unmatched = []
    importfile = Path(importfilepath)
    with importfile.open(encoding="UTF-8") as fd:
        doc = xmltodict.parse(fd.read())
        with Path("out.json").open("w", encoding="UTF-8") as fw:
            fw.write(json.dumps(doc, indent=2))
        for e in doc["feed"]["entry"]:
            if not isinstance(e["category"], list):
                categories = [e["category"]]
            else:
                categories = e["category"]
            for cat in categories:
                if cat["@term"] == "http://schemas.google.com/blogger/2008/kind#post":
                    post_count = post_count + 1
                    title = e["title"].get("#text")
                    date = datetime.strptime(e["published"][:-10], "%Y-%m-%dT%H:%M:%S") # 2004-09-12T16:42:00.000+08:00
                    url = ""
                    for l in e["link"]:
                        if l["@rel"] == "alternate":
                            url = l['@href']
                            break
                    # if already syndicated, do nothing
                    if url in urlmap:
                        continue
                    # try by title first
                    match = urlmap.get(title)
                    if match is None:
                        match = urlmap.get(clean_string(title))

                    if match is None:
                        unmatched.append(e)
                        # tag:blogger.com,1999:blog-6021610.post-113910668167270022
                        id = e["id"][e["id"].find(".post-")+6:]
                        post = PostBuilder(id, source="royondjango", content=e["content"]["#text"])
                        post.date = date
                        post.kind = "post"
                        post.title = title
                        post.add_syndication("blogger", url)
                        post.save()

                    else:
                        add_syndication(urlmap_to_mdfile(match), url, "blogger", "royondjango")
    print(len(unmatched))
    print(post_count)

import_blogger("C:\\temp\\royondjango-blog-09-21-2019.xml")
