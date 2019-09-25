import json
from pathlib import Path
from datetime import datetime
import frontmatter
import re
import string
from urllib.parse import urlparse, parse_qs, urldefrag
from urllib.error import HTTPError
import urllib.request

from utils import loadurlmap, add_syndication, get_content, add_to_listmap, contentdir
from utils import MDSearcher, URLResolver, PostBuilder, CommentBuilder
urlmap = loadurlmap(False)

# with Path("d:\\temp\\anchors.json").open() as f:
#     anchors = json.loads(f.read())

def resolve_anchor(anchor):
    
    updatedmap = False
    with Path("d:\\temp\\anchors-map.json").open() as f:
        anchors_map = json.loads(f.read())

    try:
        headers = {'cookie': 'fr=127WU1jfpIR0FRPvt.AWVkfpSTP_5fZQLs-toN02YwP4Y.BdikZ7.C5.AAA.0.0.BdirNU.AWWocTWG; sb=e0aKXVXW-PROS0DOzyumyh3E; datr=e0aKXYHXDXShgDwoImFBEJVj; wd=1271x966; c_user=632418911; xs=2%3AjWZ-uf-aKM6b6w%3A2%3A1569343105%3A17543%3A8112; spin=r.1001210818_b.trunk_t.1569343106_s.1_v.2_; act=1569367243840%2F0; presence=EDvF3EtimeF1569372106EuserFA2632418911A2EstateFDutF1569372106676CEchFDp_5f632418911F1CC'} # paste the cookie here
        if anchor in anchors_map:
            return anchors_map[anchor]
        req = urllib.request.Request(anchor, headers=headers)
        response = urllib.request.urlopen(req)
        anchors_map[anchor] = response.geturl()
        updatedmap = True
        return anchors_map[anchor]
    except Exception as e:
        print(e)
    finally:
        if updatedmap:
            with Path("d:\\temp\\anchors-map.json").open("w") as f:
                f.write(json.dumps(anchors_map, indent=2))

from bs4 import BeautifulSoup

def import_photos(photo_export_filepath, photo_loc_template, tags):
    fb_url_template = "https://www.facebook.com/stephen.roy.tang/posts/%s"
    map_by_date = {}
    with Path(photo_export_filepath).open(encoding="UTF-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        items = soup.findAll("div", {"class": "pam"})
        for item in items:
            fb_url = ""
            photo_location = ""
            caption = ""
            datestr = ""
            anchors = item.find_all('a')
            for a in anchors:
                url = a["href"]
                if url.find("www.facebook.com") >= 0:
                    fb_url = resolve_anchor(url)
                    datestr = a.text
                else:
                    photo_location = url
                    caption = a.find_next("div").text
            u = urlparse(fb_url)
            fbid = parse_qs(u.query)['fbid'][0]
            fb_url = fb_url_template % (fbid)
            # Dec 15, 2015, 3:22 AM
            date = datetime.strptime(datestr, "%b %d, %Y, %I:%M %p")

            add_to_listmap(map_by_date, datestr, {
                "fb_url": fb_url,
                "fb_id": fbid,
                "caption": caption.replace("Upload IP Address", ""),
                "date": datestr,
                "photo_location": photo_location
            })

    #print(json.dumps(map_by_date, indent=2))

    searcher = MDSearcher()

    for k in map_by_date:
        v = map_by_date[k]
        # determine the overall caption for the post, if any
        caption = None
        first_id = None
        for item in v:
            if first_id is None:
                first_id = item["fb_id"]
            if len(item["caption"]) > 0:
                if caption is None:
                    caption = item["caption"]
                else:
                    print("#### Well, now what?")
        date = datetime.strptime(k, "%b %d, %Y, %I:%M %p")

        # clean tagged users in caption
        # @[< numeric id>:< something?? >:< name >]
        # (@\[\d+:\d+:[A-Za-z\s]+\])
        parsed_tags = re.findall(r"@\[\d+:\d+:[A-Za-z\s]+\]", caption)
        for tag in parsed_tags:
            # remove outer @[] and split by :
            tagparts = tag[2:-1].split(":")
            replacement = "[%s](https://www.facebook.com/%s)" % (tagparts[2], tagparts[0])
            caption = caption.replace(tag, replacement)
        print(caption)
        datestr = date.strftime("%Y-%m-%d")
        if caption is not None:
            info = searcher.find_by_day_and_text(datestr, caption)
        else:
            caption = ""
        if info is not None:
            for item in v:
                add_syndication(Path(info["file"]), item["fb_url"], "facebook")
        else:
            post = PostBuilder(first_id, source="facebook", content=caption)
            post.date = date
            post.kind = "photos"
            for item in v:
                post.add_syndication("facebook", item["fb_url"])
                photo_loc = photo_loc_template % (item["photo_location"])
                post.media.append(photo_loc)
            post.tags.extend(tags)
            post.save()

import_photos("D:/temp/facebook/photos_and_videos/album/16.html", "file://d:/temp/facebook/%s", ["pickups"])
