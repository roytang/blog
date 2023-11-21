---
title: "The August-September Bug"
date: 2023-11-21T14:01:11+08:00
tags:
- software-development
---

For some reason or another I was reading old chat logs, and I came across this convo about a bug I encountered in 2014 that was amusing enough to share. So this is yet another [Tale from the Old Web](/2020/02/old-web/).

I was complaining that I had to work after hours because there was some issue in the deployed production environment on August 1st. It took me a while to check but I eventually figured out that it was a bug that happens only on IE in August and September, which was like WTF!! (Yes, people still used Internet Explorer at the time!)

It turned out to be a problem with JavaScript date parsing because JS's `parseInt` used to have a weird behavior when parsing numbers that start with a leading 0, treating them as octal! This meant that:

- `parseInt("07")` -> 7
- `parseInt("08")` -> 0
- `parseInt("09")` -> 0
- `parseInt("10")` -> 10

To top it off, we had coincidentally deployed this code in October of the previous year, so it was able to go a whole 10 months without encountering this issue and August 1st 2014 was the first chance for the problem to be detected!

I found [a Stackoverflow post from 2009 complaining of this exact same problem](https://stackoverflow.com/questions/850341/how-do-i-work-around-javascripts-parseint-octal-behavior). The comments in that post indicate the JS standard was eventually updated to remove this behavior so modern browsers no longer have this issue, thankfully.