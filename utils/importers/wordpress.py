from pathlib import Path
import inspect
from datetime import datetime
import re
import xmltodict

from utils import loadurlmap, add_syndication, get_content, add_to_listmap
from utils import MDSearcher, URLResolver, PostBuilder, CommentBuilder
urlmap = loadurlmap(False)

def import_wp():
    # resolver = URLResolver()
    # searcher = MDSearcher(resolver=resolver)
    attachments_map = {}
    post_count = 0
    importfile = Path("d:\\temp\\ireadcomicbooks.wordpress.2019-09-14.xml")
    with importfile.open(encoding="UTF-8") as fd:
        doc = xmltodict.parse(fd.read())
        for item in doc["rss"]["channel"]["item"]:
            post_type = item["wp:post_type"]
            if post_type == "attachment":
                parent = item["wp:post_parent"]
                add_to_listmap(attachments_map, parent, item)
            elif post_type == "post" and item["wp:status"] == "publish":
                #print(item["title"])
                post_count = post_count + 1
                content = item["content:encoded"]
                content = content.replace("http://ireadcomicbooks.com/wp-content/uploads", "/uploads")
                post = PostBuilder(item["wp:post_name"], source="ireadcomicbooks", content=content)
                post.kind = "post"
                post.params["title"] = item["title"]
                post.params["slug"] = item["wp:post_name"]
                post.tags.append("comics")
                post.date = datetime.strptime(item["wp:post_date"], "%Y-%m-%d %H:%M:%S")
                # post.add_syndication("plurk", plurk_url)
                # post.resolve_links(resolver)
                post.save()
                if "wp:comment" in item:
                    print(item["title"])
                    comment_xml = item["wp:comment"]
                    cb = CommentBuilder(post.get_source_path())
                    date = datetime.strptime(comment_xml['wp:comment_date_gmt'], "%Y-%m-%d %H:%M:%S")
                    author = {
                        "name": comment_xml.get('wp:comment_author'),
                        "url": comment_xml.get('wp:comment_author_url'),
                    }
                    cb.add_comment(comment_xml['wp:comment_id'], date, author, "wordpress", comment_xml['wp:comment_content'], overwrite=True)
    print(post_count)

import_wp()
