# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io

def clean_categories():
    count = 0
    cwd = Path.cwd() 
    p = cwd / "collections" / "sketchbook" 
    for mdfile in p.glob("**/*.md"):
        print(str(mdfile))
        with mdfile.open(encoding='UTF-8') as f:
            try:
                post = frontmatter.load(f)
            except Exception as e:
                print("Error parsing file: " + str(mdfile))
                print(e)
                continue

            has_changes = False

            tags = post.get("tags", [])
            albums = post.get("albums", [])

            for album in albums:
                if album not in tags:
                    tags.append(album)
                    has_changes = True

            newtags = []
            for tag in tags:
                if tag == "sketchbook":
                    has_changes = True
                    continue
                newtags.append(tag)

            # Save the file.
            if has_changes:
                post["tags"] = newtags
                newfile = frontmatter.dumps(post)
                with mdfile.open("w", encoding='UTF-8') as w:
                    w.write(newfile)
                    count = count + 1

    print("Updated files: " + str(count))
clean_categories()    