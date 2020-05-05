# One off: Imported wp comments do not have line breaks correctly formatted. Fix them!
from pathlib import Path
import inspect
from datetime import datetime
import re
import xmltodict
import collections
import json
from importers.utils import loadurlmap, urlmap_to_mdfile
import shutil

def import_wp():
    # index all the comments
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "post"
    # collect all plurk related comments that don't have an existing index.md in same folder
    all_comments_by_date = {}
    for jsonfile in p.glob("**/comment-*-wp-*.json"):
        # print(jsonfile)
        with jsonfile.open(encoding="UTF-8") as f:
            jsondata = json.loads(f.read())
            date = jsondata["date"]
            # print(date)
            if date in all_comments_by_date:
                print(jsonfile)
                print(date)
            else:
                all_comments_by_date[date] = jsonfile

    post_count = 0
    importfile = Path("d:\\temp\\roytang.WordPress.2020-05-05.xml")

    with importfile.open(encoding="UTF-8") as fd:
        doc = xmltodict.parse(fd.read())
        for item in doc["rss"]["channel"]["item"]:
            post_type = item["wp:post_type"]
            if post_type == "attachment":
                # parent = item["wp:post_parent"]
                # add_to_listmap(attachments_map, parent, item)
                pass
            elif post_type == "post" and item["wp:status"] == "publish":
                # print(item["title"])
                if "wp:comment" in item:
                    all_comment_xml = item["wp:comment"]
                    if not hasattr(all_comment_xml, "append"): # if not a list, make a list
                        all_comment_xml = [all_comment_xml]
                    for comment_xml in all_comment_xml:
                        post_count = post_count + 1
                        date = comment_xml['wp:comment_date']
                        # if date == '0000-00-00 00:00:00':
                        #     date = comment_xml['wp:comment_date']
                        # print(date)
                        if date not in all_comments_by_date:
                            # if True or comment_xml['wp:comment_type'] is None:
                            #     print(date)
                            #     print(comment_xml['wp:comment_author'])
                            #     print(comment_xml['wp:comment_type'])
                            pass
                        else:
                            jsonfile = all_comments_by_date[date]
                            content = comment_xml['wp:comment_content']
                            with jsonfile.open(encoding="UTF-8") as f:
                                jsondata = json.loads(f.read())
                            jsondata["text"] = content # replace the content
                            with jsonfile.open("w", encoding="UTF-8") as f:
                                f.write(json.dumps(jsondata, indent=2))
                            #print(json.dumps(jsondata, indent=2))

    print(post_count)

def import_wp_social():
    post_count = 0
    importfile = Path("d:\\temp\\roytang.WordPress.2020-05-05.xml")
    urlmap = loadurlmap()

    with importfile.open(encoding="UTF-8") as fd:
        doc = xmltodict.parse(fd.read())
        for item in doc["rss"]["channel"]["item"]:
            post_type = item["wp:post_type"]
            if post_type == "attachment":
                # parent = item["wp:post_parent"]
                # add_to_listmap(attachments_map, parent, item)
                pass
            elif post_type == "post" and item["wp:status"] == "publish":
                # print(item["title"])
                found_comments = []
                if "wp:comment" in item:
                    all_comment_xml = item["wp:comment"]
                    if not hasattr(all_comment_xml, "append"): # if not a list, make a list
                        all_comment_xml = [all_comment_xml]
                    for comment_xml in all_comment_xml:
                        post_count = post_count + 1
                        date = comment_xml['wp:comment_date']
                        if not comment_xml['wp:comment_type'] is None:
                            # print(date)
                            # print(comment_xml['wp:comment_author'])
                            # print(comment_xml['wp:comment_type'])
                            # print(comment_xml['wp:comment_content'])
                            found_comments.append(comment_xml)
                if len(found_comments) > 0:
                    link = item["link"]
                    rel_path = link.replace("http://wordpress.roytang.net", "")
                    if rel_path not in urlmap:
                        print("MISSING")
                        print(rel_path)
                    else:
                        um = urlmap[rel_path]
                        mdfile = urlmap_to_mdfile(um)
                        print(mdfile)
                        if mdfile.stem != "index":
                            newdir = mdfile.parent / mdfile.stem
                            if not newdir.exists():
                                newdir.mkdir()
                            newfile = newdir / "index.md"
                            shutil.move(mdfile, newfile)
                            mdfile = newfile

                        # for comment in found_comments:
                        #     id = "webmention-%s" % (link["wm-id"])
                        #     datestr = date.strftime('%Y%m%dT%H%M%S')
                        #     wtype = link['wm-property']
                        #     if wtype == 'like-of':
                        #         newfile = newdir / ( "like-%s-%s.json" % (datestr, id) )
                        #     elif wtype == 'repost-of':
                        #         newfile = newdir / ( "repost-%s-%s.json" % (datestr, id) )
                        #     # elif wtype == 'mention-of':
                        #     #     newfile = newdir / ( "mention-%s-%s.json" % (datestr, id) )
                        #     else:
                        #         newfile = newdir / ( "comment-%s-%s.json" % (datestr, id) )

                        #     comment = {
                        #         "id": id,
                        #         "name": link['author']['name'],
                        #         "url": link['author'].get('url', ''),
                        #         "text": link.get("content", {}).get("text", ""), 
                        #         "date": date.strftime("%Y-%m-%d %H:%M:%S"),
                        #         "photo": link['author'].get('photo', ''),
                        #         "source_url": link["wm-source"],
                        #         "mention_url": link["url"],
                        #         "source": "webmention",
                        #         "type": wtype
                        #     }

                        #     # save the comment into newdir
                        #     if not newfile.exists():
                        #         with Path(newfile).open("w", encoding="UTF-8") as f:
                        #             f.write(json.dumps(comment))                            

    print(post_count)

import_wp_social()


