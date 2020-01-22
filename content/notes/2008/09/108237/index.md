---
date: 2008-09-20 14:04:22
reply_to:
  label: '''Add a column to existing table and uniquely number them on MS SQL Server''
    on stackoverflow'
  name: Adhip Gupta
  type: stackexchange
  url: https://stackoverflow.com/questions/108211/add-a-column-to-existing-table-and-uniquely-number-them-on-ms-sql-server
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/108211/add-a-column-to-existing-table-and-uniquely-number-them-on-ms-sql-server/108237#108237
tags:
- sql
- sql-server
---

for oracle you could do something like below

    alter table mytable add (myfield integer);
    
    update mytable set myfield = rownum;