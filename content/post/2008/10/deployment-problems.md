---
date: 2008-10-21 06:52:00
source: royondjango
syndicated:
- type: blogger
  url: https://royondjango.blogspot.com/2008/10/deployment-problems.html
tags:
- royondjango
- django
- python
- software development
title: Deployment Problems
type: post
url: /2008/10/deployment-problems/
---

So I got a basic blog app up and running.

Posting, paged archives, etc.

Comments implemented using the django.contrib.comments. No problems here, the only caveat being most of the current documentation found by Google searches refer to the pre-1.0 version. Need to peruse the official docs for 1.0 stuff.

RSS feeds implemented using django.contrib.syndication, this one seems fine.

I tested it and it's running fine on localhost. I also have a free django hosting account at http://bells-n-whistles.net, so I try to upload it there. However, when I access the website there ([http://www.randomencounters.bells-n-whistles.net/blog/][1]), I get the following error:

`'comments' is not a valid tag library: Could not load template library from django.templatetags.comments, No module named comments`

I think the settings.py is not being reloaded - I tried to set Debug = False and I'm still getting the stacktraces.

Bah, I'll figure it out tomorrow.


 [1]: http://www.randomencounters.bells-n-whistles.net/blog/