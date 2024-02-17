---
date: 2024-02-17 00:45:09
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/111944638533567261
tags:
- tech
- fediverse
title: Fediverse Bridge, Bluesky, and Importing Comments
---

There was a bit of a brouhaha earlier this week on the Fediverse because someone wanted to build a bridge between the ActivityPub-powered fediverse and the AT protocol-powered one, i.e. BlueSky. Apparently a lot of people want nothing to do with BlueSky and many are angry that the bridge developer initially planned an "opt-out" approach. The bridge developer is [Ryan Barrett](https://snarfed.org/), developer of [brid.gy](https://brid.gy/), which I have used before.

I don't want to go over the details myself. TechCrunch had [an article covering the whole affair](https://techcrunch.com/2024/02/14/bluesky-and-mastodon-users-are-having-a-fight-that-could-shape-the-next-generation-of-social-media/), it's a decent summary, although the title feels a bit sensationalized. 

Two things I want to note are: 

1. Sadness at the way the bridge developer was treated and dogpiled on by many people objecting to the opt-in. It's one thing to object to the methods and another thing completely to come out swearing at the guy for doing something a lot of people would have found of interest (me included). There was also a lot of misinformation like people claiming the bridge would hoover up all of everybody's posts and send them to BlueSky (that's not how bridges work, it's not a scraper!) The dev has handled the abuse and feedback extremely well and is switching to an opt-in approach, and the furor kind of died down after that.
2. While reading through a lot of the discussions about this, I noted a lot of objections boiled down to issues of informed consent as to how their data is handled. 

---

The second point is the one I want to discuss more. I won't pretend to be an expert on informed consent as it applies to posts on the internet, but one thing that surprised me is users objecting to the idea that the BlueSky bridge could be treated as anything other than just another federation server. I've seen people argue that they only consented to their posts being distributed within the "Mastodon fediverse", and not to other platforms like BlueSky.

I had to think about this because my own website right here is "another platform" currently takes in any replies to my posts and archives them here as comments, effectively using Mastodon as a comment section. I have a warning about this on [my Mastodon profile](https://indieweb.social/@roytang):

> Fair warning: All my toots are automatically archived to my blog/website (link in profile). If you reply to my toots, your content may automatically be exported and archived on my site as comments.
>

So this got me thinking: is this a violation of informed consent? While I do have the warning above, it's certainly feasible that people reply to my posts without ever seeing that warning on my profile. In my head this was a non-issue because if a message was sent to me and only publicly-accessible mentions are imported, there shouldn't be an issue with me archiving them here on my site. Does that make sense?

Historically, I've been importing comments from external networks for a long time. When this site still ran under Wordpress I had a social plugin that imported comments from Facebook/Twitter, and later even as a static site I used the web version of brid.gy to import comments from Twitter and Mastodon. 

Another thing I noted is that many people were asking if the bridge would respect Mastodon actions like blocks and deletes (the dev said yes), and this got me thinking about my own site's behavior again. The Mastodon replies I import are a one-time import; if I am later blocked by that user (I do not believe this has happened yet!) or the post is later deleted (or edited), the imported post remains as it originally was on my website. 

Is this an issue? If it is, then that implies any sort of archival is an issue. Do things like the internet archive snapshots or screenshots of now-deleted posts violate informed consent? After all, these things can happen without the original poster being aware, as long as the content is publicly-accessible on the web.

Since the early days of the web, I have always had the mentality that anything I post publicly online is potentially public forever and I have always been fine with that. So in my head, posting publicly is already active consent for your content to be distributed, viewed, shared, etc.

I am not sure what the answers are to these questions, but I acknowledge that the online culture and landscape can be complicated. I understand that there may be possible harms that I can't even imagine because I don't have that lived experience. Moderation and other handling of abuse is tricky, and I am glad I do not have to face those problems at scale. 

I am keeping my site's behavior as-is for now, but this issue has definitely given me some things to think about moving forward, as I work towards reorganizing the website. (Although if you have a comment imported to my site and would rather not have it there, feel free to ask me to remove it.)

---

As for the BlueSky bridge, I'm all for it and hope it is successful and manages these issues. While I have little interest in using BlueSky myself, it would be nice to be able to have the ability to follow people on there from my Mastodon account. 

There was a similar brouhaha before when Threads started to federate and a lot of people (understandably) did not want to have anything to do with it; many servers ended up just domain-blocking Threads.

One of the reasons I like being on Mastodon is not just the decentralized bit, but also the fact that it's an open platform with an openly-accessible API that encourages interop. In the heyday of closed networks like Facebook and Twitter, having this kind of interop across platforms would have been fantastic, so any effort that improves interop is welcome in my book.

---

### Notes and Links of Interest

1. [Statement of support for the BlueSky bridge from Tim Chambers](https://www.timothychambers.net/2024/02/13/indiewebsocial-and-the.html), admin of my Mastodon instance indieweb.social.
2. A [thread by @hrefna@hachyderm.io](https://hachyderm.io/@hrefna/111931620167055570) discussing the nature of Mastodon as opt-out
3. Many of the objections to the bridge seemed to come from people who had misunderstandings of how federation works, so I liked this post where [jupiter_rowland explains how the bridge would (likely) work](https://hub.netzgemeinde.eu/channel/jupiter_rowland?mid=b64.aHR0cHM6Ly9odWIubmV0emdlbWVpbmRlLmV1L2l0ZW0vYjk3NTRkNzAtMTRmNi00MDYxLTliOTAtOWM4ODc4NzY1MjNm), including what data would be sent to BlueSky and when. The explainer itself is long and detailed and of interest, but aside from that, I found the entire thread interesting mostly because I learned a lot about the wider fediverse outside of Mastodon. The post itself is on Hubzilla and you can follow the account on Mastodon because Hubzilla has an ActivityPub bridge! There are some comments in there arguing that Hubzilla and similar platforms would be excluded if people didn't like bridges.
4. [Tantek on the ephemeral web](https://tantek.com/2024/046/t1/the-ephemeral-web), re: discussions about technical and cultural differences between the persistent web and platforms like Mastodon; not directly related to the bridgy issue, but arising from similar discussions.
5. A lot of Mastodon users make a big deal about hating on BlueSky because it's Jack Dorsey's brainchild, but through reading about this topic I found out he is only a minority shareholder and has much more interest in another platform called Nostr (it's a a crypto thang). Apparently [Dorsey even got bullied off BlueSky](https://www.reddit.com/r/BlueskySocial/comments/16jbbzr/jack_has_quit_bluesky/) lol