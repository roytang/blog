---
date: 2019-11-12
slug: prod-crisis
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1194052290363232257/
tags:
- software development
title: What to do in a production crisis
---

Despite our best efforts as software developers, it can still happen: production goes down. Or some sort of bug introduces catastrophic data error. Hopefully you have a support/DevOps team to handle the response. If not, the dev team themselves have to step in. This usual means a mad rush to figure out what happened and how to fix it, sometimes during off hours and maybe even into the early morning, all while facing pressure from clients and higher-ups. I was advising another developer in such a situation a while back, and it was his first stint as technical lead so he was extra worried. I gave him a few tips to see him through the time of crisis.

1. Keep calm. In Tagalog, [kalma lang](/2019/04/project-management-tip-kalma-lang/). In a crisis, there can be a lot of stress and pressure to fix things immediately. It's best to keep a level head and make sure the team is keeping it together. Don't let your emotions carry you away, and try to avoid panic.
2. Solve one problem at a time until you can go home. This is a lesson from the movie [The Martian](/2015/10/10154142633048912/). In a crisis it can be difficult to focus on the task at hand and if you're not thinking straight you might just charge in there blindly and move things around until things get better. Follow step #1, then figure out what are the most pressing problems that need to be solved immediately, then address them one at a time. It can also help your team morale to identify which issues can be left until the next day. This gives them a concrete sense of what is set of problems to focus on, and motivates them to solve those so they can go home.
3. Be extra careful. In times like these, you may find yourself needing to deploy hotfixes directly to production or maybe even update data directly in the production database, in the interest of expediency. It's also during times like these that you are more likely to make a mistake, especially if your team is under stress and working overtime/during off hours. So it would pay to be extra careful, maybe add an additional layer of review before deploying things directly to production. You're already in a crisis, don't make things worse by making a sloppy mistake.

Having to provide tech support during such a crisis is something you shouldn't wish on any developer, but sometimes it can't be avoided. (Some might even consider it a kind of rite of passage so to speak). Make sure to have the right mindset to be able to operate well under such stressful conditions.