---
categories: []
date: 2009-10-03 18:18:03
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/4583662941/
- type: facebook
  url: https://www.facebook.com/stephen.roy.tang/posts/145676038802
- type: twitter
  url: https://twitter.com/roytang/statuses/4584613727/
- type: facebook
  url: https://www.facebook.com/stephen.roy.tang/posts/276398035060
tags:
- Software Development
title: 'Weekend Project #1: MTG Utils Decklist Sharing Tool'
type: post
url: /2009/10/weekend-project-1-mtg-utils-decklist-sharing-tool/
---

I've been meaning to write a nontrivial app using [Google App Engin][1]e for a while, and here's my first weekend project: [Decklist Sharing Tool][2], an tool for MTG players to share decklists online. 

I had the decklist parsing and autocarding code available for a while (and used on my MTG related posts), so that part was fairly easy, I got it done under 3 hours I think. The rest of the time (around 5-ish hours) was spent on glue logic, fixing minor bugs, working on HTML layout, cleaning up text, etc. It feels pretty good for a one manday effort, let's see if it breaks down. Not the best code I've ever written though (until the latest upload the main class was named "hello.py")

Some notes:
  
- the Django template engine included with GAE seems to be earlier than version 1, as the escapejs filter wasn't available and I had to write it myself. Still, being familiar with the Django template engine helped a lot
- WordPress.com blogs don't allow Javascript inside the posts, so the blog sharing code I provide won't work there. It works on Blogger though. I'll look for a workaround... (iframes?)
- I've yet to try using memcache, so the current version doesn't cache anything, I mean to try it in a future version
- yes, I put adsense ads there. I was like, why not? 😀

### Social Media Archive

<time id="4583662941">[01:50]</time> thinks it's BS that there's no way to delete applications or change the app id on Google App Engine

---

<time id="4584613727">[02:36]</time> the weekend project took longer that I thought (the usual story of software estimation). now to sleep

---

### Update May 2020

The app used to be deployed on Google App Engine, but is no longer available. I've since uploaded the code to Github at https://github.com/roytang/mtg-utils

 [1]: http://appengine.google.com/
 [2]: http://mtg-utils.appspot.com/deck/

