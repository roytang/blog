# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io

# clean up the sins of old quora comments imported via tracker
def clean_quora():
    count = 0
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "collections" / "quora" / "lineitems"
    for mdfile in p.glob("**/*.md"):
        with mdfile.open(encoding="UTF-8") as f:
            try:
                post = frontmatter.load(f)
            except:
                print("Error parsing file")
                continue

            start = post.content.find("> [")
            end = post.content.find("?]")
            title = post.content[start+3:end+1]
            post["title"] = title

            newfile = frontmatter.dumps(post)
            with mdfile.open("w", encoding="UTF-8") as w:
                w.write(newfile)
                count = count + 1

    print("Updated files: " + str(count))

clean_quora()