---
date: 2017-09-17 12:17:12
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/46263980/marklogic-query-for-documents-where-a-specific-json-property-is-not-defined
tags:
- javascript
- json
- marklogic
- sjs
- questions
- stackoverflow
- software development
title: MarkLogic - query for documents where a specific json property is not defined
---

I'm using ML8. I have a bunch of json documents in the database. Some documents have a certain property "summaryData", something like:

    {
    ...(other stuff)...
      summaryData: {
        count: 100,
        total: 10000,
        summaryDate: (date value)
      }
    }

However, not all documents have this property. I'd like to construct an SJS query to retrieve those documents that don't have this property defined. If it was SQL, I guess the equivalent would be something like "WHERE summaryData IS NULL"

I wasn't sure what to search for in the docs. Any advise would be helpful.