---
title: "Indieweb Updates and Thoughts"
slug: indieweb
date: 2019-11-10 15:00:00
tags:
- tech life
- meta
- changelog
---

I [mentioned before](/2019/07/move-fast-break-things/) that I was looking into indieweb stuff. There's a [whole wiki of information](https://indieweb.org/) about it if you're into that sort of thing, but also [here's a recent post](https://www.jvt.me/posts/2019/10/20/indieweb-talk/) which kind of serves as an overview. I have some comments on the content of this post, more on that [later](#later).

Indieweb things I've already implemented on this site:

- have a personal domain ([since 2006](/2006/02/welcome-to-roytang-net/))
- [microformats](https://microformats.io/) (h-card and h-feeds and h-entrys), though I would have to be using some sort of microformats reader to make sure everything there is hunky-dory (no concrete plans for this yet)
- webmention support, via [webmention.io](https://webmention.io/). Of course, I'm not actually interacting with anyone else on the indieweb yet, so this is mostly experimental and untested.
- [POSSE](https://indieweb.org/POSSE) (partially): blog posts are syndicated to Twitter and Mastodon, but I'm also still posting content on those platforms (and to Instagram)
- owning my content: (almost) all posts I make to other social media channels now get backfed into the [archive on this site](/2019/10/archive-of-my-own/)
  
Things I hope to be able to implement (no timetable):

- POSSE (full) - currently for notes and photos I still mostly post using Twitter and Instagram because their native posting features are more convenient (especially on mobile) compared to my current workflow of "push a markdown file to git". This is largely contingent on me implementing the next item:
- A web interface for posting to the site. A web interface should be sufficient convenient for mobile use. Optionally using the next item:
- Micropub. I'm still iffy whether I really need the protocol. It could be handy in certain situations.
- I've also been [digging into ActivityPub](https://mastodon.technology/@roytang/102954512082445097) lately. My hope is to eventually have this site itself serve as an ActivityPub server, such that one would be able to follow me on Mastodon via something like roy@roytang.net. Similar to how [Aaron Parecki has done it](https://aaronparecki.com/aaronpk). I've already done some exploratory work on this but it might be a ways off (low priority I guess.)
- Archive Mastodon posts into this site (this is kinda ironic for some reason)
- Automatic sending out of webmentions

<a id="later">#</a> Anyway, back to the post I linked above. My main criticism for the indieweb movement at the moment is that I don't see a path to mass adoption, especially for the purposes of moving people away from silos like Facebook. Maybe that's not really one of the goals. My main issue is with two of the principles outlined in the post above (read the post again for more details):

- "Make What You Need / Scratch Your Itch" 
- "Use What You Make / Dogfood"

The thing about these concepts is that there is a lot of work involved and there are significant barriers to entry for getting involved. I mean, most people aren't going to (won't be able to) bother with the first step (getting your own domain), much more be able to "make what you need". It's ok for people like me who are comfortable with the highly technical and have a bunch of free time, but for the average person it seems unlikely.

I can imagine there might be created a service that supports most of the Indieweb features and can easily be adopted by the mass market, although that has a lot of its own challenges as well, and it's kind of like replacing one kind of silo with another? At least it would be a more open silo I guess? I think [micro.blog](https://micro.blog/) already supports the indieweb stuff, but I haven't yet looked too closely into that.

I am still moving forward with the indieweb stuff, and I am hopeful that it manages to coalesce into something that can challenge the way the modern internet works, but that may be a long way off. As far as I can tell, adoption is not yet very widespread, and AFAICT the main people driving the effort with their [Homebrew Website Clubs](https://indieweb.org/events/2019-11-13-homebrew-website-club) are in Western countries. It's even possible that I'm the first in the Philippines looking into this Indieweb stuff. :)

