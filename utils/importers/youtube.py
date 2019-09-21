from pathlib import Path
import inspect
from datetime import datetime
import re
import xmltodict
import json
import shutil

from utils import loadurlmap, add_syndication, get_content, add_to_listmap, urlmap_to_mdfile, clean_string
from utils import MDSearcher, URLResolver, PostBuilder, CommentBuilder
urlmap = loadurlmap(False)
archivepath = Path("C:\\temp\\YouTube\\archive")

def import_youtube(importfilepath):
    post_count = 0
    unmatched = []
    public = []
    nonpublic = []
    importpath = Path(importfilepath)
    videofiles = {}
    for videofile in importpath.glob("**/*.flv"): 
        videofiles[videofile.stem] = videofile
    for videofile in importpath.glob("**/*.mp4"): 
        videofiles[videofile.stem] = videofile
    for jsonfile in importpath.glob("**/*.json"):
        # print(jsonfile)
        post_count = post_count + 1
        with jsonfile.open(encoding="UTF-8") as f:
            doc = json.loads(f.read())[0]
            if "public" == doc["status"]["privacyStatus"]:
                public.append(doc)

                id = doc["id"]
                title = doc["snippet"]["title"]
                desc = doc["snippet"]["description"]
                url = "https://www.youtube.com/watch?v=%s" % (id)
                date = doc["snippet"]["publishedAt"]
                # "publishedAt" : "2014-11-16T06:16:06.000Z",
                date = datetime.strptime(date[:-5], "%Y-%m-%dT%H:%M:%S")                

                # find the video file for this json
                stem = jsonfile.stem
                idx = stem.rfind("-")
                videofile = videofiles.get(stem[0:idx])

                post = PostBuilder(id, source="youtube", content="%s\n%s\n\n{{< youtube \"%s\" >}}" % (title, desc, id))
                post.date = date
                post.add_syndication("youtube", url)
                post.tags = doc["snippet"].get("tags", [])
                if videofile is None:
                    print("#### Could not find videofile for %s" % (stem))
                    print(len(stem))
                else:
                    suffix = videofile.suffix
                    newfilename = "%s%s" % (id, suffix)
                    post.params["archive_url"] = "https://roytang.net/archive/videos/%s" % (newfilename)
                    # copy the videofile to the archive path
                    newfile = archivepath / newfilename
                    if not newfile.exists():
                        shutil.copy(str(videofile), str(newfile))
                post.save()

            else:
                nonpublic.append(doc)
            
    print(len(public))
    print(len(nonpublic))
    print(post_count)

import_youtube("C:\\temp\\Youtube\\videos")
