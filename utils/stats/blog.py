# generate that stats json file for all site/blog items

from pathlib import Path
import os
import json
from datetime import datetime

# load the url map
blogdir = Path(os.environ['HUGO_BLOG_OUTDIR'])
stats = {"comments": {}, "words": {}, "words_posts": {}}
kinds = ["comments"]
urlmapfile = blogdir / "urlmap.json"
with urlmapfile.open(encoding="UTF-8") as f:
    tempurlmap = json.loads(f.read())
    for u in tempurlmap:
        um = tempurlmap[u]
        kind = um.get("kind")
        if kind is None:
            continue
        if kind not in kinds:
            kinds.append(kind)
            stats[kind] = {}
        d = datetime.strptime(um["date"], '%Y-%m-%d')
        year = d.strftime('%Y')
        stats[kind][year] = stats[kind].get(year,0) + 1
        if um.get("wordcount"):
            stats["words"][year] = stats["words"].get(year, 0) + um["wordcount"]
            if kind == "post":
                stats["words_posts"][year] = stats["words_posts"].get(year, 0) + um["wordcount"]
        if "comments" in um:
            comments = len(um["comments"])
            stats['comments'][year] = stats['comments'].get(year,0) + comments
        
root = Path(__file__).parent.absolute()
outfile = root / "blog.json"
with outfile.open('w') as f:
    f.write(json.dumps(stats, indent=2))
