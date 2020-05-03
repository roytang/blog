# one-time job: rename comments from comment-wp-[username]-[datestr] to comment-[datestr]-wp-[username] so that they are sorted correctly

from pathlib import Path
import json
import io
import slugify
import shutil
from datetime import datetime

def clean_comments():
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "post"
    cf = cwd / "content" / "comment"
    for commentfile in p.glob("**/comment-wp-*.json"):
        parts = commentfile.stem.split("-")
        parts.insert(1, parts[-1])
        parts = parts[:-1]
        newfilename = "-".join(parts) + ".json"
        outfile = commentfile.parent / newfilename
        shutil.move(commentfile, outfile)
        
clean_comments()