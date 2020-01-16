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
acomments_url = "https://api.stackexchange.com/2.2/answers/%s/comments?order=desc&sort=creation&site=%s&filter=!9Z(-x.Ecg"

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
            # if site != "stackoverflow":
            #     parent = post.get_source_path().parent
            #     for comment in parent.glob("comment*.json"):
            #         print(comment)
            #         os.remove(comment)

            # attempt to get answers to questions
            if site != "stackoverflow":
                url = answers_url % (item["question_id"], site)
                print(url)
                resp = requests.get(url)
                if resp.status_code == 200:
                    resp_json = json.loads(resp.text)
                    print(json.dumps(resp_json, indent=2))
                    for c in resp_json["items"]:
                        cb = CommentBuilder(post.get_source_path())
                        date = time_to_date(c["creation_date"])
                        author_name = c["owner"]["display_name"]
                        author = {
                            "name": c["owner"]["display_name"],
                            "url": c["owner"].get("link"),
                            "photo": c["owner"].get("profile_image"),
                        }
                        cb.add_comment(c["answer_id"], date, author, "stackexchange", html.unescape(c["body_markdown"]), url=item["link"] , overwrite=True)
                else:
                    print("Error")
                    print(resp.status_code)
                    print(json.loads(resp.text)['error_message'])
                    return

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


def gen_answers_url(site, userid):
    answers_url = "https://api.stackexchange.com/2.2/users/%s/answers?site=%s&pagesize=100" % (userid, site)

    resp = requests.get(answers_url)
    if resp.status_code == 200:
        resp_json = json.loads(resp.text)

        # p = Path("d:\\temp\\%s-temp-answers.json" % (site))
        # with p.open("w", encoding='UTF-8') as f:
        #     f.write(json.dumps(resp_json, indent=2))

        aids = []
        qids = []
        # print(len(resp_json["items"]))
        for c in resp_json["items"]:
            aids.append(str(c["answer_id"]))
            qids.append(str(c["question_id"]))

        aids_join = ";".join(aids)
        # print(aids_join)
        # print(len(aids))
        final_url = "https://api.stackexchange.com/2.2/answers/%s?site=%s&pagesize=100&filter=!)snCgsemCXTJsY7Q_IiM" % (aids_join, site)
        final_json = {}
        resp = requests.get(final_url)
        if resp.status_code == 200:
            resp_json = json.loads(resp.text)
            final_json["answers"] = resp_json

        qids_join = ";".join(qids)
        # print(qids_join)
        # print(len(qids))
        final_url = "https://api.stackexchange.com/2.2/questions/%s?site=%s&pagesize=100" % (qids_join, site)
        resp = requests.get(final_url)
        if resp.status_code == 200:
            resp_json = json.loads(resp.text)
            final_json["questions"] = resp_json

        p = Path("d:\\temp\\%s-answers.json" % (site))
        with p.open("w", encoding='UTF-8') as f:
            f.write(json.dumps(final_json, indent=2))



def import_answers(importfilepath, site, extra_tags=[]):
    with Path(importfilepath).open(encoding="UTF-8") as f:
        payload = json.loads(f.read())
        qmap = {}
        print(len(payload["answers"]["items"]))
        for item in payload["questions"]["items"]:
            qmap[item["question_id"]] = item
        for item in payload["answers"]["items"]:
            post = PostBuilder(str(item["answer_id"]), source="stackexchange", content=html.unescape(item["body_markdown"]))
            post.kind = "replies"
            # post.title = html.unescape(item["title"])
            post.date = time_to_date(item["creation_date"])
            post.add_syndication("stackexchange", item["link"])
            post.tags.append("questions")
            post.tags.extend(extra_tags)

            q = qmap[item["question_id"]]

            if "Roy Tang" == q["owner"]["display_name"]:
                # my own answers to my qs are already comments under their related post
                continue

            post.tags = q["tags"]
            post.params["reply_to"] = {
                "type": "stackexchange",
                "url": q["link"],
                "name": q["owner"]["display_name"],
                "label": "'%s' on %s" % (q["title"], site) 
            }

            post.save()            

            # get comments on the question
            if item.get("comment_count", 0) > 1:
                url = acomments_url % (item["answer_id"], site)
                resp = requests.get(url)
                if resp.status_code == 200:
                    resp_json = json.loads(resp.text)
                    print(json.dumps(resp_json, indent=2))
                    for c in resp_json["items"]:
                        cb = CommentBuilder(post.get_source_path())
                        date = time_to_date(c["creation_date"])
                        author_name = c["owner"]["display_name"]
                        author = {
                            "name": c["owner"]["display_name"],
                            "url": c["owner"].get("link"),
                            "photo": c["owner"].get("profile_image"),
                        }
                        cb.add_comment(c["comment_id"], date, author, "stackexchange", html.unescape(c["body_markdown"]), url=item["link"] , overwrite=True)
                else:
                    print("Error")
                    print(resp.status_code)
                    print(json.loads(resp.text)['error_message'])
                    return

# import_qs("d:\\temp\\stackoverflow-questions.json", "stackoverflow", ["stackoverflow", "software development"])
# import_qs("d:\\temp\\superuser-questions.json", "superuser", ["superuser", "tech life"])
# import_qs("d:\\temp\\unix-questions.json", "unix", ["unix", "tech life"])

# gen_answers_url("stackoverflow", 18494)
# gen_answers_url("superuser", 10073)

import_answers("d:\\temp\\stackoverflow-answers.json", "stackoverflow", ["stackoverflow", "software development"])
