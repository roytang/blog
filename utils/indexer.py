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

def indexfile(mdfile, writer, content_type, all=False):
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
            t = str(post.get('title'))
            tags = []
            if post.get("tags") != None:
                tags = post.get("tags")
                if type(tags) == str:
                    tags = [tags] # standardize to a list

            u = post.get("url")
            if not u:
                rp = mdfile.relative_to(content_root)
                # use the title slug when possible
                if mdfile.name == 'index.md':
                    # just use the relative path as is
                    rp = rp.parent
                else:
                    if t is not None and len(t) > 0:
                        slug = slugify(t)
                        rp = rp.with_name(slug) # repl
                rp = str(rp)
                rp = "/" + rp.replace("\\", "/")
                if rp.endswith(".md"):
                    rp = rp.replace(".md", "/")
                else:
                    rp = rp + "/"
                u = rp
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

    # navigate to ./content/posts
    p = cwd / "content" / "post"
    for mdfile in p.glob("**/*.md"):
        indexfile(mdfile, writer, "post", all)
    p = cwd / "content" / "photos"
    for mdfile in p.glob("**/*.md"):
        indexfile(mdfile, writer, "photos", all)
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

