SOURCE_FILE = "D:\\temp\\facebook\\posts\\your_posts_1.json"
SOURCE_FILE_2 = "D:\\temp\\facebook\\comments\\comments.json"
TWITTER_SOURCE_FILE = "D:\\temp\\twitter\\tweet.js"
INSTA_SOURCE_FILE = "D:\\temp\\insta\\media.json"
from datetime import datetime
import json
from pathlib import Path
from gen_svg import gen_chart, thisyear

def fb():

    years = ["2007", "2008", "2009", "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019", "2020"]
    data = [6, 18, 499, 264, 133, 202, 515, 1026, 1042, 2225, 1444, 1081, 315, 32]
    data2 = [0, 0, 1, 11, 44, 46, 12, 596, 701, 2066, 765, 487, 138, 322]
    gen_chart(years, data, "fb", title="Posts", extra_data=[{"data": data2, "title": "Comments"}])    

    return

    count_by_year = {}
    with Path(SOURCE_FILE).open(encoding='utf-8') as f:
        d = json.load(f)
        for t in d:
            timestamp = t["timestamp"]
            dt = datetime.utcfromtimestamp(timestamp)
            year = str(dt.year)
            count_by_year[year] = count_by_year.get(year, 0) + 1
    print(json.dumps(count_by_year, indent=2))

    comments_by_year = {}
    with Path(SOURCE_FILE_2).open(encoding='utf-8') as f:
        d = json.load(f)["comments"]
        for t in d:
            timestamp = t["timestamp"]
            dt = datetime.utcfromtimestamp(timestamp)
            year = str(dt.year)
            comments_by_year[year] = comments_by_year.get(year, 0) + 1
    print(json.dumps(comments_by_year, indent=2))

    years = list(count_by_year.keys())
    years.sort()

    # don't include current year in stats
    if thisyear in years:
        years.remove(thisyear)
    data = []
    data2 = []
    for year in years:
        data.append(count_by_year[year])
        data2.append(comments_by_year.get(year, 0))
    gen_chart(years, data, "fb", title="Posts", extra_data=[{"data": data2, "title": "Comments"}])    

def twitter():
    replies = 0
    retweets = 0

    count_by_year = {}
    with Path(TWITTER_SOURCE_FILE).open(encoding='utf-8') as f:
        d = json.load(f)
        idx = 0
        for t in d:
            dt = datetime.strptime(t['created_at'], "%a %b %d %H:%M:%S %z %Y")
            year = str(dt.year)
            count_by_year[year] = count_by_year.get(year, 0) + 1
    years = list(count_by_year.keys())
    years.sort()
    # don't include current year in stats
    if thisyear in years:
        years.remove(thisyear)
    data = []
    for year in years:
        data.append(count_by_year[year])
    print(json.dumps(count_by_year, indent=2))
    gen_chart(years, data, "twitter")    

def reddit():
    years = ["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
    submissions = [25,52,58,63,48,31,75,20,32,20]
    comments = [43,124,256,457,136,33,829,199,148,172]
    gen_chart(years, submissions, "reddit", title="Submissions", extra_data=[{"data": comments, "title": "Comments"}])    

def insta():

    count_by_year = {}
    with Path(INSTA_SOURCE_FILE).open(encoding='utf-8') as f:
        d = json.load(f)["photos"]
        for t in d:
            year = t["taken_at"].split("-")[0]
            count_by_year[year] = count_by_year.get(year, 0) + 1
    print(json.dumps(count_by_year, indent=2))

    years = list(count_by_year.keys())
    years.sort()

    # don't include current year in stats
    if thisyear in years:
        years.remove(thisyear)
    data = []
    for year in years:
        data.append(count_by_year[year])
    gen_chart(years, data, "insta")    

fb()
#twitter()
#reddit()
#insta()