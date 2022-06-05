---
date: 2022-06-04 07:46:16
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/108418186630988049
- type: twitter
  url: https://twitter.com/roytang/status/1532998256112054272/
tags:
- blogging
- meta
- tech-life
title: Blogroll Updates
---

I finally updated my long-unmaintained [blogroll page](/page/blogroll).

The contents of this page are only one category in my feedreader. Typically when I find a new blog that seems interesting to follow, I first put in a category called "tentative". After some time of following, I'll decide whether I want it to be in my public blogroll. Reviewing the public blogroll also means removing blogs that are no longer current or updated. I will typically move those into a feedreader category called "defunct". I'll highlight new/added blogs in a future ["Follow Friday"](/tags/follow-friday/) post (a series which I have neglected to follow-up on because of reasons.)

(Aside from the public blogroll and the above categories, my feedreader includes a number of feeds that are really only for my personal consumption and not for sharing. Things like notifications, feeds with very low signal to noise ratio, etc.)

Some features added with this update:

- Added last post date and title/link to each feed, as an indicator of activity. Partially inspired by [Fraidycat](https://fraidyc.at/).
- Added [a page that shows the river of recent posts from followed blogs](/river/). Inspired by Tom Critchlow's ["Increasing the surface area of blogging"](https://tomcritchlow.com/2022/04/21/new-rss/)
- The OPML file used to generate the blogroll is now [publicly available](/blogroll/opml/) and styled to be human readable. Inspired by OPMLs from [Rubenerd](https://rubenerd.com/omake.opml), [Maya.land](https://maya.land/blogroll.opml) and [Zylstra](https://www.zylstra.org/blog/2019/06/my-human-readable-opml-blogroll/). The styling is pretty basic for now; I've yet to figure out how I actually want it to look.
- Finally: I added a `<link rel="blogroll" >` element to the HTML of each page of this site, pointing to the publicly-accessible OPML. This isn't used anywhere (at the moment), but I felt like it was a good idea to have a machine-readable link to your public follows. (It's a bit like how social media APIs expose your public follow lists). If enough sites do something like this, we could have programs that can trace/build follow graphs or create recommendation engines to improve discoverability among blogs for example. Or perhaps when you give your feed reader a site URL, it can automatically show you the list of follows as recommendations. Something to consider.

Blogs!