SOURCE_FILE = "D:\\temp\\twitter\\tweet.js"
OUTPUT_DIR = "D:\\repos\\blog\\content\\aside\\"

import frontmatter
import json

with open(SOURCE_FILE, encoding='utf-8') as f:
    d = json.load(f)
    idx = 0
    for d1 in d:
        content = d1["full_text"]

        post = frontmatter.Post(d1["full_text"])
        post['date'] = d1["created_at"]
        post['source'] = 'twitter'
        post['id'] = d1["id_str"]

        tags = []
        for ht in d1["entities"]["hashtags"]:
            tags.append(ht["text"])
        if len(tags) > 0:
            post['tags'] = tags

        media = []
        if "extended_entities" in d1:
            for m in d1["extended_entities"]["media"]:
                media.append(m["media_url_https"])
        post['media'] = media

        post["is_rt"] = False
        if content.startswith("RT @"):
            post.content = "Retweeted: {{< tweet " + post['id'] + " >}}"

        newfile = frontmatter.dumps(post)
        with open(OUTPUT_DIR + d1["id_str"] + ".md", "w", encoding='utf-8') as w:
            w.write(newfile)

        idx = idx + 1
        if idx > 200:
            break
