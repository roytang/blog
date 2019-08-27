sourcefolder = "D://temp//roytang0400_20190820"

import xmltodict
import frontmatter
from pathlib import Path
from datetime import datetime, timedelta
from urllib.parse import urlparse
import json
import time
import re
import shutil

def time_to_date(ts):
    ts = int(ts)

    # if you encounter a "year is out of range" error the timestamp
    # may be in milliseconds, try `ts /= 1000` in that case
    return datetime.utcfromtimestamp(ts) #.strftime('%Y-%m-%d %H:%M:%S'))

sourcepath = Path(sourcefolder)
scraped = sourcepath / "scraped.json"
scraped_comments = sourcepath / "scraped-comments.json"
scraped_likes = sourcepath / "scraped-likes.json"

from igramscraper.instagram import Instagram
instagram = Instagram()

def scrape_media():
    medias = instagram.get_medias("roytang0400", 1000)
    out = []
    for media in medias:
        print(media)
        d = time_to_date(media.created_time) - timedelta(hours=7)
        print(d)
        out.append({
            'id': media.identifier,
            'shortcode': media.short_code,
            'caption': media.caption,
            'type': media.type,
            'created': time_to_date(media.created_time).strftime('%Y-%m-%dT%H:%M:%S'),
            'adjusted': d.strftime('%Y-%m-%dT%H:%M:%S'),
            'comments': media.comments_count,
            'likes': media.likes_count,
            'hrimg': media.image_high_resolution_url
        })

    with scraped.open('w', encoding='UTF-8') as f:
        f.write(json.dumps(out))


def scrape_comments():

    out = {}
    count = 0
    with scraped.open(encoding='UTF-8') as f, scraped_comments.open(encoding='UTF-8') as f2:
        j = json.loads(f.read())
        j2 = json.loads(f2.read())
        out = j2
        for p in j:
            print(p)
            if p['shortcode'] in j2:
                print("Skipping...")
                continue
            try:
                comments = instagram.get_media_comments_by_id(p['id'], 100)
            except:
                break

            out[p['shortcode']] = []
            for comment in comments['comments']:
                out[p['shortcode']].append({
                    'text': comment.text,
                    'owner': comment.owner.username,
                    'created_at': time_to_date(comment.created_at)
                })
            count = count + 1
            # if count > 10:
            #     break

    print("%s processed!" % (count))


    with scraped_comments.open('w', encoding='UTF-8') as f:
        f.write(json.dumps(out))

currfolder = Path.cwd()
baseoutfolder = currfolder / "content" / "photos"

def create_photo_post(p, m):
    d = datetime.strptime(m['adjusted'], '%Y-%m-%dT%H:%M:%S')
    print(d)

    # create the output folder
    outfolder = baseoutfolder / str(d.year) / ('%02d' % (d.month)) / m['shortcode']
    if not outfolder.exists():
        outfolder.mkdir(parents=True)

    # create the front matter index
    caption = m['caption']
    if caption is None:
        caption = ""
    fm = frontmatter.Post(caption)
    fm['source'] = 'instagram'
    fm['syndicated'] = [{
        'type': 'instagram',
        'url': "https://instagram.com/p/%s/" % m['shortcode'] 
    }]
    fm['location'] = m.get('location', '')
    fm['date'] = d
    fm['tags'] = []
    hashtags = re.findall(r"#(\w+)", caption)    
    for ht in hashtags:
        fm['tags'].append(ht)
    
    newfile = frontmatter.dumps(fm)
    outfile = outfolder / "index.md"
    with outfile.open("w", encoding="UTF-8") as f:
        f.write(newfile)

    # copy the photo into the target folder
    photo = sourcepath / p['path']
    if photo.exists():
        to_file = outfolder / photo.name
        shutil.copy(str(photo), str(to_file))    
    else:
        print("##### Missing photo!")
        print(m)

scraped_media = {}
with scraped.open(encoding="UTF-8") as f:
    j = json.loads(f.read())
    for p in j:
        cr_dt = p['adjusted'][0:10]
        if cr_dt not in scraped_media:
            scraped_media[cr_dt] = []
        scraped_media[cr_dt].append(p)

media = sourcepath / "media.json"
count = 0
unmatched = 0
with media.open(encoding="UTF-8") as f:
    j = json.loads(f.read())
    for p in j['photos']:
        photo = sourcepath / p['path']

        if 'created' in p:
            cr_dt = p['created'][0:10]
            dt2 = p['created'][-5:]
        else:
            cr_dt = p['taken_at'][0:10]
            dt2 = p['taken_at'][-5:]

        if cr_dt in scraped_media:
            matchbydate = scraped_media[cr_dt]
            # print(matchbydate)
            if len(matchbydate) > 1:
                found = False
                emptycaptions = []
                for m in matchbydate:
                    if m['caption'] == p['caption'] or m['adjusted'][-5:] == dt2:
                        match = m
                        found = True
                        break
                    if m['caption'] is None or len(m['caption']) == 0:
                        emptycaptions.append(m)

                if not found and len(p['caption']) ==0 and len(emptycaptions) == 1:
                    match = emptycaptions[0]
                    found = True

                # this is terrible
                    
                if not found:
                    print("############# Multiple matches: %s :: %s :: %s :: Photo exists? %s" % (cr_dt, dt2, p['caption'], photo.exists()))
                    continue
            else:
                match = matchbydate[0]

            create_photo_post(p, match)
            
        else:
            print("############# Unmatched: %s :: %s" % (cr_dt, p['caption']))
            unmatched = unmatched + 1

        # print("======")
        count = count+1

