---
author: roy
categories: []
date: 2016-11-03 01:30:18
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/152666290735/software-development-feedback-loops
- type: twitter
  url: https://twitter.com/roytang/statuses/793988761541611525/
tags:
- Software Development
title: Software Development Feedback Loops
type: post
url: /2016/11/software-development-feedback-loops/
---

The software development process is already difficult mainly because a lot of it so imprecise. Requirements are often only vague wishes that the client has, with no regard to the sheer number of instructions needed to implement those requirements. Throughout the entire process it's important to use feedback loops to determine whether development is on the right path. And like all feedback loops, their effectiveness often hinges on how quickly we are able to turn around and give and incorporate feedback into future iterations

Feedback loops happen whenever someone gets to review something of course. Prototyping with the client is the most basic form of feedback loop. Building a quick prototype, then showing it to the client, seeing what works and what doesn't and what the clients wants to change, then iterating into the next prototype -- all of these reduce the risk that we are not building the correct thing in the first place. Similar feedback loops appear whenever someone reviews your design or your code or your documentation

For me personally, the more important feedback loop happens at the coding level. It is very rare for a dev to code to everything in a program (no matter what size) in one go. Instead, programs are almost always built incrementally, in a loop of code->build->test->back to coding again. Thus it is very important to make sure that this build is as tight and as optimized as possible

One of my major annoyances with working with Java and Eclipse over the past ten years is that even though Eclipse has that "build automatically" feature that should provide instant feedback, in practice there can be significant lag time while the application is built and for web applications, often your local server will need to be restarted to reflect the changes. Given how often devs iterate while coding, even a few seconds of lag time in each loop is already a minor annoyance. Build times of one minute or more will be deadly to productivity, often taking the dev out of the much-desired "flow zone". Thus you have to optimize this cycle as much as possible -- with Java/Eclipse/Tomcat, that meant disabling all unnecessary build validations, reducing your application size by removing redundant code and dependencies, and so on. Hardware optimizations are also an option -- I was really happy when the company finally decided to spend money on SSDs for the devs (money well spent)

This problem also happens in the bigger loop of devs coding -> build deployment -> verification by the testing team -> send bugs/comments back to devs for fixing. Often the main bottleneck is the build deployment, so you want this process as fast as possible as well. I've been on projects where we had the misfortune to have the build process go as long as 2 hours at a time. After some optimization, we were able to trim it to around 30-40 minutes, but this is still pretty bad. During hard deadlines when you have to deliver something the next day, this loop can cycle many, many times, and long build times will be the difference between whether your team merely does a bit of overtime or have to stay until morning. Unfortunately it can be a difficult problem to address, and the fact that the problems only become urgent during the times of greatest schedule pressure does not help. I believe that once you have a large enough system and dev team, having people dedicated to maintaining and optimizing the build system quickly becomes a necessary evil