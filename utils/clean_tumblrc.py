# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io
from importers import utils
import os

urlmap = utils.loadurlmap()

# clean up old IRCB tumblr posts that were imported as tweets - merge them with the actual tumblr post
def clean_reddit():
    count = 0
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "notes"
    for_deletion = []
    for mdfile in p.glob("**/*.md"):
        with mdfile.open(encoding="UTF-8") as f:
            try:
                post = frontmatter.load(f)
            except:
                print(str(mdfile))
                print("Error parsing file")
                continue

            has_changes = False

            if post.get("source", "") == "twitter":
                # raw_urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
                content = post.content
                if content.find("ireadcomicbooks.tumblr.com") >= 0:
                    print("\n\n===============")
                    print(str(mdfile))
                    print(content)

                    # the tumblr url is always at the end, so we just clip the end of the string
                    start = content.find("https://ireadcomicbooks.tumblr.com/")
                    url = content[start:]
                    url = url.replace("#_=_", "")
                    print(url)

                    # find the actual post this tumblr was syndicated to
                    um = urlmap[url]
                    target_file = utils.urlmap_to_mdfile(um)
                    print(target_file)
                    for item in post["syndicated"]:
                        utils.add_syndication(target_file, item["url"], item["type"])

                    # lastly, we delete the old file
                    if mdfile.name == "index.md":
                        print ("THERE WAS A PROBLEM")
                        return
                    else:
                        for_deletion.append(str(mdfile))
                    count = count + 1

    for filepath in for_deletion:
        os.remove(filepath)

    print("Updated files: " + str(count))

clean_reddit()