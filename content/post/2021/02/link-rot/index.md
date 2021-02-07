---
title: "Link Rot"
date: 2021-02-08T20:15:16+08:00
tags:
- tech life
---

#### 1

For a while now, I'd been meaning to go through the [links section](/links/) of this site and clean up/organize all the bookmarks I've logged there over the years (first via [delicious](https://del.icio.us/) and later via [pocket](https://getpocket.com/)). One of the first things I had to do was to go through and identify any broken links. So I wrote a quick Python script to ping the URLs and it turns out there were a lot of them, unsurprising given the archives go back to 2004.

I'm not happy with it, but I know link rot is a natural part of the internet, especially as time goes by. Websites fall out of maintenance, run out of funding, get restructured and so on, and the links to those pages break and rot. 

The amount of link rot is proportional to age: almost half of all the links back in 2004 are now inaccessible, and the percentage drops quickly as we get back to modern day:

{{< html "utils/stats/broken_links.svg" >}}

#### 2

I've also been meaning to update the [blogroll](/page/blogroll/) on the site, since I haven't added things there in a while. So I went through the good old RSS reader to find items to add to the blogroll, and I noted with sadness a number of blogs from old friends/people I knew who were still on my follows and were no longer active. But at least they were still there and I can still revisit all their old posts and thoughts. 

Worse than the inactive ones are those that are no longer accessible at all, either because their domains were no longer renewed, or their accounts on platforms like wordpress.com have been deactivated. Just another form of link rot.

It's one of the disadvantages of the whole ["owning your personal domain"](https://indieweb.org/personal-domain) principle promoted by the [Indieweb](https://indieweb.org/). Domains require maintenance, which means money, and which also means such personal sites can easily fall out of maintenance and thus contribute to link rot. Granted, running your website on one of the silos has no guarantees either (see: Geocities), but at least those silos have more resources than any individual and are likely to give you a chance to archive your data before they shut down, if ever. (Well, IDK if Parler let their users do that...)

Link rot is one of the reasons that when I no longer use Twitter embeds on this site, since if the source tweet is deleted or the account gets banned or goes private, the embed breaks (and back when I was using [Hugo](https://gohugo.io/) it would even break the build completely)).

#### 3

Link rot is inevitable, as I said. It's part of the nature of the internet. Despite services such as [archive.org](https://archive.org/), it's probably impossible to keep the entire web of the internet online at the same time. Links will break and rot as time goes by. Maybe trying to avoid link rot completely is an impossible ideal, akin to wishing people never die.

And I guess that it's also a bit selfish of me to want everything to be preserved no matter what. People have a right to want their content off the internet or be private if that's what they want.

#### 4

As for my own content, I am well aware of my own mortality, and hope all this nonsense I write, such as it is can somehow survive beyond me. Aside from my current hosting, a mirror of all the site content is currently published to [mirror.roytang.net](https://mirror.roytang.net/). Of course, that's still under my domain, so if I ever slip and lose the domain, or if I kick the bucket, it won't be accessible either. But at least all my content exists in source form on the [github repo for this blog](https://github.com/roytang/blog/). And a good chunk of that has already been preserved in [Github's Arctic Code Vault](https://archiveprogram.github.com/), so at the very least if all of humanity perishes, some record of me personally may still survive.