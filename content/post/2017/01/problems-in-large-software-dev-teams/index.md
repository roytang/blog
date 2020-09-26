---
author: roy
categories: []
date: 2017-01-26 01:30:20
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/156378509465/problems-in-large-software-dev-teams
- type: twitter
  url: https://twitter.com/roytang/statuses/824431448748920836/
tags:
- Software Development
title: Problems in Large Software Dev Teams
type: post
url: /2017/01/problems-in-large-software-dev-teams/
---

Hopefully by now most developers and project managers are well aware [of the mythical man-month and Brooks' Law:][1]

> Adding manpower to a late software project makes it later

The idea is that communications overhead scales up quickly as you add more people to a project. Oftentimes it is counter-intuitively not worthwhile to keep adding more people to try to catch up. Some implications of larger team/project size may not be immediately obvious. Some problems scale up faster as team/project size grows:

Lower productivity due to increased overhead as mentioned above.

- Meetings will tend to involve more people and take longer
- There will be a lot more emails
- Project management effort scales up quickly too
- More people need to be allocated to maintaining builds and servers
- More time needs to be spent on task prioritization, bug triage, etc
- More people asking WTF happened to their code (LOL)
- Any decision making that requires consensus building takes longer
- It becomes more difficult to find the right person to ask things

Simply due to the number of people, there are more things that could go wrong

- Developers breaking the build happens more often
- People going on sick days will happen more often
- Server performance becomes much more important since any delay or downtime affects more people
- Schedule delays or others unexpected problems will be more likely

Maintainability becomes more important

- Technical debt becomes more burdensome and poor code is more likely to come back and bite you in the ass in the future
- The need for good coding and development standards increases
- Higher likelihood of code duplication ("I didn't know that Developer R already wrote a function that does X!")
- More important for code to be well-decoupled, to reduce the likelihood of one developer breaking a lot of things

Source control gets harder to use, with so many people making so many changes.

- The team needs to develop standards for commit messages and linking commits to bug reports. to make it easier to track and monitor changes
- Source control commit comments need to be a lot more helpful or descriptive.
- More commits happening in the same amount of time, the more you need to be constantly updating from the repository.
- Merging is more likely to become difficult and complicated (may be made easier by modern source control systems)
- More important to use more, smaller files instead of fewer large files (less likely to produce conflicts)
- Need better coding/programming standards. Otherwise you have the problem of changes/commits being difficult to track for example if one developer uses different autoformatting standard (his commits will have many small reformats)

Having consistent rules for naming, UI,  and other things becomes more important

- The more developers you have, the more likely that they will have different ways of thinking. There are far more likely conflicts among a team of 8-10 developers than between 2-3 developers.
- It becomes more important to have a standard or plan for where different kinds of files should be placed. Otherwise you run into problems like different developers using different folders for their css or different package naming conventions, etc.
- Consistency and standards more difficult to enforce (since there are more devs)
- Need to keep things consistent on all levels: databases, code, UI, and so on.

Documentation becomes more important

- Tribal knowledge is often spread out among multiple developers
- Undocumented things are less likely to be passed on to new developers
- Developers unaware of undocumented things are more likely to have difficulties or to break things
- Becomes a lot more difficult to absorb new developers into the team in times of urgentness
- Documentation more likely to quickly become out of date due to rapid pace of changes


Anything you want to add?

 [1]: https://en.wikipedia.org/wiki/The_Mythical_Man-Month