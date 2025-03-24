---
date: 2016-03-01 08:16:07
source: twitter
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/704580965784354817/
tags:
- programming
- javascript
title: Fun with Javascript Dates
repost_source:
  name: recursecenter
  type: twitter
  url: https://twitter.com/recursecenter/status/704429884374958080/
---

1/ In honor of leap day, here are some facts about JavaScript date parsing:

---

2/ All dates are secretly times and have time zones. Date strings are parsed at midnight UTC and then converted into your local time zone.

---

3/ This means that `new Date('2016-02-29')` run on a computer in EST will return a date representing 2016-02-28 (one day before!) at 7pm.

---

4/ With the exception of RFC2822 and ISO 8601 dates, date parsing is implementation specific.

---

5/ In Firefox and Safari, `new Date('2016-2-29')` returns `Invalid Date`. In Chrome, it returns a date representing midnight in local time.

---

6/ This means that in Chrome, `new Date('2016-2-29')` and `new Date('2016-02-29')` may return *different* dates depending on your timezone!

---

7/ You can tell if something is an `Invalid Date` by calling `toString` on it and comparing it to \"Invalid Date\"...

---

8/ ...or you can call `getTime` and see if it's equal to `NaN`. Of course, `NaN` isn't equal to `NaN`, but this is really IEEE 754's fault.

---

9/ Parsing dates with ordinals (`new Date('February 29th, 2016')`) return `Invalid Date`.

---

10/ Days of the month (found with `getDate`) start counting at 1, but months of the year (found with `getMonth`) start counting at 0.

---

11/ This means `new Date('2016-02-29').getMonth()` returns 1, not 2.

---

12/ In Safari and Firefox, parsing dates without a year (`new Date('March 1')`) return `Invalid Date`.

---

13/ In Chrome, dates parsed without a year are assumed to be in 2001.

---

14/ The More You Know™

---

That was our first ever tweetstorm. Are we doing this right?

---

15/ A few extra thoughts on today's wat-storm:

---

16/ We didn't mean to imply that JavaScript is somehow worse than other programming languages because of how it parses dates.

---

17/ These funny date parsing edge cases exist because JavaScript has a special place in the architecture of the web.

---

18/ JavaScript can't be changed in backwards incompatible ways because every version of every browser is basically deployed permanently.

---

19/ You find issues like this every time that legacy software has to be supported, especially when it's users are other programmers.

---

20/ JavaScript is the ultimate version of this: legacy software that's deployed literally everywhere.

---

21/ Plus, the world has changed since these APIs were created. People want to do new things with JavaScript that they couldn't do before.

---

22/ Imagine if you had one shot to make a decision that couldn't ever be changed and had to stand up for the next 20 years.

---

23/ Programming is complicated, and there is always more than meets the eye. Exploring edge cases can be lots of fun, and even funny!

---

24/ It's fun to chuckle at unintended results of decades old design decisions, but it's better to do it with curiosity than animosity.

---

25/ There's lots to learn in examining which design decisions hold up over time and which run into trouble.

---

26/ Happy programming and happy leap day!

---

PS/ There are even reasons that `NaN` isn't equal to itself. We swear!

---

PPS/ Design is all about trade-offs after all.