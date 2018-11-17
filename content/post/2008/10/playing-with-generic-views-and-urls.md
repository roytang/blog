---
categories:
- Software Development
date: 2008-10-20 13:44:00
tags:
- royondjango
title: Playing with Generic Views and URLs
type: post
url: /2008/10/playing-with-generic-views-and-urls/
---

"when redirecting, how can I make the redirect URL decoupled from the urls.py of the parent app?&#8221;

-> It turns out that HttpResponseRedirect supports relative paths, so this was fine.

return HttpResponseRedirect("../&#8221; + str(post.id) + "/&#8221;)

I got the basic posting structure up.

/post/new/ -> To make new posts

/post// -> To view a single post

/post/all/ -> To view all posts

I should probably start thinking of a better url scheme. Ideally, I'd want the @login_required views to be indicated as such in the urls. Something like "/admin/post/&#8221; for new posts "/admin/manage/&#8221; for a screen to manage posts to differentiate it from a screen just to list them out.

Next I think I'll try to CSS-ify the blog; I'll probably just reuse stuff from one of the blogger templates as I'm still not very good with the HTML/CSS.

I'll also look into using some of the date-based generic views to get an archive view. I'll need more data though. Will consider importing from the WordPress blog.