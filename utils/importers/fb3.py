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
    'cookie': 'fr=103AEBsct6KCQRsmx.AWXg0HaUWnFqQ_3rnAzNqNqao0Y.BdjKWd.Z_.F29.0.0.Be0NDc.AWURYLd1; datr=naWMXY6J_4tOd8nfDzUs7oCI; sb=pKWMXWmDVFUG9iVOfr8b_QM9; c_user=632418911; xs=42%3Af_gMqEFxvrASow%3A2%3A1569498532%3A17543%3A8112; wd=1920x938; presence=EDvF3EtimeF1590743260EuserFA2632418911A2EstateFDsb2F1590725822102EatF1590727055434Et3F_5bDiFA2thread_3a1474557102572072A2EoF1EfF1CAcDiFA2thread_3a537742362963432A2EoF2EfF2CAcDiFA2user_3a623410364A2EoF3EfF3C_5dEutc3F1590716747909G590727055446CEchF_7bCC; act=1590707590692%2F19; spin=r.1002174684_b.trunk_t.1590687066_s.1_v.2_',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
} # paste the cookie here
cache_folder = Path("D:\\temp\\cache")
last_html = Path("D:\\temp\\cache\\last.html")

def parse_container(child):
    item = {"attachments":[]}
    if child.get("data-ft") is not None:
        item["metadata"] = json.loads(child["data-ft"])
        story_id = item["metadata"].get("mf_story_key", item["metadata"].get("top_level_post_id"))
        # if story_id != "10150117629288912":
        #     return []
        print(story_id)
        if story_id is None:
            # recursing 
            items = []
            for article in child.select("article"):
                items.extend(parse_container(article))
            return items
        item["permalink"] = "https://www.facebook.com/stephen.roy.tang/posts/" + story_id
    else:
        item["metadata"] = {}
        # find the permalink via the comments anchor
        for link in child.select("a"):
            if link.text.find("Comment") >= 0:
                link_url = "https://m.facebook.com" + link["href"]
                u = urlparse(link_url)
                qparams = parse_qs(u.query)
                story_id = qparams.get("fbid", qparams.get("story_fbid"))[0]
                item["permalink"] = "https://www.facebook.com/stephen.roy.tang/posts/" + story_id
                break

    if child.text.find("for your birthday") >= 0:
        item["type"] = "bday"
        item["details"] = child.text
        return [item]
    children2 = child.contents
    header = None
    body = None
    footer = None
    if len(children2) == 2:
        footer = children2[1]
        body = children2[0]
        if body.text.find("posted on your") >= 0:
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
        return [item]

    date_containers = footer.select("abbr")
    for dc in date_containers:
        item["date"] = dc.text
    actual_contents = body.contents
    item["text"] = actual_contents[1].text
    for link in actual_contents[0].select("a"):
        item["poster_url"] = link["href"].split("?")[0]
        item["poster"] = link.text
        if len(link.text.strip()) > 0:
            break
    if len(actual_contents) > 2:
        print("Getting attachment")
        # attachment exists
        if "original_content_id" in item["metadata"] and len(actual_contents[2].select("h3 a")) > 0:
            # attachment is a repost
            item["repost"] = True
            for link in actual_contents[2].select("h3 a"):
                poster = link.text
                poster_url = link["href"].split("?")[0]
                poster_url = "https://www.facebook.com" + poster_url
                break # only the first link is the poster
            all_details = []
            for link in actual_contents[2].select("a"):
                link_text = link.text
                if link_text == poster:
                    continue # we already got this link
                url = link.get("href")
                if url is None:
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
                    details = qparams.get("u")
                else:
                    src_url = link["href"]
                    if not src_url.startswith("http"):
                        src_url = "https://m.facebook.com" + src_url
                    details = get_link_details(src_url)

                all_details.append(details)

            item["attachments"].append({
                "type": "repost",
                "poster": poster,
                "poster_url": poster_url,
                "src_url": src_url,
                "url": url,
                "desc": actual_contents[2].text,
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
                    "desc": actual_contents[2].text
                })
    return [item]

def get_timeline():

    base_url = "https://m.facebook.com/profile/timeline/stream/?profile_id=632418911"
    # base_url = "https://m.facebook.com/profile/timeline/stream/?cursor=AQHRNHzgDUaMNRbvinfasyPFur6eI6Xwm3DVx_2Dyppn5zgNwAwJCE4JFISOBVCjdRvz2QDXgLMbAET6Fw4_pQZ6zYUDtM5L-W3V6p6CUAv9Q5GlGqq6dvVXAi-EjHDJM-2m&profile_id=632418911&replace_id=u_0_0"
    url_next = base_url
    items = []
    index = 0
    try:
        while len(url_next) > 0:
            index = index + 1
            out_html = cache_folder / "html" / (str(index) + ".html")

            req = urllib.request.Request(url_next, headers=headers)
            next_link = ""
            with urllib.request.urlopen(req) as url:
                text = url.read()
                with last_html.open("w", encoding="UTF-8") as f:
                    f.write(text.decode('utf-8'))
                with out_html.open("w", encoding="UTF-8") as f:
                    f.write("<!-- " + url_next + " //-->")
                    f.write(text.decode('utf-8'))
                soup = BeautifulSoup(text, "html.parser")
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
            # break
    # except Exception as e:
    #     print(e)
    finally:
        with Path("d:\\temp\\out.json").open("w", encoding="UTF-8") as f:
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
            soup = BeautifulSoup(text, "html.parser")
            # print(soup.prettify())
            for i in soup.select("#MPhotoActionbar"):
                # indicates a photo
                mode = "PHOTO"
                for d in soup.select("div.msg"):
                    el = d.contents[2]
                    # sometimes there's a space that gets returned as d.contents[2], 
                    # when that happens skip to next sibling
                    while el.name is None:
                        el = el.next_sibling
                    desc = el.text
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
                    "downloaded": str(download_to)
                }

            for div in soup.select("#m_story_permalink_view > div > div > div > div:nth-child(2)"):
                mode = "STORY"
                return {
                    "desc": div.prettify(),
                    "type": "story"
                }

            # print(soup.prettify())
            return {
                "type": "ERROR",
                "url": url
            }
    except urllib.error.HTTPError as e:
        return {
            "type": "ERROR",
            "desc": str(e),
            "url": url
        }


get_timeline()

# src_url = "https://m.facebook.com/story.php?story_fbid=10158244363002497&id=508217496&_ft_=mf_story_key.10158473723063912%3Atop_level_post_id.10158473723063912%3Atl_objid.10158473723063912%3Acontent_owner_id_new.632418911%3Aoriginal_content_id.10158244363002497%3Aoriginal_content_owner_id.508217496%3Athrowback_story_fbid.10158473723063912%3Astory_location.4%3Athid.632418911%3A306061129499414%3A2%3A0%3A1590994799%3A3441436630452290644&__tn__=%2AsH-R"
# print(get_link_details(src_url))