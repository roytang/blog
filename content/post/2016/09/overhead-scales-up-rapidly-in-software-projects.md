---
author: roy
categories:
- Software Development
date: 2016-09-22 01:30:22
title: Overhead scales up rapidly in software projects
type: post
url: /2016/09/overhead-scales-up-rapidly-in-software-projects/
---

Overhead scale up rapidly as project team size increases. Every time you add a new person to the team, he comes with a lot of overhead such as the need to learn the project details, responsibilities of other team members, who to consult when there's trouble, custom project procedures, and so on

It's a reinforcing cycle too. As overhead increases, the team imposes more processes and restrictions to make sure everyone is doing the right thing and there are no screw-ups. More processes means even greater overhead when new team members join. And the cycle repeats

As team size increases, mistakes become more costly too. When you're a team of two or three developers all in the same room, you can barrel ahead quickly and when there's a problem you can quickly figure out who broke the build. But when there's like eighty of you split over two floors, it becomes a tedious exercise. And every broken build and every critical bug now costs a lot more man-hours because it affects a lot more people. So everybody needs to be even more careful, and yeap even more overhead. You end up introducing more coordinators, reviewers, etc.

In so many words, the above is simply a restatement of the famous "Mythical man-month" quote:

> Adding more people to a late project makes it even later

In practice though, I find that people who are aware of this quote find themselves falling into the trap of "this won't happen to me", so a more nuanced discussion of the problems of scale might need to be had. Management typically responds more to qualitative costs, so maybe there are some metrics that you team could find? Something like "for every N developers, we need an additional X amount of coordination work" and so on

Or maybe it's one of those myths we are doomed to relive again and again... 