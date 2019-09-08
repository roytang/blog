from pathlib import Path
import frontmatter
import os
import json

blogdir = Path(os.environ['HUGO_BLOG_OUTDIR'])
urlmapfile = blogdir / "urlmap.json"
urlmap = {}
with urlmapfile.open(encoding="UTF-8") as f:
    urlmap = json.loads(f.read())

# migrate comments from content/comments to page bundles
def migrate_comments():
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "comment"
    for mdfile in p.glob("**/*.md"):
        print(str(mdfile))
        with mdfile.open(encoding="UTF-8") as f:
            try:
                post = frontmatter.load(f)
            except:
                print("Error parsing file")
                continue

        urlpath = post['parent_page']['urlpath']
        info = urlmap.get(urlpath)
        if info is None:
            print("##### Path not found, map manually %s" % urlpath)
            continue
        parentmd = cwd / "content" / info["source_path"]
        if parentmd.name != "index.md":
            # migrate the post to a page bundle
            newdir = parentmd.parent / parentmd.stem
            if not newdir.exists():
                newdir.mkdir(parents=True)
            if parentmd.exists():
                newfile = newdir / "index.md"
                os.rename(str(parentmd), str(newfile))
        else:
            newdir = parentmd.parent
        
        wtype = post.get("webmention_type", None)
        if wtype == 'like-of':
            newfile = newdir / ( "like-%s.json" % (mdfile.stem) )
        elif wtype == 'repost-of':
            newfile = newdir / ( "repost-%s.json" % (mdfile.stem) )
        else:
            newfile = newdir / ( "comment-%s.json" % (mdfile.stem) )

        comment = {
            "id": mdfile.stem,
            "name": post['author']['name'],
            "url": post['author'].get('url', ''),
            "text": post.content, 
            "date": post['date'].strftime("%Y-%m-%d %H:%M:%S"),
            "photo": post['author'].get('photo', ''),
        }

        # save the comment into newdir
        with Path(newfile).open("w", encoding="UTF-8") as f:
            f.write(json.dumps(comment))

migrate_comments()