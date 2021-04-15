---
title: "Google Chrome and FloC"
date: 2021-04-15T21:30:52+08:00
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/106069611626842206
- type: twitter
  url: https://twitter.com/roytang/statuses/1382689456294129673/
tags:
- tech-life
title: Chrome Floc
---

Google Chrome is adding a new feature that lets their browser target you with ads without using third-party browser cookies. 

Here's some more info: [How to fight back against Google FLoC](https://plausible.io/blog/google-floc).

But basically it comes down to: if you're a web user who doesn't want your browsing history to be used to target you with advertisments, stop using Google Chrome. There are many alternatives. I'm a [Firefox](https://www.mozilla.org/en-US/firefox/new/) boy myself.

For site owners, you can add a `Permissions-Policy: interest-cohort=()` response header to opt-out of your site being included in the data collected about your Chrome visitors. I've updated this site to add the header.