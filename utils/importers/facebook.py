import json
from pathlib import Path
from datetime import datetime
import frontmatter
import re
import string

def add_syndication(mdfile, url, stype):
    with mdfile.open(encoding="UTF-8") as f:
        try:
            post = frontmatter.load(f)
        except:
            print("Error parsing file")
            return

        if post.get('syndicated') == None:
            post['syndicated'] = []
        else:
            for s in post['syndicated']:
                if s["type"] == stype and s["url"] == url:
                    # dont add a duplicate!
                    return

        post['syndicated'].append({
            'type': stype,
            'url': url
        })
        newfile = frontmatter.dumps(post)
        with mdfile.open("w", encoding="UTF-8") as w:
            w.write(newfile)

printable = set(string.printable)
def clean_string(str):
    # clean string for matching purposes
    str = "".join(list(filter(lambda x: x in printable, str)))
    return str[0:100]

importfile = Path("D:\\temp\\facebook-stephenroytang-20190718\\posts\\your_posts_1.json")
with importfile.open(encoding="UTF-8") as f:
    posts = json.loads(f.read())

dumpfile = Path("D:\\temp\\dump.json")
# map timestamp to url 
fburlmap = {}
fburlmapday = {} # secondary map, if the first one fails
with dumpfile.open(encoding="UTF-8") as f:
    dump = json.loads(f.read())
    for d in dump:
        minutes = datetime.strptime(d["date"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M")
        if minutes in fburlmap:
            fburlmap[minutes].append(d)
        else:
            fburlmap[minutes] = [d]
        day = datetime.strptime(d["date"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
        if day in fburlmapday:
            fburlmapday[day].append(d)
        else:
            fburlmapday[day] = [d]

notesfolder = Path("D:\\repos\\blog\\content\\notes")
photosfolder = Path("D:\\repos\\blog\\content\\photos")
cachednotes = {}

count = 0
unprocessed = []
contentless = []
syndicated = []
notfound = []
othertimelines = []
regex = re.compile(r"\@\[[0-9]+:[0-9]+:([^\]]+)\]", re.IGNORECASE)
for post in posts:
    date = datetime.utcfromtimestamp(post["timestamp"])
    if date.year > 2017:
        continue

    post['fmdate'] = date.strftime("%Y-%m-%d %H:%M:%S")
    data = post.get("data", [])
    content = ""
    postcount = 0
    for d in data:
        if "post" in d:
            content = d["post"]
            postcount = postcount + 1
    # if content.find("Too much bad news this week, time for some chocolate") < 0:
    #     continue
    # print(content)

    processed = False
    # let's worry about content less posts later
    if len(content) > 0:

        search = content
        search = regex.sub(r'\g<1>', search)
        search = clean_string(search)

        title = post.get("title", "")
        if title.startswith("Roy Tang wrote on ") and title.endswith("timeline."):
            othertimelines.append(post)
            # ignore posts written on other people's timelines
            continue
        
        # find the fburl for this post
        match = None
        datestr = date.strftime("%Y-%m-%d %H:%M")
        if datestr in fburlmap:
            fburl = fburlmap[datestr]
            for fbu in fburl:
                if clean_string(fbu["text"]).find(search) >= 0:
                    match = fbu
                    break
        if match is None:
            datestr = date.strftime("%Y-%m-%d")
            fburl = fburlmapday.get(datestr, [])
            for fbu in fburl:
                if clean_string(fbu["text"]).find(search) >= 0:
                    match = fbu
                    break
        if match is None:
            notfound.append(post)
            # continue
        else:
            # check for any matching notes for the same year and month
            searchfolder = notesfolder / date.strftime("%Y") / date.strftime("%m")
            searchfolder2 = photosfolder / date.strftime("%Y") / date.strftime("%m")
            my = date.strftime("%Y-%m")
            if my in cachednotes:
                for note in cachednotes[my]:
                    if clean_string(note["text"]).find(search) >= 0:
                        syndicated.append(post)
                        add_syndication(note["file"], match["url"], "facebook")
                        processed = True
            else:
                foundnotes = []
                for mdfile in searchfolder.glob("**/*.md"):
                    with mdfile.open(encoding="UTF-8") as f:
                        try:
                            mdpost = frontmatter.load(f)
                        except:
                            print("Error parsing file")
                            continue
                        foundnotes.append({
                            "date": mdpost['date'],
                            "text": mdpost.content,
                            "file": mdfile
                        })
                        if clean_string(mdpost.content).find(search) >= 0:
                            add_syndication(mdfile, match["url"], "facebook")
                            syndicated.append(post)
                            processed = True
                for mdfile in searchfolder2.glob("**/*.md"):
                    with mdfile.open(encoding="UTF-8") as f:
                        try:
                            mdpost = frontmatter.load(f)
                        except:
                            print("Error parsing file")
                            continue
                        foundnotes.append({
                            "date": mdpost['date'],
                            "text": mdpost.content,
                            "file": mdfile
                        })
                        if clean_string(mdpost.content).find(search) >= 0:
                            add_syndication(mdfile, match["url"], "facebook")
                            syndicated.append(post)
                            processed = True
                # cache the foundnotes for the given month and year
                cachednotes[my] = foundnotes
    else:
        contentless.append(post)

    if not processed:
        unprocessed.append(post)
    count = count + 1

with Path("d:\\temp\\notfound.json").open("w", encoding="UTF-8") as f:
    f.write(json.dumps(notfound, indent=4))
with Path("d:\\temp\\contentless.json").open("w", encoding="UTF-8") as f:
    f.write(json.dumps(contentless, indent=4))


print("notfound %s" % (len(notfound)))
print("othertimelines %s" % (len(othertimelines)))
print("contentless %s" % (len(contentless)))
print("syndicated %s" % (len(syndicated)))
print("unprocessed %s" % (len(unprocessed)))
print(count)