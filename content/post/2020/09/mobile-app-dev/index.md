---
title: "On Mobile App Development"
slug: mobile-app-dev
date: 2020-09-03
tags:
- software development
- tech life
---

This post is just quite a few thoughts on mobile apps and mobile app development, all mishmashed together. I don't claim to be a mobile app specialist, at best I've *dabbled* in them, but enough to form some opinions I guess?

### A Bit of History

My first exposure to mobile app development when I got pulled to help my then-company's then-fledgling mobile team with cleaning up the codebase for their iOS app. This was back in maybe 2011? It was one of those projects where some devs built a quick proof-of-concept demo using new technology, then management liked it and asked for new features and they kept adding new features haphazardly until there was just this huge unmaintainable mess of code. This isn't a knock against Objective-C or iOS development specifically or the dev team; the fact is they were new to the stack and were learning as they went while still trying to meet deadlines. I also spent some time reviewing the corresponding Android team's code as well. This was the bulk of my exposure to native mobile dev on iOS/Android. (This was before Swift, so I never got to experience that. Language looks neat though.)

Coming from a web dev background, I've always found the fragmentation of platforms annoying. Basically your effort gets multiplied by the number of platforms you have to support, and what would work well on iOS may not work well on Android and vice versa.

Later on, this concern was alleviated a bit with the rise of common frameworks that could publish to both iOS and Android. The first one I tried of these was React Native. I tried it for a small mobile project I did around 3-ish years ago. I wasn't tremendously happy with the experience. My mistake was probably diving head-first into React Native, when this was my first experience with React and front-end frameworks in general (something new to someone with [my jQuery background](/2020/02/old-web/)!), so a lot of concepts were new to me. 

To make matters worse, the React Native docs at that time seemed to assume some familiarity already with React, or at least similar frameworks like Angular. I had a bit of confusion with whether I should be using Expo or not, and how to eject, and it resulted in having to restart the project a couple of times. It was also my first encounter with NPM's dependency management, and that annoyed me a lot. A lot of the third-party dependencies I used back then were still immature too, so I often had problems with things like accessing the camera roll and so on. 

Nevertheless, it was experience, and the ability to publish cross-platform to iOS and Android was invaluable. I went on to use React Native as my go-to mobile framework I would recommend for other projects afterwards.

Recently, I had to do a UI revamp for that small mobile app I wrote three years ago, and I hadn't touched it for a while so I had some trouble with NPM trying to get it to run. In frustration, I gave up on it and decided to rewrite it in Flutter, of which I've heard good things. Flutter turned out to be great, and it took me just a little over two weeks, part-time to rewrite the app, probably slightly less effort than it took me to write it in the first place. I don't have enough experience yet to have a detailed review of Flutter, but I was generally much happier with the experience compared to React. Part of that may be I'm much more familiar with the mobile landscape now and have a better idea of what I'm doing, but I really did encounter much fewer points of friction and Flutter seems to have much better documentation. I believe it will be my first choice of frameworks moving forward.

### Not Everything Needs to Be a Native App

One of the things that annoys me about mobile apps is that people/companies unnecessarily want things to be native mobile apps when they would work perfectly fine as web apps. I can understand applications such as Uber may need numerous native functionality (GPS, timely notifications, offline functionality), so that's fine (although many of those things are available using modern browser APIs as well!). Things like online newspapers, forums like Reddit, and so on, are perfectly fine as normal web apps, and should stop prompting me to install their native apps when they detect I am on mobile. Granted that you may get a much better UX experience with a native app, but you also have to install it locally and grant it more access than what the browser's sandbox provides, and that feels like a tradeoff decision that the user needs to make, and not something to nag the user about constantly.

I guess part of it is that I grew up with the open web and have a significant bias towards it. In general, if I can just access an app via web, I will prefer that, unless the native app experience is vastly superior or otherwise necessary. And this focus on native apps can be bad for the web. This is apparent in apps like Instagram, which don't allow you to use their primary function - uploading images - on a desktop browser. I also had a similar discussion with a freelance client a few years ago, when they wanted to make a mobile app, but not a corresponding web platform, when all of the app's functionality was simple stuff that web could do easily. 

### Different Platforms

The differences in iOS and Android are particularly annoying to me as a developer, especially since I'm used to web development. With web, everything is open and standards-based, so you generally write everything using a single stack, and any reasonably standards-compliant web browser will work with the web app in a reasonably consistent way. (Granted, there will be browser-specific issues, but nowadays those aren't too common.) With iOS and Android, you have to test on both platforms extensively, and the build processes and distribution methods are different for each. Frameworks like React Native and Flutter lighten this load considerably, but you still really have to devote more time and resources to testing on the different platforms.

### Backward Compatibility

Okay, this one may be an unfounded concern of mine since I don't have much experience in the matter, but I have this worry that native mobile apps tend to *rot* more easily, and by *rot* I mean, get worse with time, as the mobile OSes upgrade themselves very rapidly. Unlike, say, Windows, which gets a new major version every few years, iOS and Android are constantly getting new versions and more importantly, deprecating APIs and adding new ones! Hence my worry that unmaintained, a perfectly functional app may become unworkable a few years down the line and no longer work on the latest mobile OSes. It's my totally unfounded belief that this is a significant reason why [more than 50% of my lifetime App Store purchases are no longer listed on the App Store](/2020/07/itunes-purchases/). (And also why I've pretty much disavowed making mobile purchases again.) Say what you will about Windows, but at least they have a pretty good record of backward compatibility when software I've written for Windows in the early 2000s is still very likely to run on Windows today. 

### Closed Platforms

Another issue I have with native apps is that I have been used to working on open platforms. Windows, for all its faults, is still an open platform, and anyone can write software for it and distribute it using whatever method they desire. And the web is even more open and standards-based (for now at least). For mobile, Android is mostly open, but iOS is mostly a closed platform.

Apple's tight control over the iOS platform has been in the tech news recently. First was [the kerfuffle with hey.com](https://www.theverge.com/2020/6/18/21296180/apple-hey-email-app-basecamp-rejection-response-controversy-antitrust-regulation) a few months ago, and more recently, [their removal of Fortnite and battle with Epic](https://www.macrumors.com/guide/epic-games-vs-apple/) due to Epic's objection to Apple taking a cut of all purchases on iOS.

As a mobile developer, the most annoying things about Apple's tight control over iOS apps are:

- that $100 annual fee for an Apple Developer account. If you're a 1st world developer, that cost isn't much, but if you're a young hobbyist developer who just wants to try making an app, it can be a significant hurdle. Google also charges you some token amount for Play Store access, but it's a one-time fee. 
- the fact that you need to use a Mac to publish apps to the App Store. This is another significant hurdle for hobbyist developers; Macs are typically very expensive computers. Granted Android development requires a beefy setup too, but at least you get a choice of platform for Android development.
- App store review can be unpredictable; sometimes things that were perfectly fine during a previous release are now flagged in the next review. It feels like you need to get lucky with the reviewer you get. And if the reviewer is unfair to your app, you may be out of luck unless you're a big company like Epic or [Wordpress that can raise a stink about it](https://www.digitaltrends.com/news/wordpress-developers-says-apple-wants-30-percent-of-its-profits-from-app-store/).

Many of the issues that could be levied against Apple for their monopoly over the App Store could be largely addressed if the platform allowed users to install apps via alternative methods, the same way Android does. I fully understand that Apple's tight controls enable a safer environment for naive end users (presumably, assuming they don't screw up), but more advanced users should be given the option to use alternative methods if they so choose. They can still flag apps installed via alternative methods as "potentially unsafe" and add hurdles to prevent less capable users from being easily tricked by malicious actors, (Android does this, I believe).

### In conclusion

I don't really have a point here. Maybe I just want everything to be open? I like open platforms lol.