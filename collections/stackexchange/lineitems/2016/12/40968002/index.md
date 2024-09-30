---
date: 2016-12-05 06:02:58
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/40968002/how-to-query-marklogic-triples-using-sparql
tags:
- sparql
- marklogic
- questions
- stackoverflow
- software development
title: How to query Marklogic triples using SPARQL?
---

I inserted a test document using the Node.js API:

  

      db.documents.write(
    	{
            uri: "/test/doc1.json",
            contentType: "application/json",
            collections: "test",
            content: {
            	name : "Peter",
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

Then I tried querying it via SPARQL on the Marklogic console webapp:

    SELECT ?s ?p ?o
      WHERE { ?s ?p ?o }

The query above works fine, it retrieves the test triple I inserted above

However, if I want to filter by the literal value "Paris", I tried the following:

    PREFIX loc: <http://example.com/location/>
    
    SELECT ?s ?p 
      WHERE { ?s ?p loc:Paris }

But in this case I got zero results. Is this syntax incorrect? I was just following how the queries looked in https://docs.marklogic.com/guide/semantics/semantic-searches

What is the proper way to do it?