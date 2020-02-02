
from whoosh.filedb.filestore import FileStorage
indexpath = "utils/index"
storage = FileStorage(indexpath)

from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED, DATETIME
from whoosh.analysis import StemmingAnalyzer
from datetime import datetime
from slugify import slugify
from pathlib import Path
import shutil
import frontmatter

schema = Schema(path=ID(unique=True),
                content=TEXT(analyzer=StemmingAnalyzer(), stored=True),
                title=TEXT(stored=True),
                tags=KEYWORD,
                date=DATETIME(stored=True),
                url=STORED,
                content_type=TEXT(stored=True)
                )

INDEX_FILES_BY_AGE_IN_DAYS = 1
cwd = Path.cwd() 
content_root = cwd / "content"

import os
import json
blogdir = Path(os.environ['HUGO_BLOG_OUTDIR'])
urlmapfile = blogdir / "urlmap.json"

urlmap = {}
with urlmapfile.open(encoding="UTF-8") as f:
    tempurlmap = json.loads(f.read())
    for u in tempurlmap:
        if "source_path" in tempurlmap[u]:
            mdfilepath = tempurlmap[u]["source_path"]
            urlmap[mdfilepath] = tempurlmap[u]
            urlmap[mdfilepath]['rel_path'] = u

def indexfile(mdfile, writer, content_type, all=False):
    rp = mdfile.relative_to(content_root)
    ukey = str(rp)
    if ukey in urlmap:
        um = urlmap[ukey]
    else:
        # dont index anything not published
        return
    try:
        modtime = datetime.fromtimestamp(mdfile.stat().st_mtime)
        n = datetime.now()
        daysdelta = (n - modtime).days
        if not all and daysdelta > INDEX_FILES_BY_AGE_IN_DAYS:
            # dont index files older than 1 day
            return
        with mdfile.open(encoding='utf-8') as f:
            post = frontmatter.load(f)
            post_text = str(post)
            draft = post.get('draft')
            if draft:
                # dont index drafts
                return
            d = post.get('date')
            if type(d).__name__ == 'date':
                d = datetime(d.year, d.month, d.day)
            if d > n:
                # dont index files from the future
                return
            t = str(post.get('title', ''))
            tags = []
            if post.get("tags") != None:
                tags = post.get("tags")
                if type(tags) == str:
                    tags = [tags] # standardize to a list

            # derive the url path from the urlmap
            u = um['rel_path']

            writer.update_document(title=t, content=post_text, content_type=content_type,
                path=str(mdfile), tags=",".join(tags), date=d, url=u)
    except Exception as e:
        print("Failed to index " + str(mdfile))
        print(e)

def index(all=False):
    if all:
        # recreate the index
        if Path(indexpath).exists():
            shutil.rmtree(indexpath)
        Path(indexpath).mkdir()
        ix = storage.create_index(schema)
    else:
        # Open an existing index
        try:
            ix = storage.open_index()
        except:
            ix = storage.create_index(schema)

    writer = ix.writer()

    for kind in ["post", "photos", "notes", "links"]:
        p = cwd / "content" / kind
        for mdfile in p.glob("**/*.md"):
            indexfile(mdfile, writer, kind, all)
    writer.commit()

def query_test():
    from whoosh.qparser import QueryParser

    qp = QueryParser("content", schema=ix.schema)
    q = qp.parse(u"javascript")

    with ix.searcher() as s:
        results = s.search(q)
        for hit in results:
            print(hit["title"])
            print(hit["url"])
            # Assume "content" field is stored
            print(hit.highlights("content"))
            print("------------")

import sys
index('all' in sys.argv[1:])

