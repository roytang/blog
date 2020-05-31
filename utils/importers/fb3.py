import json
from pathlib import Path
from datetime import datetime
import frontmatter
import re, os
import string
from urllib.parse import urlparse, parse_qs, urldefrag
from urllib.error import HTTPError
import urllib.request
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
} # paste the cookie here
cache_folder = Path("D:\\temp\\cache")
save_file = Path("d:\\temp\\out.json")
last_html = Path("D:\\temp\\cache\\last.html")
base_url = "https://m.facebook.com/profile/timeline/stream/?profile_id=632418911"
# base_url = "https://m.facebook.com/profile/timeline/stream/?cursor=AQHRZZP0w6Ci0lRZKPNLsNpupJHCFFX9QpP9h4J68DErLxTQZXFKsepZ3CPxaj0Lb7E4_yWjKJq2kbLviquAPcMAH-RHH3hyfeeW0fXsVBq54uqLPlyXq8n5UIeu_paa7EEj&profile_id=632418911&replace_id=u_0_0"
FOCUS_ID = ""
SINGLE = False
USE_CACHE_COMMENTS = True
USE_CACHE_MAIN = False
ME = "Roy Tang"
parser = "lxml"


def get_text(soup):
    return ' '.join(soup.findAll(text=True))

def get_comments_detail(url, story_id, page=0, replyto=""):

    out_html = cache_folder / "html" / "detail" / (story_id + "-" + str(page) + replyto + ".html")
    if out_html.exists() and USE_CACHE_COMMENTS:
        with out_html.open(encoding="UTF-8") as f:
            text = f.read()
    else:
        req = urllib.request.Request(url, headers=headers)
        try: 
            with urllib.request.urlopen(req) as urlr:
                text = urlr.read()
                with out_html.open("w", encoding="UTF-8") as f:
                    f.write("<!-- " + url + " //-->")
                    f.write(text.decode('utf-8'))
        except urllib.error.HTTPError as e:
            return [ {
                "error": str(e),
                "text": "Could not retrieve comments url",
                "url": url
            }]

    out_comments = []
    soup = BeautifulSoup(text, parser)
    selector = "#m_story_permalink_view > div:nth-child(2) > div > div:nth-child(4) > div"
    if len(replyto) > 0:
        selector = "#root > div > :nth-child(3) > div"
    comments = soup.select(selector)
    for c in comments:
        # print(c["id"])
        # only follow "previous" link
        if c["id"].startswith("see_prev"):
            for link in c.select("a"):
                prev_page_url = "https://m.facebook.com" + link["href"]
                out_comments.extend(get_comments_detail(prev_page_url, story_id, page+1))
            continue
        if c["id"].startswith("comment_replies_more"):
            if c.text.find("previous replies") >= 0:
                for link in c.select("a"):
                    prev_page_url = "https://m.facebook.com" + link["href"]
                    out_comments.extend(get_comments_detail(prev_page_url, story_id, page+1, replyto))
            continue
        if c["id"].startswith("see_next"):
            continue
        comment = { "id" : c["id"] }
        for link in c.select("h3 a"):
            comment["poster"] = link.text
            comment["poster_url"] = link["href"]
        # for a in c.contents[0].contents:
        #     try:
        #         print(a.name, a.text)
        #     except:
        #         print(str(a))
        comment["text"] = get_text(c.contents[0].contents[1])
        # meta row contains the date
        if len(c.contents[0].contents) >= 4:
            for abbr in c.contents[0].contents[3].select("abbr"):
                comment["date"] = abbr.text
        if len(replyto) > 0:
            comment["replyto"] = replyto
        # check if replies link exists
        if len(c.contents[0].contents) >= 5:
            for link in c.contents[0].contents[4].select("a"):
                replies_url = "https://m.facebook.com" + link["href"]
                comment["replies"] = (get_comments_detail(replies_url, story_id, page, c["id"]))
        out_comments.append(comment)

    return out_comments

def parse_container(child):
    item = {"attachments":[]}

    story_id = None
    comments_link = None
    # find the permalink via the comments anchor
    for link in child.select("a"):
        if link.text.find("Comment") >= 0:
            comments_link = link
            comments_link_url = "https://m.facebook.com" + link["href"]
            u = urlparse(comments_link_url)
            qparams = parse_qs(u.query)
            arr = qparams.get("fbid", qparams.get("story_fbid"))
            if arr is not None and len(arr) > 0:
                story_id = arr[0]

    item["metadata"] = {}
    if child.get("data-ft") is not None:
        item["metadata"] = json.loads(child["data-ft"])
        if story_id is None:
            story_id = item["metadata"].get("mf_story_key", item["metadata"].get("top_level_post_id"))

    if story_id is None:
        return []

    item["permalink"] = "https://www.facebook.com/stephen.roy.tang/posts/" + story_id

    if len(FOCUS_ID) > 0 and story_id != FOCUS_ID:
        return []

    print(story_id)
    if story_id is None:
        # recursing 
        items = []
        for article in child.select("article"):
            items.extend(parse_container(article))
        return items

    if child.text.find("for your birthday") >= 0:
        item["type"] = "bday"
        item["details"] = get_text(child)
        return [item]
    children2 = child.contents
    header = None
    body = None
    footer = None
    # print(child.prettify())
    print(len(children2))
    if len(children2) == 2:
        footer = children2[1]
        body = children2[0]
        if body.text.find("posted on your") >= 0 or body.text.find("posted from") >= 0 or body.text.find(" is playing ") >= 0:
            # recursing 
            items = []
            for article in footer.select("article"):
                items.extend(parse_container(article))
            return items
    elif len(children2) == 3:
        header = children2[0]
        body = children2[1]
        footer = children2[2]
        if len(body.text.strip()) == 0:
            body = children2[0]
            header = None
        if body.text.find("was tagged") >= 0:
            body = footer.contents[0]
            footer = footer.contents[1]
    elif len(children2) == 1:
        print("ERROR")
        item["type"] = "error"
        item["desc"] = get_text(child)
        return [item]

    date_containers = footer.select("abbr")
    for dc in date_containers:
        item["date"] = dc.text
    print(body.text)
    actual_contents = body.contents

    if len(actual_contents) == 1:
        if header is not None and header.text.find(" is playing "):
            item["text"] = get_text(body)
            for link in body.select("a"):
                item["url"] = link["href"]
            items = []
            for article in footer.select("article"):
                items.extend(parse_container(article))
            item["subitems"] = items
            return [item]

    item["text"] = actual_contents[1].text
    for link in actual_contents[0].select("a"):
        item["poster_url"] = link["href"].split("?")[0]
        item["poster"] = link.text
        if len(link.text.strip()) > 0:
            break

    # get comments, but only if it's my content
    if comments_link is not None and not comments_link.text.startswith("Comment") and item["poster"] == ME:
        item["comments"] = get_comments_detail(comments_link_url, story_id)


    if len(actual_contents) > 2:
        print("Getting attachment")
        # attachment exists
        if "original_content_id" in item["metadata"] and len(actual_contents[2].select("h3 a")) > 0:
            # attachment is a repost
            item["repost"] = True
            for link in actual_contents[2].select("h3 a"):
                poster = link.text
                raw_poster_url = link["href"].split("?")[0]
                poster_url = "https://www.facebook.com" + raw_poster_url
                break # only the first link is the poster
            all_details = []
            for link in actual_contents[2].select("a"):
                link_text = link.text
                url = link.get("href")
                if url is None:
                    continue
                raw_url = url.split("?")[0]
                # skip any links to the poster profile
                if link_text == poster or raw_url == raw_poster_url:
                    continue
                # compose the permalink
                u = urlparse(url)
                qparams = parse_qs(u.query)
                story_id = qparams.get("fbid", qparams.get("story_fbid"))
                if story_id is not None:
                    url = poster_url + "/posts/" + story_id[0]
                
                src_url = link["href"]
                if src_url.startswith("https://lm.facebook.com"): # external link
                    u = urlparse(src_url)
                    qparams = parse_qs(u.query)
                    details = {
                        "url": qparams.get("u")
                    }
                else:
                    src_url = link["href"]
                    if not src_url.startswith("http"):
                        src_url = "https://m.facebook.com" + src_url
                    details = get_link_details(src_url)
                details["text"] = get_text(link)
                details["src_url"] = src_url

                all_details.append(details)

            item["attachments"].append({
                "type": "repost",
                "poster": poster,
                "poster_url": poster_url,
                "url": url,
                "desc": get_text(actual_contents[2]),
                "details": all_details
            })
        else:
            # attachment is photo or link
            for link in actual_contents[2].select("a"):
                url = link["href"]
                if url.startswith("/photo.php"):
                    # image attachment, find the image tag
                    imgs = link.select("img")
                    for img in imgs:
                        item["attachments"].append({
                            "type": "photo",
                            "url": img["src"],
                            "desc": img["alt"]
                        })
                    # TODO: Download the images if they're not from me
                if url.startswith("https://lm.facebook.com"): # external link
                    u = urlparse(url)
                    qparams = parse_qs(u.query)
                    desc = ""
                    for h3 in actual_contents[2].select("h3"):
                        desc = h3.text
                    item["attachments"].append({
                        "type": "link",
                        "url": qparams["u"][0],
                        "desc": desc
                    })
            if len(item["attachments"]) == 0:
                img_url = ""
                for img in actual_contents[2].select("img"):
                    img_url = img["src"]
                    if img_url.find("safe_image.php") >= 0:
                        u = urlparse(img_url)
                        qparams = parse_qs(u.query)
                        img_url = qparams["url"][0]

                u = urlparse(img_url)
                filename = u.path.split("/")[-1]
                download_to = cache_folder / "dls" / filename

                if not download_to.exists():
                    try: 
                        # download the image
                        opener = urllib.request.build_opener()
                        opener.addheaders = list(map(lambda x: (x, headers[x]), headers))
                        urllib.request.install_opener(opener)
                        urllib.request.urlretrieve(img_url, str(download_to))
                    except urllib.error.HTTPError as e:
                        download_to = e
                    except urllib.error.URLError as e:
                        download_to = e


                item["attachments"].append({
                    "type": "unknown",
                    "url": "",
                    "img_url": img_url,
                    "downloaded": str(download_to), 
                    "desc": get_text(actual_contents[2])
                })
    return [item]

def get_timeline():

    url_next = base_url
    items = []
    index = 0
    try:
        while len(url_next) > 0:
            index = index + 1
            out_html = cache_folder / "html" / (str(index) + ".html")

            if out_html.exists() and USE_CACHE_MAIN:
                with out_html.open(encoding="UTF-8") as f:
                    text = f.read()
            else:
                req = urllib.request.Request(url_next, headers=headers)
                next_link = ""
                with urllib.request.urlopen(req) as url:
                    text = url.read()
                    with last_html.open("w", encoding="UTF-8") as f:
                        f.write(text.decode('utf-8'))
                    with out_html.open("w", encoding="UTF-8") as f:
                        f.write("<!-- " + url_next + " //-->")
                        f.write(text.decode('utf-8'))
            soup = BeautifulSoup(text, parser)
            # print(soup)
            # break
            links = soup.find_all("a")
            for link in links:
                if link.text.find("See More Stories") >= 0:
                    next_link = "https://m.facebook.com" + link["href"]
            containers = soup.select("#structured_composer_async_container > *:nth-child(1)")
            for c in containers:
                for child in c.contents:
                    # print(json.dumps(item, indent=2))
                    for item in parse_container(child):
                        if item is not None:
                            item["source_url"] = url_next
                            item["source_downloaded"] = str(out_html)
                        items.append(item)
            url_next = next_link
            print("#### " + url_next)
            if SINGLE:
                break
    # except Exception as e:
    #     print(e)
    finally:
        with save_file.open("w", encoding="UTF-8") as f:
            f.write(json.dumps(items, indent=2))
        print("Done")

def get_link_details(url):
    # print("Getting link details")
    # print(url)
    if url.startswith("https://m.facebook.com/video_redirect/"):
        u = urlparse(url)
        qparams = parse_qs(u.query)
        return {
            "type": "video",
            "desc": "",
            "url": qparams.get("src")
        }

    req = urllib.request.Request(url, headers=headers)
    try: 
        with urllib.request.urlopen(req) as urlr:
            text = urlr.read()
            soup = BeautifulSoup(text, parser)
            # print(soup.prettify())
            for i in soup.select("#MPhotoActionbar"):
                # indicates a photo
                mode = "PHOTO"
                desc = ""
                for d in soup.select("div.msg"):
                    el = d.contents[2]
                    # sometimes there's a space that gets returned as d.contents[2], 
                    # when that happens skip to next sibling
                    while el.name is None:
                        el = el.next_sibling
                    desc = get_text(el)
                imgs = soup.select("img.img")
                out_url = imgs[1]["src"]

                u = urlparse(out_url)
                filename = u.path.split("/")[-1]
                download_to = cache_folder / "dls" / filename

                if not download_to.exists():
                    try: 
                        # download the image
                        opener = urllib.request.build_opener()
                        opener.addheaders = list(map(lambda x: (x, headers[x]), headers))
                        urllib.request.install_opener(opener)
                        urllib.request.urlretrieve(out_url, str(download_to))
                    except urllib.error.HTTPError as e:
                        download_to = e

                return {
                    "type": "photo",
                    "desc": desc,
                    "url": out_url,
                    "orig_url": url,
                    "downloaded": str(download_to)
                }

            for div in soup.select("#m_story_permalink_view > div > div > div > div:nth-child(2)"):
                mode = "STORY"
                return {
                    "desc": div.prettify(),
                    "type": "story"
                }

            # print(soup.prettify())

            if soup.text.find("You can try again later.") >= 0:
                return {
                    "type": "rate-limited",
                    "url": url
                }

            return {
                "type": "ERROR",
                "desc": get_text(soup),
                "url": url
            }
    except urllib.error.HTTPError as e:
        return {
            "type": "ERROR",
            "desc": str(e),
            "url": url
        }

def verify():
    with save_file.open(encoding="UTF-8") as f:
        data = json.loads(f.read())

        print(len(data))

        posters = {}
        for item in data:
            poster = item.get("poster", "")
            if poster not in posters:
                posters[poster] = 1
            else:
                posters[poster] = posters[poster] + 1

        print(json.dumps(posters, indent=2))

verify()

# get_timeline()

