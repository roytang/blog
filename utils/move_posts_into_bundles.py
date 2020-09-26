# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io
import shutil

def do_the_thing():
    count = 0
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "post"
    for mdfile in p.glob("**/*.md"):
        # print(str(mdfile))
        if mdfile.name == "index.md":
            continue

        print(str(mdfile))
        new_dir = mdfile.parent / (mdfile.stem)
        if not new_dir.exists():
            new_dir.mkdir(parents=True)
        new_file = new_dir / "index.md"
        shutil.move(mdfile, new_file)

    print("Updated files: " + str(count))

do_the_thing()