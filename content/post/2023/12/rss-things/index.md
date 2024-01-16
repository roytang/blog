---
title: "Things with RSS Feeds you might not have known about"
date: 2024-01-16T20:53:04+08:00
tags:
- tech
- web
- rss
dontinlinephotos: true
---

RSS/Atom feeds are typically used for subscribing to blogs and podcasts, but in theory, any site that publishes items regularly can have them. Here are some you might not have known about:

### Youtube channels

Handy if you're tired of Youtube itself never showing you new videos from channels you're actually subscribed to. The RSS feed URL for each channel is something like `https://www.youtube.com/feeds/videos.xml?channel_id=<the channel id>` but getting the channel id may not be straightforward. The feed URL is not shown prominently anywhere, but most RSS readers will support just pasting in the channel url like `https://www.youtube.com/@roytang` and it will find the feed automatically.

Example feed URLs:

- My channel [@roytang](https://www.youtube.com/feeds/videos.xml?channel_id=UCwpuHIsvCAdmcZ4hIS3tQHA)
- Trivia team [@teamcamoteph](https://www.youtube.com/feeds/videos.xml?channel_id=UCptXvNbp4ETVttb_k-1oOww)

### Git repositories

This isn't a standard or anything, but some of the more popular Git repository providers have RSS feeds that show new commits, handy if you're monitoring certain public repos I guess?

Github: You can follow the commits for a branch via a feed URL like `https://github.com/<namespace>/<repo name>/commits/<branch name>.atom`

Gitlab: The feed URL is in the format `https://gitlab.com/<namespace>/<repository name>.atom`. I'm not sure if there are different URLs for different branches.

### Google Alerts

Google search is [much less useful these days](https://danluu.com/seo-spam/), but you might still get some mileage out of this one. When you set up a new Google alert, you can set "Deliver to" to "RSS feed" and it will give you a feed URL you can add to your feed reader. I only use this for some vanity searches (i.e. alerts set up for my name or companies I work for), which isn't especially useful because a bunch of other people have my name (and my website isn't indexed by Google), but it's kinda fun.

{{% photos alert %}}

### Goodreads

I don't use Goodreads anymore myself (all my book reviews are [here on my site instead](/lists/media/books/)), but this can be handy if you want to follow what your friends on there are reading without using the site yourself. The feed URL is something like `https://www.goodreads.com/review/list_rss/<user id>`, but again you can just plug the Goodreads user profile into your feed reader and it should find the URL automatically. My Goodreads RSS feed is [here](https://www.goodreads.com/review/list_rss/18436248) (last entry is from 2018!)

### StackOverflow (and other StackExchange sites)

I am not sure how much these sites will stay relevant in the face of the current AI apocalypse (and it's meme status as being hostile to newbies), but the StackExchange network of Q&A sites support [a bunch of feeds](https://meta.stackexchange.com/questions/151519/what-other-hidden-or-inobvious-rss-feeds-are-available-on-stack-exchange-and-its). 

I would guess the more useful ones are:

- Feed for responses to a user's questions: `https://<site name>/feeds/user/<user id>/responses`. You can follow your own feed so that you know when someone replies to your questions. Mine is [here](https://stackoverflow.com/feeds/user/18494/responses)
- Feeds for questions in a specific tag: `https://<site name>/feeds/tag/<tag>`. You can follow this if you like answering questions under this topic.

### ShowRSS

[ShowRSS](https://showrss.info/) is a site that generates RSS feeds of new TV show releases. It's chief purpose is probably illegal where you are, because the RSS feeds include torrent links, but you can also just use it as a notifier of when new episodes of a show come out. You need to sign up to create your custom feed.

### Mastodon

Well, this one might be well-known to people who are already on Mastodon, but you can get an RSS feed for any Mastodon profile using a URL like `https://<instance name>/@<user id>.rss`. Mine is [here](https://indieweb.social/@roytang.rss). I suspect most other Fediverse platforms have similar features.

### Others

I'm sure there are many other uses of RSS I'm not aware of, these are just samples of what I had in my own feed reader. RSS is a great format for decentralization, even better than ActivityPub and it can be used to easily facilitate interop - generating RSS feeds is super easy and there are standard libraries to do it for most programming languages.