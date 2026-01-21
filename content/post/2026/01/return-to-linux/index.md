---
date: 2026-01-21 06:06:18
dontinlinephotos: true
resources:
- src: Screenshot from 2026-01-21 15-41-21.png
  title: 'Screenshot of VSCodium running in Linux Mint'
tags:
- tech-life
- linux
title: Return to Linux
---

[Last week](https://indieweb.social/@roytang/115890485872188737) I set up Linux Mint + Windows dual boot on my computer! I am writing this post from the comfort of my desktop running Linux Mint (dual boot with Windows)!

### Previously

Tracing through previous blog posts, it looks I started playing around with Linux in 2006: [Adventures in Linux Land, Part 1](/2006/01/adventures-in-linux-land-part-1/), [Adventures in Linux-land, part 2](/2006/02/adventures-in-linux-land-part-2/), [Adventures in Linux-land, part 3](/2006/03/adventures-in-linux-land-part-3/), and I think I kept the dual boot around until at least January 2008, based on [this desktop screenshot I posted on DeviantArt](https://www.deviantart.com/roytang/art/January-16-2008-Desktop-74783687).

### Why Linux?

I think that back then I was treating Linux as more of a toy than anything else, something to satisfy the tinkerer in me. There wasn't really any intention of turning it into a daily driver. The main reason was for gaming - back then Linux gaming wasn't very well supported and loved playing games then as I still do now so that was a no-go. Also, I shared the computer usage with my brothers (and sometimes my mom) back then, so I couldn't just abandon Windows willy-nilly.

Today, the landscape has changed. Linux gaming is in a very strong position, thanks in large part to Steam's efforts on platforms like SteamOS and the SteamDeck. And Windows has gotten very annoying, with Microsoft deciding to be more aggressive with pushing their "AI" nonsense even if you never asked for it. So here I am once again, exploring the Linux space. 

This time, the intent is very much to attempt to migrate to using Linux as the primary OS for my daily use. 

### Why Linux Mint

Honestly, any flavor would have been fine, Mint is just the most recommended.

### Dual-Boot Setup

The only real issue I encountered while trying to set up the Linux Mint / Windows dual boot was when I had to resize my SSD partition to make room for an ext4 partition to hold Mint. Windows Disk Management only gave me a ridiculous 4MB of allowable shrink space for some reason. After trying various disk checks to figure that out, I ended up just using a third-party program to shrink the partition: I used Resizer Portable from https://www.resize-c.com/. (I just crossed my fingers and hoped it did not screw up my SSD!)

Happily it worked. Some articles online suggested around 100gb for the Linux Mint partition; I allocated around 120gb to have a bit more leeway. After that, it was a straightforward install from bootable USB drive. After the install, I had to muck around a bit in my BIOS to make sure the computer booted using GRUB.

### First Impressions

I think last time I favored Kubuntu because I liked how KDE looked. This time I am using Linux Mint Cinnamon which is based on Gnome. A bit more boring I think, but remember I'm not tinkering (yet) this time, I'm trying to migrate to a new platform, find a new daily driver.

Reading through my older posts and comparing the experience then and now, it was like night and day. Back then I had trouble setting up networking, installing Firefox, playing MP3s etc. This time most everything just worked out of the box: internet was accessible, both monitors were working, media playback was fine, all my hard drives were accessible, etc etc. Even my printer was immediately accessible wirelessly! A few months ago, I had trouble with the Windows HP drivers and had to resort to connecting my printer via USB; Linux Mint detected it without needing any extra setup and print and scan features worked just fine! 

What a world of difference 20 years makes!

### Software Setup

- Firefox: Came pre-installed! I logged in to my profile and it remembered most of my settings but of course I had to relogin to a lot of sites.
- Thunderbird: Took me a while to figure out how to import my TB profile from the Windows side as at first I wasn't seeing the "ImportExportToolsNG" extension as available. Turns out I just had to update Thunderbird to the latest version, then install the extension, then it was able to import my profile straight up. No need to recall my mailbox passwords!
- VSCodium: The Chromium to VSCode's Chrome. I had trouble with the initial version I installed from the Software Manager; it seemed to be running a custom terminal that wasn't sharing settings with the my other shells. Turns out that it was because of something called Flatpak, and it had its own packaged shell. I ended up uninstalling and reinstalling from a DEB file downloaded from [the VSCodium website](https://vscodium.com/).
- [NAPS2](https://www.naps2.com/): This is the software I use for scanning on the Windows side, and I was happy to learn it had a Linux version as well, so this was pretty straightforward.
- Steam: Available from the Software Manager. No issues. Some other notes under "Gaming" below.
- Discord: I initially installed from the Software Manager which was also via Flatpak, but I think I screwed something up at some point because I couldn't launch it. Ended up just reinstalling it from a DEB file from the Discord website.

### Gaming

At first I tested some small Steam games that I play regularly: [Root](/2021/05/root/), **Dune Imperium**, [Eternal Card Game (Steam)](/2018/11/review-eternal/). At first I was experiencing some unacceptable slowdown. Then I found this article about optimizing Mint for gaming: https://github-wiki-see.page/m/MalwareTester74/Linux-gaming-guide/wiki/Linux-Mint-Cinnamon-Gaming. After some tweaks, the performance became more acceptable.

Then I tried **Witcher 3**, which I'm currently playing through. It wouldn't launch at all! This was annoying. This game was around 50gb so I had installed it on one of the NTFS partitions but [a steam forums thread](https://steamcommunity.com/app/292030/discussions/0/684113461911793702/) suggested that was a bad idea for Linux gaming in general. So I moved it to the ext4 partition (using up a good chunk of the precious space), but it still wouldn't launch. Finally, I figured the problem was the CDProjekt launcher that Steam was launching before the game itself. I set it up to skip the launcher and after that the game launched normally! I have been able to play a few hours on the Linux side since then, everything is fine!

The next thing to try was to setup MTG Arena. I had [already gotten this working on the Steam Deck previously](/2025/11/weeknotes-11-09/#steam-deck-updates) so I already knew what to do. This worked without issue.

Overall happy with the state of gaming this time around. I still expect other games might have issues similar to Witcher 3, but we'll deal with that on a case by case basis I suppose.

Also, I briefly considered making a second ext4 partition just for Steam games off one my HDDs, but the only one that had enough free space was a "Dynamic Drive" managed by Windows Logical Disk Manager, and apparently I can't resize that without wiping the drive! So that is something to consider for the future.

### Some Issues

I think most of the issues I encountered were tech-related: either because I was trying to work with dual boot and needed access to NTFS drives or because I was trying to get programming things working.

#### Apache and NTFS mounting

I normally have a local static webserver running both for my own dev efforts and for easy access from other devices. I set up Apache2, but the problem was trying to serve files from my NTFS drives. I ran into permission issues and couldn't figure it out at first. Finally I came upon this solution: https://linuxvox.com/blog/apache-access-to-ntfs-linked-folders-in-linux/. Basically, the drives need to be mounted using the `ntfs-3g` driver and suitable permissions set. After that, everything was fine!

#### Cloud Storage

On the Windows side I had both the Dropbox and OneDrive clients for cloud storage. I was at first assuming that I would just be able to access those folders on the Linux side and just boot back into Windows every so often to cloud sync. Sadly this was not the case. At first neither folder was viewable on my NTFS drives. Apparently they were both using some Windows API that made it so that the files don't actually exist on disk until you access/download them, which made them not visible from the Linux side.

For Dropbox, I eventually figured out that I needed to set it to disable this behavior. I did the solution mentioned [in this thread](https://www.dropboxforum.com/discussions/101001016/i-cant-access-my-dropbox-files-on-an-ntfs-drive-from-linux-after-the-latest-upda/839170):

> You need to reinstall Dropbox and opt out from "Dropbox for Windows Updates" during the installation (in Advanced options in the last step of the installation wizard) in order to mount Dropbox folder under Linux again :-)

In addition to reinstalling with this setting, I had to go back to the Windows side, I had to go to my Dropbox folder and right click and choose "Make available offline" for all the folders. Then I had to wait for Dropbox to download everything I think, and after that I went back to the Linux side and was able to access everything normally.

For OneDrive, as of this writing I am still unable to access the folder from the Linux side. I tried compiling an alernative `ntfs-3g-onedrive` driver (https://github.com/gbrielgustavo/ntfs-3g-onedrive/), but that does not seem to have worked. 

Next steps: Dropbox has an official Linux client while for OneDrive there is [a OneDrive Client for Linux available on Github](https://github.com/abraunegg/onedrive) that is still actively maintained. I was hoping to just have access to the folders on the Windows partitions to save on some space, but if OneDrive is giving me trouble anyway, I might as well install clients on the Linux side as well and have sync access.

#### Dev Stuff

I set up my local dev environment (VSCodium, git repos, postgres db) mostly without issue, though it took some time.

I did encounter a problem that [this Java program I use to support my scanning activities](https://github.com/michielproce/multicrop-scanned-photos) did not have a working Linux release. It's a jar file, so I'm supposed to be able to just run it the same way on Linux, but it was making linked native calls to a Windows DLL for [OpenCV](https://opencv.org/). Took me a while, but I eventually got this working by downloading an older version of OpenCV (the same version used as a dependency by the Java program) and following [the documented Linux build compilation process](https://docs.opencv.org/4.x/d7/d9f/tutorial_linux_install.html). The older source code had some compatibility issues with C++ 17 (?) so I ended up having to edit a bit, but I got there eventually, and the script has worked!

#### Random Issues

I think I accidentally uninstalled some core cinnamon thing because at one point I encountered an error that Mint refused to startup and had an error about `cinnamon-session-cinnamon not found`. I ended up booting into recovery mode and reinstalling the needed packages via command line. Easier than I thought it would be, but definitely something only a techie would be able to solve (and maybe not likely for a normie to encounter anyway)

#### Minor Annoyances

I set up [my rotating set of desktop wallpapers](/collections/albums/wallpapers/), but it seems that the Desktop backgrounds don't support having different wallpapers on each monitor! (Windows 11 has this natively.) I think there are some custom software that can enable this, but I haven't had time to look into it yet. (Also new OS might mean I should add some new backgrounds to the rotation lol.)

### A Screenshot

{{% photos %}}

Always good to include screenshots so that future me can remember what this time was like! IDK why the generated screenshot is misaligned like that.

### Overall 

Overall quite happy with where I am after about a week of Linux usage. I am spending more time on the Linux side now! Gaming is fine, and I am able to do most of my dev/side project/archival work on the Linux side so far. I have high hopes for eventually maybe even ditching Windows altogether at some point!