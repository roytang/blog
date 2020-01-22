---
date: 2011-12-13 02:31:45
reply_to:
  label: '''how to reference an oracle pl/sql out parameter of table%rowtype as an
    object in java'' on stackoverflow'
  name: Matthew Quiros
  type: stackexchange
  url: https://stackoverflow.com/questions/8483352/how-to-reference-an-oracle-pl-sql-out-parameter-of-tablerowtype-as-an-object-in
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/8483352/how-to-reference-an-oracle-pl-sql-out-parameter-of-tablerowtype-as-an-object-in/8483644#8483644
tags:
- java
- oracle
- jdbc
- plsql
---

"rowtype" here is an Oracle PL/SQL-specific type, I don't think it would be supported by JDBC. A quick search of the oracle forums (google "jdbc rowtype site:oracle.com") suggests the same. You're probably better off returning a cursor, or just execute the SQL from JDBC directly.