from datetime import datetime
from slugify import slugify
from pathlib import Path
import shutil
import frontmatter


def cleanup():
    cwd = Path.cwd()
    content_root = cwd / "content"

    for section in ("post", "photos", "notes"):
        p = content_root / section
        for mdfile in p.glob("**/*.md"):
            this = mdfile
            if mdfile.name == "index.md":
                this = mdfile.parent
            monthpath = this.parent.name
            with mdfile.open(encoding='utf-8') as f:
                post = frontmatter.load(f)
                postmonth = post['date'].strftime('%m')
                if monthpath != postmonth:
                    print("%s :: %s :: %s" % (str(mdfile), monthpath, postmonth))

cleanup()