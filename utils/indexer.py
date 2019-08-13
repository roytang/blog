from whoosh.filedb.filestore import FileStorage
storage = FileStorage("utils/index")

from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED, DATETIME
from whoosh.analysis import StemmingAnalyzer
from datetime import datetime
from slugify import slugify

schema = Schema(path=ID(unique=True),
                content=TEXT(analyzer=StemmingAnalyzer(), stored=True),
                title=TEXT(stored=True),
                tags=KEYWORD,
                date=DATETIME(stored=True),
                url=STORED,
                )

# Open an existing index
try:
    ix = storage.open_index()
except:
    ix = storage.create_index(schema)

def index(ix, all=False):
    writer = ix.writer()

    from pathlib import Path
    import frontmatter

    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "post"
    for mdfile in p.glob("**/*.md"):
        try:
            modtime = datetime.fromtimestamp(mdfile.stat().st_mtime)
            n = datetime.now()
            daysdelta = (n - modtime).days
            if not all and daysdelta > 1:
                # dont index files older than 1 day
                continue
            with mdfile.open(encoding='utf-8') as f:
                post = frontmatter.load(f)
                post_text = str(post)
                draft = post.get('draft')
                if draft:
                    # dont index drafts
                    continue
                d = post.get('date')
                if d > n:
                    # dont index files from the future
                    continue
                t = str(post.get('title'))
                tags = []
                if post.get("tags") != None:
                    tags = post.get("tags")
                    if type(tags) == str:
                        tags = [tags] # standardize to a list

                u = post.get("url")
                if not u:
                    rp = mdfile.relative_to(p)
                    # use the title slug when possible
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
                writer.update_document(title=t, content=post_text,
                    path=str(mdfile), tags=",".join(tags), date=d, url=u)
        except:
            print("Failed to index " + str(mdfile))

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
index(ix, 'all' in sys.argv[1:])

