---
date: 2016-05-02 00:00:00
slug: what-is-the-mindset-that-every
source: quora
syndicated:
- type: quora
  url: https://www.quora.com/What-is-the-mindset-that-every-developer-should-have-when-developing-new-features-and-maintaining-old-features/answer/Roy-Tang
tags:
- answers
title: What is the mindset that every developer should have when developing new features
  and maintaining old features?
---

Someone on [quora](https://quora.com) asked:

> [What is the mindset that every developer should have when developing new features and maintaining old features?](https://www.quora.com/What-is-the-mindset-that-every-developer-should-have-when-developing-new-features-and-maintaining-old-features/answer/Roy-Tang)


When developing new features, make sure to write to clean, maintainable code that future maintainers won't have a problem with. If you can write unit tests, do so.

When maintaining old features, it's kind of like being a doctor: first, do no harm. Perform the minimum changes necessary to implement your changes to minimize the chance of breaking existing behavior. But still try to avoid writing terrible code. It helps if the existing feature has unit tests