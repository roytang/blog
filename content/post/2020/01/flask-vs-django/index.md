---
title: "Flask vs Django"
date: 2020-01-24
tags:
- software development
- python
- flask
- django
featuredResource:
  filename: code.png
---

In a bid to reduce the number of webapps actually running on my server (for resource consumption reasons), I decided to migrate a small Flask app I had and merge into this larger Django app where I have a lot of my personal data tracking stuff. The Flask app was small enough, mostly containing backend support for this blog (like search and comment submissions) and some Twitter things. The migration was straightforward, taking around half a day, most of that was wrangling with Twitter API rate limits.

It got me thinking, why did I build this using Flask in the first place? And that led to the more general question: when do I prefer using Flask over Django?

Personal experience: I'm much more familiar with Django than Flask, having started using it back in 2008. Professionally, I've also worked on more Django projects, compared to only one Flask project that actually made it to production.

The usual quick comparison is that Flask is the more lightweight web framework, suitable to smaller apps like microservices perhaps; while Django is the big monolithic web framework with all the bells and whistles already available. In practice this means Django already provides a lot of functionalities out of the box, while with Flask you have to install and figure out extensions for even the most common tasks like database management. A negative for Flask, but partly due to my inexperience: if you were already well-versed in the use of those extensions, I imagine getting everything together and setting them up will be easier.

If there is need for a traditional RDBMS, I will probably use Django. I'm not super familiar with SQLAlchemy, the usual recommended ORM for Flask, so that's a big factor. That being said, if I needed to work with something like a NoSQL database or some other nontraditional backend, it might be better to consider Flask since Django isn't super flexible in that record - most of the pluses are oriented towards RDBMS-backed models.

Admin: The built-in Django admin is a big plus for me; it means that for things like simple record CRUD, if usability and presentation isn't a big concern, I can just use the Django admin as my backend without needing to write maintenance screens. There is an equivalent [Flask Admin plugin](https://flask-admin.readthedocs.io/en/latest/), but I've not tried that either.

API building: I'm already familiar with the Django REST framework, I'm not sure if there's an equivalent for Flask. The one Flask project we did, we rolled our own API backend.

I find that I tend to favor Flask when building quick proof-of-concept apps that don't need a database. An example that was part of the app I migrated recently would be this quick [Twitter app I wrote about a year ago](https://apps.roytang.net/twitter/), to find intersections between follows/followers. It didn't need a database, only twitter API calls. (I have since merged it into the Django app, so the current version is using Django now.)

In general I prefer Django, but that is probably due to familiarity and experience. I would love to have a full-scale project that uses Flask though! Perhaps in the future, for now all my personal projects are running on Django.