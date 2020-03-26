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

            # Save the file.
            if has_changes:
                newfile = frontmatter.dumps(post)
                with mdfile.open("w", encoding="UTF-8") as w:
                    w.write(newfile)
                    count = count + 1

    print("Updated files: " + str(count))

clean_quora()