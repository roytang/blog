---
date: 2017-11-23 06:32:35
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/47449002/marklogic-template-driven-extraction-and-triples-dealing-with-array-nodes
tags:
- marklogic
- marklogic-9
- questions
- stackoverflow
- software development
title: 'MarkLogic template driven extraction and triples: dealing with array nodes'
---

I've been studying the examples here: https://docs.marklogic.com/guide/semantics/tde#id_25531

I have a set of documents that are structured with a parent name and an array of children nodes with their own names. I want to create a template that generates triples of the form "name1 is-a-parent-of name2". Here's a test I tried, with a sample of the document structure:

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
                 }
               ]
             }
           },
           {permissions : xdmp.defaultPermissions(),
            collections : ['test']})
    
    cts.doc('/test/tde.json')
    
    var tde = require("/MarkLogic/tde.xqy");
    // Load the user template for user profile rows
    var template = xdmp.toJSON(
    {
      "template":{
        "context":"content",
        "collections": [
          "test"
        ],
          "triples":[
          {
            "subject": {
              "val": "xs:string(name)"
            },
            "predicate": {
              "val": "sem:iri('is-parent-of')"
            },
            "object": {
              "val": "xs:string(children/name)"
            }     
          }
        ]   
      }
    }
    );
    //tde.validate([template]),
    tde.templateInsert("/templates/test.tde", template);
    tde.nodeDataExtract( 
      [cts.doc( '/test/tde.json' )]
    )


However, the above throws an Exception:

>    [javascript] TDE-EVALFAILED: tde.nodeDataExtract([cts.doc("/test/tde.json")]) -- Eval for Object='xs:string(children/name)' returns TDE-BADVALEXPRESSION: Invalid val expression: XDMP-CAST: (err:FORG0001) Invalid cast: (fn:doc("/test/tde.json")/content/array-node("children")/object-node()[1]/text("name"), fn:doc("/test/tde.json")/content/array-node("children")/object-node()[2]/text("name")) cast as xs:string?

What is the proper syntax for extracting array nodes into a triple?

2nd somewhat related question: say I also wanted to have triples of the form "child1 is-sibling-of child2". For the example above it would be "Bob Child is-sibling-of Sue Child". What would be the proper syntax for this? I'm not even sure how to begin with this one.

Is TDE even the way to go here? Or is it better to do this programmatically? i.e. on document ingestion, generate those triples inside the document directly?

(If it's relevant, the ML version being used is 9.)