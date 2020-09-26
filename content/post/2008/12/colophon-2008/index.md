---
date: 2008-12-27 02:08:22
tags:
- royondjango
- django
- python
- software development
title: Colophon 2008
type: post
url: /2008/12/colophon-2008/
---

**Frontend**: All page templates are valid (X)HTML. However, I choose not to claim valid XHTML (and no doc type declaration) since I can't guarantee that blog posts I write are compliant! The site uses standard CSS and uses the [Blueprint CSS Framework][1] for the grid layout of the page. The site design is entirely original (if not simple and bland -- I'm not very good with website design yet!). The site has minor usage of [JQuery Javascript library][2] in some parts.

**Backend**: The server side uses [Python][3] and [Django][4] behind mod_python on Apache, with a MySQL database. The following Django apps and Python libraries are used:

  1. custom made blog application by myself
  2. built-in (contrib) apps: admin, comments, sitemaps, flatpages
  3. [django-tagging][5]
  4. [django-xmlrpc][6]
  5. [comment_utils][7] for advanced comment moderation features
  6. [template_utils][8]
  7. [django-pingback][9]
  8. [Beautiful Soup][10] for XML/HTML parsing
  9. [Pygments][11] for syntax highlighting. See the [Pygments Demo!][12]
 10. [Feedparser][13]
 11. [Markdown2][14] so that I can post using Markdown.

As is typical for hobbyist software development, I started working on this site with only a minimal set of features considered, but as I kept working I kept wanting to add more stuff. Some notable custom-made features:

  1. XMLRPC server, supporting [Metaweblog API][15] and Pingbacks. I actually only added the metaweblog support so I could post from [Flock][16]
  2. Autocard support (same as [my previous Autocard plugin for WP][17]) and syntax highlighting of code.
  3. Automatic extraction of twitter and delicious entries into the sidebar
  4. [Gravatar][18] support for comments

All entries from the previous "roytang / weblog", "Roy on Magic" and "Roy on Django" have been imported using a custom data conversion script, but nothing is perfect so some of the older posts may be badly formatted. (Comment on those posts!)

**Hosting**: Provided by [Webfaction][19].

 [1]: http://blueprintcss.org "Blueprint CSS Framework"
 [2]: http://jquery.com/, "JQuery"
 [3]: http://python.org
 [4]: http://djangoproject.com
 [5]: http://code.google.com/p/django-tagging/
 [6]: https://launchpad.net/django-xmlrpc
 [7]: http://code.google.com/p/django-comment-utils/
 [8]: http://code.google.com/p/django-template-utils/
 [9]: http://code.google.com/p/django-pingback/
 [10]: http://www.crummy.com/software/BeautifulSoup/
 [11]: http://pygments.org/
 [12]: /pygments/
 [13]: http://www.feedparser.org/
 [14]: http://code.google.com/p/python-markdown2/
 [15]: http://www.xmlrpc.com/metaWeblogApi
 [16]: http://www.flock.com/
 [17]: http://roytang.net/games/2008/02/mtg-autocard-wordpress-plugin/
 [18]: http://gravatar.com
 [19]: http://www.webfaction.com/?affiliate=roytang