---
categories: []
date: 2019-08-14 00:00:00
tags:
- meta
- changelog
title: "Perpetually under renovation"
type: post
featuredImage: /uploads/2019/roytangnet_201908.png
---

Perhaps unsurprisingly, I'm enjoying tinkering with the site layout at the moment. I give up on expecting a "stable version" of the site anytime soon and readers can expect incremental updates unannounced going forward. This site is now perpetually under renovation.

Current layout image (this image is recursive):

![](/uploads/2019/roytangnet_201908.png)

Recent changes:

1. Someone called me out for not using a dark theme, so now here we are with a garish gray and green and orange theme, you're welcome.
2. Generally moving around of content and UI and adding of navigation items and such
3. Comment system revamp! I've removed Disqus, since that was a bit of a loading problem. Comments are now saved in the repo as static files; it took me a bit to figure that out, [I described my approach on the Hugo forums](https://discourse.gohugo.io/t/static-comment-for-hugo/1944/17?u=roytang). Unfortunately this means that for now there is no way to comment directly on posts. I will be adding that back later, hopefully in a matter of days. Having the comments be a separate post type means you can now [browse them directly](/comment/). 
4. Webmentions! I set up [webmentions.io](https://webmentions.io) and [brid.gy](https://brid.gy) so this site now accepts webmentions. Currently only Twitter webmentions are enabled on brid.gy (see the samples in the screenshots above).
5. Search! Previously the search widget was only sending you to a `"site:roytang.net"` search on DuckDuckGo. I changed it to perform indexing on the server, via the [Python Whoosh library](https://whoosh.readthedocs.io/en/latest/intro.html). Then any search request is sent via Javascript to a Flask server I have running, which queries the index and returns the relevant results.

There are almost certainly broken things still around, but I wanted to push the initial changes for now.