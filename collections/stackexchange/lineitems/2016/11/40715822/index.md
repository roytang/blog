---
date: 2016-11-21 08:37:08
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/40715822/marklogic-node-js-api-group-by-and-sort-by-count
tags:
- node.js
- marklogic
- questions
- stackoverflow
- software development
title: MarkLogic node.js api - group by and sort by count
---

In a relational db you'd have something like "select name, count(1) as c from mytable group by name order by c desc". Basically I want to count how many records contain each name value and get the ones with highest counts first.

Is there a way to do a similar thing in Marklogic using the Node.js API?