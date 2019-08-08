from whoosh.filedb.filestore import FileStorage
storage = FileStorage("utils/index")

from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED, DATETIME
from whoosh.analysis import StemmingAnalyzer

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

def index(ix):
    writer = ix.writer()

    from pathlib import Path
    import frontmatter

    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "post"
    for mdfile in p.glob("**/*.md"):
        with mdfile.open(encoding='utf-8') as f:
            post = frontmatter.load(f)
            post_text = str(post)
            d = post.get('date')
            t = str(post.get('title'))
            tags = []
            if post.get("tags") != None:
                tags = post.get("tags")
                if type(tags) == str:
                    tags = [tags] # standardize to a list

            u = post.get("url")
            if not u:
                rp = str(mdfile.relative_to(p))
                rp = "/" + rp.replace("\\", "/")
                if rp.endswith(".md"):
                    rp = rp.replace(".md", "/")
                u = rp

            writer.update_document(title=t, content=post_text,
                path=str(mdfile), tags=",".join(tags), date=d, url=u)

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

index(ix)

