---
date: 2019-07-31 11:51:34
repost_source:
  name: Joe8Bit
  type: twitter
  url: https://twitter.com/Joe8Bit/status/1156312965265707013
source: twitter
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1156532855171760128/
tags: []
title: 'Joe Pettersson: Unsubscribe'
---

*(Originally shared via [LibyaLiberty](https://twitter.com/LibyaLiberty/statuses/1156530354523652096/), who said:)*

> Best email unsubscribe button story i've ever come across. 

---

I saw a tweet asking why sometimes when you unsubscribe from an email list it says it can ‘take a few days’. Buckle up, as I have a RIDICULOUS story about this happening in The Enterprise...

---

There’s a bank. Let’s assume you’ve heard of them, in fact if you’re in the UK there’s a 10 in 1 chance they’re YOUR bank. I was an overpayed ‘consultant’ at this bank.

---

This bank sends marketing emails. There’s a little ‘unsubscribe’ link at the bottom of the mail. People often click it.

---

When they do it calls an antique web service that runs ‘somewhere’ at the bank. Honestly, it took me 3 weeks to find out where.

---

This web service sends an email to an internal email address every time it’s clicked. This happens 100s of times a day.

---

This email was originally sent to an individual. They left the bank five years before.

---

This mail address is now forwarded to an email group. They couldn’t change the address as it’s hard coded and they don’t have the code that was used to compile this Java 6 service.

---

This email group is monitored by two people in the banks offshore centre in Hyderabad. They worked super hard and always SMASHED their job; but holy crap it was soul crushing.

---

When I spoke to them via VC they had the Enterprise 1000 Yard Stare. They’ve banged their head against this thing for YEARS and it’s NEVER changed.

---

When they get a mail, they need to run a SQL query to see if that mail address is associated with a customer (which results in one process) or if it’s not (which results in a separate process)

---

If they’re a customer, they execute another SQL query that updates a customer record in a type of ETL staging area. Every one of these changes is reviewed (at 4pm UK time) by a team in an office in Scotland. If they approve it, it gets executed 24 hours LATER at 4pm

---

If this person is NOT a customer, they add it to an excel and email it (just before they go home) to a marketing team in Swindon.

---

The marketing team use tea leaves and chicken bones to decide if this person is a ‘high vale prospect’ (their ‘SLA’  is ‘within 48 hours’). If they AREN’T they add the address to another excel and email the original team in India. They use their ‘process’ to execute a SQL query

---

If they ARE a ‘high value prospect’ the marketing team MANUALLY sends an email asking if they REALLY REALLY want to unsubscribe? It looks like an automated email, but it ain’t.

---

If they answer yes (they had to literally reply ‘YES’) then the team in Swindon send a THIRD excel back to India and the ceremonial SQL queries are run.

---

IIRC this took FOUR BUSINESS DAYS on average. On average ~700 people unsubscribed a day and ~70% of those were deemed ‘high value prospects’.

---

There’s another story about how the two people from India joined our engineering team and became the Product Owners for the thing that replaced it 

---

They were also two of the nicest, most caring, hardest working people I've ever had the opportunity to work with. They were the reason why this awful corporate clusterfuck of a process worked so 'smoothly' for all those years.

---

If those things didn't make an ideal, A+ candidate to own the replacement system I don't know what did.

---

They eventually moved to the UK, and one of them is now in charge of a team of 40+ people!

---

Why had they been ignored and overlooked for so long, and why every bit of their work needed to be 'checked' by a team in the UK… you'll need to fill in the gaps on that one-oh wait no, it was prejudice against offshore workers and a light sparkling of racism! 

---

My consigliere have informed me I should take advantage of this sudden attention to mention @permutive is hiring! We’re like, cool to work for and stuff "