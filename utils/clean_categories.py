# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io

default_category='Just Another Day'

cats_map = {
    "Books" : "Pop Culture",
    "Comics": "Pop Culture",
    "Hardware": "Tech Life",
    "Job Hunting": "", # empty means throw it to default cat if no other cats
    "Learning Things": "Self-Improvement",
    "Legacy Blog Posts": "",
    "Movies": "Pop Culture",
    "Music": "Pop Culture",
    "Nostalgia": "",
    "Politics": "Opinions",
    "Puzzles": "Tech Life", # das weird
    "Review" : "",
    "TV Series": "Pop Culture",
    "Current Events": "",
    "Myself": ""
}

albums_map = {
    "sketch": "sketchbook",
    "sketchdaily": "sketchbook",
    "pickups": "pickups"
}

tags_map = {
    "comicbooks": "comics",
    "games": "gaming",
    # "magic the gathering": "mtg",
    # "magicarena": "mtg",
    # "magic arena": "mtg",
    # "magic arena": "magicarena",
    # "m11": "mtg",
    # "m12": "mtg",
    # "m13": "mtg",
    # "mtgakh": "mtg",
    # "mtgavr": "mtg",
    # "mtgbar": "mtg",
    # "mtgbfz": "mtg",
    # "mtgdom": "mtg",
    # "mtgdtk": "mtg",
    # "mtgeldraine": "mtg",
    # "mtgemn": "mtg",
    # "mtgfinance": "mtg",
    # "mtgfnm": "mtg",
    # "mtgfrf": "mtg",
    # "mtggtc": "mtg",
    # "mtghou": "mtg",
    # "mtginn": "mtg",
    # "mtgjou": "mtg",
    # "mtgkld": "mtg",
    # "mtgktk": "mtg",
    # "mtgmm2015": "mtg",
    # "mtgnationals": "mtg",
    # "mtgnationalsph": "mtg",
    # "mtgnph": "mtg",
    # "mtgo": "mtg",
    # "mtgocc": "mtg",
    # "mtgocube": "mtg",
    # "mtgogw": "mtg",
    # "mtgpc": "mtg",
    # "mtgrix": "mtg",
    # "mtgrna": "mtg",
    # "mtgseattle": "mtg",
    # "mtgsoi": "mtg",
    # "mtgun3": "mtg",
    # "mtgwar": "mtg",
    # "mtgwmc": "mtg",
    # "mtgwritingcontest": "mtg",
    # "mtgxln": "mtg",
}

delete_tags = [
    "magic the gathering",
    "magic arena",
    "1s",
    "comicbooks",
    "games",
    "reddit_submission"
]

def clean_categories():
    count = 0
    cwd = Path.cwd() 
    # navigate to ./content/posts
    p = cwd / "content"
    for mdfile in p.glob("**/*.md"):
        # print(str(mdfile))
        with mdfile.open(encoding='UTF-8') as f:
            try:
                post = frontmatter.load(f)
            except Exception as e:
                print("Error parsing file: " + str(mdfile))
                print(e)
                continue

            has_changes = False

            tags = []
            if post.get("tags") != None:
                tags = post.get("tags")
                # print(tags)
                if type(tags) == str:
                    tags = [tags] # standardize to a list

            newcats = []
            if post.get('categories') == None:
                # post['categories'] = [default_category]
                # has_changes = True
                pass
            else: # Categories exists
                cats = post['categories']
                if type(cats) == str:
                    cats = [cats] # standardize to a list

                for cat in cats:
                    has_changes = True
                    if cat == default_category:
                        continue
                    if cat not in tags:
                        tags.append(cat)
                    # if cats_map.get(cat) == None: # no changes, copy over as-is
                    #     if cat not in newcats:
                    #         newcats.append(cat)
                    # else:
                    #     newcat = cats_map[cat]
                    #     # old cat is now a tag
                    #     tags.append(cat)
                    #     has_changes = True
                    #     if len(newcat) > 0:
                    #         # move to new cat
                    #         if newcat not in newcats:
                    #             newcats.append(newcat)
                    #     else:
                    #         # move to default cat if no other cats
                    #         if len(cats) == 1:
                    #             newcats.append(default_category)
                newcats = [] # no more cats!

            new_tags = []
            for tag in tags:
                tag = tag.lower()
                if tag in delete_tags or tag.isnumeric():
                    has_changes = True
                else:
                    new_tags.append(tag)
                if tag in tags_map:
                    new_tag = tags_map[tag]
                    has_changes = True
                    if new_tag not in new_tags and new_tag not in delete_tags:
                        new_tags.append(new_tag)
            tags = new_tags              


            # oldlen = len(tags)
            # if oldlen > 0:
            #     tags = list(set(tags))
            #     newlen = len(tags)
            #     if oldlen > newlen:
            #         has_changes = True
            #     post['tags'] = tags
            # if len(newcats) > 0:
            #     post['categories'] = newcats
            post['tags'] = tags
            if post.get('categories', None) is not None:
                post.__delitem__('categories') # no more cats!

            # print(post['categories'])
            # print(post.get('tags'))

            album = None
            for tag in tags:
                if tag in albums_map:
                    album = albums_map[tag]      
            if album is not None:
                has_changes = True
                post['album'] = album

            # Save the file.
            if has_changes:
                newfile = frontmatter.dumps(post)
                with mdfile.open("w", encoding='UTF-8') as w:
                    w.write(newfile)
                    count = count + 1

    print("Updated files: " + str(count))
clean_categories()    