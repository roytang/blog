---
title: Django Update – WordPress Import and More
type: post
date: 2008-11-23T00:04:00+00:00
url: /2008/11/django-update-wordpress-import-and-more/
categories:
  - Software Development
tags:
  - royondjango

---
I&#8217;ve been busy at work so fell a bit behind with Django. Last night I worked on a WordPress importer, so that I could migrate posts from my current blog(s) into the Django-powered blog that I&#8217;m coding. I&#8217;m using BeautifulSoup to parse the WordPress export file and insert them as Django objects.

Since I was running the script repeatedly, I had to figure out how to easily run it from the command line, without having to run it from inside manage.py shell. After some searching, I found that what I needed to do was set an environment variable DJANGO\_SETTINGS\_FILE to point to my settings file. After that, the importer script could be run repeatedly.

Also made a few tweaks to my dev copy:

  * Modified URL mapping to follow the permalinks of the old blog (so that people linking to me don&#8217;t suddenly have broken links)
  * Added a tag cloud (Still using django-tagging)
  * Added markdown support to the admin maintenance screen. I used to think I would need to code my own form for posting, but I think I can live with just using the admin-provided one (initially at least)

I plan to migrate my main blog over once I take my Christmas break (hopefully 2nd week of December)

Stuff to do:

  * Use clean, non-hardcoded urls (url template tag and reverse())
  * Customize the admin screen for posting
  * Clean up the layout and templates