---
date: 2021-05-23 23:27:00
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/106290687020646217
- type: twitter
  url: https://twitter.com/roytang/status/1396838282332303361/
tags:
- software development
title: Thoughts on Vue.js
---

I'm not big on modern frontend JavaScript frameworks (mostly because I think web pages should use as little JS as possible), but when I do find the need to use one, my weapon of choice is [Vue.js](https://vuejs.org/). I dislike React, but mostly because (a) my first experience with React was with mobile development using React Native for [mobile app development](/2020/09/mobile-app-dev/), which I generally don't like; and (b) I don't like Facebook, which backs React. I have no opinion on Angular.

Despite being my frontend framework of choice, I don't actually have that much experience with Vue beyond a few small projects each with a minimal number of screens / pages. That being said, I do have some thoughts, coming mostly from the POV of a developer [more used to the old-school ways of Javascript and web development in general](/2020/02/old-web/).

The entry point of course, is the [getting started guide on the Vue website itself](https://vuejs.org/v2/guide/), which walks you through most of the framework features. I have no concern about most of these; the features are explained well and I find most of the documentation quite good.

My issue is with how the site recommends to beginners to set up their Vue projects: via a script include from a CDN. When I first saw this guide, I assumed this was the standard, recommended way to build a Vue project, so this was how I did it for my first small project, a small demo site I needed to produce in a few days. Due to the short timeframe, I had decided to learn as I go. The component registration section of the guide also gives no guidance or recommendation on how to structure your components or projects, so I ended up with most of the components set up in a single JS file. (Admittedly, as a person with more than a decade of web dev experience, I should have at least split it up into several files, but time was short.) A technical person reviewing the code commented that I had implemented the frontend "in a very strange manner".

It gets worse when you try to install third-party components, which is a big feature of the ecosystem of these frontend frameworks. In my experience, most third-party components will only give instructions for installation via `npm` and a JS module system, neither of which are covered nor recommended by the beginner sections of the guide.

A few projects later, and I now know that I vastly prefer developing Vue projects as Node projects built using the scaffolding provided by [Vue CLI](https://cli.vuejs.org/), with the components implemented as standalone `.vue` files. The usage of these tools and methods are covered in the [Installation section of the guide](https://vuejs.org/v2/guide/installation.html) (which the "Get Started" link skips over) and the [Single File Components section under the Tooling section](https://vuejs.org/v2/guide/single-file-components.html) (which seemed like an advanced section a beginner is not likely to get into.) This method also makes installing third-party components much more straightforward. It's not even necessary to cover what tools like Webpack or Babel are doing, since those are largely abstracted away by the scaffolding.

Basically my main complaint is that the guide doesn't do a good job of transitioning from the introducing the beginner to the language specifics to introducing a recommended approach and tools for organizing more intermediate or complex projects. The method of using a script include seems suitable for little more than a single-page todo list webapp. I suppose the perceived shortcoming might be attributed to my background at least partially - I still tend to think like a developer using jQuery, and I don't default to thinking about Node applications when doing webapps.

That being said, I am overall happy with Vue.js and it's still my choice of frontend framework moving forward (should a frontend framework even be needed!) Although, maybe I should at least consider trying out / evaluating Angular so I can pretend to make a fair comparison?