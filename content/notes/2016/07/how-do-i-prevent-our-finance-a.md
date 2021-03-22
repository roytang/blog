---
date: 2016-07-10 00:00:00
slug: how-do-i-prevent-our-finance-a
source: quora
syndicated:
- type: quora
  url: https://www.quora.com/How-do-I-prevent-our-finance-accounts-to-be-seen-by-programmers/answer/Roy-Tang
tags:
- answers
---

Someone on [quora](https://quora.com) asked:

> [How do I prevent our finance accounts to be seen by programmers?](https://www.quora.com/How-do-I-prevent-our-finance-accounts-to-be-seen-by-programmers/answer/Roy-Tang)


Developers will generally have access to code, not data. They will implement, test, and debug the system using dummy/test data and not actual live data. I worked in an environment of offshore development where the actual client management was done by our colleagues in another country and the development team had no access to their data at all. It was often a pain especially when the software passes all our tests but new problems emerge once deployed to the client since their data may contain cases not expected by the system.

Some developers *may* have occasion to access the data, especially those involved in the deployment operations or live-site maintenance and debugging. There is no preventing such developers from having access as it is necessary for their work. Most companies will attempt to have some sort of legal and/or informal agreement requiring the developer to agree to keep confidential information confidential before they can be assigned such responsibilities.