---
author: roy
date: 2019-03-25T13:56:56+08:00
type: post
categories:
- Software Development
title: "A Quick Twitter App I Wrote"
type: post
---

I wish I had a more concise way to describe it, but I really don't.

Some time ago this guy I follow on Twitter, [visakanv](https://twitter.com/visakanv/) wanted to know how to do a certain search: he wanted to know who a given famous person follows on Twitter, and among those, finds the one who follow him (visakanv), so he could network through them. I might not be explaining the concept too well, here's [the thread](https://twitter.com/visakanv/status/1087316852663939072).

Anyway, in a fit of "I'm a bit bored, anything interesting I could do?" I figured I could set up a quick webapp to do that. I did a quick PoC in Python/Flask, with [Tweepy](http://www.tweepy.org/) for accessing the Twitter API. I normally prefer Django for my webapps, but since this was just a small, quick app, I figured Flask would be ideal. That worked out fine, except that I had to use my personal access tokens to for all the API calls. This means that if many people were using the app, it was likely to hit Twitter's rate limits!

That was a few months back. A couple of days ago, someone emailed me asking about an error he encountered using the app, and sure enough it was due to the rate limits. I had a couple of free hours last weekend, so I figured I'd update the app a bit. I decided to add a Twitter login requirement, that way we can use the individual user's access token instead of using mine globally. This would allow the rate limits to be per user and thus less likely to be hit. Now, I've tried implementing OAuth login some years ago and it can be terribly complicated, but luckily I found out that there's a nifty Python package called [Flask-Dance](https://github.com/singingwolfboy/flask-dance) that made it super easy to add Twitter OAuth to a Flask app. This also let me discard the Tweepy dependency, since the Twitter OAuth session let me query the API endpoints directly. I also did a bit of UI cleanup and error handling and deployed the changes quickly.

The app is available online at [apps.roytang.net/twitter](http://apps.roytang.net/twitter). There's a few other Twitter tools I've been meaning to build, so I'll probably put them here too when I get around to them.