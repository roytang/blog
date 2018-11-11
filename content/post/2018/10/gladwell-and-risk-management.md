---
author: roy
categories:
- Software Development
date: 2018-10-25 13:00:02
tags:
- risk-management
title: Gladwell and Risk Management
type: post
url: /2018/10/gladwell-and-risk-management/
---

Malcolm Gladwell, in [an article from 1996 discussing the Challenger disaster][1], tells us:

> This kind of disaster is what the Yale University sociologist Charles Perrow has famously called a "normal accident." By "normal" Perrow does not mean that it is frequent; he means that it is the kind of accident one can expect in the normal functioning of a technologically complex operation. Modern systems, Perrow argues, are made up of thousands of parts, all of which interrelate in ways that are impossible to anticipate. Given that complexity, he says, it is almost inevitable that some combinations of minor failures will eventually amount to something catastrophic.

The description of &#8220;modern systems&#8221; above reminds me most of modern software systems. And it is true that modern software systems are made of thousands of &#8220;parts&#8221;, and the way they all interrelate with each other can be impossible to anticipate. This is why software defects are inevitable, especially as system size grows. Once a software system is large enough, there will be no single developer who can see all the details of every operation the software does. While we try to maximize testing scope, we cannot possibly handle every possible combination of thousands of inputs, and we limit ourselves to the most likely cases. This is considered an acceptable risk of software development.

While your critical software bug is not likely to cost millions of dollars to clean up, a lot of what Gladwell discusses in the article can still be applicable to software development.

If software systems can be compared to normal accidents, what else does Gladwell's article say about such accidents that might be applicable to software systems? Later on Gladwell tells us about _risk homeostasis:_

> There is another way to look at this problem, and that is from the standpoint of how human beings handle risk. One of the assumptions behind the modern disaster ritual is that when a risk can be identified and eliminated a system can be made safer. The new booster joints on the shuttle, for example, are so much better than the old ones that the over-all chances of a Challenger-style accident’s ever happening again must be lower-right? This is such a straightforward idea that questioning it seems almost impossible. But that is just what another group of scholars has done, under what is called the theory of "risk homeostasis." It should be said that within the academic community there are huge debates over how widely the theory of risk homeostasis can and should be applied. But the basic idea, which has been laid out brilliantly by the Canadian psychologist Gerald Wilde in his book "Target Risk," is quite simple: under certain circumstances, changes that appear to make a system or an organization safer in fact don’t. Why? Because human beings have a seemingly fundamental tendency to compensate for lower risks in one area by taking greater risks in another.

Risk management is a big part of software development, especially as projects grow larger. We need to be careful that we are evaluating the collective risks on a project accurately and not just trading one set of risks for another.

 [1]: http://gladwell.com/blowup/