---
title: IFTTT
author: roy
date: 2019-01-06T13:58:22+08:00
categories:
  - Tech Life
---

A free web-based service I've found very useful over the past few years is [IFTTT](https://ifttt.com). The initialism is a bit unwieldy; it stands for "If this, then that". It basically provides a way to "glue" different services and APIs together so you can set up some kind of automation. You set up rules with conditions and specify what to do when those conditions are met.

One of my main uses for it was for social media cross-posting. Some examples are:

- whenever I tweet, cross-post to Facebook`*`
- whenever I post to Instagram, cross-post to Twitter and Tumblr
- whenever I publish a new blog post, send the link to Facebook`*` and Twitter
- whenever I publish an image post on Tumblr, tweet the image
- whenever I post on Mastodon, cross-post to Twitter
- whenever I save a new link on Pocket, cross-post to Twitter

The ones marked `*` are unfortunately no longer working since Facebook changed their API to prevent automated publishing. My blog posts now cross-post to [a Facebook page](https://www.facebook.com/roytangpage/) instead. 

Additionally, since I like to archive/backup everything and track my data, IFTTT is also helpful with that. I use it to:

- save all SMS messages to a Google doc
- save tagged FB photos to Dropbox
- save my daily Fitbit activity to a spreadsheet

I'm only using a very small subset of the functionality too. There's a lot more apps and services that it can hook up to, and they always recommend new "recipes" or "applets" that you might find useful. I think many of their services might be limited to US people though, especially the ones related to smart appliances and such. I wish there were some more advanced output capabilities though. Like, I went to publish a custom API endpoint to accept output from IFTTT, so I can route inputs from different services to my own systems for tracking/archiving/analysis. But maybe that's too much to ask for a general-purpose service. Still, the fact that IFTTT exists is super helpful because otherwise I might consider writing my own APIs for the above functionality. Nowadays when I want to do some sort of service glue I first ask myself "Can I do this using IFTTT?"