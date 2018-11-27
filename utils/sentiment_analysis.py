# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import frontmatter
import io
from textblob import TextBlob
from dateutil.parser import parse

def check_posts():
    cwd = Path.cwd() 
    stats = []
    max = 0
    maxfile = ''
    aggstats = {}
    # navigate to ./content/posts
    p = cwd / "content" / "post"
    for mdfile in p.glob("**/*.md"):
        # print(str(mdfile))
        with mdfile.open(encoding='utf-8') as f:
            post = frontmatter.load(f)
            post_text = str(post)
            # print(post_text)
            blob = TextBlob(post_text)
            score = blob.sentiment.polarity
            # print(score)
            d = post.get('date')
            year = d.year
            if year not in aggstats:
                aggstats[year] = {
                    "count": 1,
                    "total": score
                }
            else:
                aggstats[year]["count"] = aggstats[year]["count"] + 1
                aggstats[year]["total"] = aggstats[year]["total"] + score
            if score > max:
                max = score
                maxfile = mdfile
            stats.append((str(mdfile), score, year))

    #print(aggstats)
    for y in aggstats:
        year = aggstats[y]
        ave = year["total"]/year["count"]
        print(str(y) + ": " + str(ave))

import csv
import datetime

def check_tweets():
    file_reader= open("tweets.csv", "rt", encoding='utf-8')
    read = csv.reader(file_reader)
    idx = 0
    stats = []
    max = 0
    maxfile = ''
    aggstats = {}
    count = 0
    for row in read:
        idx = idx + 1
        if idx == 1:
            continue
        #print(row[3])
        dt = (datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S +0000"))
        #print(dt)
        count = count + 1
        post_text = str(row[5])
        # print(post_text)
        blob = TextBlob(post_text)
        score = blob.sentiment.polarity
        # print(score)
        year = dt.year
        month = dt.month
        key = str(year) + "-" + str(month).zfill(2)
        if key not in aggstats:
            aggstats[key] = {
                "count": 1,
                "total": score
            }
        else:
            aggstats[key]["count"] = aggstats[key]["count"] + 1
            aggstats[key]["total"] = aggstats[key]["total"] + score
        stats.append((key, score, post_text))

    for y in aggstats:
        year = aggstats[y]
        ave = year["total"]/year["count"]
        if ave > 0:
            print(str(y) + "," + str(ave))
    # for s in stats:
    #     try:
    #         print("%s,%s,%s" % s)
    #     except:
    #         pass

check_tweets()