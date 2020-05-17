# generate that stats json file for all site/blog items

from pathlib import Path
import os
import json
from datetime import datetime

def count_files():
    count = 0
    cwd = Path.cwd() 
    # navigate to ./content/posts
    stats_by_suffix = {}
    p = cwd / "content" # / "notes" # / "2010" / "08"
    p = Path("d:\\repos\\roytang.github.io\\")
    for afile in p.glob("**/*.*"):
        if not afile.is_dir():
            suffix = afile.suffix
            size = afile.stat().st_size / 1024 / 1024
            if afile.suffix not in stats_by_suffix:
                stats_by_suffix[suffix] = { "count": 1, "size": size }
            else:
                stats_by_suffix[suffix]["count"] = stats_by_suffix[suffix]["count"] + 1
                stats_by_suffix[suffix]["size"] = stats_by_suffix[suffix]["size"] + size

    print(json.dumps(stats_by_suffix, indent=2))

count_files()