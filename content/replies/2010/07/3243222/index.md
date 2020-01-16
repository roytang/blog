---
date: 2010-07-14 03:29:29
reply_to:
  label: '''Oracle Insert with mutli-valued column'' on stackoverflow'
  name: Jared
  type: stackexchange
  url: https://stackoverflow.com/questions/3243055/oracle-insert-with-mutli-valued-column
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/3243055/oracle-insert-with-mutli-valued-column/3243222#3243222
tags:
- sql
- oracle
- insert
---

Try something like this:

    insert into onTeam(date, player, teamName) 
    select 'newDate','Matt Holliday', teamName 
    from onTeam where player = 'Matt Holliday'