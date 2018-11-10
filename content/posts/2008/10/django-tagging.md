---
categories:
- Software Development
date: 2008-10-26 04:22:00
tags:
- royondjango
title: django-tagging
type: post
url: /2008/10/django-tagging/
---

I wanted to add some basic tagging to my blog app so I tried out
  
[
  
django-tagging
  
][1] 
  
. Unfortunately, the featured downloads on the Google Code site are quite out-of-date and would not work with Django 1.0, so I did a subversion checkout instead. If you're getting an error like &#8220;ImportError: cannot import name parse_lookup&#8221;, then you need to get the source code from SVN.

Adding the tagging to the blog was pretty easy:

1. Add the tagging app to settings.py

2. Add a tagging.fields.TagField to the Post model

3. Add a &#8220;tags&#8221; text field to the post form used.

4. Modify templates to display the tags.

5. I used something like &#8220;/tag/&#8221; url mapping to get all posts associated with a tag. Then you just need to write a wrapper around the object_list generic view:

> from tagging.models import Tag, TaggedItem
> 
> from django.views.generic.list\_detail import object\_list
> 
> def posts\_by\_tag(request, tag):
> 
> o_tag = Tag.objects.get(name=tag)
> 
> queryset = TaggedItem.objects.get\_by\_model(Post, o_tag)
> 
> return object_list(request, queryset)

This view will use the same template used to list out posts normally.

 [1]: http://code.google.com/p/django-tagging/