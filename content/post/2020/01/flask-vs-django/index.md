---
title: "Flask vs Django"
date: 2020-01-24
draft: true
tags:
- software development
- python
- flask
- django
---

In a bid to reduce the number of webapps actually running on my server (for resource consumption reasons), I decided to migrate a small Flask app I had and merge into this larger Django app where I have a lot of my personal data tracking stuff. It got me thinking, why did I build this using Flask in the first place? And that led to the more general question: when do I prefer using Flask over Django?

Personal experience: I'm much more familiar with Django than Flask, having started using it back in 2008. Professionally, I've also worked on more Django projects, compared to only one Flask project that actually made it to production.

The usual quick comparison is that Flask is the more lightweight web framework, suitable to smaller apps like microservices perhaps; while Django is the big monolithic web framework with all the bells and whistles already available. In practice this means Django already provides a lot of functionalities out of the box, while with Flask you have to install and figure out extensions for even the most common tasks like database management. A negative for Flask, but partly due to my inexperience: if you were already well-versed in the use of those extensions, I imagine getting everything together and setting them up will be easier.



