# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io
import json
import shutil

# clean up the sins of old quora comments imported via tracker
def clean_plurk():
    count = 0
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "notes" # / "2010" / "08"
    # collect all plurk related comments that don't have an existing index.md in same folder
    found_comments = {}
    for jsonfile in p.glob("**/comment-*.json"):
        with jsonfile.open(encoding="UTF-8") as f:
            data = json.loads(f.read())
            source_url = data.get("source_url")
            mention_url = data.get("mention_url")
            mapped_url = ""
            is_plurk = False
            if source_url and source_url.find("plurk") >= 0:
                mapped_url = source_url
                is_plurk = True
            elif mention_url and mention_url.find("plurk") >= 0:
                mapped_url = mention_url
                is_plurk = True
            if is_plurk:
                index = jsonfile.parent / "index.md"
                if not index.exists():
                    print(jsonfile)
                    found_comments[mapped_url] = found_comments.get(mapped_url, [])
                    found_comments[mapped_url].append(jsonfile)
    print(len(found_comments))          
    # next we get all md files
    for mdfile in p.glob("**/*.md"):
        comments = []
        with mdfile.open(encoding="UTF-8") as f:
            try:
                post = frontmatter.load(f)
            except:
                print("Error parsing file")
                continue
            plurks_found = 0
            #print(mdfile)
            for syn in post.get("syndicated", []):
                if syn["type"] == "plurk":
                    url = syn["url"]
                    if url in found_comments:
                        comments = comments + found_comments[url]
                    plurks_found = plurks_found + 1
        if len(comments) > 0:
            print(mdfile)
            #print(comments)
            outfolder = mdfile.parent
            if mdfile.stem != "index":
                # copy the mdfile into a child folder
                newfolder = mdfile.parent / mdfile.stem
                if not newfolder.exists():
                    newfolder.mkdir()
                newfile = newfolder / "index.md"
                shutil.move(mdfile, newfile)
                outfolder = newfolder
            for c in comments:
                newfile = outfolder / c.name
                shutil.move(c, newfile)

    # for mdfile in p.glob("**/*.md"):
    #     with mdfile.open(encoding="UTF-8") as f:
    #         try:
    #             post = frontmatter.load(f)
    #         except:
    #             print("Error parsing file")
    #             continue

    #         has_changes = False

    #         if post.get("source") == "quora":
    #             content = post.content
    #             # idx = content.find('<span class="ui_qtext_rendered_qtext">')
    #             # prechar = (ord(content[idx-3]), ord(content[idx-2]), ord(content[idx-1]))
    #             # filename = (str(mdfile))
    #             # print(prechar, filename)
    #             content = content.replace('<span class="ui_qtext_rendered_qtext">', '\n<span class="ui_qtext_rendered_qtext">')
    #             if content != post.content:
    #                 post.content = content
    #                 has_changes = True

    #         # Save the file.
    #         if has_changes:
    #             newfile = frontmatter.dumps(post)
    #             with mdfile.open("w", encoding="UTF-8") as w:
    #                 w.write(newfile)
    #                 count = count + 1

    # print("Updated files: " + str(count))

clean_plurk()