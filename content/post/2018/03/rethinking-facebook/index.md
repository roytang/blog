---
author: roy
categories: []
date: 2018-03-29 01:00:11
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/172361367865/rethinking-facebook
- type: twitter
  url: https://twitter.com/roytang/statuses/979177921981140994/
tags:
- Tech Life
title: Rethinking Facebook
type: post
url: /2018/03/rethinking-facebook/
---

There's been a recent brouhaha lately over Facebook's data privacy issues after the Cambridge Analytica scandal came out. For a while, a #DeleteFacebook hashtag even made the rounds. I will admit that I had been considering reducing my own Facebook usage for a while, but not because of any data privacy issues.

While I understand that Facebook probably mishandled private data and that this is a serious concern for a lot of people and even for society at large. It's just that it's not that much of an issue for me personally because of reasons:

  * **I fully understand what data I'm giving up to Facebook.** And I consent to their gathering that data. I even use that own data for my own purposes every so often. I like having access to a history of my online interaction with other people. It allows me an additional channel to look back into my own past and learn from it.
  * **I'm careful about what permissions I give to apps**. Supposedly the source of the Cambridge Analytica data was a personality quiz app. While I do take the occasional personality quiz, I wouldn't authorize one that was asking for any authorizations beyond the basic demographic information. I also don't seem to be affected by the logging of Android calls and texts, most probably because I didn't opt-in to something silly or manage to opt-out. I also regularly purge my Facebook app list of apps I no longer use. _(I understand that the CA situation was because FB allowed users to authorize access to their friends' data, so I would have been vulnerable to this too even if I was careful.)_
  * As a developer, **I've studied the Facebook API myself**, and I know it's limitations. In its current form, it's way more limited than it used to be. The Cambridge Analytica leak, where users who took the personality quiz leaked their friends' info without consent, is basically impossible now because the current version of the Graph API won't give access to a user's info unless that user has also authorized the same app. (This used to be not true, which is probably why the leak happened in the first place.)
  * I appreciate the **idea of gathering large social data sets** to study trends and patterns, so I do not necessarily consider the mass collection of user data an automatic bad. It can be useful if the data is handled and used properly. I will admit that I had considered gathering data via Facebook myself, for some research purposes, but the above-mentioned limitations of the GraphAPI made it very difficult. I also don't necessarily think it's bad that advertisers are given more power to target certain market segments according to the data gathered. This is an efficiency improvement, i.e. it can bring users more relevant ads. The problem is when the data is misused for nefarious purposes such as propaganda or misinformation.

There are however, other reasons that I have considered quitting Facebook (or at least reducing my usage) Foremost of which is it's a **big time-waster**. This is of course, true of the internet in general. But because I use Facebook to stay in touch mainly with family and friends whose interests don't always intersect with mine, the ratio of interesting to not-relevant-to-me content on my Facebook feeds is much worse than compared to say, Twitter or Reddit where I freely choose to follow only those sources that are relevant to my interests. Hence, my Facebook time has significantly more scrolling past irrelevant content comparatively. I try to mitigate this by ruthlessly unfollowing any Facebook friends whose content historically I have not found very interesting. (If you are one of those people and you actually find out and you read this far into this post, don't take it personally, we're still friends). Secondary reason would be I'm not a fan of the way the News Feed is handled right now. Stupid algorithmic sorting, and too many ads. (I've recently tried reporting every single ad in my feed as offensive, just to see what happens. I have yet to find any meaningful difference.) I'm also not a fan of Facebook's moderation policies, or their tendency to try to turn the internet into a monolithic walled garden (Facebook is the AOL of our times). And of course, there has been the recent trend of Facebook being used for propaganda and misinformation.

Even with all the problems above, it would still be difficult for a lot of people to give up on Facebook. The main problem is the network effect. I mean, most of my family and friends are on there! **My parents are on there, and all their friends**. That means I occasionally have to help them with their Facebook accounts and post grandkid pictures for them, and they will ask me to use it to communicate with other relatives and organize family reunions so on. I also rely on Facebook for information on upcoming events such as [Magic tournaments][1] or [quiz nights][2]. This is another network effect thing; if the organizers of these events made their information publicly available anywhere other than Facebook, it would reduce Facebook's power. But it's a chicken-and-egg thing: most people are on Facebook, so it's easier to just post your events there.

In the meantime, I have tried reducing my Facebook footprint overall. I no longer have the app installed on my devices (I still have Messenger. Messenger is useful). Firefox also recently released an [extension to help reduce Facebook's online tracking of your behavior][3], which was nice of them. I've also set it up so that my microblogging will be primarily from [Twitter][4]. (Twitter of course has its own problems as a platform but at least they're not a monolithic juggernaut.)

I think the main problem is Facebook being this giant monolithic platform that handles multiple things -- microblogging, networking, events, groups, photo sharing, etc. Having all of these functionalities all under the same platform makes it incredibly convenient for users, but it also gives the platform incredible power that can be easy to misuse.

If it were up to me, I would prefer having a set of **open protocols** that would allow multiple separate smaller services to exist and communicate with each other while being **decentralized**. Imagine if you had Service A for networking, Service B for microblogging, Service C for photo sharing, etc, all tied together by an open identity protocol. One would be able to "add as friend" or "follow" people from other networks. Each network would store its data separately, and would only make accessible whatever data the user has authorized for sharing. Imagine that Facebook users could choose to follow Twitter users on Facebook and see their Tweets appearing in your Facebook feed, but Facebook wouldn't have any data on the Twitter users' browsing habits etc, only the shared tweets. Ideally, if I didn't want to trust any platform with my data I should be able to deploy my own social media instance/node on my own personal hosting and still be able to interact with other users in the same way.

The concept of smaller services held together by open protocols is closer to what I imagine an idealized internet should be. There are open source decentralized social media platforms being developed such as Diaspora or Mastodon, but I haven't studied them enough to know if they are being built to work in this direction. I don't know if this misstep is something that starts the fall of Facebook, but hopefully the current problems would be enough to nudge the internet in a better direction, away from the large monolithic platforms capitalism seems to be urging us towards.

&nbsp;

 [1]: https://roytang.net/category/magic/
 [2]: https://roytang.net/2013/03/scenes-from-a-quiz-night/
 [3]: https://www.theverge.com/2018/3/27/17167094/mozilla-firefox-facebook-container-tracker-blocker?utm_campaign=theverge&utm_content=chorus&utm_medium=social&utm_source=twitter
 [4]: https://twitter.com/roytang/