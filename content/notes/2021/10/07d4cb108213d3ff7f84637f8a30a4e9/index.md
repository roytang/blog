---
date: 2021-10-26 17:04:14.808036
source: form
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/107168914187690558
- type: twitter
  url: https://twitter.com/roytang/status/1453044820490940416/
- type: twitter
  url: https://twitter.com/roytang/status/1453051021458952196/
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/107169012963987063
tags:
- software-development
title: ''
---

Just spent an hour trying to figure out why my Django webapp suddenly wasn't working because apparently if you accidentally delete an `__init__.py` you're gonna have a bad time.

<time>[01:28]</time> It took me a while because the issue only happened on the live server and not on local. Django only complained when it was run via WSGI and nothing was showing up in the logs.
