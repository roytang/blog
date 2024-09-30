---
date: 2016-11-21 12:52:39
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/40720684/marklogic-node-api-how-to-filter-the-results-from-a-valuesbuilder
tags:
- node.js
- marklogic
- questions
- stackoverflow
- software development
title: Marklogic Node API - how to filter the results from a valuesBuilder
---

I want to retrieve all documents in my MarkLogic db that have month=November and also group them by name, and get the count of records per name. I know I can get the frequency per name by using valuesBuilder with a range index on the name field, but how can I filter this result so that I only get the count of records for the month of November?

Supposedly valuesBuilder.fromIndexes().where() can do the filtering, but I don't know what to pass here and examples online seem to be sparse.