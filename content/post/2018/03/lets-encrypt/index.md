---
author: roy
categories: []
date: 2018-03-01 01:00:07
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/171398937145/lets-encrypt
- type: twitter
  url: https://twitter.com/roytang/statuses/969018906449973248/
tags:
- Learning Things
- Self-Improvement
- Meta
- Tech Life
title: Let's Encrypt!
type: post
url: /2018/03/lets-encrypt/
---

<figure style="width: 559px" class="wp-caption alignnone"><img src="https://i.redd.it/hfd9ok7bstf01.png" alt="" width="559" height="235" /><figcaption class="wp-caption-text">(Image credit: r/ProgrammerHumor)</figcaption></figure> 

I've been meaning to add SSL to this blog ever since I first heard of [Let's Encrypt][2] last year. Unfortunately, support on my otherwise awesome webhost was not yet first-class and seemed complicated at the time, so I kept putting it off. But recently I was testing something unrelated and found out that I [needed to have SSL on my server in order for OAuth2 to work][3], so I grudgingly got to it.

Luckily I found out about a handy utility written in Ruby that does most of the stuff for me: [letsencrypt-webfaction][4]. It was surprisingly easy to setup, with only a [single false start because I had a silly typo][5].

So now this site has SSL! Hooray!

 [1]: https://www.reddit.com/r/ProgrammerHumor/comments/7x2ugb/lets_encrypt/
 [2]: https://letsencrypt.org/
 [3]: https://github.com/requests/requests-oauthlib/issues/287
 [4]: https://github.com/will-in-wi/letsencrypt-webfaction
 [5]: https://github.com/will-in-wi/letsencrypt-webfaction/issues/116#issuecomment-368930373