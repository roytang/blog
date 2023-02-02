---
date: 2023-02-02 16:16:49
syndicated:
- type: triviastorm
  url: https://triviastorm.net/blog/post/mastodon-migration/
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/109796073285176346
- type: twitter
  url: https://twitter.com/roytang/status/1621183002364747777/
tags:
- triviastorm
- projects
title: Triviastorm TriviaBot is now on Mastodon
---

*(Cross-posted from [the TriviaStorm blog](https://triviastorm.net/blog/post/mastodon-migration/))*

### Shutting Down The Twitter Bot

Sad news today, as Twitter [has announced that API access will no longer be free startong on Feb 9, 2023](https://twitter.com/TwitterDev/status/1621026986784337922). Sadly this means the end of the bot's run on Twitter which started in Feb 2017. Almost 5 years! It was fun while it lasted. The Twitter bot will run until it can't.

### Migrating to Mastodon

That was the bad news. The good news is that a version of the trivia bot is already up and running on the fediverse/Mastodon networks. You can follow the bot at https://botsin.space/@triviastorm. It follows the same rules and uses the same question set: a new question is asked every hour, and the bot will collect and score correct responses after an hour. Additionally, the bot supports hiding your responses behind Mastodon's spoiler/content warning feature!

### New Feature: Reporting

Unfortunately, the question pool still includes a lot of old questions from quizzes and such that were never encoded properly for use in a trivia bot, so some questions may still have some issues. Back on Twitter you could complain to the bot directly and I would just check the bot's notifications every so often, and as needed I would correct questions and re-check questions. This was a very human process which meant some complaints would fall by the wayside or be forgotten.

For the Mastodon migration, I've added a new feature where you can reply to the bot with a certain format to report problems with a question. This sends the reports directly to me via an RSS feed that I follow, hopefully making it easier for me to see reports. The Mastodon triviabot includes in it's summary posts the instructions for reporting a question: `"If you think there was a problem with this question, please reply to this post with "!report <details>", thanks!"`

*(I had already done the work to update the Twitter bot to include this feature as well, but with the impending API shutdown, it no longer seems necessary.)*

### Blog Update

This is only the second post on this blog, and I'm still playing around with the theme. What do you think? (I am keeping those old-timey Share buttons at the bottom of each post for now.)

### Support Us

If you enjoy the use of the trivia bot(s), consider [leaving me a tip](https://ko-fi.com/roytang)!

### Happy Quizzing!