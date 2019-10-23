---
date: 2010-01-14 03:57:51
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/2062066/far-future-expire-header-and-http-304
tags:
- http
- questions
- stackoverflow
- software development
title: Far future expire header and HTTP 304
---

I'm trying to optimize the loading time of a website. One of the things I've done is set a far-futures expires header for static content so that they are cached (as described by [Yahoo][1]). However, even though they are cached, the browser still sends a request and gets back a 304 (Not Modified) response for that resource.

I realize the 304 response is very small and probably has minimal performance effect, but is there a way to make it such that the browser will no longer send the request at all and just always use the cache for that resource?


  [1]: http://developer.yahoo.com/performance/rules.html#expires