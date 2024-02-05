---
date: 2017-01-11 00:00:00
slug: when-i-work-on-a-new-software
source: quora
syndicated:
- type: quora
  url: https://www.quora.com/When-I-work-on-a-new-software-project-using-unfamiliar-technologies-its-extremely-difficult-to-get-start-what-should-I-do/answer/Roy-Tang
tags:
- answers
---

Someone on [quora](https://quora.com) asked:

> [When I work on a new software project using unfamiliar technologies, it's extremely difficult to get start, what should I do?](https://www.quora.com/When-I-work-on-a-new-software-project-using-unfamiliar-technologies-its-extremely-difficult-to-get-start-what-should-I-do/answer/Roy-Tang)


The activity of building software is fundamentally about breaking things down into smaller tasks until they are small enough for you to write them in code. Look at your entire system. Study your requirements. Figure out the steps that have to be executed, the things that the system needs to do. Then iterate on each step and break it down further until you feel that you understand it well enough to implement it.

I find it’s often easy to follow the flow of data as it travels through your system. (Your mileage may vary - or maybe you favor a different approach.) Don’t think about analyzing millions of emails. Think about analyzing one email. Where does it come in? Where is it stored? How does the system process it? Where is the processed data stored? Where is it sent to afterwards.

If you still find yourself struggling to move forward, try building a prototype. Just a small proof-of-concept. Implement a small part first. Maybe get the email from somewhere? Don’t worry about authentication or security or anything, just get that data flowing from one end to the next. You’ll discover things you hadn’t considered and you’ll learn some things you did right and some things you did wrong.

Then prototype the next step.

Now you have two prototypes. Link them together. Integrate them. Then prototype the next step. And the next.

Now you have all these prototypes linked together and moving data and processing it from end to end.

Throw out all the prototypes.

Go over the lessons learned and do another iteration.

Repeat until satisfied.