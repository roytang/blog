---
date: 2024-06-11 05:32:44
dontinlinephotos: true
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/112596981748729324
tags:
- tech
title: Google Timeline and Microsoft Recall
---

### Google Timeline

I found out recently that [Google Timeline](https://timeline.google.com)/Location History is scheduled to be removed from the web, WTH! This is because they are migrating to on-device location data storage: [(AndroidPolice) Google Maps Timeline now stores your location data on-device](https://www.androidpolice.com/google-maps-timeline-location-data-on-device-migration/). The web timeline won't have any more data to access because your location history will be stored on your phone instead.

{{% photos timeline-alert %}}

Now, I understand this is actually an improvement in terms of security and privacy - it means Google won't be storing your location data on their servers after all. But it's super annoying for me because I use Google Timeline a lot, and 99% of the time via the web. I am often revisiting the past, and timeline helps me answer questions like "Where was I when this picture was taken?", "Did we attend this event?", and so on. Location History is like foursquare check-ins that automatically happen and that only I can see. I understand this change means everything will still be available on mobile, but I vastly prefer using the web version. Plus, the date filters on the web timeline are so much better than the annoying ones on the mobile app ugh.

I have already made a backup of my timeline data via Google Takeout (and have set a reminder to do so again before the deadline on Dec 7), and maybe I can do something with that data myself to make it easier for me to search than having to use my phone. And I am hoping that the location history data stored on-device will still have a way to export it!

### Microsoft Recall

Only tangentially related: Microsoft recently announced a new Windows 11 feature called Recall which is basically a usage history of your computer, complete with screenshots every 5 seconds that will capture all of your most sensitive data (except of course anything protected by DRM, because God forbid Disney's copyrights are violated!) and use OCR and LLMs to anaylze the data so you can query it later.

People are rightly furious with the idea: [(Windows Central) A PR disaster: Microsoft has lost trust with its users, and Windows Recall is the straw that broke the camel's back](https://www.windowscentral.com/software-apps/windows-11/microsoft-has-lost-trust-with-its-users-windows-recall-is-the-last-straw). The initial implementation (preview already available) has a ton of security issues, including just storing most of the data in a plaintext SQL database. Even before any official release, people are already finding exploits based on the preview version and even being able to access remotely. The feature is supposedly only available for "Copilot PCs" with specialized hardware, but people have been able to enable it for normal PCs. This [thread by @GossiTheDog@cyberspace.social](https://cyberplace.social/@GossiTheDog/112509779763217312) does a good job covering the problems and the general negative reaction to the whole thing. 

This whole thing feels to me like another instance of AI hype leading to a solution in search of a problem. And like some higher-ups needed some sort of killer app for their "Co-pilot PCs" to be relevant. It definitely does not seem to be a feature that the majority of Windows users would want. Certainly any kind of security-conscious corporate or finance IT guy would NOT want this sort of thing running on their employees' computers!

I think the main issue here isn't the functionality specifically, but that they wanted to include it as a default feature of Windows and was initially opt-out. It feels like a huge forced error - if they had announced the feature as a separate software that people could install if they wanted, something like a [PowerToy](https://github.com/microsoft/PowerToys), there wouldn't have been this whole brouhaha. But having it be available by default magnifies the security concerns because any time you connect to or access a Windows PC you would be able to assume Recall is installed and may be able to use exploits to access it. And many people may end up having it enabled by default with no idea what Recall even is.

After the backlash, Microsoft responded: [(The Verge) Windows won’t take screenshots of everything you do after all — unless you opt in](https://www.theverge.com/2024/6/7/24173499/microsoft-windows-recall-response-security-concerns). The big changes are making Recall opt-in, encrypting the locally stored data, and requiring additional authentication before you access. These are good changes, but they don't mitigate the biggest problem that Recall would still available by default on Windows 11, even if not enabled. Even if the security implementation is perfect today (and it likely isn't), there's no telling what may happen down the line; new exploits may emerge that make it possible to enable recall remotely and silently and access the data and so on. Plus, people don't even trust Microsoft enough to believe that the data stored by Recall will remain permanently on-device; even if that is the policy now, nothing stops them from changing that in the future. And even if you don't have Recall enabled on your PC, what happens when you're sharing information with someone else who DOES have it enabled? It's a very sticky situation.

The only real way to 100% mitigate the problems would be to make installing Recall at all optional, so that it's not widely available enough to be a major security concern. But then again, that would probably hurt someone's KPIs or something.

As someone who does a lot of my own tracking of my own activities, Recall is actually the sort of feature I might have been tempted to check out. I suspect that the specific implementation - OCR data extracted from screenshots every few seconds would not have been very useful to me particularly, because that is probably not a level of granularity I would find useful. I do think a local-only search engine over a more limited subset of data - for example my browser history (including page summaries) - might be useful, but again, probably better if that wasn't an OS-level thing. I think I would at the very least try it out, but I am very aware however that I am a power user, and probably 99% of Windows users won't need or want this sort of feature.