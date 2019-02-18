---
author: roy
date: 2019-02-20T13:56:56+08:00
type: post
categories:
- Software Development
- Philippines
tags:
- reddit
title: "Reddit PH: Software Dev Q&A"
type: post
---

I had some free time the other day so I randomly decided to post in the [PH subreddit](https://www.reddit.com/r/Philippines/)'s regular afternoon [random discussion thread](https://www.reddit.com/r/Philippines/comments/arsxjg/afternoon_random_discussion_feb_18_2019/), asking for [questions about software development](https://www.reddit.com/r/Philippines/comments/arsxjg/afternoon_random_discussion_feb_18_2019/egpog87/). I ended up typing some longish answers, I thought I'd copy them over to the blog in case anyone was interested. TBH I meant more like StackOverflow type questions with specific technical problems, but I ended up answering mostly career-related questions, which is fine, but disclaimer: I don't claim to be an expert, these are just my opinions on things.

> [capybara_c0de](https://www.reddit.com/r/Philippines/comments/arsxjg/afternoon_random_discussion_feb_18_2019/egpolbt/): project/s junior devs should include in his/her portfolio? 

I've technical interviewed a lot of entry-level/junior level devs. Honestly any kind of project would probably be okay, as long as you're able to explain what role you played, bonus points if you're able to discuss technical decisions you made (why was this choice made, and why not this other one etc) or specific technical challenges you were able to overcome. That kind of stuff. Really, if you can demonstrate that you really worked on a project (and not just coasted by on teammates help etc), you're already an above average interview.

Entry-level candidates might have more trouble since they often won't have a portfolio, but the quality of candidates is a bit low locally, so if you can demonstrably do simple stuff like loops, recursion, stacks, etc you're probably already an above average interview. Bigger companies will have written exams to filter out peeps who can't do that though.

More random technical interviewing tips, even though you didn't ask for that: being able to communicate well is a big plus, mandatory even. Lack of confidence makes the interviewer worry that you don't really know what you're talking about. Sometimes I'll slip in something I know to be wrong "Diba pag cinall mo yan, ganito mangyayari?", and see how the candidate reacts

> [veeequalseyeare](https://www.reddit.com/r/Philippines/comments/arsxjg/afternoon_random_discussion_feb_18_2019/egpp2yr/): How many years of experience do you have? And what's your basic salary?

Why do people keep asking about salary? That's not really a programming or software dev question. I am a freelancing consultant at the moment, so I can't really give a simple answer to that anyway (it's almost always "it depends")

I will answer the experience one - 15ish years in the industry (yeah, I'm old).

Edit: Also, there is a high range in the salaries of software devs in this country (not sure if the same elsewhere, probably), because:

- some people are better at selling themselves than others
- some devs are way better than others (and thus are more valuable)
- each dev's career path and growth is often unique, so it's difficult to compare, especially once you rack up some years of experience

i.e. for a given number of years of experience, the salary band will be quite wide. 

I get that when you're starting out, salary is a big deal, but honestly if you're a decent enough programmer, you can get into any place with above average salary. You can grow your salary a bit faster by hopping jobs every so often, but too many hops looks bad on a resume. 

Anyway, my advice is that once you get to a decent salary range that is good for you (i.e. you're not starving), focus less on comparing yourself to other people, and more on increasing your own value and managing your work/life balance. Money isn't everything, beyond basic survival.

> [getmeoutofherealive](https://www.reddit.com/r/Philippines/comments/arsxjg/afternoon_random_discussion_feb_18_2019/egpqfdb/): Anong advice ang maibibigay mo kapag gusto magcareer shift? Ex: IT Support to Development/Programming.

Shifting careers from IT support isn't an unreasonable proposition, but you need to already know your stuff before going in for interviews. You will also still need some basic level of programming knowledge. A lot of things you'll need can be learned on the fly/on the job (like usage of specific languages or tools or libraries), but you need a good basic foundation to build on.

If I'm interviewing someone coming from a nonprogrammming background, I'll basically be treating her as an entry-level candidate. You will need to be able to justify why I should hire you over say, a fresh grad who still remembers his java programming from his college days. The interviewer will need to know you're not trying to BS your way into the position. Having some work you can show off (side projects or whatever) can be a big help. You can also cite anything you're doing in your current domain that might show off some related skillset. Like, if you did some minor scripting to gather support statistics, something like that? IDK if IT support people do that kind of stuff. See my other interview tips in the other answer elsewhere in this thread too.

> [captainph](https://www.reddit.com/r/Philippines/comments/arsxjg/afternoon_random_discussion_feb_18_2019/egpquyz/): web services in web development, ELI5 please

Wait, what do you mean? Web services are like web pages, except they're endpoints that usually do only one thing and return some machine readable format like JSON or XML instead of HTML that can be rendered and viewed by a human in a browser. Basically you send them an HTTP request and they maybe do some processing and spit back an HTTP response that you consume.

Some types are simpler than others - REST-based web services are usually very simple for example, and can sometimes be invoked directly via the browser address bar. Some follow more complicated protocols (SOAP) that support things like authentication and signing and so on.

Web services are developed the same way as normal web pages, with the usual backend processing and stuff (but there are some frameworks to make this easier, especially for complicated protocols like SOAP), but the client program (the one calling the web services) does not have to be another web application. It can be a mobile app for example.

One of the typical usages would be third-party integration. For example, Philhealth I believe currently has some kind of e-Claims web services in development (maybe? IDK the current status), where the idea is to allow third-party systems to submit Philhealth claims electronically. The idea is that individual hospitals have their own medical records systems, those systems can send HTTP requests to the e-claims web services in order to for example check whether a patient is eligible for a claim.

Ok, sorry I know that explanation doesn't really work for a 5-year old lol

> [acequeen21](https://www.reddit.com/r/Philippines/comments/arsxjg/afternoon_random_discussion_feb_18_2019/egptmll/): Do you have plans going abroad? Either work temporarily or move permanently. Why or why not?

Nah, I like living here, in spite of everything, and I'm programming avails me a good living naman. I've worked abroad on short stints (pinadala ng company), but TBH, I had never even considered leaving the country long-term, but I started looking into it after 2016. Hassle for me na ma-uproot and to try to start over elsewhere.

