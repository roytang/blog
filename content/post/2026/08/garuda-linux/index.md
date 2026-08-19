---
title: "Trying Out Garuda Linux"
date: 2026-08-19T13:15:19+08:00
tags:
- linux
- tech-life
dontinlinephotos: true
---

Early this year, I set up Linux Mint dual boot with Windows 11, coming back to desktop Linux after so many years: [Return to Linux](/2026/01/return-to-linux/)

While my time with Linux Mint has generally been good, I have been meaning to try some other distros for some time now, for a few reasons:

- First and foremost is that back in May, Ubuntu (from which Mint is derived) announced that they're starting with the GenAI nonsense: https://discourse.ubuntu.com/t/the-future-of-ai-in-ubuntu/81130/72
- I have found Mint's cinnamon desktop a bit restrictive in terms of customization 
- Some minor nitpicks and issues like with a limit on open file counts

I started looking at alternative distros after the Ubuntu announcement above. My considerations were few and simple:

- not based on Ubuntu
- had to be good for gaming
- prefer KDE for more customization. I had already tried Gnome and KDE back in 2008, so I knew I'd find Gnome boring lol.

I looked at a few different options:

- [Bazzite](https://bazzite.gg/) was the first one I looked at it was supposed to be similar to SteamOS, but I didn't like the idea of an immutable OS (I like to tinker!)
- Also considered [Nobara](https://en.wikipedia.org/wiki/Nobara_(operating_system)) (I didn't like the idea that it was developed by a single person) and [Pop OS](https://en.wikipedia.org/wiki/Pop!_OS) (based on Ubuntu)

Eventually settled on Garuda Linux. I did have some free partition space available for some other reasons and so Monday morning I took the leap with little precaution. Though I did have the sense to back some stuff up before proceeding. 

Having the free partition space meant I was able to set up a triple-boot with Linux Mint and W11 instead of my previous plan of overwriting Mint directly, so that was a bit safer too.

I chose the Mokka version of Garuda because I felt the Dragonized color scheme looked a bit too gaudy for me. Mokka was only slightly better but at least more tolerable lol.

The install went pretty smoothly, though I will note it's definitely worse for beginners. The install process involved a lot more options compared to Mint (paradox of choice and all that). You had to choose what software to bring in under a bunch of categories; it would probably have been overwhelming for anyone new to computers.

Had to configure the boot order but after that the triple boot was working fine and I confirmed Mint and W11 still booted successfully as well.

After that was the "test everything and install missing things I needed and login to all my web services" phase, which took most of the rest of the day. And honestly might not be done yet, there's always things one forgets!

Some other minor annoyances during the process:

- Printer software (CUPS) had to be installed manually (https://forum.garudalinux.org/t/new-printer-setup/2554/8). This worked out of the box in Mint!
- VLC had codec issues and I had to install them manually as well (https://archlinux.org/packages/extra/x86_64/vlc-plugins-all/). This also worked out of the box in Mint!

I had a lot of my stuff on separate drives like my Thunderbird email profile and Steam library, so those were easily imported and reused from Mint. And I had access to the Mint partition as well so I could copy over files as needed.

Of course I also had to make sure most of my installed games had no issues running.

I haven't done a lot of customization yet, but here's a couple of screenshots:

{{< photos >}}

I did have to disable the autohiding panel, I always find that kind of thing annoying.

One day was enough to get to the point that I think Garuda is safe enough to use as a daily driver, and this post being published means my local dev / writing environment is also up and running. I am still getting used to the color scheme and some of these icons though. I'll see over the next few weeks/months how this shakes out.
