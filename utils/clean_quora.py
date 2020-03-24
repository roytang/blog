# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io

# clean up the sins of old quora comments imported via tracker
def clean_quora():
    count = 0
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "notes"
    for mdfile in p.glob("**/*.md"):
        with mdfile.open(encoding="UTF-8") as f:
            try:
                post = frontmatter.load(f)
            except:
                print("Error parsing file")
                continue

            has_changes = False

            if post.get("source") == "quora":
                content = post.content
                # idx = content.find('<span class="ui_qtext_rendered_qtext">')
                # prechar = (ord(content[idx-3]), ord(content[idx-2]), ord(content[idx-1]))
                # filename = (str(mdfile))
                # print(prechar, filename)
                content = content.replace('<span class="ui_qtext_rendered_qtext">', '\n<span class="ui_qtext_rendered_qtext">')
                if content != post.content:
                    post.content = content
                    has_changes = True

            # Save the file.
            if has_changes:
                newfile = frontmatter.dumps(post)
                with mdfile.open("w") as w:
                    w.write(newfile)
                    count = count + 1

    print("Updated files: " + str(count))

clean_quora()