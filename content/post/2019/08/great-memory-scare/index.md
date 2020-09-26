---
categories: []
date: 2019-08-22 00:00:00
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1164328992012460033/
tags:
- tech life
- gaming
title: The Great Memory Scare of 2019
type: post
---

My current desktop PC has been with me since late 2015, so going on 4 years now. I bought relatively high-end parts for it at the time, hoping to be a bit future-proof so that it would last me longer than previous desktops. So I was a bit worried when I started encountering issues during the recent weeks.

Here's the timeline:

- May 2019, before my overseas trip. It happened a few times that the computer would completely shut down while I was playing [Starcraft 2](/2019/04/starcraft-2/) coop. The displays would go black, but they still had power, and for a little while the OS would keep going. I know this because I could still hear the game sounds for a bit. Eventually the PC would be inaccessible, even via network. Only choice would be to hard reset. It didn't happen regularly enough for me to figure it out before we left for the 5 week trip.
- July 2019. After getting back from the trip, I encountered the Starcraft 2 issue again. Some reading indicated early concerns that SC2 may be killing video cards, but that was from 4 years ago! Besides, after my quick hard reboot, the GPU temp would be quite normal so I didn't think that was the issue. The problem began to happen regularly, until I could not play SC2 at all. Eventually, a friend suggested I tried lowering SC2 graphics settings and surprisingly that worked! Things looked terrible, but I didn't mind, and I could play again.
- EVO weekend, Aug 3-4 2019. I started playing Dragonball Fighter Z because it had a free weekend promo. I enjoyed the game and eventually bought it before the free weekend finished. The loading times were a bit long on my system, but tolerable.
- After EVO weekend, I tried installing Microsoft Windows update 1903, as my current version was nearing end of life. Update went smoothly.
- After the update, I noticed the performance of DBFZ had drastically worsened. Incredibly long loading times, occasionaly framerate drops during battles.
- On Aug 5, first BSOD encountered:

![](/uploads/2019/bluescreen.png)

- because of the recent Windows update, I assumed first that was the cause of the problems. So I rolled it back first and observed the behavior.
- over the next two weeks, additional instances of BSODs were observed, along with occasional crashes where the PC just straight freezes in place (often with annoying beeping sound) and a hard reset is needed. The crashes would happen even during normal usage (browsing etc) and sometimes even while the PC was unattended!
- last week I got fed up and started doing serious diagnostics:
  - I re-installed the Windows 10 1903 update
  - I updated my graphics drivers
  - I uninstalled a bunch of unnecessary old stuff
  - I ran `chkdsk` and `sfc`. System File Checker found some issues and repaired them! Maybe that fixed things? Nope.
  - I tried running the Windows Memory Diagnostic tool. Standard check froze up the first time, but was successful on the second try.
- At this point I was still hoping it was a software issue (since hardware issues generally require cash to fix), but all signs pointed to either video card (due to SC2) or memory (due to memory diagnostic failure) problems. Time to test each component in turn!

![](/uploads/2019/20190819_080244.jpg)

- I'm no stranger to digging through computer parts, but this is literally my least favorite part of being PC master race: having to figure out which of your hardware components is failing. At least my PC case is a lot more organized and spacious this time; my older PCs had super tight layouts that were hard to manipulate
  - I started with the easy one: I moved my monitors to the onboard graphics card and enabled it in the BIOS. If the issue is the video card, then I shouldn't encounter it while using the onboard graphics. Nope, had a crash less than an hour in.
  - Next we try the memory. I had two 8gb DDR3 ram sticks installed. I removed one of the sticks (pretty sure I could live on 8gb RAM tbh) and then rebooted and ran the memory diagnostics. Pass! I used the PC for one whole day with this config, even playing some SC2 and DBFZ and no issues were encountered. Things were looking up, it was likely there was a faulty memory stick!
  - the next day I decided to confirm it by swapping the memory sticks. Oops, now PC wouldn't boot. Displays don't get any signal, USB devices (mouse and keyboard unpowered). Is it because of the faulty memory stick? I swap back the "good" RAM, but still the same issue. I try a few other combinations, different RAM slots, but no such luck. 
  - This was last Monday (Quezon City holiday!). I concede defeat and acknowledge that this is beyond my power. I call up a nearby EasyPC branch and ask if they can take a look at it for me. I take a quick Grab there and the guy starts taking a look. He starts by pulling out the mem sticks and the vid card and cleaning out the connectors with an eraser. He pops out the CMOS battery to reset the board. He plugs them back in but the PC doesn't boot. He tells me the motherboard is dead. He tries some thing with a jumper, and the MB comes back to life! 
  - I have my full 16GB back. He tells me the memory problems were probably due to the dirty connectors and suggests I take the desktop back home to do an extended memory diagnostic. I agree, since I don't want to leave it at the shop. I happily pay the repair fee plus a small tip and take another Grab back home. I was expecting that I would have to shell out for new memory sticks as the best case! The whole process took less than an hour. This is one of those examples where I was wasting too many man-hours trying to do something myself!
  - Back home, I run the standard Memory Diagnostic first and it passes! Hooray. I use the PC for a while, no issues. Before going to sleep, I start the extended Memory Diagnostic and left it running overnight. In the morning, it was still going around 10 hours after it started, at less than 80% of the first pass! I reduce the passes from 2 to 1, because to be honest I wasn't going to wait another 10-12 hours for a second pass! Luckily, the test finished a couple of hours later without issues.
- Hooray! All is well! Generally, at least. It's been 48 hours and no crashes or BSODs or such have been encountered. Gaming seems fine. There seems to be a minor problem of Windows Explorer randomly spiking in CPU usage every so often, but that's probably some software issue I'll have to figure out independently. In any case, the Great Memory Scare of 2019 was over, and I get to keep using this desktop, hopefully for a lot longer!

I was a bit amused at how sad I felt when I first realized there might be a hardware problem with the PC, especially since I was hoping it would last me for years down the line. I may be a bit too attached to it lol. Well, my desktop generally does give me joy, so I'm not Kondo-ing it anytime soon!