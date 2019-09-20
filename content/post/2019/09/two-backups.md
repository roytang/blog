---
categories: []
date: 2019-09-20 12:00:00
tags:
- tech life
- gaming
title: A Tale of Two Backups
slug: two-backups
type: post
---

Despite my desktop PC being generally more stable after the events of the [Great Memory Scare of 2019](/2019/08/the-great-memory-scare-of-2019/), I was still encountering occasionally crashes when playing games. And by crash I mean the displays dying although the PC continues to run for a short while thereafter and after which they proceed to apparently stop operating completely. It only happens when playing games, and most often when playing Magic Arena and sometimes (rarely) when playing Starcraft 2 or Borderlands 2.

Given that I didn't want to try swapping out the video card just yet, and I had already tried doing all the driver updates during the previous episode, I decided it was time to try a more extreme approach. I was going to re-install Windows 10.

I say "extreme" even though reinstalling my OS is not something I wasn't used to. Back in the days of [Windows XP](/2007/12/today-is-a-good-day-to-nuke-your-xp-install/) I used to reinstall my OS multiple times in a year, if not in a month. It's only unusual now because Windows 10 managed to go four whole years without giving me even a hint of a bluescreen or any sort of issue like this, so props to MS for improving the stability of their OS. That being said, running an OS over such a long period means a significant amount of cruft has probably been installed and uninstalled and reinstalled over the years, with most of the details long forgotten which leads to a sort of OS rot. So in any case, I figured a reset was due anyway.

I did the research first, and apparently Windows 10 provides the reset option itself, I didn't need to make an install USB or anything like that. And the reset happens "in place", theoretically without needing to reformat your partitions or displacing your user files, which was good. But I didn't put much stock in theory, so of course for safety, I had to make a backup first. If I had needed to reset Windows 10 two weeks ago I would have been out of luck because I wouldn't have had any space to backup critical stuff. Luckily, there was a bit of coincidental foresight.

{{< note "2019/09/1172359392714358784/" >}}

So around last week I purchased a 2TB Seagate Backup Plus, so I had a bunch of space available for backups. Now, there is a generally recognized backup rule where any critical data should be backed up using a "3-2-1" rule; that is: 3 different places, 2 different media types, and 1 offsite. This is a bit too much for a home-based setup where my critical backups consist mostly of documents, family photos, mail archives, old chat logs and such, so I figured having two copies of the stuff I wanted backed up would be sufficient. One copy would remain on my secondary HDD on the desktop, and a second copy on my new Backup Plus. (And yes, that means I was living without the second copy before, which spoiler alert for the end of this story, was very dangerous.) In theory for anything that I didn't mind backing up to the cloud for privacy reasons, I already had a third copy there via Google Drive and/or Dropbox, but I haven't been too religious with that.

So, backups created, we proceed with Operation Fresh Start:

{{< photo "2019/09/1174123501470408704/" >}}

"20 minutes or longer" was pretty much a lie (or a programmer's estimate, as you will), and it took more like half a day. But it went smoothly more or less. Afterwards I had to reinstall a bunch of software (more on that in the next post!). And then I tried using the PC for a while.

Since my main purpose was to avoid the crashing, the first test was running Magic Arena. Sure enough, no crashes since the reset, all the games finished smoothly etc. Pretty good!

Now for the bad news: I was getting terribly slow read/write times on my secondary 2TB HDD. At first I thought there was some ridiculousness with Windows Explorer or other background processes gumming up the worst, so I booted into Ubuntu (using a USB boot drive) to see if copying from the disk would be better there. (Side note: I miss having an Ubuntu desktop, but discretion is the better part of valor, so maybe I won't try to dual-boot it just yet). Sadly, Ubuntu told me there were some 40,000+ bad sectors on the 2TB drive (!) which meant it was almost certainly failing. 

Luckily I had the foresight to do backups beforehand and got all the critical stuff. Or not. It turns out I forgot to archives a whole 20+ gigs of photos from my Mom's old PC after that PC's hard drive had died. And violating the backup rule, there was no other copy of those photos anywhere else!

The secondary drive was still there, so my first instinct was to power through and try to copy them off that drive but this turned out to be impractical as it was taking forever. Then I remembered that before using the old PC (which she inherited from me after I bought this current one), my Mom had been using a small ASUS netbook whose display had died. I confirmed with her that all the photos from the PC had come from that netbook, and happily I was able to boot it up and connect it to an old VGA monitor so I could copy her files from there. It took the better part of a day, but I was able to save most of her files. Whew! I'm backing these up to her Google Photos account as soon as she remembers to give me her creds.

Now, the next problemw as what to do with my current desktop's 2TB drive. A couple of consecutive chkdsk runs (both of which took more than a workday to finish) confirmed the worst: many bad sectors and many unreadable segments. It would certainly not be prudent to continue to use it, it had to be replaced. I considered just replacing with a 500GB SSD, but I needed the 2TB capacity. Not just for the critical stuff, but mostly for game installations as well and also I had been running a Plex media server off this desktop so there were a bunch of movies and TV series eps there. It was ok to lose them to a reformat, since most of them could be re-downloaded, but I couldn't go to a smaller capacity.

I really liked the idea of getting a second SSD though (to help with load times), so I considered getting both a 500GB SSD **and** a new 2TB HDD but this was a bit of an expensive option. Then I learned about the existence of so-called SSHDs or Solid State Hybrid Drives. Basically they're normal HDDs except they come with a small SSD cache to boost read/write speeds for commonly-used files. Basically you're getting something a bit faster than a normal HDD, but not with the capacity costs of a full-blown SSD. Not a bad idea, and I convinced myself to try it out. The 2TB Seagate Firecuda looked like a good SSHD to try out, and it was a quite a bit less expensive than my previous option of an SSD+an HD. I wanted to get one today! 

Unfortunately, all the shops I called didn't have any in stock, so I went ahead and ordered one from Lazada (slightly pricier). I'm a bit wary about ordering electronics online, because of warranty issues and such. But what the heck, I should risk my money every so often. Purchased! Ordering online meant I'd have to wait a few days for the delivery, so until then I have to live only with my primary 250GB SSD. Luckily this is sufficent to play Magic Arena and SC2 and write on this blog and SSH to work servers etc. I won't be able to install most Steam games or download videos and such until the new drive gets here though.

I am hopeful that the failing hard drive was the cause of my recent gaming crashes and that replacing it solves the issue. All of the offending games were previously installed on the 2TB secondary so it's a decent hypotheses. Both Arena and SC2 have been behaving since I moved them to the SSD, so signs are good. That being said, this HDD failure combined with the previous episode is pretty much an indication that my PC is getting on with age. I'm hoping it will last me a few more years still, but that is more the optimist in me than anything else.

In summary:

- backups good
- gonna try out an SSHD
- pc might be dying. Well, we're all dying I guess