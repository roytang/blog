---
date: 2020-10-27
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/105104806762996697
- type: twitter
  url: https://twitter.com/roytang/statuses/1320941945070313472/
tags:
- hugo
- django
- Meta
- Tech Life
- changelog
title: Site Migration from Hugo to Django
---

### Leaving Hugo

It's been a bit under two years since [I migrated the site from Wordpress to Hugo](/2018/11/site-migration-to-hugo/). As discussed in [this post one year ago](/2019/11/one-year-with-hugo/), I was very happy with the general workflow of managing posts through markdown files in git, but had big problems with the Hugo build time, largely a consequence of [my social media archiving](/2019/10/archive-of-my-own/). At that time, I didn't want to invest effort into migrating to a different backend, but the problem has only gotten incrementally worse since then, so I decided to take the jump and started working on it last month.

### Migration goals

The main goal is to get rid of the unnecessary build time. I also don't want to have to store all the pre-generated HTML files. It's fine for a small site, but with the large number of posts here, there's a large amount of unnecessary duplication, considering listing pages and such. That means reverting to a system where each page is generated on the fly.

I want to retain the current workflow of managing content via markdown files, so that rules out something like Wordpress. Still, I figured I needed some kind of database for indexing, so that things like listing and archive pages work properly. Given that we would be migrating away from a static site, I fully expect a performance hit, at least initially, but ideally it's not too bad.

I'd also like to retain the current content written for Hugo as much as possible. This means the new system will need to be able to parse the custom Hugo shortcodes I'd set up for the site.

I would also be migrating to a new server which I would be managing myself, which means I would need to set up the deployment myself.

### Why Django

I naturally fell back on Django, it's my ORM+backend framework of choice, and the one I'm most familiar with. Also, I already had a handful of small Django apps that I needed to migrate to the new server as well, so no matter what I needed to have a Django app on the server anyway. I also had a bunch of Python scripts that were doing already doing support functions for the site like search and ingestion of social media content, so that's something to fold into the new backend as well.

### Why Bother?

I will fully admit I spent far too much effort unnecessarily doing this, but the realization is that it's actually work I enjoy. This site is primarily a project for myself, and I enjoy the time working on it and learning stuff and improving things.

That being said, the effort wasn't too much. There was a lot of code to reuse and migrate, so most of the effort was testing and making sure things worked. Most of the new code was for parsing the markdown files to render the hugo shortcodes as HTML; I basically wrote Django templates for each Hugo shortcode to be supported.

### Changes

The migration was largely done in-place: site design remains mostly the same, post URLs should be more or less retained. I did take the opportunity to make one nontrivial change: Photos are now under [Notes](/notes) category. I really only had a separate photos category before because in Hugo I didn't have a way to query posts that have attached images. Even with everything under Notes, since I have a database now, I can do silly things like show [random photos](/photos/random). Also, now the notes section is closer to a microblog/tumblr-like feed.

The source for the site content will still be [available publicly via Github](https://github.com/roytang/blog), as it was before. Unfortunately, I am not ready to make public the source for this site, because (a) a lot of it is old code that I reused so it looks terrible; and (b) some level of security by obscurity I guess?

Not that the site needs to be secure; there isn't actually any critical/important data being stored anywhere. But the fact that a database now exists means I need to follow some kind of security practices.

The server is now hosted on DigitalOcean. Here's [my affiliate link](https://m.do.co/c/6c2e6b11b260). Since I'm on a self-managed VPS now, that means Github webhooks now work, so whenever I push new posts, they take less than a minute to now appear on the site. This is a vast improvement over the old system where it would take anywhere between 30-60 minutes depending on how Travis was feeling.

Speaking of Travis, I set up a new mirror, Travis now publishes to https://mirror.roytang.net once a day, hosted on Netlify. The mirror is still generated using Hugo! I don't know how long I can keep up having the content generate correctly for both builds, but we'll see how it goes.

### Summary

All of this actually went out much smoother than I thought it would. Took less effort than expected, deployment was a breeze. The listing pages have slightly worse performance, but individual pages are hitting 100 on Pagespeed, so that's mostly fine. 

This post was just the overview of the site changes. There's still a bunch of technical notes to be written up, so that's stuff for a future blog post. 

The last time I used a Django backend for my website was [waaaay back in 2008](/2008/12/roytang-net-site-update/), and that didn't last more than a year before I switched to Wordpress. We'll see how long this one holds out!