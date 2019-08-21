---
categories: []
date: 2019-08-20 00:00:00
tags:
- devnotes
- software development
title: "Devnotes: TT Miniproject (Django Rest Framework, Unit Testing, VueJS, Geocoding, Nightwatch e2e Testing)"
type: post
url: /2019/08/devnotes-tt-miniproject
aliases:
- /2019/08/devnotes-tt-miniproject-django-rest-framework-unit-testing-vuejs-geocoding-nightwatch-e2e-testing/
---

I recently found myself doing a really small project as sort of a proof of concept/demo for a potential client. It often seems that it might be a waste of time to do something like this since you don't know if the project will actually push through or maybe the client will want something else. To kind of hedge my bets a bit, I decided to take the opportunity to try out some new technologies so that no matter what I at least learned something from all of this. (What is life if not learning?)

**Django Rest Framework**. I've been on projects using DRF before, but it's my first time building a full CRUD-style API from scratch using it. There is a little bit of a learning curve when it comes to views and serializers, but for the most part it's straightforward. I did enjoy how the framework has out of the box support for the most common REST API scenarios, and there are available backends for different authentication methods. I used JWT Authentication, which isn't part of the library by default, but already had a pretty good implementation available elsewhere.

**Python Unit Testing**. I have dabbled [a little bit with Django's Unit Test framework before](/2019/02/triviastorm-text-and-answer-parsing/), but not having worked with any company that does TDD I've never tried doing it the "test first" way. For reference I used an online book: [Test Driven Development with DJango](https://www.obeythetestinggoat.com/book/part1.harry.html). I actually enjoyed the exercise, perhaps a little too much. My impression of TDD has always been that the value lies in how much courage it can give the developer - the courage to try new things without worrying about whether you have broken something that was working before. This support came in handy while I was trying to figure out some issues with DRF especially around permissions etc. Really helpful for backend APIs like this.

**Python Social Auth**. The proof-of-concept needed some social media logins. I used [Python Social Auth](https://github.com/python-social-auth/social-core) for this, really straightforward library with good documentation and supports a lot of backends. I ended up using Twitter and Github OAuth as those were the simplest to implement.

**VueJS**. The proof-of-concept needed to be a single-page app, so that meant a bunch of Javascript was needed. I willingly admit I'm still behind with the latest web frontend frameworks and trends. In my head I'm still living in a jQuery world. I dabbled a bit with React when trying out [React Native](/2019/07/upgrading-a-react-native-project/), but I wasn't fond of it. For this project I decided to use [VueJS](https://vuejs.org) since I had skimmed through their documentation before and things seemed cool. I used it mostly for the dynamic parts and the data binding. I didn't get too far into using components, my VueJS app was a huge monolith, which is apparently is frowned upon when using these frameworks lol. (Someone familiar with VueJS who looked at the code said it was "very strange"). I have barely scratched the surface of this framework, I will probably need to build something a bit more involved with it to get a better grasp. I will say that I enjoyed the VueJS syntax/structure better than React.

**Google Maps API and Geocoding**. The miniproject had some components that required me to show stuff on a map and do some geocoding, so I had to set up the API for that. Google's documentation is fairly good here. One thing I didn't expect is that you need a Google Cloud account with a billing method in order to access the API. My understanding is I wouldn't be charged for anything since I was just using the free tier, I hope that was accurate.

**Nightwatch e2e Testing**. I've had some projects with end to end testing before, mostly via scripts or Selenium, but it's my first time trying out one of these end to end testing frameworks by writing the scripts myself. I chose to go with Nightwatch, it was reasonably strightforward and worked on Mac and Windows. One thing I will note that initially gave me problems during set up is that using the ChromeDriver can be a bit finnicky on Windows. You have to specify the actual location of the executable in your nightwatch.json, like so: `"server_path": "node_modules/chromedriver/lib/chromedriver/chromedriver.exe",` instead of just the `node_modules/.bin/chromedriver` the documentation implies.

All in all the mini-project didn't take much work - maybe 2-3 mandays of effort at most, and I did learn a lot from it, so no matter the outcome it was already a win.