# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io

# clean up the sins of old quora comments imported via tracker
def clean_quora():
    count = 0
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content"
    for mdfile in p.glob("**/*.md"):
        with mdfile.open(encoding="UTF-8") as f:
            try:
                post = frontmatter.load(f)
            except:
                print("Error parsing file", str(mdfile))
                continue

            has_changes = False

            curr_album = post.get("album", "")
            if len(curr_album) > 0:
                del post["album"]
                post["albums"] = [curr_album]
                has_changes = True

            curr_albums = post.get("albums", [])
            if len(curr_albums) > 0:
                if mdfile.name != "index.md":
                    del post["albums"]
                    has_changes = True
                else:
                    container = mdfile.parent
                    img_found = False
                    for img in container.glob("*.jpg"):
                        img_found = True
                        break
                    for img in container.glob("*.png"):
                        img_found = True
                        break
                    for img in container.glob("*.gif"):
                        img_found = True
                        break
                    for img in container.glob("*.mp4"):
                        img_found = True
                        break
                    if not img_found:
                        del post["albums"]
                        has_changes = True
                    else:
                        is_sketchbook = False
                        if "sketchdaily" in post.get("tags", []):
                            is_sketchbook = True
                        if is_sketchbook:
                            if "sketchbook" not in post.get("albums", []):
                                post["albums"] = post.get("albums", []).append("sketchbook")
                                has_changes = True

            # Save the file.
            if has_changes:
                newfile = frontmatter.dumps(post)
                with mdfile.open("w", encoding="UTF-8") as w:
                    w.write(newfile)
                    count = count + 1

    print("Updated files: " + str(count))

clean_quora()