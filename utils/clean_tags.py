# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io

TAGS_TO_REMOVE = ["mobile-uploads", "timeline-photos", "timeline",
    "fbreposts01", "fbreposts02", 
    "fbreposts03", "fbreposts04", "fbreposts05", "fbreposts06", 
    "fbreposts07", "fbreposts08", "fbreposts09", "fbreposts10" ]

# clean up the sins of old quora comments imported via tracker
def clean_tags():
    count = 0
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "collections"
    for mdfile in p.glob("**/*.md"):
        with mdfile.open(encoding="UTF-8") as f:
            try:
                post = frontmatter.load(f)
            except:
                print("Error parsing file", str(mdfile))
                continue

            has_changes = False

            tags = post.get("tags", [])
            if tags is not None:
                newtags = []
                for tag in tags:
                    if tag in TAGS_TO_REMOVE:
                        has_changes = True
                    else:
                        newtags.append(tag)
                if has_changes:
                    post["tags"] = newtags

            # Save the file.
            if has_changes:
                newfile = frontmatter.dumps(post)
                with mdfile.open("w", encoding="UTF-8") as w:
                    w.write(newfile)
                    count = count + 1

    print("Updated files: " + str(count))

clean_tags()