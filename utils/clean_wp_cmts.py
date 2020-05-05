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

                        newdir = mdfile.parent
                        for comment in found_comments:
                            id = "wp-%s" % (comment["wp:comment_id"])
                            date = datetime.strptime(comment['wp:comment_date'], "%Y-%m-%d %H:%M:%S")
                            datestr = date.strftime('%Y%m%dT%H%M%S')
                            comment_type = comment["wp:comment_type"]
                            # print(comment_type)
                            if comment_type == "social-facebook-like":
                                wtype = "like-of"
                                newfile = newdir / ( "like-%s-%s.json" % (datestr, id) )
                            elif comment_type == "social-twitter-rt":
                                wtype = "repost-of"
                                newfile = newdir / ( "repost-%s-%s.json" % (datestr, id) )
                            else:
                                wtype = "in-reply-to"
                                newfile = newdir / ( "comment-%s-%s.json" % (datestr, id) )

                            photo_url = ""
                            social_id = ""
                            social_url = ""
                            for cm in comment["wp:commentmeta"]:
                                if cm['wp:meta_key'] == 'social_profile_image_url':
                                    photo_url = cm['wp:meta_value']
                                if cm['wp:meta_key'] == 'social_status_id':
                                    social_id = cm['wp:meta_value']
                            if comment_type.find("facebook") >= 0:
                                post_id = social_id.split("_")[1]
                                social_url = "https://www.facebook.com/stephen.roy.tang/posts/%s" % (post_id)
                                photo_url = "/img/icons/facebook.png"
                            if comment_type.find("twitter") >= 0:
                                photo_url = "/img/icons/twitter.png"

                            comment = {
                                "id": id,
                                "name": comment["wp:comment_author"],
                                "url": comment["wp:comment_author_url"],
                                "text": comment["wp:comment_content"], 
                                "date": date.strftime("%Y-%m-%d %H:%M:%S"),
                                "photo": photo_url,
                                "source_url": social_url,
                                "mention_url": social_url,
                                "source": "wordpress-social",
                                "type": wtype,
                                "raw_source": comment
                            }

                            # save the comment into newdir
                            if not newfile.exists():
                                with Path(newfile).open("w", encoding="UTF-8") as f:
                                    f.write(json.dumps(comment, indent=2))

    print(post_count)

import_wp_social()


