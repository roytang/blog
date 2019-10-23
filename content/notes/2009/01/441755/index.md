---
date: 2009-01-14 02:51:43
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/441755/regular-expression-to-remove-hostname-and-port-from-url
tags:
- javascript
- regex
- questions
- stackoverflow
- software development
title: Regular expression to remove hostname and port from URL?
---

I need to write some javascript to strip the hostname:port part from a url, meaning I want to extract the path part only.

i.e. I want to write a function getPath(url) such that getPath("http://host:8081/path/to/something") returns "/path/to/something"

Can this be done using regular expressions?