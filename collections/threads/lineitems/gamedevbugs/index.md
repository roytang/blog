---
date: 2018-11-24 16:39:20
source: twitter
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1066370696186449921/
tags:
- gamedev
repost_source:
  name: AeornFlippout
  type: twitter
  url: https://twitter.com/AeornFlippout/status/1066013031560294400
title: 'AeornFlippout: Bizaare gamedev bugs'
---

I'd like to tell you a little story about what it's like to actually run an indie game company. We've been working on this Limited Run release for Race The Sun for some time now. We thought we were on the home stretch around June with getting everything finished...

---

But Sony's QA found a couple bugs to fix in the Vita version. One of them was a minor thing that just took me a minute to fix. The other one was a crash. The game crashed 3 times for their testers. They weren't able to give me a lot of info - it was mostly random.

---

I assumed this would be straightforward to figure out. 

[narrator voice] it wasn't.



I tried to reproduce the crash for about 20 hours, with no luck. I made a couple speculative fixes, and re-submitted it. Same results - they even got it to crash a couple more times.

---

This time, I was able to discover a rare crash that only happened in one mode (sunrise) and only if you played and then went back to the menu and waited 5 minutes. I fixed it, and resubmitted. A week later - they were still getting crashes to happen.

---

I reached out to their QA lead, and they were very helpful. But ultimately, their team was reproducing crashes that I wasn't seeing. I hired @SyrenneMcN to do a QA pass and see if she could reproduce a crash. She did after many hours, but we weren't able to narrow down the cause.

---

At this point, I decided to write a testing script that would automatically play the game. I let it run overnight - it would run out of memory after like 24 hours, but surely that wasn't the cause if Sony's QA team was reproducing crashes regularly.

---

So I started to wonder if maybe their testing environment was different. Their (very helpful) team talked through it all with me, and we confirmed we were using the same test devices, same OS version. They were getting crashes and I wasn't.

---

Finally, after weeks of this tedium, I had an epiphany: What if their network speeds over at Sony were somehow different? I turned on the 3G network emulation on my device, and tweaked my "auto play" script, and let it run - viola! It crashed within an hour.

---

It turns out that there was what's called a "race condition" - when bugs only occur when one thing happens in a certain order relative to another thing. In this case, it was a leaderboard submission happening while fetching scores, violating some obscure rule that caused a crash.

---

I fixed this bug, resubmitted it, and after 4 submissions, finally passed certification. This was something like 4-5 weeks of work spread out over months, working on fixing a bug in a game we shipped in 2013, so we could do a physical release.

---

Anyway - all that is to say, sometimes keeping your game studio afloat requires doing really tedious, not very fun work. But also, that Vita version of Race The Sun is undoubtedly the most battle-tested version of the game to date, and I hope everyone who got a copy enjoys it :)

---

Twitter seems to be hiding @mmalex's excellent Little Big Planet story within this thread for some reason, so I'm just going to link it directly: https://twitter.com/mmalex/status/1066111290580582403

---

> I feel your pain! We had a ‘fun’ one on LittleBigPlanet 1: 2 weeks to gold, a Japanese QA tester started reliably crashing the game by leaving it on over night. We could not repro. Like you, days of confirmation of identical environment, os, hardware, etc; each attempt took /
>
> Over 24h, plus time differences, and still no repro. Eventually we realised they had an eye toy plugged in, and set to record audio (that took 2 days of iterating) still no joy. Finally we noticed the crash was always around 4am. Why? What happened only in Japan at 4am? We begged
>
> To find out. Eventually the answer came: cleaners arrived. They were more thorough than our cleaners! One hour of vacuuming near the eye toy- white noise- caused the in game chat audio compression to leak a few bytes of memory (only with white noise). Long enough? Crash.