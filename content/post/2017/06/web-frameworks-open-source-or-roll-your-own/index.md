---
author: roy
categories: []
date: 2017-06-22 04:19:27
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/162111375975/web-frameworks-open-source-or-roll-your-own
- type: twitter
  url: https://twitter.com/roytang/statuses/877764910188548096/
tags:
- Software Development
title: Web Frameworks -- Open Source or Roll Your Own?
type: post
url: /2017/06/web-frameworks-open-source-or-roll-your-own/
---

A while back I [wrote about my experience](/2016/10/coding-frameworks/) coding and maintaining an in-house web framework at a previous job. It was a full-stack web framework. We had libraries for front-end Javascript up to server-side database connections. And the entire stack was tightly coupled. But while the framework was serviceable, it was almost always behind modern trends in web development. I always felt like we were playing catch-up. And as a developer I wanted to widen my horizons and try out more things. So more than once I had discussions with higher management about using open source web frameworks in some projects.
 
Unfortunately, our in-house web framework already had a long history and most of the devs in our company were used to it. The company had tried using a different Java-based framework stack before. It was back in the days when things like Struts, Spring, Hibernate, etc were beginning to ramp up. It kind of ended in disaster -- that project ended up taking a lot of effort, had a lot of technical problems, and so on. I believe this gave the company leadership the impression that investing in other frameworks are not worth the risk and effort. It's a form of [Not Invented Here syndrome](https://en.wikipedia.org/wiki/Not_invented_here).
 
I admit there are some advantages to having your own in-house web framework. After all, all the popular web frameworks today started out in-house in some company and later they decided to release as open source. And many companies do fine using in-house frameworks. Using an in-house framework means full control over the behavior. And you can tailor the functionality and coding style to your internal processes. In fact it can be a good value add to your company if your in-house framework did something better or unique compared to open source ones.
 
But there are also significant advantages to using open source frameworks. Maybe I should have used some of these during discussions when I was there:
 
- With an open source framework, we wouldn't have to maintain the core functionality of the framework ourselves. We wouldn't have to maintain the full stack ourselves. We would only need to maintain any customisations and extensions we write for our own needs. For our in-house web framework, every so often we'd spend some effort to come out with a new version with incremental improvements. With an open source framework, we could instead redirect that effort to higher-value work.
- There's more learning material available online, and they don't have to be maintained in-house.
- There's a wider base of experience to draw from. For our in-house framework if you encountered a problem requiring deep framework knowledge, there were only a handful of high-level experts in the company. For an open-source web framework, that expertise is widely available on the internet through sites such as [Stack Overflow](https://stackoverflow.com/).
- Having knowledge/experience in established frameworks means your company can get more contracts. You can take on projects that use those frameworks. You don't have to spend proposal space trying to convince clients that your in-house framework is great. With open source frameworks you can reuse marketing copy by someone else!
- Working on well-known, established frameworks is better for your developers career-wise. It gives them more knowledge that could be transferable to other jobs. While this isn't a benefit to the company per se, it will make the company more attractive to developers. It even allows the flexibility of hiring developers experience with that framework.


There are some disadvantages too of course:

- As mentioned above, there is time and effort involved in learning a new open source framework. This effort is mostly for the experienced developers -- for new hires they will need to learn something regardless
- Having an in-house team developing your own framework means you have a core set of developers experienced in the full stack. Reliance on open source frameworks means most of your developers won't be familiar with the low level details.

In the end, there's no guarantee that using an open source framework will be painless or be better than developing one in-house. So I can understand the decision to stick with what you know. But for me as a developer, I feel that it's more rewarding to be exposed to different frameworks.

In fact I wrote this post because recently someone asked me what my "go-to web framework" was and I said I didn't have one. I'd rather be flexible enough to learn and work with any existing framework. In our industry where change happens quickly and can catch you by surprise, I think that flexibility is a much more valuable asset to have.