---
date: 2018-02-01 07:11:13
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/48557175/django-syndication-framework-prevent-appending-site-id-to-the-links
tags:
- django
- django-syndication
- questions
- stackoverflow
- software development
title: 'Django syndication framework: prevent appending SITE_ID to the links'
---

According to the documentation here: https://djangobook.com/syndication-feed-framework/

> If link doesn’t return the domain, the syndication framework will
> insert the domain of the current site, according to your SITE_ID
> setting

However, I'm trying to generate a feed of magnet: links. The framework doesn't recognize this and attempts to append the SITE_ID, such that the links end up like this (on localhost):

    <link>http://localhost:8000magnet:?xt=...</link>

Is there a way to bypass this?