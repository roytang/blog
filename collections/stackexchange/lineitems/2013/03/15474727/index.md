---
date: 2013-03-18 10:35:55
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/15474727/jquery-listing-out-ready-handlers
tags:
- javascript
- jquery
- questions
- stackoverflow
- software development
title: 'jquery: listing out ready handlers'
---

I'm trying to trace a slowdown on load of a web page in our application and there's a ton of JavaScript to go through so I'd rather not process them individually.

I'm trying to see if there's a way to list out all the event handlers added to `$(document).ready()` so that I would just look through those handlers to see what might be causing the problem.

Is there a way to do this?