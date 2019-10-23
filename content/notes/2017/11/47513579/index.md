---
date: 2017-11-27 14:42:48
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/47513579/marklogic-template-driven-extraction-and-triples-forming-triples-between-array
tags:
- marklogic
- questions
- stackoverflow
- software development
title: 'MarkLogic template driven extraction and triples: forming triples between
  array nodes'
---

This is a follow-up to my question here: https://stackoverflow.com/questions/47449002/marklogic-template-driven-extraction-and-triples-dealing-with-array-nodes/47459250#47459250

So let's say I have a number of documents structured like this:

    declareUpdate();
    
    xdmp.documentInsert(
           '/test/tde.json',
           {
             content: {
               name:'Joe Parent',
               children: [
                 {
                   name: 'Bob Child'
                 },
                 {
                   name: 'Sue Child'
                 },
                 {
                   name: 'Guy Child'
                 }
               ]
             }
           },
           {permissions : xdmp.defaultPermissions(),
            collections : ['test']})

I want to define a template that would extract triples from these documents defining sibling relationships between the children. For the above example, I would want to extract the following triples (the relationship is two-way):

    Bob Child sibling-of Sue Child
    Bob Child sibling-of Guy Child
    Sue Child sibling-of Bob Child
    Sue Child sibling-of Guy Child
    Guy Child sibling-of Bob Child
    Guy Child sibling-of Sue Child

How can i set up my template to accomplish this?

Thanks!