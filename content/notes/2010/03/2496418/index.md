---
date: 2010-03-22 23:12:29
reply_to:
  label: '''comparing two cursors in oracle instead of using MINUS'' on stackoverflow'
  name: Omnipresent
  type: stackexchange
  url: https://stackoverflow.com/questions/2496360/comparing-two-cursors-in-oracle-instead-of-using-minus
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/2496360/comparing-two-cursors-in-oracle-instead-of-using-minus/2496418#2496418
tags:
- performance
- oracle
---

MINUS is the same as saying "get all the rows of the first query, then from that set remove the rows that are also in the second query", so you could like load the results from the first query into an array in-memory, then loop through the second query results and check them one-by-one against the first query results and remove them if they exist.

I'm not sure that will actually perform better though (depends on a lot of things). You might also want to consider using NOT EXISTS instead and check that performance, i.e.

    SELECT  RTRIM(LTRIM(A.HEAD)),
      A.EFFECTIVE_DATE,
    FROM   TABLE_1 A
    WHERE  A.TYPE_OF_ACTION='6'
    AND    A.EFFECTIVE_DATE >= ADD_MONTHS(SYSDATE,-15)  
    AND NOT EXISTS (
      SELECT 1 fFROM TABLE_2 B
      WHERE RTRIM(LTRIM(A.HEAD)) = RTRIM(LTRIM(B.HEAD))
      AND A.EFFECTIVE_DATE = B.EFFECTIVE_DATE
    )

Some functional indexing may also be needed on RTRIM(LTRIM(A.HEAD))