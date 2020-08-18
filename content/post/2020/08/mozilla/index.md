---
date: 2020-08-18
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/104709292313278002
- type: twitter
  url: https://twitter.com/roytang/statuses/1295629020504010753/
tags:
- tech life
- software development
title: On Mozilla and Firefox
---

Mozilla made the tech news recently for laying off a whole lot of people. ([Official statement](https://blog.mozilla.org/blog/2020/08/11/changing-world-changing-mozilla/)). People were alarmed and worried about the future of what is the last major independent browser and the open web, bit it looks like it isn't that bleak. Most of the layoffs were to teams other than those working on Firefox, things like the experimental browser engine Servo, devtools, and MDN. The core Gecko team seems to be unaffected.

Not that these things aren't important. MDN, if you're not familiar, is a set of documentation of web standards and browser support, [available online](https://developer.mozilla.org/en-US/), that is one of the best resources for web developers working on cross-platform things. Mozilla no longer funding it's maintenance is a big deal, it means it's less likely to be kept up-to-date, even though community work can still continue. Peter-Paul Koch, writer of [quirksmode.org](https://quirksmode.org), which was the original resource for cross-browser compatibility back in the heyday of the browser wars, wrote an article about Mozilla's problems titled ["The Cult of the Free"](https://quirksmode.org/blog/archives/2020/08/the_cult_of_the.html) where he argues that it's time to step out of this mentality that all these resources must be maintained for free by "the community", but that we as consumers must get used to the idea of paying or donating to support these resources. Expecting "the community" to step in and maintain these resources [also devalues the work of technical writers.](https://www.quirksmode.org/blog/archives/2020/08/i_love_mdn_or_t.html) Trying to get more people to support these "free" resources is a good idea, but I worry it goes against the grain of years of internet culture which has conditioned people to expect online content for free.

Speaking of contributing, a while back I had considered looking for open source projects I could contribute to, and preferred projects that I actively use. Given that I'd been using Firefox [since before version 1.0](/2004/10/firefox-1-0-on-november-9/), one of the projects I considered was Firefox. I went through the whole rigmarole of [their instructions to set up my machine for the Windows build](https://firefox-source-docs.mozilla.org/setup/windows_build.html), and just the setup process, which involved setting up and checking out code took more than an hour. That was fine for initial setup, but actually building and running Firefox itself took an additional hour or so. Might have been more than that even, it was a while back so I don't clearly remember, but I do remember thinking that I didn't have time for these hour-long build times. The whole set up also took up a nontrivial amount of my SSD disk space (imagine how much worse the build time would have been if I had used my non-SSD drive!), which I am always dangerously low on. These 2 factors led me to shelve the idea for the time being; perhaps I could revisit the idea of contributing to Firefox when I upgraded my computer or had more SSD space available. (TBF, I kind of gave up real quick after the first build, maybe the builds get faster on succeeding runs?). So that's my personal "contributing-to-Firefox" story, for now.

The sheer size of the codebase and the long build times just drive home the point of how much modern browsers are these large complex beasts that are doing so much. They are pretty much an OS of their own since they host a ton of features and web applications and JIT JS and all of that. This means it's really difficult for independent browser efforts to hit feature parity with modern web browsers - even just working with JS and CSS standards, there are so many to implement.

Drew DeVault laments that [Web browsers need to stop](https://drewdevault.com/2020/08/13/Web-browsers-need-to-stop.html) with all these new functionalities and APIs that add scope and complexity, and maybe focus more on performance, efficiency, etc. I do agree - if I was contributing to Firefox, I would want to find a way to reduce the massive memory footprint it always has. I don't even use that many tabs, and I already feel burdened by Firefox's memory footprint. (Pretty sure Chrome is pretty bad in this regard as well.)

Why care about Mozilla/Firefox at all? Why not just use Chrome, it's pretty good right? 

First of all, no, Chrome is not necessarily "pretty good", given how it props up a surveillance capitalsm engine.

Secondly, even if you didn't dislike Google, having a browser (engine) monoculture is not a good thing. I [got my start in web development](/2020/02/old-web/) at around the height of Internet Explorer 6's dominance, and I'd rather not find my way back there. Granted, one of the issues back then was that IE6 was a stagnant platform that upstarts Firefox and eventually Chrome left behind. No such problem exists now, since Chrome is still in active development and still pushing new web standards forward. And the fact that Chrome is an open-source platform means in theory someone could just fork it if ever Google goes off the rails or such. (And people have already built indie browsers on top of Chrome of course!) But it's still dangerous for a single company and/or codebase to be the sole major implementer of web standards. A single company dictating the future of the web isn't a good thing, and is the very opposite of the idea of an "open" web.

Side note: Maybe I should try building Chromium too, just for comparison.

Anyway, that's all my ranting for today. In conclusion: reduce your surveillance capitalism footprint and support the open web, use Firefox.