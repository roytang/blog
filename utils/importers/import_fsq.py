import json
from pathlib import Path
import datetime
import frontmatter
import io
import re
from utils import URLResolver, PostBuilder
import requests
from bs4 import BeautifulSoup

FOURSQUARE_DATA = "d:\\temp\\foursquare.json"
def load_fsq_json():
    out_items = []
    with Path(FOURSQUARE_DATA).open(encoding="UTF-8") as f:
        data = json.loads(f.read())
        for item in data[0]["response"]["checkins"]["items"]:
            epoch_time = item["createdAt"]
            d = datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
            print(d)
            out_items.append({
                "lat": item["venue"]["location"]["lat"],
                "lng": item["venue"]["location"]["lng"],
                "label": item["venue"]["name"] + " " + item["venue"]["location"].get("address", ""),
                "date": d,
                "shout": item.get("shout", ""),
                "source": "foursquare"
            })

    # print(json.dumps(out_items, indent=2))

    # count repeats I guess?

    label_map = {}
    for item in out_items:
        label = item["label"]
        if label not in label_map:
            label_map[label] = [item]
        else:
            label_map[label].append(item)

    keys = []
    for key in label_map:
        print(key, len(label_map[key]))
        keys.append(key)

    keys.sort(key=lambda x: len(label_map[x]))

    for key in keys:
        print(key, len(label_map[key]))


    # with Path("out.json").open("w", encoding="UTF-8") as f:
    #     f.write(json.dumps(label_map, indent=2))

TWITTER_MAP_FILE = "d:\\temp\\twitter_fsq_map.json"

def get_twitter_map():
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "notes"
    with Path(TWITTER_MAP_FILE).open(encoding="UTF-8") as f:
        tfmap = json.loads(f.read())
    l = []
    for mdfile in p.glob("**/*.md"):
        with mdfile.open(encoding="UTF-8") as f:
            try:
                post = frontmatter.load(f)
            except:
                print("Error parsing file")
                continue

            content = post.content
            raw_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
            for raw_url in raw_urls:
                if raw_url.find("swarmapp.com") >= 0:
                    filename = str(mdfile)
                    if filename not in l:
                        l.append(filename)
                    else:
                        print(filename)
                if raw_url.find("4sq.com") >= 0:
                    filename = str(mdfile)
                    if filename not in l:
                        l.append(filename)
    #                 # syns = post.get("syndicated")
    #                 # for s in syns:
    #                 #     print(s)
    #                 tfmap.append({
    #                     "url": raw_url,
    #                     "mdfile": str(mdfile),
    #                     "final_url": raw_url
    #                 })

    # with Path(TWITTER_MAP_FILE).open("w", encoding="UTF-8") as f:
    #     f.write(json.dumps(tfmap, indent=2))

def expand_twitter_map():
    u = URLResolver()
    finalmap = [] # ok these arent really maps
    with Path(TWITTER_MAP_FILE).open(encoding="UTF-8") as f:
        tfmap = json.loads(f.read())
        for item in tfmap:
            furl = u.get_final_url(item["url"], False)
            print(furl)
            item["final_url"] = furl[0]
            finalmap.append(item)
    with Path(TWITTER_MAP_FILE).open("w", encoding="UTF-8") as f:
        f.write(json.dumps(finalmap, indent=2))

SWARMAPP_URL1 = "https://www.swarmapp.com/user/405004/checkin/"
SWARMAPP_URL2 = "https://www.swarmapp.com/roytang/checkin/"
SWARMAPP_URL3 = "https://www.swarmapp.com/c/"
SWARMAPP_URL4 = "swarm://checkins/"

def map_checkin_ids():
    finalmap = [] # ok these arent really maps
    unprocessed = 0
    with Path(TWITTER_MAP_FILE).open(encoding="UTF-8") as f:
        tfmap = json.loads(f.read())
        for item in tfmap:
            if "checkin_id" not in item:
                furl = item["final_url"]
                if furl.find(SWARMAPP_URL1) >= 0:
                    cid = furl[len(SWARMAPP_URL1):len(SWARMAPP_URL1)+24]
                    item["checkin_id"] = cid
                elif furl.find(SWARMAPP_URL2) >= 0:
                    cid = furl[len(SWARMAPP_URL2):len(SWARMAPP_URL2)+24]
                    item["checkin_id"] = cid
                elif furl.find(SWARMAPP_URL3) >= 0:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
                    response = requests.get(furl, headers=headers)
                    soup = BeautifulSoup(response.text, "html.parser")
                    metas = soup.find_all("meta")
                    for m in metas:
                        if m.has_attr("name"):
                            if m["name"] == "twitter:app:url:googleplay":
                                print(m["content"])
                                cid = m["content"][len(SWARMAPP_URL4):len(SWARMAPP_URL4)+24]
                                item["checkin_id"] = cid
                                break
                print(furl)
                unprocessed = unprocessed + 1
            finalmap.append(item)
    with Path(TWITTER_MAP_FILE).open("w", encoding="UTF-8") as f:
        f.write(json.dumps(finalmap, indent=2))
    print(unprocessed)
    print(len(finalmap))

def add_locations():
    # use the twitter map and the foursquare data to add locations to existing md files
    files = {}
    with Path(TWITTER_MAP_FILE).open(encoding="UTF-8") as f:
        tfmap = json.loads(f.read())
        for tf in tfmap:
            if 'checkin_id' in tf:
                cid = tf['checkin_id']
                files[cid] = tf
    checkins = {}
    with Path(FOURSQUARE_DATA).open(encoding="UTF-8") as f:
        data = json.loads(f.read())
        for item in data[0]["response"]["checkins"]["items"]:
            itemid = item["id"]
            # print(itemid, item["venue"]["name"])
            checkins[itemid] = item
        for item in data[1]["response"]["checkins"]["items"]:
            itemid = item["id"]
            # print(itemid, item["venue"]["name"])
            checkins[itemid] = item
    venues = {}
    for cid in checkins:
        ci = checkins[cid]
        vid = ci["venue"]["id"]
        if vid not in venues:
            venues[vid] = ci["venue"]
        addr = ci["venue"]["location"].get("address")
        if addr is None:
            addr = ""
        else:
            addr = " " + addr
        location = ci["venue"]["name"] + addr
        location = location.replace(".", "")
        location = location.replace(",", "")
        location = location.replace("#", "")
        location = location.replace(":", "")
        location = location.replace("\"", "")
        # print(location)
        epoch_time = ci["createdAt"]
        d = datetime.datetime.fromtimestamp(epoch_time) #.strftime('%Y-%m-%d %H:%M:%S')
        
        if cid in files:
            tf = files[cid]
            mdfile = Path(tf["mdfile"])
            with mdfile.open(encoding="UTF-8") as f:
                try:
                    post = frontmatter.load(f)
                except:
                    print("Error parsing file")
                    continue
            post["locations"] = location
            syn = post["syndicated"]
            post["syndicated"].append({
                "url": tf["final_url"],
                "type": "foursquare"
            })
            post["checkin_id"] = cid
            newfile = frontmatter.dumps(post)
            with mdfile.open("w", encoding="UTF-8") as w:
                w.write(newfile)
        else:
            content = ci.get("shout", "") + " (@" + location + ")"
            post = PostBuilder(cid, source="foursquare", content=content)
            post.date = d
            post.params["locations"] = location
            post.params["checkin_id"] = cid
            post.add_syndication("foursquare", SWARMAPP_URL2 + cid)
            post.save()

    cwd = Path.cwd() 
    for vid in venues:
        venue = venues[vid]
        post = frontmatter.Post("")
        addr = venue["location"].get("address")
        if addr is None:
            addr = ""
        else:
            addr = " " + addr
        location = venue["name"] + addr
        location = location.replace(".", "")
        location = location.replace(",", "")
        location = location.replace("#", "")
        location = location.replace(":", "")
        location = location.replace("\"", "")
        post["title"] = location
        post["description"] = " ".join(venue["location"].get("formattedAddress", []))
        post["city"] = venue["location"].get("state", venue["location"].get("city", ""))
        post["country"] = venue["location"].get("country", "")

        outdir = cwd / "content" / "locations" / location 
        if not outdir.exists():
            outdir.mkdir(parents=True)
        outfile = outdir / "_index.md"
        newfile = frontmatter.dumps(post)
        with outfile.open("w", encoding="UTF-8") as w:
            w.write(newfile)


# get_twitter_map()                    
# expand_twitter_map()

add_locations()