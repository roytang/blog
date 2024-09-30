---
date: 2009-12-23 08:20:52
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1951373/automated-regression-tests-for-java-applets
tags:
- applet
- automated-tests
- questions
- stackoverflow
- software development
title: Automated regression tests for java applets?
---

We're working on a project with a number of applets that has to work across a large range of OS (WIndows, Mac, Linux), browsers (IE, FF, Safari, etc) and Java versions (1.5+), and it often happens that a fix we apply will cause some sort of security exception an another platform or some other error.

Is there any way for us to prepare automated tests to immediately catch those problems in different platforms? I think it's not necessary to check that the gui parts are appearing as intended, but just to detect whether unexpected exceptions are occuring.