---
date: 2017-12-28 17:04:03
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/48011448/marklogic-node-js-stream-end-event-doesnt-fire-for-certain-collections
tags:
- node.js
- marklogic
- questions
- stackoverflow
- software development
title: 'MarkLogic node.js: stream end event doesn''t fire for certain collections'
---

I have a query using MarkLogic node.js that basically boils down to something like this:

    db.documents.query(qb.where(qb.collection('test'))).stream()
    .on('data', function(row) {
        console.log("Stream on data");
    })
    .on('end', function() {
        console.log("Stream on end");
    })
    .on('error', function(error) {
        console.log(error);
    })
    ;

Now, for a certain collection we have in our database, the 'end' function doesn't fire, i.e. I never see "Stream on end" appear in the log. There's no error or anything, processing just stops. It's only for this particular collection, other collections seem fine.

If I query documents in that collection directly using other methods such as qb.value() without using qb.collection(), the end event fires correctly. But once I add qb.collection() into the mix (using qb.and), the end event doesn't fire.

I'm unsure how to debug this, as this is my first time trying to use streams in the nodejs client library. Any advice as to what I can check?

Thanks!