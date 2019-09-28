import json
from pathlib import Path
from datetime import datetime
import frontmatter
import re, os
import string
from urllib.parse import urlparse, parse_qs, urldefrag
from urllib.error import HTTPError
import urllib.request

from utils import loadurlmap, add_syndication, get_content, add_to_listmap, contentdir, urlmap_to_mdfile, clean_string
from utils import MDSearcher, URLResolver, PostBuilder, CommentBuilder
urlmap = loadurlmap(False)
postsfile = Path("d:\\temp\\fbposts.json")

excludefile = Path("d:\\temp\\fb-exclude.json")
excludes = []
with excludefile.open() as f:
    excludes = json.loads(f.read())
def exclude_id(fbid):
    rawfbid = fbid
    colonidx = fbid.rfind(":")
    if colonidx >= 0:
        rawfbid = fbid[:colonidx]
    if rawfbid in excludes:
        return True
    return False


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
        print(anchor)
    finally:
        if updatedmap:
            with Path("d:\\temp\\anchors-map.json").open("w") as f:
                f.write(json.dumps(anchors_map, indent=2))

from bs4 import BeautifulSoup

## merge: combine posts where applicable
def import_photos(photo_export_filepath, photo_loc_template, tags, merge=False):

    # load the posts data for use in grouping the photos under a post id
    postsmap = {}
    with postsfile.open(encoding="UTF-8") as f:
        posts = json.loads(f.read())
        for post in posts:
            # colonidx = post["url"].rfind(":")
            # if colonidx >= 6: # ignore the one in https://
            #     post["url"] = post["url"][:colonidx]
            for m in post["media"]:
                postsmap[m] = post

    fb_url_template = "https://www.facebook.com/stephen.roy.tang/posts/%s"
    photosmap = {}
    with Path(photo_export_filepath).open(encoding="UTF-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        items = soup.findAll("div", {"class": "pam"})
        count = 0
        for item in items:
            fb_url = ""
            photo_location = ""
            caption = ""
            datestr = ""
            anchors = item.find_all('a')
            for a in anchors:
                url = a["href"]
                if url.find("https://www.facebook.com") >= 0:
                    fb_url = resolve_anchor(url)
                    datestr = a.text
                else:
                    photo_location = url
                    nextdiv = a.find_next_sibling("div", {"class": "_3-95"})
                    if nextdiv is not None:
                        caption = nextdiv.text
            # if not fb_url.startswith("https://www.facebook.com/photo.php?fbid=10157592577573912"):
            #     continue
            u = urlparse(fb_url)
            qparams = parse_qs(u.query)
            if 'fbid' in qparams:
                fbid = parse_qs(u.query)['fbid'][0]
            else:
                fbid = Path(fb_url).stem
            # remove the :N at the end of fb urls
            colonidx = fbid.find(":")
            if colonidx >= 0:
                fbid = fbid[:colonidx]
            if exclude_id(fbid):
                continue
            fb_url = fb_url_template % (fbid)
            # Dec 15, 2015, 3:22 AM
            date = datetime.strptime(datestr, "%b %d, %Y, %I:%M %p")

            photo = {
                "fb_url": fb_url,
                "fb_id": fbid,
                "caption": caption.replace("Upload IP Address", ""),
                "date": datestr,
                "photo_location": photo_location
            }
            if photo_location in postsmap:
                # group by post url
                photo["post"] = postsmap[photo_location]
                #photo["post"]["new_fb_url"] = fb_url
                add_to_listmap(photosmap, fb_url, photo)

    # print(json.dumps(photosmap, indent=2))
    # return

    if merge:
        oldphotosmap = photosmap
        photosmap = {}
        # Rewrite the photosmap
        for k in oldphotosmap:
            v = oldphotosmap[k]
            for photo in v:
                post_url = photo["post"]["url"]
                colonidx = post_url.rfind(":")
                if colonidx > 10: # ignore the colon in https://
                    post_url = post_url[:colonidx]
                    photo["post"]["url"] = post_url
                    photo["post"]["caption"] = "" 
                add_to_listmap(photosmap, post_url, photo)

    searcher = MDSearcher()
    count = 0
    for k in photosmap:
        v = photosmap[k]
        vpost = v[0]["post"] # post should be the same for all in the array
        # print(vpost)
        # check for syndication
        fb_url = vpost["url"]
        # if fb_url != "https://www.facebook.com/stephen.roy.tang/posts/10157444984478912":
        #     continue
        if fb_url in urlmap:
            # already syndicated, nothing to do
            continue
        #print(fb_url)
        count = count + 1

        fb_id = fb_url.rfind("/")
        fb_id = fb_url[fb_id+1:]
        if exclude_id(fb_id):
            continue

        # determine the overall caption for the post, if any
        date = datetime.strptime(vpost["date"], "%b %d, %Y, %I:%M %p")
        caption = None
        if len(vpost["caption"]) > 0:
            caption = vpost["caption"][0]
        else:
            caption = ""

        datestr = date.strftime("%Y-%m-%d")
        info = None
        if len(caption) > 0:
            info = searcher.find_by_day_and_text(datestr, caption)
        if info is not None:
            if info["file"].find("photos") >= 0:
                add_syndication(Path(info["file"]), fb_url, "facebook")
            else:
                # why is it in another folder? let's move it!
                post = PostBuilder.from_mdfile(Path(info["file"]))
                post.kind = "photos"
                post.source = "facebook"
                post.add_syndication("facebook", fb_url)
                for item in v:
                    photo_loc = photo_loc_template % (item["photo_location"])
                    post.media.append(photo_loc)
                post.save()
                # delete the old file
                os.remove(info["file"])
        else:
            # unmatched, create new post
            post = PostBuilder(fb_id.replace(":", "-"), source="facebook", content=caption)
            post.date = date
            post.kind = "photos"
            post.add_syndication("facebook", fb_url)
            resources = []
            for item in v:
                photo_loc = photo_loc_template % (item["photo_location"])
                post.media.append(photo_loc)
                if item["caption"] != caption:
                    resources.append({
                        "src": Path(item["photo_location"]).name,
                        "title": item["caption"]
                    })
            if len(resources) > 0:
                post.params["resources"] = resources
            post.tags.extend(tags)
            post.save()
    print(count)
    
def get_posts_data(posts_export_filepath):
    with Path(posts_export_filepath).open(encoding="UTF-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        posts = []
        items = soup.findAll("div", {"class": "pam"})
        for item in items:
            media = []
            other_urls = []
            anchors = item.find_all('a')
            for a in anchors:
                url = a["href"]
                #print(url)
                if url.find("https://www.facebook.com") >= 0:
                    fb_url = resolve_anchor(url)
                    datestr = a.text
                elif url.startswith("photos_and_videos"):
                    media.append(url)
                    # nextdiv = a.find_next_sibling("div", {"class": "_3-95"})
                    # if nextdiv is not None:
                    #     caption = nextdiv.text
                else:
                    other_urls.append(url)
            captions = []
            divs = item.find_all("div", {"class": "_2pin"})
            for div in divs:
                if len(div.text) > 0:
                    caption = div.text
                    # clean tagged users
                    parsed_tags = re.findall(r"@\[\d+:\d+:[A-Za-z\s\.\-\(\)]+\]", caption)
                    for tag in parsed_tags:
                        # remove outer @[] and split by :
                        tagparts = tag[2:-1].split(":")
                        replacement = "[%s](https://www.facebook.com/%s)" % (tagparts[2], tagparts[0])
                        caption = caption.replace(tag, replacement)
                    captions.append(caption)
            headers = []
            divs = item.find_all("div", {"class": "_2lel"})
            for div in divs:
                if len(div.text) > 0:
                    header = div.text
                    headers.append(header)
            u = urlparse(fb_url)
            params = parse_qs(u.query)
            if 'fbid' in params:
                fbid = params['fbid'][0]
                fb_url_template = "https://www.facebook.com/stephen.roy.tang/posts/%s"
                fb_url = fb_url_template % (fbid)
            # # Dec 15, 2015, 3:22 AM
            # date = datetime.strptime(datestr, "%b %d, %Y, %I:%M %p")
            posts.append({
                "url": fb_url,
                "date": datestr,
                "media": media,
                "headers": headers,
                "caption": captions,
                "other_urls": other_urls
            })
        with postsfile.open("w", encoding="UTF-8") as f:
            f.write(json.dumps(posts, indent=2))

def import_status_updates():

    count = 0
    syndicated = 0
    resolver = URLResolver()
    searcher = MDSearcher(resolver=resolver)
    with postsfile.open(encoding="UTF-8") as f:
        posts = json.loads(f.read())
        for post in posts:
            if post["url"] in urlmap:
                continue
            # if post["url"].find("123163401028086") <= 0:
            #     continue
            fb_id = Path(post["url"]).stem            
            if fb_id in excludes:
                continue
            if "Roy Tang updated his status." in post["headers"]:
                date = datetime.strptime(post['date'], "%b %d, %Y, %I:%M %p")
                caption = ""
                if len(post["caption"]) > 0:
                    caption = post["caption"][0]
                else:
                    continue
                datestr = date.strftime("%Y-%m-%d")

                print(caption)

                # resolve urls
                raw_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', caption)
                urlmatched = False
                for raw_url in raw_urls:
                    expanded_url, no_errors = resolver.get_final_url(raw_url)
                    caption = caption.replace(raw_url, expanded_url)
                    if expanded_url.find("://roytang.net") >= 0:
                        info = urlmap.get(expanded_url)
                        if info is not None:
                            add_syndication(urlmap_to_mdfile(info), post["url"], "facebook")
                            syndicated = syndicated + 1
                            urlmatched = True
                            continue
                        else:
                            print("##### Unmatched roytang url!")
                            print(expanded_url)
                            print(post)

                if urlmatched:
                    continue

                search_text = caption
                # "Retweeted Mo Twister (@djmotwister):" -> "RT @djmotwister"
                search_text = re.sub(r"(Retweeted [^@]+)([^\)]+)\)", r"RT \2", search_text)
                info = searcher.find_by_day_and_text(datestr, search_text)
                # info = None
                if info is not None:
                    add_syndication(Path(info["file"]), post["url"], "facebook")
                    syndicated = syndicated + 1
                    continue
                else:
                    # unmatched, create new post
                    print("Creating new post")
                    p = PostBuilder(fb_id.replace(":", "-"), source="facebook", content=caption)
                    p.date = date
                    p.add_syndication("facebook", post["url"])
                    p.save()
                    pass

                count = count + 1
                #print(caption)

    print(syndicated)
    print(count)

def get_post_stats(posts_export_filepath):
    countbyheader = {}
    countbyyear = {}
    with Path(posts_export_filepath).open(encoding="UTF-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        posts = []
        items = soup.findAll("div", {"class": "pam"})
        for item in items:
            media = []
            other_urls = []
            anchors = item.find_all('a')
            for a in anchors:
                url = a["href"]
                #print(url)
                if url.find("https://www.facebook.com") >= 0:
                    # fb_url = resolve_anchor(url)
                    fb_url = url
                    datestr = a.text
                elif url.startswith("photos_and_videos"):
                    media.append(url)
                    # nextdiv = a.find_next_sibling("div", {"class": "_3-95"})
                    # if nextdiv is not None:
                    #     caption = nextdiv.text
                else:
                    other_urls.append(url)
            captions = []
            divs = item.find_all("div", {"class": "_2pin"})
            for div in divs:
                if len(div.text) > 0:
                    caption = div.text
                    captions.append(caption)
            headers = []
            divs = item.find_all("div", {"class": "_2lel"})
            for div in divs:
                if len(div.text) > 0:
                    header = div.text
                    headers.append(header)
            # # Dec 15, 2015, 3:22 AM
            date = datetime.strptime(datestr, "%b %d, %Y, %I:%M %p")
            posts.append({
                "url": fb_url,
                "date": datestr,
                "media": media,
                "headers": headers,
                "caption": captions,
                "other_urls": other_urls
            })
            year = date.strftime("%Y")
            countbyyear[year] = countbyyear.get(year, 0) + 1
            # if "Roy Tang updated his status." in headers:
            #     countbyyear[year] = countbyyear.get(year, 0) + 1
            for header in headers:
                if header.startswith("Roy Tang wrote on ") and header.endswith("'s timeline."):
                    header = "Roy Tang wrote on someone's timeline."
                elif header.startswith("Roy Tang posted ") and header.endswith(" on Tumblr."):
                    header = "Roy Tang posted something on Tumblr."
                elif header.startswith("Roy Tang reviewed ") and header.endswith(" on Goodreads — "):
                    header = "Roy Tang reviewed a book on Goodreads."
                elif header.startswith("Roy Tang finished reading ") and header.endswith(" on Goodreads — "):
                    header = "Roy Tang finished reading a book on Goodreads."
                elif header.startswith("Roy Tang finished reading ") and header.endswith(" on Goodreads."):
                    header = "Roy Tang finished reading a book on Goodreads."
                elif header.startswith("Roy Tang listened to ") and header.endswith(" on Spotify."):
                    header = "Roy Tang listened to a track on Spotify."
                elif header.startswith("Roy Tang was traveling "):
                    header = "Roy Tang was travelling somewhere."
                elif header.startswith("Roy Tang was watching "):
                    header = "Roy Tang was watching something."
                elif header.startswith("Roy Tang posted in "):
                    header = "Roy Tang posted to a group."
                countbyheader[header] = countbyheader.get(header, 0) + 1
    print("Count by header:")
    for h in countbyheader:
        print("\t%d: %s" % (countbyheader[h], h))
    print("Count by year:")
    for h in countbyyear:
        print("\t%d: %s" % (countbyyear[h], h))
    print("Total posts: %d" % (len(posts)))

# get_post_stats("D:/temp/facebook/posts/your_posts_1.html")
# get_posts_data("D:/temp/facebook/posts/your_posts_1.html")

# import_photos("D:/temp/facebook/photos_and_videos/album/16.html", "file://d:/temp/facebook/%s", ["pickups"])
# import_photos("D:/temp/facebook/photos_and_videos/album/23.html", "file://d:/temp/facebook/%s", ["timeline-photos"])
# import_photos("D:/temp/facebook/photos_and_videos/album/14.html", "file://d:/temp/facebook/%s", ["mobile-uploads"])
# import_photos("D:/temp/facebook/photos_and_videos/album/17.html", "file://d:/temp/facebook/%s", ["ps4"])
# import_photos("D:/temp/facebook/photos_and_videos/album/29.html", "file://d:/temp/facebook/%s", ["ios-photos"])
# import_photos("D:/temp/facebook/photos_and_videos/album/7.html", "file://d:/temp/facebook/%s", [])
# import_photos("D:/temp/facebook/photos_and_videos/album/10.html", "file://d:/temp/facebook/%s", ["travels", "london2015"], merge=True)
# import_photos("D:/temp/facebook/photos_and_videos/album/24.html", "file://d:/temp/facebook/%s", ["travels", "japan2017"], merge=True)
import_photos("D:/temp/facebook/photos_and_videos/album/5.html", "file://d:/temp/facebook/%s", ["travels", "europe", "europe2015"], merge=True)

# import_status_updates()

