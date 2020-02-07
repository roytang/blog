---
date: 2019-11-22 19:48:47
slug: one-year-with-hugo
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1198008086260338689/
tags:
- tech life
- blogging
- hugo
title: 'One Year with Hugo: Highs and Lows'
---

It was a bit more than a year ago that I decided to [haphazardly and suddenly migrate from Wordpress to Hugo](/2018/11/site-migration-from-wordpress-to-hugo/). It's a good time to look back and reflect on that decision and consider where we are now, and how to move forward.

Good:

- I am extremely happy with the site's browser performance. It currently scores an insanely high 96 on [Google's Pagespeed tool](https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Froytang.net), and I'm pretty sure I I know how to close the remaining 4% gap. (I just need to get around to it.)
- generally all the advantages listed in the original post a year ago. I'm particularly happy with managing the posts through the file system, especially with a decent editor like VS Code. I don't miss Wordpress's clunky editor at all. 

Bad:

- The main sticking point right now is that the build time is really high. I have a Travis build script setup that automatically builds the hugo site from source whenever I push a new commit, then the output is committed to a second repo, which is the one deployed to the live site every 15 minutes. This build right now takes on average around 8 mins, which is ridiculous. The hugo build itself takes around 3 mins, the rest is copying files and git clones and push and so on. The build times really skyrocketed when I did the [social media archiving](/2019/10/archive-of-my-own/), since the number of markdown files skyrocketed from around 1000 to almost 16,000. For sure, a lot of it is the fault of the theme I am using on this site, because I am adding a lot of features like static comments, image resizing, monthly archives, a bunch of taxonomies, and so on. I don't blame Hugo at all, and I'm pretty sure any other static site generator would simply choke on the amount of posts I have. There are surely a lot of optimizations that can be done, but even if I manage to pare down the template generation to bare minimum, I am most probably hitting the limits on disk I/O. As mentioned in [this discussion I had on the Hugo forums](https://discourse.gohugo.io/t/performance-expectations-for-large-number-of-pages/21887), simply copying the entire content folder already takes 30 seconds on my local computer, so that is the bare minimum I could go. This is not an intolerable problem, but it means I don't have immediate feedback when I push a post, it can take at least 15 minutes or more for recent changes.
- There are also a number of dynamic features I want to implement, which are impossible with just a static website. I have a python web app backing the static hugo site which I use for things like search, comments, and so on, but basically there is nontrivial effort when I want to implement new things. This is even less of an issue than the last one, mostly because I enjoy working with Python anyway lol.

The build performance is such a big issue for me that I briefly considered the option of migrating back to Wordpress. Ha! I'm not ruling it out, but the fact is I find managing posts through the Wordpress interface to be extremely clunky, especially compared to my current set up.

Another option would be to write my own database-backed webapp. This is something I've done before after all, and again, I enjoy working on Python anyway. But it's a lot of work, so maybe shelve that for now.

Moving forward, I think I'm going to stay with my current static hugo + dynamic python support, and try to optimize the build time as much as I can. I will probably be on the look out for possible alternative solutions, some other blogging software perhaps, or some other hybrid approach.