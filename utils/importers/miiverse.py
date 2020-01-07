IMPORT_FILE = "d:\\temp\\archiverse.html"
from pathlib import Path
from bs4 import BeautifulSoup
from utils import PostBuilder, CommentBuilder
from datetime import datetime

import re
def strip_date_ordinal(s):                                             
    return re.sub(r'(\d)(st|nd|rd|th)', r'\1', s)

def filename_from_url(url):
    parts = url.split("/")
    filename = parts[-2] + "_" + parts[-1] + ".png" # presumptuous
    return filename

def import_main(filepath):
    with Path(filepath).open(encoding='UTF-8') as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        posts = soup.findAll("div", {"class": "post"})
        for post in posts:
            timestamp = post.findAll("span", {"class": "timestamp"})[0]
            dt = datetime.strptime(strip_date_ordinal(timestamp.text), "%A, %B %d, %Y %H:%M:%S %p")
            # print(dt)
            contentContainer = post.find("p", {"class": "post-content-memo"})
            content = contentContainer.text

            # to derive the post id, let's find the archive link
            anchors = post.find_all("a")
            archive_link = ""
            for a in anchors:
                if a.text == "View Archive Page":
                    archive_link = a["href"]
                    break

            post_id = archive_link.split("/")[-1]

            # find the link to the community
            commLinkContainer = post.find("h1", {"class":"community-container-heading"})
            communityName = commLinkContainer.text
            communityLink = "https://archiverse.guide%s" % (commLinkContainer.find("a")["href"])
            game_name = communityName.replace(" Community", "")

            content_header = "Posted in MiiVerse's [%s](%s):\n\n" % (communityName, communityLink)
            content = content_header + content

            post = PostBuilder(post_id, source="miiverse", content=content)
            post.date = dt
            post.kind = "note"
            for img in contentContainer.find_all("img"):
                post.kind = "photos"
                post.media.append(img["src"])
            post.tags = ["gaming", game_name]
            post.add_syndication("archive.org", archive_link)
            post.filename_from_url = filename_from_url
            post.save()

        print(len(posts))

def import_comments(filepath, parent_source_path):
    with Path(filepath).open(encoding='UTF-8') as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        posts = soup.findAll("div", {"class": "post"})
        index = 0
        for post in posts:
            index = index + 1
            if index == 1:
                continue # skip first entry, its always the orig post

            timestamp = post.findAll("span", {"class": "timestamp"})[0]
            dt = datetime.strptime(strip_date_ordinal(timestamp.text), "%A, %B %d, %Y %H:%M:%S %p")
            print(dt)
            contentContainer = post.find("p", {"class": "post-content-memo"})
            content = contentContainer.text
            print(content)

            # to derive the post id, let's find the archive link
            anchors = post.find_all("a")
            archive_link = ""
            for a in anchors:
                if a.text == "View Archive Page":
                    archive_link = a["href"]
                    break

            post_id = archive_link.split("/")[-1]

            # get author details
            container = post.find("p", {"class":"user-name"})
            anchor = container.find("a")
            span = container.find("span")
            author_name = "%s (%s)" % (anchor.text, span.text)
            author_url = "https://archiverse.guide%s" % (anchor["href"])

            img = post.find("img", {"class", "icon"})

            author = {
                "name": author_name,
                "url": author_url,
                "photo": img["src"]
            }

            cb = CommentBuilder(Path(parent_source_path))
            cb.add_comment(post_id, dt, author, "miiverse", content, overwrite=True)


# import_main(IMPORT_FILE)
import_comments("d:\\temp\\comments1.html", "D:\\repos\\blog\content\\note\\2014\\08\\AYMHAAACAADMUKl8-uaEQw\\index.md")
import_comments("d:\\temp\\comments2.html", "D:\\repos\\blog\content\\photos\\2014\\08\\AYMHAAACAABnUYoE7CRSyQ\\index.md")