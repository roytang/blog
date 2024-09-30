---
date: 2017-08-27 05:09:50
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/45901868/marklogic-node-js-sorting-by-the-value-of-a-json-element-with-multiple-instance
tags:
- marklogic
- questions
- stackoverflow
- software development
title: 'MarkLogic node.js: sorting by the value of a json element with multiple instances
  in the same document'
---

Sorry if the title is unclear, but I'm finding my problem hard to explain concisely. I have a number of JSON documents with structure like this:

    {
      "count": 100,
      "groups": [
        {
        "name": "group A",
        "count": 12
        },
        {
        "name": "group B",
        "count": 22
        },
        {
        "name": "group C",
        "count": 7
        }
      ]
    }

Basically, the document has an item count plus a breakdown of that count into smaller groups. So this record represents a collection of 100 items, of which 12 are from group A, 22 are from group B, 7 are from group C.

Now, I have an element range index on "count" and a bunch of such documents. I'd like to be able to sort by any of the options:

- sort by total count (descending or ascending)
- sort by group A count (descending or ascending)
- sort by group B count (descending or ascending)
- sort by group C count (descending or ascending)

I've tried

    .orderBy(qb.sort("count", "descending"))

This seems to be sort by the total cost (the one in the document root), but I'm not sure if that's always true or I need to specify something else to guarantee it always gets that particular one.

For sorting by a specific group, I have no idea how to specify it.

Any advice?