---
date: 2017-09-08 08:53:55
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/46112486/marklogic-node-js-conditional-updates-using-fields-other-than-versionid
tags:
- marklogic
- questions
- stackoverflow
- software development
title: MarkLogic node.js - conditional updates using fields other than versionId
---



I'm using ML8 and Node.js. The documentation here: http://docs.marklogic.com/guide/node-dev/documents#id_68765 describes how to do conditional updates in ML using the versionId field.

But for example if I want to do a conditional update on a different field, is it possible?

My scenario is: I have JSON documents with elements assignedTo and assignDate (where assignDate is set to current date every time a new value is set to assignedTo)

Now, for my "Assign" operation, I would like to make sure that no one else has changed the assignedTo/assignDate fields between the time I read the document and when I perform the update. I don't care if other fields in the same document have been updated or not - if other fields have been updated, I can still proceed with the Assign operation (hence I cannot use the versionId approach, since that covers the whole document)

How can this be done?