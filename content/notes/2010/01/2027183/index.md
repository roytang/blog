---
date: 2010-01-08 11:21:43
reply_to:
  label: '''How to express &quot;never&quot; with java.util.Date?'' on stackoverflow'
  name: deamon
  type: stackexchange
  url: https://stackoverflow.com/questions/2027171/how-to-express-never-with-java-util-date
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/2027171/how-to-express-never-with-java-util-date/2027183#2027183
tags:
- java
- date
- coding-style
---

I would just choose a far-future date as the value for the constant NEVER. Then to check for deletion/expiry, just compare against NEVER.