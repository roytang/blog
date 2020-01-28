sourcefolder = "C:\\Users\\USER\\Dropbox\\backups\\delicious.html"

from pathlib import Path
from bs4 import BeautifulSoup
import utils
from slugify import slugify

sourcefile = Path(sourcefolder)

def create_post(d, link_text, link_url, text, tags, overwrite=True):

    title = link_text
    slug = slugify(title)

    post = utils.PostBuilder(slug, source="delicious", content=text)
    post.date = dt
    post.title = title
    post.params["slug"] = slug
    post.params['link'] = {
        "url": link_url,
        "text": link_text,
        "source": "delicious",
        "source_url": "https://del.icio.us/roytang"
    }
    post.kind = "links"
    post.tags = tags
    post.save()


with sourcefile.open(encoding="UTF-8") as fd:
    soup = BeautifulSoup(fd.read(), "html.parser")
    anchors = soup.find_all("a")
    for a in anchors:
        dt = utils.time_to_date(a["add_date"])
        #print(a)
        text = ""
        next = a.next_sibling.next_sibling
        if next is not None and next.name == "dd":
            for c in next.children:
                if c.name is None:
                    text = str(c)
                    break
        create_post(dt, a.get_text(), a["href"], text, a["tags"].split(","))