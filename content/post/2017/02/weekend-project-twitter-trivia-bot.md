---
author: roy
categories: []
date: 2017-02-23 01:30:00
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/157591662160/weekend-project-twitter-trivia-bot
tags:
- projects
- python
- triviastorm
- Software Development
title: 'Weekend Project: Twitter Trivia Bot'
type: post
url: /2017/02/weekend-project-twitter-trivia-bot/
---

I had been meaning to try writing a Twitter bot for a while now.&nbsp;I figured a trivia bot would be pretty easy to implement, so I spent some time a couple of weekends to rig one together.

It's (mostly) working now, the bot is active as&nbsp;[triviastorm on Twitter][1], with a supporting webapp deployed on&nbsp;<http://trivia.roytang.net/>. The bot tweets out a trivia question once every&nbsp;hour. It will then award points to the first five people who gave the correct answer.&nbsp;The bot will only recognize answers given as a direct reply to the tweet with the question, and only those submitted within the one hour period.

Some technical details:

My scripting language of choice for the past few years has been Python 2.7. I'm using [Tweepy][2]&nbsp;to interact with the Twitter API, [PyMySQL][3]&nbsp;to connect&nbsp;to the database, and [Flask][4]&nbsp;to run the webapp.&nbsp;I haven't used Flask in some time, but it's still very straightforward. I actually had a harder time configuring the webapp&nbsp;with mod_wsgi on my host.

The main problem with a trivia system is that you need a large and high-quality set of questions.&nbsp;Right now the bot is using a small trivia set --around a thousand questions I got from a variety of sources.&nbsp;If I want to leave this bot running for a while, I'm going to need a much larger trivia set. However, reviewing and collating the questions is a nontrivial task. Hopefully I can add new questions every so often.

Feel free to follow the bot and help test it out. I'd be grateful!

 [1]: https://twitter.com/triviastorm/
 [2]: http://www.tweepy.org/
 [3]: https://github.com/PyMySQL/PyMySQL
 [4]: http://flask.pocoo.org/