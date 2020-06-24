---
date: 2020-06-24
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/104397000139419911
- type: twitter
  url: https://twitter.com/roytang/statuses/1275642321334394882/
tags:
- tech life
- software development
title: Scraping Facebook
---

I had been meaning to [quit Facebook](/2020/06/quitting-facebook/) for more than a year maybe, but I kept putting it off. The main reason being that I like having backups of my own digital data (still very much a [pack rat](/2007/12/pack-rat-mentality/)), and Facebook's [social media export](/2019/03/export-your-social-media-data/) is less than ideal, for me at least.

Less than ideal why? It doesn't include a lot of content I would like backed up, including:

- comments on my posts (there have been some good conversations with friends over the years I would prefer to preserve)
- things I've reposted from other people
- content of certain groups I'm members of (again, mostly for some interesting discussions over the years)
- pictures posted by other people that I've been tagged in

For a while I looked around for scraper programs/scripts to this for me, but none really did what I wanted. Early this month I finally wrote my own scraper scripts to pull that data out of Facebook, as a supplement to the actual FB export. It seems unlikely that these will be helpful to anyone else, especially since web scraping is an inherently brittle activity; any slight change in the FB HTML generation will break the scripts. In spite of that, I thought I'd share them publicly anyway, via Github gists.

- [Script to export FB timeline](https://gist.github.com/roytang/a5b4a8e4d511e97b9d25cb190f9dfb5d)
- [Script to export FB group](https://gist.github.com/roytang/1cb3a682a2c223e569e3009aceb0e319)

These are basically the same file, with minor changes between configuration and some scraping details. I wasn't expecting to need these scripts again in the future so I didn't bother with any kind of reusability. 

Some other notes about these scripts:

- made with Python! Using my favorite HTML parsing library, BeautifulSoup
- the scripts run against the mobile web version m.facebook.com. The main web version is troublesome because it executes JS to do its infinite scroll and I didn't want to waste time reverse engineering that
- there are some variables near the start that you should probably set. Most of it is output folders and group details, but the main one is the FB login cookie - basically you need to login to FB, then use dev tools or whatever to copy your cookie string
- the main output file is a gigantic JSON. There is no specified schema, basically I made things up as I went along. I'll figure out how to process this at a later date lol. 
- As a secondary output, there is also a cache folder that should contain the raw HTML parsed for each page. These aren't necessary to retain, as all the information they have should also be in the JSON. Images from posts are also downloaded into a `dls` folder. (The JSON will include the download path for the images from each post.)
- running the timeline export on my machine took the better part of 2-3 hours, for roughly 13 years worth of FB content. The output JSON was around 22 MB.
- running this might be considered spammy behavior by Facebook (understandably, but it's their fault they won't me do this via API), but the only consequence I've seen was that I wasn't able to view other people's profiles for some minutes after running the script

As for what I'm going to do with this data, that's still to be determined. The nonpublic content can be imported into the archive on this blog (if it isn't there yet), but that's a lot of manual work. As for the scripts, hopefully I won't have to use them again in the future, but maybe they can be useful to someone else!