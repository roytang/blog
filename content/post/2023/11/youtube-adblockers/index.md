---
date: 2023-11-24 07:51:58
dontinlinephotos: true
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/111464731725065541
tags:
- tech-life
- web
title: Youtube vs Adblockers, Apps vs the Open Web
---

Last month, Youtube started to aggressively challenge users who had adblockers installed on their browsers, showing them a popup:

{{% photos popup %}}

At first it was fine because I could just close the popup, but the more they appeared, the more annoying they got. They were basically another ad! I have uBlock Origin installed and I think they went back and forth with Youtube a lot in some kind of adblocking arms race, and sometimes the popup would be there and sometimes not.

At some point I tried installing an extension called [libredirect](https://libredirect.github.io/) that would redirect Youtube URLs to an Invidious instance. I tried this for a while, but it was always jarring to see the redirect because honestly the Invidious UI isn't very good and is kind of slow, although that might just have been a problem with me picking an instance at random. Also, I had to make an exception for the YT homepage because I actually like the recommendations on the homepage. I gave up on Invidious after a while (I still have the extension installed, it just doesn't do anything.)

I think things have kind of blow over by now, as I haven't seen any YT ads or popups recently so I guess uBlock Origin won. Has YT given up? I heard that [Youtube has added a 5-second delay for users with ad-blockers](https://www.howtogeek.com/youtube-adds-5-second-delay-to-punish-ad-blockers-in-all-browsers/), so maybe they're trying an alternate approach? I haven't actually experienced any delay myself though, so maybe uBO catches it also?

I also read that a privacy consultant has [brought charges against YT in Europe for detecting ad-blockers](https://www.androidauthority.com/youtube-criminal-spying-charges-ad-blocker-detection-3384885/), claiming it's a form of spying on him. IDK if that suit has any legal leg to stand on or if it has gotten anywhere though.

I didn't used to have an adblocker, at least 10 years ago I didn't, I just immediately went for the skip button:

{{% collections-embed surveys 427795493750452224 %}}

But these days Youtube ads are super obnoxious, many of them are unskippable and you get so many, sometimes two ads for a video that's only a few minutes long. It's super annoying and no wonder that more and more people are using ad blockers. It's all part of the platform's enshittification!

I thought about all of this because Manuel Moreale recently had [a post about ad blockers](https://manuelmoreale.com/on-ad-blockers), and he says:

> Things become a lot more complex when you start dealing with all the other factors that are attached to the ads world. For example, you can find this kind of argument:
> 
> > People who don't pay and block ads are scamming YouTube, or scamming advertisers.
> 
> Or even this kind of argument:
> 
> > And more importantly, they are scamming the content creators. They are not usually a massive company, but working alone, with YouTube revenue as their main income.
> 

The post doesn't provide any clear answers for the above arguments, and I don't have any either, except maybe on some level it's Youtube that's scamming their advertisers by promising them so many views on their ads when that's not really viable in terms of annoying the users. Or the web users at least. Manuel was right, ads suck!

The web being an open platform means it's biased in favor of user control - clients and browsers will always have the capability to control what kind of content they see on their devices (and rightly so!). I remember back in [the days of the old web](/2020/02/old-web/) when IE was still dominant, people would implement all sorts of scripts to stop users from doing things like copy-pasting or accessing right-click menus. Even our web projects at the time tried to do this stuff! All of these attempts to prevent the user from controlling their web experience are ultimately useless and easy to overcome because of the way the web is architected.

---

Let me segue into [this post by Aaron Straup Cope](https://www.aaronland.info/weblog/2023/11/11/therapy/#wishful) where he tackles the open web and the use of new-fangled extended-reality technologies in the cultural heritage sector. Near the middle of the talk he describes how radical and miraculous the web's foundations are:

> It might be hard to see but that's a little house in the middle of the stage and inside that house was Tim Berners Lee, the creator of the web, sitting at a desk in front of a computer. The script called for him to type a message in a web page which was then lit up in the seats around the arena. That message read:
> 
> "This (meaning the web) is for everyone."
> 
> When Berners Lee first announced the web, he also announced that it was being released without any use or licensing restrictions.
>
> Aside from the corniness of the setup at the Olympics it's hard to overstate how big a deal this was. It's taken me a long time to really appreciate what those actions represented. He put the means to deploy an asynchronous and global network of linked documents in the hands of everyone. For free.
>
> When you consider the media landscape that both predates the web and that continues to dominate our lives, one defined by a handful of companies exercising a disproportionate influence on what can be said, when it can be said and by whom it is hard not to understand the web as an intensely political act.
> 
> It is worth remembering that the internet, and the web in particular, "happened" to the media and technology companies that existed at the time.
> 
> In as much as any of them were imagining what a universe of networked computers might look like they did not imagine the web. What they imagined, what they were actively promoting and marketing, were a series of branded communities, of walled gardens, with only limited means to interact with one another.
> 

Cory Doctorow [takes Aaron's article and expounds further](https://pluralistic.net/2023/11/13/this-is-for-everyone/), contrasting the open web with the closed garden of apps:

> As bad as this is in the social media context, it's even worse in the context of apps, which can't be linked into, bookmarked, or archived. All of this made apps an ominous sign right from the beginning:
> 
> https://memex.craphound.com/2010/04/01/why-i-wont-buy-an-ipad-and-think-you-shouldnt-either/
> 
> Apps interact with law in precisely the way that web-pages don't. "An app is just a web-page wrapped in enough IP to make it a crime to defend yourself against corporate predation":
> 
> https://pluralistic.net/2023/08/27/an-audacious-plan-to-halt-the-internets-enshittification-and-throw-it-into-reverse/
> 
> Apps are "closed" in every sense. You can't see what's on an app without installing the app and "agreeing" to its terms of service. You can't reverse-engineer an app (to add a privacy blocker, or to change how it presents information) without risking criminal and civil liability. You can't bookmark anything the app won't let you bookmark, and you can't preserve anything the app won't let you preserve.
> 

*(The rest of the above two quoted posts are great too, go ahead and read the rest of them!)*

This is why a lot of platforms have their web pages trying to convince you to open apps instead: it gives them a lot more control over the user's experience (and lets them hoover up a lot more data for selling to advertisers!). This is why I avoid using YT's mobile app unless absolutely necessary; there's no way for users to avoid the ads and the popups and whatever nonsense they decide to throw your way.

---

*(Kind of a tangent)* Last week I got a text message from a financial institution where I have some money, and the text went:

> On Nov. 25, 2023, say goodbye to Customer Portal, welcome [$INSTITUTION] App! Download [$INSTITUTION] APP now on Google Play or Apple Store for easier, safer policy management.
>

When I read this I just sighed internally and wondered if it was worth the hassle to withdraw my account from them. I can understand providing a mobile app for people who aren't comfortable with using a web browser, but why sunset the web portal at the same time? What about people who don't have an Apple or Android phone! Or people who don't use their phone for financial stuff! (I have sent them an email clarifying if I can still use the web portal and that I don't want to use my phone.)

---

I guess platforms gonna platform and try to scam us out of the open web. More recent attempts to undermine the open web are [Google Chrome's switch to Manifest V3](https://developer.chrome.com/docs/extensions/mv3/intro/) which will take away the ability to use adblockers or Google's [thankfully-now-abandoned Web Environment Integrity API proposal](https://www.theregister.com/2023/11/02/google_abandons_web_environment_integrity/). 

I want to remain optimistic that we will always have the open web - that it is still around after all this time is a testament to the power of Tim Berners-Lee's original concept of the web as an open platform.