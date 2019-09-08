---
categories: []
date: 2008-10-19 07:33:00
tags:
- royondjango
- Software Development
title: Starting out
type: post
url: /2008/10/starting-out/
---

The quintessential app to learn from is of course a blog.

Started using a simple Post model. Added the new post form and view. Can now successfully insert posts into the DB.

Next:

-- create the detail page that will show the post after saving

Figure out:

-- when redirecting, how can I make the redirect URL decoupled from the urls.py of the parent app?

i.e. if the parent app has the following mapping:

&#8216;^blog/' -> pass to blog.urls.urlpatterns

the blog app has mappings for

&#8216;^post/new/' -> new post

&#8216;^post/([A-Za-z\-])/' -> post detail

inside the view, I want to redirect to "post/", but with respect to the app, it should be "blog/post/"

I should subscribe to one of the Django mailing lists to ask stuff like this.