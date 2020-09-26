---
author: roy
categories: []
date: 2016-10-13 01:30:27
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/151729262325/coding-frameworks
- type: twitter
  url: https://twitter.com/roytang/statuses/786380194185617408/
tags:
- Software Development
title: Coding Frameworks
type: post
url: /2016/10/coding-frameworks/
---

For the better part of my software development career so far, I've had the doubtful pleasure of being one of the devs using and maintaining our in-house web development framework. Framework coding is a bit different from the actual application development. At the core it's a simple idea: you have a whole bunch of code that helps do programming tasks that you expect will often be necessary in a certain set of projects, so you write that code with the intent of reusing it across multiple projects. For a web development framework, those tasks will be things like handling request parameters, form validation, form to database mapping, and so on. You can have frameworks for a variety of domains too, not just web development. There are mobile development frameworks, and game development frameworks, and so on

Typically, a framework is developed alongside a project using that framework (to save on costs), but the framework's objective of code reuse may not always align with the project's objectives of "get stuff done already".  Investing in reusable code often means there will be a bit more work done as you start up, to make sure that the code is flexible and reusable enough for future projects, but when your schedules are tight, these concerns may become secondary and you will be tempted to write in some substandard code that you will "just refactor later". Technical debt by itself already tends to be a problem, it gets worse when it's technical debt in framework code since you're going to carry that across multiple projects, so be wary when sacrificing the quality of framework code for the sake of one project

Another thing is that you need to be more aware of separation of concerns, especially if the application development team overlaps with the framework development team. The idea of a framework is that it should be handling the most common tasks in a typical project, but when you're embedded in a project there will be a tendency to try to handle even those special cases that are unique to the project. The danger here is that parts of the project domain will start seeping into your framework code because of requests by devs to provide a way to handle so-and-so scenario. And you end up with a situation where a few years later you ask, what the hell is this code doing, and the answer is that it was something needed by a developer three projects ago

Speaking of separation of concerns, I've also found that devs working on framework code need to be more cognizant of things like that, meaning they have to be able to write good, modular, flexible code that can be easily reused for future projects. That means you need a solid understanding of coupling, separation of concerns, interfaces, and so on

Flexibility is particularly important, as I've found in one of my later projects that was sold to multiple clients. Different clients will have varying needs and wants, so making sure your code is flexible and configurable enough to cater to a wide variety of needs. When you're writing framework code, your clients are other developers, all the more reason to present an API that is consistent and flexible enough for their use. If you expect your framework to be used as the baseline for multiple projects, you will need to make sure it can cater to a wide variety of projects

That flexibility will have limits though. Frameworks will tend to require a "certain way of doing things", meaning devs will have to do some adapting to be able to use it. For example, if you post about an out of the box approach on a Ruby on Rails forum, you might get some replies about how "that's not how things are done in Rails". In practice, it's impossible for a framework's maintainers to anticipate all possible future needs of different projects, and developers will need to be able to build on top of your framework or even extend it as necessary. Instead of wasting effort trying to anticipate everything, framework developers should provide an easy, default path for the most common things, but be flexible enough to allow divergence for things the framework doesn't support

Another thing to pay attention to is how tightly coupled different components of your framework are. Is the framework still useful if you have to support a third-party component to replace some functionality later on? What if you need to use a different database vendor? What if the client requires a different way of storing resource strings? You don't have to support all the different possible implementations up front, but it would be wise to leave room for a future extension or plug-in to be easily swappable with the framework's components

The most important thing to keep in mind is that the objectives of a framework are two-fold: (a) be reusable across multiple projects; (b) make it easier for developers to do the most common tasks in the chosen domain. Anything else beyond that, tread carefully