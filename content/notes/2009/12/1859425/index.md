---
date: 2009-12-07 11:27:02
reply_to:
  label: '''triggers statement level atomicity'' on stackoverflow'
  name: user226276
  type: stackexchange
  url: https://stackoverflow.com/questions/1859411/triggers-statement-level-atomicity
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1859411/triggers-statement-level-atomicity/1859425#1859425
tags:
- oracle
- transactions
---

It means that any single SQL statement you run is atomic in nature - it will either succeed completely or fail completely. If your SQL statement fails, and triggers that would have run as a result of that SQL statement will fail as well.