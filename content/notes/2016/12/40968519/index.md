---
date: 2016-12-05 06:44:52
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/40968519/marklogic-node-js-api-how-to-get-the-document-where-an-embedded-triple-lives
tags:
- node.js
- sparql
- marklogic
- questions
- stackoverflow
- software development
title: 'Marklogic Node.js API: How to get the document where an embedded triple lives?'
---

I tried to insert the following test document:

    db.documents.write(
    	{
            uri: "/test/doc1.json",
            contentType: "application/json",
            collections: "test",
            content: {
            	name : "Peter",
            	hobby: "Sleeping",
            	other: "Some other info",
    		  	"triple": {
    			    "subject": {   
    			    	"datatype": "http://example.com/name/",  
    			      	"value": "Peter"   
    			    },   
    			    "predicate": {     
    			    	"datatype": "http://example.com/relation/",  
    			      	"value": "livesin"   
    			    },   
    			    "object": {     
    			    	"datatype": "http://example.com/location/",  
    			      	"value": "Paris"   
    			    }
    		  	}
    		}
        }
      ).
      result(function(response){
        console.log("Done loading");
      }); 

Then I queried as follows:

    var query = [
      'SELECT ?s ?p ?o' ,
      'WHERE { ?s ?p ?o }' ,
    ];
    db.graphs.sparql('application/sparql-results+json', query.join('\n')
    ).result(function (result) {
      console.log(JSON.stringify(result, null, 2));
    }, function(error) {
      console.log(JSON.stringify(error, null, 2));
    });

The results showed me the values of the triple, but what if I also want to get the entire document where the triple was embedded? Is it also possible to filter by other fields in the document?