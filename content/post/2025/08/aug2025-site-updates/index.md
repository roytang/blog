---
date: 2025-08-21 23:17:28
dontinlinephotos: true
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/115069545963415463
tags:
- changelog
title: Aug 2025 Site Updates
---

I expect this is one of those blog posts that is mostly of interest to me instead of the public (isn't that all of them?), but I deployed some changes to the site last night that I wanna talk about.

### The Problem

Over the past year or so (maybe longer), my server has constantly been plagued with increasingly high traffic likely due to poorly-behaving scraper bots. This results in high resource usage for what I call "my rinky-dink server". I've tried various mitigating measures like Cloudflare filters and periodically rebooting services (causing some downtime), but the problem persists.

### The Solution

The truth is this is at least partially my fault - [my python/mysql backend implementation](/2021/11/cypress/) surely has some inefficiencies I have yet to root out. 

So my planned solution for a while has been to switch the publicly-accessible site content to be fully statically generated again. This would mean no hits to the database from the spammy requests, in theory greatly improving server loads.

### Some History

For a time, the site was already 99% statically-generated using Hugo, but when [I introduced the notes archive section back in 2019](/2019/10/archive-of-my-own/) this caused some problems. The sheer number of posts added to the system meant the generation time skyrocketed. To solve this, in 2020 [I switched to the current python backend](/2020/10/site-migration-to-django/). At the time this was fine; there was no deluge of scraper bots back then and the site doesn't get enough traffic to worry about huge loads.

### No More Notes Archive

The time has come to revisit those decisions. In order to facilitate switching back to statically-generated content, the notes archive is no longer publicly accessible. The problem with the notes archive is that the content there is primarily for me, to help with my trawling through the past. I know it is not of particular interest to the public because the feed URLs being accessed in my logs are mostly for the [blog](/blog/) and [links](/links/) section. The notes archive is still of interest to me, so it is still available to me. A fine compromise since my lone traffic will not sink the server.

### Collections

There were however some items in the notes archive that I would like to keep publicly accessible. For example, I used to post a lot of drawings on social media and I used to have a prominent link on my homepage to the sketchbook album to show those drawings. For the past few months I have been separating such items from the notes archive and adding them to [a new "collections" section](/collections/) that I have now added to the sidebar/footer menus for the first time.

The collections section is also a fulfillment of my vision for the site as a "commonplace book". From [Wikipedia](https://en.wikipedia.org/wiki/Commonplace_book):

> Commonplace books (or commonplaces) are a way to compile knowledge, usually by writing information into blank books. They have been kept from antiquity, and were kept particularly during the Renaissance and in the nineteenth century. Such books are similar to scrapbooks filled with items of many kinds: notes, proverbs, adages, aphorisms, maxims, quotes, letters, poems, tables of weights and measures, prayers, legal formulas, and recipes. 

So the collections section is a place where I can compile groups of such items. The entire collections section is also statically-generated, same as the rest of the site.

### Static Site Generation Technical Notes

I'm writing this part just so I can reference it in the colophon when I eventually write an updated one. 

Currently the static site generation is split into two parts: 

1. The main site (blog, links and other things) uses the same python backend and database to generate the static HTML pages. I already had some code before for generating HTML cached versions of new pages (one of the mitigating features I tried, especially when I realized the effects of [the Mastodon stampede](https://www.jwz.org/blog/2022/11/mastodon-stampede/)), so it was just a matter of repurposing that code to generate the entire site instead. I briefly considered using Hugo for this, but that had some space/storage concerns - Hugo duplicates all image resources attached to posts in the output folder. I tend to put a lot of screenshots at times, so this could be problematic as my server was low on space. Also, I wanted to be able to generate "partial" builds: for example, only re-generating the most recent posts on the site and such. This was easy to do with my custom code, and I believe impossible in Hugo.
2. The collections section uses Hugo for generation. Mostly because I had started implementing that before finalizing the main site's SSG implementation. This does create the problem that many of my HTML templates are now in two different places, something I will eventually have to resolve by unifying the implementations. (And also the image resource duplication problem mentioned above exists for collections posts.) But for now, this should be fine. To improve performance and allow "partial" generation, each collection is actually a separate Hugo project independent of the others.

### Limitations and Problems

The new approach means I have had to make some site features no longer publicly available. For example: there is no longer any site search, "on this day", or "random post" feature available. These features were seldom used by the public and are still accessible to me. I may try to figure out adding back site search at some point.

There are no longer "global" tag pages where you can view all items of different types under the same tag. There are specific tag pages for the blog and for link posts and for each collection.

These new changes also inevitably will create a ton of broken links in the older posts. I have tried to mitigate this by setting up redirects and such, but I can't do anything about older posts that link to items from the notes archive that are no longer accessible. This makes me a bit sad, because [Cool URIs shouldn't change](https://www.w3.org/Provider/Style/URI), but I decided it was an acceptable tradeoff.

I have also temporarily removed some automations. Mainly, my posts will no longer be automatically syndicated to Mastodon like before, I have to do them manually. This is mostly because I want to see how the new workflow shakes out before setting up automations again.

### Performance Results

It has been less than 12 hours since I deployed the changes. There were some hiccups: for example, someone quickly pointed out that some of the new RSS links were broken (the fact that someone almost immediately gave feedback was great though), and I forgot to include `robots.txt` in the initial set. These problems have been corrected.

So far, the resource usage has drastically improved. Here is the memory usage graph from the last 24 hours, and it is clearly noticeable when I deployed the new changes:

{{< photos memory >}}

The new changes also mean I can take down the database backend at any time for debugging or whatever without affecting the publicly accessible site!

### Other Site Changes

#### New Lightbox Implementation

This one had actually been already deployed for a while, but just noting it here for the record. I used to have [pure CSS/HTML lightboxes](/2020/07/hugo-lightbox/) for photos on the site, mostly because I wanted to minimize or completely avoid using JavaScript. I've kind of outgrown that implementation though, and I have softened a bit on the whole JS thing, as long as progressive implementation is considered.

The new lightbox implementation is a modified version of [PXGallery](https://github.com/StevenYuysy/PXGallery). It's a bit old and unmaintained, but I didn't want to use anything too heavyweight like react components or whatever. It should also degrade gracefully - if you don't have JS enabled, each thumbnail should just be a link to the full-size image.

The new lightbox implementation can be seen most easily in [the Image Galleries collection](/collections/albums/)

#### Other Minor Changes

Moved some menu items around, reduced stuff on the front page (I want to redesign this eventually anyway). 

### That's It!

Hopefully this solves most if not all of the site's performance issues moving forward!