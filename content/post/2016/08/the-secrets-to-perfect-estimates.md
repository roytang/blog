---
author: roy
categories:
- Software Development
date: 2016-08-25 01:30:43
title: The Secrets to Perfect Estimates
type: post
url: /2016/08/the-secrets-to-perfect-estimates/
---

Estimation is hard. Estimation has long been the bane of many software developers and software development projects. But there are two secret ways to be able to produce perfect estimates for software development work all the time! One is dependent on talent, and the other is dependent on technology

  1. Psychic precognition, i.e. be able to predict the future
  2. Have a time machine, so you can go back in time and tell yourself how long the work would have taken

Such precognition is necessary to have perfect estimates because of all the unknowns present at the start of a software project. Unknowns include imperfect requirements or design, unknown user needs, future changes that may happen during the course of the project, unforeseen technical challenges, and so on

In the absence of the ability to break the laws of causality however, the only time we can have perfect estimates is at the end of the project! Before that, we are sadly restricted to imperfect estimates. In reality, **the best estimates will still always be an educated guess**

Okay, for real now: there are two ways to handle the risks associated with poor estimates, and for most projects both will be necessary.

The first is **to plan around inaccurate estimates. **This means that your planning acknowledges that estimates will often be inaccurate and building a sufficient amount of loose or buffer time in your scheduling to accommodate any variance. Less enlightened managers and executives will hate this, especially anyone who comes from a world like manufacturing where the rate of production is extremely well-known and predictable. They will view any kind of schedule buffer as some sort of justification for slacking off. As a software developer, you will have to deal with these sorts of people throughout your career. It will be part of your job to work with them to manage the schedule, manage their expectations, and get them to understand that while the software development process is in many ways an engineering process, there are still numerous uncertainties that will not resolve themselves until you [find the right arrangement of code][1]

The second is **to learn how to make better estimates**. "Better&#8221; here doesn't necessarily mean "more accurate&#8221;, but rather "less likely to be very far off&#8221;. There are numerous books already written on this subject (I recommend [Steve McConnell's Software Estimation: Demystifying the Black Art][2]**_ _**if you can afford it), but basically the advice can always be summed up as: **use data from previous experiences to predict the likely effort needed for future tasks**.

It's usually best if you are able to draw upon your own experiences since often the actual amount of work needed will be specific to the developer's experience, for example: "It took me N days to do a similar task before, so I think I can do it in N+2 days. The other guy doesn't have experience with this stack, so I guess that he can do it in N+7 days&#8221;

In the absence of your own direct experience, you can look to either expert opinion (consult someone else who has more experience with the subject and ask him for an estimate, and compensate accordingly for any difference in skill/knowledge) or use some sort of numerical model. Such models will typically rely on some sort of metric to measure the size of the system being developed, then use historical data to predict how much effort a system of this size would require. An example of such models is [Function Point Analysis][3]. Different models will tend to have their own advantages and disadvantages &#8211; for example, I've found from personal experience that Function Point Analysis can be greatly inaccurate if there is a lot of technical risk in the proposed system &#8211; so it would still be wise to make planning adjustments accordingly and not just follow the model blindly

One last thing that software developers need to note with regard to estimates: if you know that you have made a good estimate, that it is already as accurate as it could possibly be: **do not allow anyone to pressure you into providing a different estimate**. Giving in to such pressure does no one any good: it only puts the project at increased risk, and it puts your own credibility into question. Such pressure often comes from management or clients as a result of schedules or deadlines, something that I will talk about in a later post.

In the end though, all the best practices will be for naught unless you understand the fundamental truth: **there is always a chance for estimates to be inaccurate**. No amount of planning or best practices can completely mitigate that risk &#8211; unless of course you have either a precognitive crystal ball or time machine!

 [1]: http://roytang.net/2016/08/programming-is-finding-the-right-arrangement-of-code/
 [2]: https://www.amazon.com/Software-Estimation-Demystifying-Developer-Practices-ebook/dp/8178531038/
 [3]: https://en.wikipedia.org/wiki/Function_point