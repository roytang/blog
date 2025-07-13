---
date: 2025-07-12 04:58:10
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/114838578019817611
tags:
- printer
title: It's 2025, Why Is HP's Printer and Scanner Software Still Terrible?
---

I have an HP3635 printer/scanner I've been using for the past 9 years. All this time I've been using their old "print and scan" software which wasn't very modern UX-wise but was at least functional and good for doing batches of scans. But during the past couple of weeks, the software would often fail saying "An error occured while scanning" without any further details.

I decided to try their more "modern" HP Smart software which I also had installed a few months ago for an older printer which I tried using. It also had scanning capability, so I wanted to see if the problem was with the old "print and scan" software. The HP Smart scanning solution worked, but it was TERRIBLE:

- required me to create an HP account before I could even do any scanning
- just more clicks over all to do scans, which is more annoying when I'm doing batches of scans
- defaulted to some very high resolution setting which meant the scanned pages were way larger than what I was previously getting
- did not handle batch scan filenames very well, I ended up having to rename the saved files manually

It did work, but I didn't want to use it again and wanted to revert to the old "print and scan" software. I searched up the "An error occured while scanning" thing and [this support forum post](https://h30434.www3.hp.com/t5/Scanning-Faxing-Copying/how-to-fix-quot-an-error-occurred-while-scanning-quot/td-p/7254102) suggested I uninstall all the HP drivers and software and such and then reinstall the software from the website. Okay, I will try that.

Uninstalling was straightforward, but reinstalling was not. First, the HP website would not just let me input my printer's model number to find the needed software. Instead, I needed to find the device serial number. Why?!? How could that possibly be easier than just identifying the model?!? And even when I got the serial number, the website wouldn't accept it WTH.

I ended up having to download a different thing that would let HP detect my printer model and that would tell the website where to go. I did that, and sure enough the website soon identified the correct model with the SAME SERIAL NUMBER I gave it earlier. And then, when I click through to where the drivers for the model should be, it coughs up a 404! Ugh, this is so stupid.

After some looking around, I found out that the "print and scan" software was [discontinued a couple of months ago because of a vulnerability](https://support.hp.com/us-en/document/ish_12490059-12490108-16) and was no longer available and the only software they provide now is... HP Smart. Sigh.

I briefly considered downloading the old software from somewhere other than HP, but that seemed like a bad idea especially if it had a vulnerability. So I resigned myself to reinstalling the drivers via HP Smart and possibly just using that for my scanning. Ugh.

And then while trying to reinstall the printer drivers, the HP software refused to complete the process over Wifi! This was despite seeing and detecting the printer via Wifi! Ugh again. Luckily I still had the printer box, so I dug out the USB cable and just hooked it up to my desktop and soon got it detected and working and printing again via USB.

That still left me with terrible scanning software to use. Luckily during all of those HP software reinstalling periods, I had begun searching for scanning software alternatives. A [reddit thread](https://www.reddit.com/r/printers/comments/u4umee/how_to_use_hp_printer_without_hp_smart_app_to/) led me to a very good candidate: a free and open source software called [NAPS2](https://www.naps2.com/).

I installed NAPS2 and once I resolved the driver issues above I tried it out and it was very good. Much better than the old "print and scan" software I was using since it had more modern UX conveniences for batch scanning and editing and cropping and filenames and all that. Just better workflow overall. I was stressed for a couple of hours because of the above problems with the HP software, but I ended up quite happy with this alternative I found! 

I was so annoyed at HP last night I decided to write a blog post about it!