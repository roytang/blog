---
date: 2010-01-06 13:12:35
reply_to:
  label: '''Mysql: Which to use when: drop table, truncate table, delete from table''
    on stackoverflow'
  name: gameover
  type: stackexchange
  url: https://stackoverflow.com/questions/2012974/mysql-which-to-use-when-drop-table-truncate-table-delete-from-table
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/2012974/mysql-which-to-use-when-drop-table-truncate-table-delete-from-table/2013086#2013086
tags:
- sql
- mysql
---

In addition to the answers above, on Oracle RDBMS, "delete" is a transaction that can be rolled back if you didn't commit. "Truncate" cannot.