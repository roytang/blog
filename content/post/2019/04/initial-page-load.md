---
author: roy
categories: []
date: 2019-04-10 05:56:56
tags:
- Tech Life
- Meta
title: Initial Page Load
type: post
---

I read a recent [blog post from a friend](https://testkeis.wordpress.com/2019/03/21/wondering-how-much-it-matters-initial-load-of-page/) about the large page sizes on initial load of a web page. From there, I got to a link which said that the [average page size nowadays is at least 3MB](https://speedcurve.com/blog/web-performance-page-bloat/).

This led me to check the performance of this very blog/site. Initial load of the home page clocks in with 13 requests weighing around 140KB total. This is not bad, in fact it would be a significant improvmenet since [I migrated to a static site using Hugo](/2018/11/site-migration-from-wordpress-to-hugo/). The homepage of the old Wordpress version of the blog comes with 44 requests totalling a bit over 500KB. And the new homepage lists way more posts too.

The page for individual posts leaves some room for improvement however, coming at 62 requests totalling more than 2MB. The main culprit is Disqus which I use for commenting. At least Disqus uses delayed loading, so the content renders immediately, but that's still a lot of bandwidth that could be saved. Leaving aside the question of "Do I really need comments?", I did a quick search if there were pre-existing solutions for optimizing Disqus loading on static sites.

The best hit so far was [disqusLoader](https://css-tricks.com/lazy-loading-disqus-comments/), which avoids loading Disqus until the comment area actually scrolls into view. It's a neat idea, but I encountered some JS errors when I did a quick test with it. I'll revisit this again later when I have more time.

An alternative of course would be to write my own JS-based commenting engine to rival Disqus, which seems to have no competition in its particular niche. I like building things so this option naturally came to mind, but in all likelihood I don't have time to do that, and there's a good chance it may end up as heavy as Disqus anyway. 

Need to think about this some more.