---
date: 2017-08-04 12:55:30
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/45507423/marklogic-node-js-is-it-possible-to-support-a-derived-value-in-parsebindings
tags:
- marklogic
- questions
- stackoverflow
- software development
title: MarkLogic node.js - is it possible to support a derived value in parseBindings?
---

We have a search application using MarkLogic node.js. We use parsedQuery like this:

                qb.parsedFrom(prop.search, 
                qb.parseBindings(
                    qb.word('name', qb.bind('name')),
                    qb.word('birthdate', qb.bind('birthdate')),
                    qb.range('count', qb.datatype('float'), qb.bind('count'))
                )
            )

The above currently supports search syntax like "count GT 50", etc. We would like to support searching using a derived value such as age. That is, we want to support a search syntax like "age GT 10", where the age value is not stored in the documents in the database but rather needs to be computed from the birthdate on the fly. We can't store the age in the documents since the age changes depending on the current date.

Is this possible and if so, how? If it matters, we are using ML8