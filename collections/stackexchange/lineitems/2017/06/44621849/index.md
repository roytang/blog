---
date: 2017-06-19 03:27:09
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/44621849/marklogic-node-js-api-group-by-sum
tags:
- node.js
- marklogic
- questions
- stackoverflow
- software development
title: MarkLogic node.js api - group by sum
---

Something similar to my question here: https://stackoverflow.com/questions/40715822/marklogic-node-js-api-group-by-and-sort-by-count

I have documents in Marklogic with fields *name* and *amount*. I want to get the total amount for each name. Basically in SQL it would be 

    select name, sum(amount) from table group by name

I have **range indexes** for both *name* and *amount*.
 For getting sum aggregates, the documentation suggests something like **valuesBuilder.fromIndexes('amount').aggregates('sum')**, but this only gets the sum for all records, instead of per name like I want.

Any advice?