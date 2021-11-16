---
title: "Cypress: My Custom Blogging System"
date: 2021-11-16T14:45:13+08:00
tags:
- blogging
- tech-life
---

In [October 2020](/2020/10/site-migration-to-django/), I migrated this site from serving static Hugo-based files to a site running on a custom Django-based backend. My internal name for that backend is ***Cypress***, which has no particular meaning other than I wanted something that was an alternative to *Wordpress*. (Yes, I am aware there is [a testing framework by that name](https://www.cypress.io/), that's a problem for future me.)

So it's been a bit over a year since I decided to write my own custom blogging system. I decided to write about it for a bit because of some recent posts from other bloggers I follow who have also written their own custom blogging systems:

- Jan-Lukas Else's open source [Go-Blog](https://git.jlel.se/jlelse/GoBlog) [recently hit its one year anniversary](https://jlelse.blog/micro/2021/11/2021-11-13-lrhvj). 
- Colin Walker replied that his own custom system called "(b)log-in" [is almost a year old as well](https://colinwalker.blog/?date=2021-11-14#p3)
- Another blogger I follow [James Van Dyne](https://jamesvandyne.com/) also wrote his own custom open-source system called [Tanzawa](https://github.com/jamesvandyne/tanzawa), which I believe he started working on earlier this year.

It's an interesting convergence that several different people started working on custom blogging systems within the past year or so. (I'll spare you the speculation that maybe it's a sign of how blogging is coming back or such.) Unlike the above bloggers though, I haven't yet had the guts to make ***Cypress*** open source or otherwise publicly accessible. I've thought about it but I hesitate because of reasons:

- **The code is probably terrible.** I cobbled together a lot of it from a hodgepodge of Python scripts I was using to support the old Hugo-based static site. Still a lot of refactoring and cleanup to do, although there is a real possibility that job may never end.
- **The system is highly opinionated.** The system follows certain conventions that exist largely due to the structure of the content for my old Hugo site. I'm not yet convinced it would actually be useful for other people to see or use given they may have completely different blogging needs.
- **It's not yet 'stable'** even though the site has been using it live for more than a year. I don't consider it stable because I'm still constantly making changes, tweaks, adding new features etc. It doesn't help that I'm constantly changing my mind about how I want the site organized!
- **I don't have documentation**. There are a lot of features that work only by convention, i.e. needing certain files to be in certain places for example, and it will take me a while to document all of those for public consumption.

I felt the need to write my own system because of specific blogging needs, some of which aren't easily catered to by existing systems. The most critical needs are:

- Able to handle more than 16,000 archive items (a result of my using this site to [archive posts from other social media platforms](/2019/10/archive-of-my-own/)). This was the main reason I switched from Hugo: the sheer number of files made each site rebuild painfully slow.
- All site content should be synced from a separate repository - i.e., I didn't want my content to live only in a database like Wordpress and I wanted the ability to publish simply by uploading a markdown file to the repository. This means the content and the system that serves the site can exist independently of each other. In fact, the site content should still be fully compatible with Hugo. (Although I've already stopped updating [the Hugo-based site mirror](https://mirror.roytang.net/).)
- Robust searching functions. I often use the site to refer to something I've said in the past or look for old convos or comments or such. This is the reason I needed to have a database in addition to the separate content repository. The content exists separately, but the database does indexing and allows for easier searching by things like date, tag, source, syndication, linked domains, media referenced, location, etc. Cypress actually has a bunch of URLs configured that aren't linked to from anywhere, I use them for my own searching.

The system also handles some [Indieweb](/2019/11/indieweb/) related features like webmentions.

I also have a general site philosophy of:

- responsiveness and performance
- minimal JavaScript usage
- no annoyances like ads, popups, etc

I'm not sure how long I'm going to keep working on Cypress (it might be forever!). There are features I've long wanted but never got around to.
Some examples:

- Mastodon compatibility, i.e. I'd want someone to be able to follow something like blog@roytang.net from a Mastodon instance
- micropub support
- theme-switching
- automated tests

And as mentioned I'm constantly tweaking and adding new features whenever I think of them. I suppose it's good that I do these "state of the blogging system" reviews on a regular (annual?) basis, so I can constantly be evaluating the way forward.