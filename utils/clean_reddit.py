# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io

# clean up the sins of old reddit comments imported via tracker
def clean_reddit():
    count = 0
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "replies"
    for mdfile in p.glob("**/*.md"):
        print(str(mdfile))
        with mdfile.open() as f:
            try:
                post = frontmatter.load(f)
            except:
                print("Error parsing file")
                continue

            has_changes = False

            if post["source"] == "reddit":
                content = post.content
                content = content.replace("\\n\\n", "\n\n")
                if content != post.content:
                    post.content = content
                    has_changes = True

            # Save the file.
            if has_changes:
                newfile = frontmatter.dumps(post)
                with mdfile.open("w") as w:
                    w.write(newfile)
                    count = count + 1

    print("Updated files: " + str(count))

clean_reddit()