---
date: 2024-10-16 12:32:28
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/113317294927757270
tags:
- blogging
title: Website Gardening
---

Terence Eden writes in ["Tending to My Digital Garden"](https://shkspr.mobi/blog/2024/10/tending-to-my-digital-garden/):

> I've written over 3,000 blog posts throughout the years. This blog has become a repository of my thoughts, feelings, experiments, hopes, and creations.
> 
> It has also become outdated, buggy, and suffers from link-rot.
> 
> So, every day, I tend to my digital garden. I go in to old posts and check that the links are still pointing somewhere relevant. Are the embeds still live or do they need replacing? Has my writing somehow been mangled by me buggering about with CSS?
>

I like this gardening metaphor to refer to website maintenance. It is an activity that I also try to indulge in daily - I had previously been referring to it as "OTD cleanup" where "OTD" stands for "On this day", since I primarily use that function of the site to go through old posts.

### The Notes Archive

Aside from just checking and reviewing old links, a lot of the work revolves around the [notes archive](/notes/). As described in ["An Archive Of My Own"](/2019/10/archive-of-my-own/): about 5 years ago, I imported some 14,000 old posts from various social media platforms into this site. While I very much still value retaining that old data, I have over time come to realize that not all of it was worth preserving, and not necessarily in the form I had imported them.

To be sure, there was a lot of information there I wanted to keep - photos, sketches, interesting reposts, short reviews that never made it to the blog, etc. But there is also a ton of noise, which is typical of how people used social media during the decade from 2009 to 2019. It would have been a ton of effort to go through all of the old posts manually at the time, so I just imported everything, with the intent that I would be pruning the archive eventually over time. 

So I've been doing this pretty regularly over the past 5 years, reviewing old notes and deciding which ones to keep, checking to see if my initial import missed anything from Facebook (that site's export data was pretty bad), among other things. One would think that given I do it on a "on this day" basis, one year of such cleanup would be enough! But it's not because my ideas about what to retain and HOW to retain them are changing constantly.

#### Performance Issues

When I did the initial notes import, the large number of posts on the site quickly overwhelmed the performance of Hugo I was using for static site generation. I ended up [migrating my system to Django](/2020/10/site-migration-to-django/) about a year later to help manage the large number of files without the exceedingly long build times. 

And it has mostly worked! Except when it doesn't. Sometimes, especially [when bots and scrapers decide to prey on my site](/2024/06/bots-scrapers/), my cheap rinky-dink VPS hits memory limits pretty quickly, I suspect because of the sheer number of pages that can be crawled. I have been doing some backend rewrites to help improve performance, but the best fix would be to rapidly reduce the number of posts. Not only would this reduce the surface area for crawlers to hit, it would also lighten the resource usage of the database (less records).

So during the past couple of years or so, my thinking about the notes archive has changed, and I have been more aggressive in removing old notes. This doesn't necessarily mean the content is deleted or lost - I may decide to consolidate them into backdated blog posts (which I have tagged as ["backpost"](/tags/backpost/)). Recently I have also been planning to introduce a separate section of my website to host sets of old notes that I want to preserve, but served in a static site format so that the performance is great. I realized I could avoid the long Hugo build times by grouping the posts into smaller sets that could each be a separate static "site" - avoiding the exponential cross-referencing that the old repo encountered. I am hoping to publicly make that new section available before the end of the year, but there is a lot of work to be done yet.

#### Cleanup and Endgame

So during the past couple of years or so, my thinking about the notes archive has changed, and I have been more aggressive in removing old notes. This doesn't necessarily mean the content is deleted or lost - I may decide to consolidate them into backdated blog posts (which I have tagged as ["backpost"](/tags/backpost/)). Recently I have also been planning to introduce a separate section of my website to host sets of old notes that I want to preserve, but served in a static site format so that the performance is great. I realized I could avoid the long Hugo build times by grouping the posts into smaller sets that could each be a separate static "site" - avoiding the exponential cross-referencing that the old repo encountered. I am hoping to publicly make that new section available before the end of the year, but there is a lot of work to be done yet. For some topics, I am also planning to write future blog posts discussing and consolidating old notes.

I am not 100% clear on this, but right now what I imagine as the eventual endgame is that I want the site content to be primarily the [blog](/blog/) and the [linkblog](/links/), with the notes section serving as a temporary holding area for content that will be moved to other sections or consolidated into blog posts as necessary.

It will be a long road to get there - from a peak of more than 15,000 notes in the archive, I only recently got it down to below 10,000. There are many notes that I am not sure yet how to handle them or where they belong or whatever. I can only assume I will figure it out in the future!

Not that it's tedious work or anything. As Terence Eden says in the post linked above, it is meditative work. And I do enjoy the daily trip down memory lane the activity allows. And while I have a presumed endgame goal, I understand full well that this site will always be [perpetually under renovation](/2019/08/perpetually-under-renovation/)