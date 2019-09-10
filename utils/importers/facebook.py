import json
from pathlib import Path
from datetime import datetime
import frontmatter

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

importfile = Path("D:\\temp\\facebook-stephenroytang-20190718\\posts\\your_posts_1.json")
with importfile.open(encoding="UTF-8") as f:
    posts = json.loads(f.read())

dumpfile = Path("D:\\temp\\dump.json")
# map timestamp to url 
fburlmap = {}
with dumpfile.open(encoding="UTF-8") as f:
    dump = json.loads(f.read())
    for d in dump:
        if d["url"][-2:-1] == ":":
            continue
        minutes = datetime.strptime(d["date"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M")
        if minutes in fburlmap:
            fburlmap[minutes].append(d)
        else:
            fburlmap[minutes] = [d]

notesfolder = Path("D:\\repos\\blog\\content\\notes")
cachednotes = {}

count = 0
syndicated = 0
notfound = []
for post in posts:
    date = datetime.utcfromtimestamp(post["timestamp"])
    if date.year > 2017:
        continue

    print(date)
    data = post.get("data", [])
    content = ""
    postcount = 0
    for d in data:
        if "post" in d:
            content = d["post"]
            postcount = postcount + 1
    print(content)

    # let's worry about content less posts later
    if len(content) > 0:

        # find the fburl for this post
        match = None
        datestr = date.strftime("%Y-%m-%d %H:%M")
        if datestr in fburlmap:
            fburl = fburlmap[datestr]
            for fbu in fburl:
                if fbu["text"].find(content) >= 0:
                    match = fbu
                    break
        
        if match is None:
            print(datestr)
            print("#### NOT FOUND IN FB DUMP!")
            post["fmdate"] = datestr
            notfound.append(post)
            continue

        # check for any matching notes for the same year and month
        searchfolder = notesfolder / date.strftime("%Y") / date.strftime("%m")
        my = date.strftime("%Y-%m")
        if my in cachednotes:
            for note in cachednotes[my]:
                if note["text"].find(content) >= 0:
                    print("##### FOUND!!!")
                    syndicated = syndicated + 1
                    add_syndication(note["file"], match["url"], "facebook")
        else:
            foundnotes = []
            for mdfile in searchfolder.glob("**/*.md"):
                with mdfile.open() as f:
                    try:
                        post = frontmatter.load(f)
                    except:
                        print("Error parsing file")
                        continue
                    foundnotes.append({
                        "date": post['date'],
                        "text": post.content,
                        "file": mdfile
                    })
                    if post.content.find(content) >= 0:
                        print("#### FOUND!!!")
                        add_syndication(mdfile, match["url"], "facebook")
                        syndicated = syndicated + 1
            # cache the foundnotes for the given month and year
            cachednotes[my] = foundnotes

    count = count + 1

with Path("d:\\temp\\notfound.json").open("w", encoding="UTF-8") as f:
    f.write(json.dumps(notfound))

print(len(notfound))
print(syndicated)
print(count)