import frontmatter
import json
import requests
import urllib.request
from urllib.parse import urlparse, parse_qs, urldefrag
from urllib.error import HTTPError
import sys
from pathlib import Path
import os, shutil
import inspect
from datetime import datetime
import re
import html

from utils import loadurlmap, add_syndication, get_content, add_to_listmap, contentdir, time_to_date
from utils import MDSearcher, URLResolver, PostBuilder, CommentBuilder
#urlmap = loadurlmap(False)

answers_url = "https://api.stackexchange.com/2.2/questions/%s/answers?order=desc&sort=activity&site=%s&filter=!9Z(-wzftf"
qcomments_url = "https://api.stackexchange.com/2.2/questions/%s/comments?order=desc&sort=creation&site=%s&filter=!9Z(-x.Ecg"

def import_qs(importfilepath, site, extra_tags=[]):
    with Path(importfilepath).open(encoding="UTF-8") as f:
        payload = json.loads(f.read())
        for item in payload["items"]:
            post = PostBuilder(str(item["question_id"]), source="stackexchange", content=html.unescape(item["body_markdown"]))
            post.title = html.unescape(item["title"])
            post.date = time_to_date(item["creation_date"])
            post.add_syndication("stackexchange", item["link"])
            post.tags = item["tags"]
            post.tags.append("questions")
            post.tags.extend(extra_tags)
            post.save()            

            # delete comments
            if site != "stackoverflow":
                parent = post.get_source_path().parent
                for comment in parent.glob("comment*.json"):
                    print(comment)
                    os.remove(comment)


            # attempt to get answers to questions
            # url = answers_url % (item["question_id"], site)
            # resp = requests.get(url)
            # if resp.status_code == 200:
            #     resp_json = json.loads(resp.text)
            #     print(json.dumps(resp_json, indent=2))
            #     for c in resp_json["items"]:
            #         cb = CommentBuilder(post.get_source_path())
            #         date = time_to_date(c["creation_date"])
            #         author_name = c["owner"]["display_name"]
            #         author = {
            #             "name": c["owner"]["display_name"],
            #             "url": c["owner"].get("link"),
            #             "photo": c["owner"].get("profile_image"),
            #         }
            #         cb.add_comment(c["answer_id"], date, author, "stackexchange", html.unescape(c["body_markdown"]), url=item["link"] , overwrite=True)

            # get comments on the question
            # url = qcomments_url % (item["question_id"], site)
            # resp = requests.get(url)
            # if resp.status_code == 200:
            #     resp_json = json.loads(resp.text)
            #     print(json.dumps(resp_json, indent=2))
            #     for c in resp_json["items"]:
            #         cb = CommentBuilder(post.get_source_path())
            #         date = time_to_date(c["creation_date"])
            #         author_name = c["owner"]["display_name"]
            #         author = {
            #             "name": c["owner"]["display_name"],
            #             "url": c["owner"].get("link"),
            #             "photo": c["owner"].get("profile_image"),
            #         }
            #         cb.add_comment(c["comment_id"], date, author, "stackexchange", html.unescape(c["body_markdown"]), url=item["link"] , overwrite=True)
            # else:
            #     print("Error")
            #     print(resp.status_code)
            #     print(json.loads(resp.text)['error_message'])
            #     return


import_qs("d:\\temp\\stackoverflow-questions.json", "stackoverflow", ["stackoverflow", "software development"])
import_qs("d:\\temp\\superuser-questions.json", "superuser", ["superuser", "tech life"])
import_qs("d:\\temp\\unix-questions.json", "unix", ["unix", "tech life"])
