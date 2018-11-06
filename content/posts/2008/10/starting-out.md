---
title: Starting out
type: post
date: 2008-10-19T07:33:00+00:00
url: /2008/10/starting-out/
categories:
  - Software Development
tags:
  - royondjango

---
The quintessential app to learn from is of course a blog.

Started using a simple Post model. Added the new post form and view. Can now successfully insert posts into the DB.

Next:

&#8211; create the detail page that will show the post after saving

Figure out:

&#8211; when redirecting, how can I make the redirect URL decoupled from the urls.py of the parent app?

i.e. if the parent app has the following mapping:

&#8216;^blog/&#8217; -> pass to blog.urls.urlpatterns

the blog app has mappings for

&#8216;^post/new/&#8217; -> new post

&#8216;^post/([A-Za-z\-])/&#8217; -> post detail

inside the view, I want to redirect to &#8220;post/&#8221;, but with respect to the app, it should be &#8220;blog/post/&#8221;

I should subscribe to one of the Django mailing lists to ask stuff like this.

## Comments

### Comment by Tim Medina on 2008-10-20 08:46:00 +0000
Hey Roy!

Good to see another pinoy interested in django. (You might want to join the
  
\[google group of pinoy django users\]\[1\])

About your problem, you might want to take a look at \[ this\]\[2\].

\[Tim\]\[3\]

[1]: <a href="http://djangoph.com" rel="nofollow">http://djangoph.com</a>

[2]: <a href="http://docs.djangoproject.com/en/dev/topics/http/urls/#reverse" rel="nofollow">http://docs.djangoproject.com/en/dev/topics/http/urls/#reverse</a>

[3]: <a href="http://devblog.timmedina.com/" rel="nofollow">http://devblog.timmedina.com/</a>