---
date: 2019-02-18 06:53:56+00:00
reply_to:
  label: a comment by [deleted] on 'Afternoon random discussion - Feb 18, 2019' on
    /r/Philippines
  name: ''
  type: reddit
  url: https://reddit.com/r/Philippines/comments/arsxjg/afternoon_random_discussion_feb_18_2019/egpquyz/
source: reddit
syndicated:
- type: reddit
  url: https://www.reddit.com/r/Philippines/comments/arsxjg/afternoon_random_discussion_feb_18_2019/egprpiq/
tags:
- Philippines
---

Wait, what do you mean? Web services are like web pages, except they're endpoints that usually do only one thing and return some machine readable format like JSON or XML instead of HTML that can be rendered and viewed by a human in a browser. Basically you send them an HTTP request and they maybe do some processing and spit back an HTTP response that you consume. 

Some types are simpler than others - REST-based web services are usually very simple for example, and can sometimes be invoked directly via the browser address bar. Some follow more complicated protocols (SOAP) that support things like authentication and signing and so on.

Web services are developed the same way as normal web pages, with the usual backend processing and stuff (but there are some frameworks to make this easier, especially for complicated protocols like SOAP), but the client program (the one calling the web services) does not have to be another web application. It can be a mobile app for example.

One of the typical usages would be third-party integration. For example, Philhealth I believe currently has some kind of e-Claims web services in development (maybe? IDK the current status), where the idea is to allow third-party systems to submit Philhealth claims electronically. The idea is that individual hospitals have their own medical records systems, those systems can send HTTP requests to the e-claims web services in order to for example check whether a patient is eligible for a claim. 


Ok, sorry I know that explanation doesn't really work for a 5-year old lol