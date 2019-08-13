# one-time job: clean up comments embedded into the mdfile for legacy blog posts imported from wordpress

from pathlib import Path
import frontmatter
import io
import slugify
from datetime import datetime

def end_comment(mdfile, p, cf, post, comment):
    # derive the path for the parent post
    # this part is copy-pasted from indexer.py
    # a little bit more and imma gonna need a utils.py lol
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
    
    fm = frontmatter.Post(comment["content"])
    fm['source'] = 'wordpress'
    date = comment['date']
    fm['date'] = date
    # create the year folder if it doesnt exist
    yearfldr = cf / str(date.year)
    if not yearfldr.exists():
        yearfldr.mkdir()
    # same for month 
    month = str(date.month)
    if len(month) == 1:
        month = "0" + month
    monthfldr = yearfldr / month
    if not monthfldr.exists():
        monthfldr.mkdir()

    fm['parent_page'] = { 'urlpath' : u, 'title': post['title'] }
    fm['author'] = { 'name': comment['author']['name'], 'url': comment['author'].get('url', '') }

    newfile = frontmatter.dumps(fm)
    newfilename = "wp-%s-%s.md" % ( comment['author']['name'], date.strftime('%Y%m%d%H%M%S'))
    outfile = monthfldr / newfilename
    with outfile.open("w", encoding='utf-8') as w:
        w.write(newfile)                                

def clean_comments():
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content" / "post"
    cf = cwd / "content" / "comment"
    for mdfile in p.glob("**/*.md"):
        with mdfile.open(encoding="UTF-8") as f:
            try:
                post = frontmatter.load(f)
            except:
                print("Error parsing file " + str(mdfile))
                continue

            if post.content.find("\n## Comments") < 0:
                continue

            #print(str(mdfile))

            parts = post.content.split("\n## Comments")
            main_content = parts[0]
            comments_part = parts[1]

            comment = None
            lines = comments_part.split("\n")
            for line in lines:
                if line.startswith("### Comment by "):
                    # ends the existing comment
                    if comment is not None:
                        end_comment(mdfile, p, cf, post, comment)
                        comment = None
                    
                    # starts a new comment
                    comment = { 'content' : '', 'author': {} }
                    authorondate = line[len("### Comment by "):]
                    parts = authorondate.split(" on ")
                    author = parts[0]
                    datestr = parts[1]

                    if author.startswith("["):
                        # i feel like i could be doing more regex usage here, but then i'd have two problems lol
                        # remove leading [ and trailing )
                        author = author[1:-1]
                        authorparts = author.split("](")
                        comment['author'] = { 'name': authorparts[0], 'url': authorparts[1] }
                        # special handling for me
                        if comment['author']['url'] == 'http://roytang.net':
                            comment['author']['url'] = 'https://roytang.net/'
                        if comment['author']['url'] == 'http://roytang.net/blog':
                            comment['author']['url'] = 'https://roytang.net/'
                    else: 
                        comment['author'] = { 'name': author }

                    date = datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S %z')
                    comment['date'] = date
                    #print(date)
                else:
                    if comment is not None:
                        comment['content'] = comment['content'] + line

                if comment is not None:
                    end_comment(mdfile, p, cf, post, comment)

            # Remove the old comments from the main file
            post.content = main_content
            newfile = frontmatter.dumps(post)
            with mdfile.open("w", encoding="UTF-8") as w:
                w.write(newfile)

clean_comments()