---
date: 2017-12-19 05:31:56
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/47880549/marklogic-template-driven-extraction-how-to-define-nullable-in-javascript-templ
tags:
- javascript
- marklogic
- questions
- stackoverflow
- software development
title: 'Marklogic Template Driven Extraction: How to define nullable in Javascript
  template?'
---

How to specify that a column in the schema should be nullable?

I tried adding a nullable attribute:

    var myFirstTDE = xdmp.toJSON(
      {
        "template": {
          "context": "/match",
          "collections": ["source1"],
          "rows": [
            {
              "schemaName": "soccer",
              "viewName": "matches",
              "columns": [
                {
                  "name": "id",
                  "scalarType": "long",
                  "val": "id",
                  "nullable": 0
                },
                {
                  "name": "document",
                  "scalarType": "string",
                  "val": "docUri"
                },
                {
                  "name": "date",
                  "scalarType": "date",
                  "val": "match-date"
                },
                {
                  "name": "league",
                  "scalarType": "string",
                  "val": "league"
                }
              ]
            }
          ]
        }
      }
    );
    
    tde.validate( 
      [myFirstTDE]
    );

But this gave me a template error:

    "message": "TDE-INVALIDTEMPLATENODE: Invalid extraction template node: fn:doc('')/template/array-node('rows')/object-node()/array-node('columns')/object-node()[1]/number-node('nullable')"

For a template defined using XQuery, adding nullable to the column works:

    <column>
      <name>ISSN</name>
      <scalar-type>string</scalar-type>
      <val>Journal/ISSN</val>
      <nullable>true</nullable>
    </column>

How to do the same thing using JS/Json?