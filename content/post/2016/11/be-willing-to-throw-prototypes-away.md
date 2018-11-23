---
author: roy
categories:
- Software Development
date: 2016-11-10 01:30:09
title: Be Willing To Throw Prototypes Away
type: post
url: /2016/11/be-willing-to-throw-prototypes-away/
---

&nbsp;

There was this project we had where there was a strange bug. The developer working on it found that the problem only appears when the record ID was 12. When it was 11 or less, everything was fine. When it was 13 or more, everything was also fine. After some investigation, it was found that there was some code that executed with a condition of "if record id == 12", which was already a WTF. It turns out that some behavior had been hardcoded for a previous demo to a client and was never reverted and made it all the way into acceptance testing builds.

Prototyping and demo builds are great tools and all, but I've observed a dangerous tendency for upper management to afterwards say "we already have the code right? So we just deploy it", or something to that effect. The urge to save on development costs is understandable, but the developers who built the prototype have a responsibility to raise any risks due to poor code or hacks or workarounds or some sort of hardcoded shenanigans to make sure they are properly addressed before the code gets deployed anywhere serious. Many of these shenanigans tend to be found in prototypes or demo codes that were developed in a short timeframe to hit a particular demo date.

Above all, the team should be more than willing to decide if there is no way the demo codebase is good enough to be rolled out to an actual client and be willing to say no to such requests if needed.

_(Demoing functionality you don't really have yet is a separate matter entirely, one I don't approve of naturally)_