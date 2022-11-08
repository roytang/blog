---
title: "Thoughts on Mastodon"
date: 2022-11-08T07:32:46+08:00
tags:
- tech-life
---

Recently: Elon Musk bought Twitter and seems intent on running it into the ground in record time. This has sent many people seeking alternatives, and one of the beneficiaries of that is Mastodon, [which has seen record growth](https://mastodon.social/@Gargron/109300967725833789) over the past week or so. 

I've been on Mastodon since 2018, currently at [@roytang@indieweb.social](https://indieweb.social/@roytang), feel free to give me a follow! What follows is a rambling stream of thoughts about the platform.

Mastodon has a completely different vibe compared to Twitter, a much more small-town, homespun vibe. The signal to noise ratio is definitely higher, and there are very few "influencers" who try to "game the algorithm" or whatever. (There is no algorithm to game!)

I think the ship has sailed on this, but I dislike that the promoted Twitter alternative is the term "Mastodon" instead of something like the more generic "Fediverse". It's like saying you should send me an Outlook instead of an email. 

I think it's unlikely that Mastodon ever gets near mass adoption on the same scale as Twitter, but that's okay. Maybe that kind of single centralized global public square isn't really what we need right now. See ["the common digital square should be the entire web"](https://www.manton.org/2022/10/27/dear-elon-musk.html).

It would be nice to have more Mastodon users though. But the main reason I think Mastodon won't get mass adoption is for the same reason it never was "the year of the Linux desktop": developers often vastly underestimate how much friction can turn off normal, everyday people who don't really care about tech.

I mean, the first choice you're asked to make when signing up on https://joinmastodon.org/ or when using any of the client apps is that you have to choose a server/instance. This isn't Discord where you're targeting gamers used to this kind of thing. There are lots of people who will have trouble thinking of a password, and you ask them to choose a server? If your intro starts off with technical terms like these, you're already turning off a nontrivial chunk of users. 

Add to that the fact that a lot of the servers will be hitting their resource limits due to a surge of new users, the onboarding process can be tricky for those who don't have the patience for dealing with "computer things."

One of the Mastodon features touted is the ability to easy migrate to a different server, [something I had to do recently](/2022/10/109151752766558627/). Even for a tech person like me, it was not straightforward and I had to look up a guide and ran into a caching issue. Really it should be something as straightforward as an "Import from another server?" option when signing up on the new instance.

One way towards larger scale mass adoption would be something similar for email, which is the only other federated online service that laypeople might be familiar with. With email, if someone asks "how do I use email?" the easiest way is to point them to one of the big providers (it used to be a larger set but I guess that's mostly just GMail now?). It would be great if we had something similar for Mastodon. "How do I get on the fediverse?" "Oh, just sign up at <easymastodonprovider.com>", where <easymastodonprovider> has the resources to absorb a large number of users without issue and probably have some kind of white-labelled mobile client specifically pointing to their server. Maybe they have different servers for each region and automatically assign you one based on location data? The problem with this approach is that probably only big tech companies have the resource for it, and they are unlikely to spring for it unless they can profit off it somehow and they try to inject advertising and we fall into the same old problems all over again. Or maybe the fediverse as a network can be more resilient to some instances having advertising because of the way it's designed?

Another danger of having a default instance with the biggest population is the network effect might give that instance undue power/influence, the same way GMail can bully smaller mail providers through spam filtering, etc. Although again, the federated nature of the network probably (?) lets us avoid that issue.

Maybe a better way for Mastodon's growth would be for institutions like schools or media outlets or big companies or governments to host their own Mastodon servers and automatically give out accounts to students/employees. This was basically how email got started! It comes with the upside of automatic verification, since you can assume anyone from the newyorktimes.com mastodon domain really is an employee of the NYT, etc. [At least one country is already doing this](https://mstdn.science/@corneliusroemer/109298270704374835), maybe more will follow? [My university alma mater also has its own server](https://social.up.edu.ph/about)! (Not a lot of users yet, but at least it's there!)

Some Mastodon features I like:

- When viewing profiles of people you follow, you have the option of adding a private note about that account. I've wished for years that Twitter (or other platforms) had this option because sometimes I randomly follow people then later when I see them in my timeline I've totally forgotten why I followed them or where I found them from. However, I have yet to use this option on Mastodon.
- You can add multiple links to your profile and you can self-verify them by adding a `rel=me` link back from the target page. You even get a green checkmark on that link, no need for $8 a month!
- The API is very good and simple and straightforward. My site auto-syndicates some stuff to and from Mastodon, and integrating with Mastodon was always way easier compared to Twitter.

Some relevant links:

- Dan Hon had [a recent newsletter](https://newsletter.danhon.com/archive/s13e18-mastodon-or-what-happens-when-your-7233/) which touched and expanded on some of the points I've mentioned here, and raised some other interesting ones.

Regardless of what happens, it looks to be an interesting time to be on Mastodon (and hopefully the open web) moving forward!