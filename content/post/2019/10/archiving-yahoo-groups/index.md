---
author: roy
categories: []
date: 2019-10-20
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1185854214645407746/
tags:
- tech life
title: Archiving Yahoo Groups
type: post
---

So a couple of days ago, Yahoo announced that it was shutting down [Yahoo Groups](https://www.vice.com/en_us/article/8xwe9p/yahoo-groups-is-winding-down-and-all-content-will-be-permanently-removed). I was a big user of Yahoo Groups back in the day. I was a member of several active mailing lists in the early 2000s, including some fandom groups (see: [The Rise and Fall of the Final Fantasy Forum](https://roytang.net/2018/10/the-rise-and-fall-of-the-final-fantasy-forum/)) and a few alumni groups and some [MTG](https://roytang.net/tags/mtg/)-related ones. Now all of that content is vanishing!

Since I hate losing content to the sands of time, I immediately looked at my options for archiving my Yahoo Groups content. Groups like archive.org are working to archive publicly-accessible groups, but most of the relevant ones for me were private groups, so I had to do things myself. Yahoo itself provided a link to a ["data privacy dashboard"](https://help.yahoo.com/kb/groups/download-data-privacy-dashboard-sln28671.html) which could supposedly export your data, but it's ridiculously useless. It only exports your subscribed groups and your preferences for each group. None of the relevant things like messages, files, photos, etc. Yahoo also provides a page with instructions on how to "download your files and photos", but it basically only says to go to the web interface and download them one by one, also ridiculous.

I looked instead to an open source [archive script written in Python](https://github.com/andrewferguson/YahooGroups-Archiver) that I could easily modify for my own needs. I made a [fork with my own changes](https://github.com/roytang/YahooGroups-Archiver). The only change to the main script was to continue processing when an error 500 was encountered. The original script terminated processing at this time, assuming you had been rate-limited. But manual checking revealed that Yahoo Groups was throwing the error because there were some messages it simply could not retrieve for whatever reason. I simply removed the script-ending line so that the processing could continue after an error 500. I also added a separate script to download group photos, since the original only downloaded messages. (More on that later.)

### What to Archive?

I decided to only archive groups where I had actively sent messages myself for a period of time. I was a member of some public developer-oriented groups that I never really participated in, so those were out. I also decided to archive messages, files and attachments for the relevant groups. There's this one group where I was only active for maybe a few months in the early 2000s, but the group itself stayed semi-active for up to a decade, so I ended up archiving more than a 100k messages from that group, most of which were not personally relevant to me. Well, it's not like these archives take a whole lot of space, so I'll keep them for now.

### Files and Photos

As mentioned, the original python script only exported messages but I wanted files and photos too. I was a bit more selective for the files and photos and only chose to archive from those groups that were more personally relevant to me. (i.e. I didn't get the files/photos for that 100k-message group mentioned above). Luckily, the relevant groups didn't have many files. It would have taken longer to write a script to do it, so I just manually downloaded files one by one.

Photos were a different matter. A couple of the relevant groups had too many photos to bother downloading one at a time, so I ended up doing the method of 

- "load the webpage and scroll down until you have all the photos"
- save the html
- run a [python script](https://github.com/roytang/YahooGroups-Archiver/blob/master/archive_photos.py) to parse the HTML, store the metadata and download the full-res photo

### Wrapping up

I didn't have that many groups so I only ended up with around 300MB (compressed) total worth of messages, files and photos archived. I stored them in my usual archive places (cloud storage, a couple of external HDs). Most of that (maybe 80%) is that really big group too, so if needed I can dump most of those messages later. Someday I may do a further deep dive or analytics of all this archived YG data, who knows what I'll find! (Spoken like a true digital pack rat.)