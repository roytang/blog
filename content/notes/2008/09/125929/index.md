---
date: 2008-09-24 07:57:10
reply_to:
  label: '''Versioning Database Persisted Objects, How would you?'' on stackoverflow'
  name: Chris Vest
  type: stackexchange
  url: https://stackoverflow.com/questions/125877/versioning-database-persisted-objects-how-would-you
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/125877/versioning-database-persisted-objects-how-would-you/125929#125929
tags:
- database
- database-design
- versioning
---

You'll need a master record in a master table that contains the information common among all versions.

Then each child table uses master record id + version no as part of the primary key.

It can be done without the master table, but in my experience it will tend to make the SQL statements a lot messier.