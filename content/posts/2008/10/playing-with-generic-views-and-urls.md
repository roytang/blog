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

&#8220;when redirecting, how can I make the redirect URL decoupled from the urls.py of the parent app?&#8221;

-> It turns out that HttpResponseRedirect supports relative paths, so this was fine.

return HttpResponseRedirect(&#8220;../&#8221; + str(post.id) + &#8220;/&#8221;)

I got the basic posting structure up.

/post/new/ -> To make new posts

/post// -> To view a single post

/post/all/ -> To view all posts

I should probably start thinking of a better url scheme. Ideally, I&#8217;d want the @login_required views to be indicated as such in the urls. Something like &#8220;/admin/post/&#8221; for new posts &#8220;/admin/manage/&#8221; for a screen to manage posts to differentiate it from a screen just to list them out.

Next I think I&#8217;ll try to CSS-ify the blog; I&#8217;ll probably just reuse stuff from one of the blogger templates as I&#8217;m still not very good with the HTML/CSS.

I&#8217;ll also look into using some of the date-based generic views to get an archive view. I&#8217;ll need more data though. Will consider importing from the WordPress blog.