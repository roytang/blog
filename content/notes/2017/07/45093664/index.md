---
date: 2017-07-14 02:27:11
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/45093664/marklogic-detecting-similar-duplicate-names
tags:
- marklogic
- questions
- stackoverflow
- software development
title: MarkLogic - detecting similar/duplicate names
---

I have a number of documents from different sources. Many of them reference a company name, but may have stored the information slightly differently. The name is a field in the documents.

I'd like to be able to detect variations on the same name, something like:

- Ajax Company Incorporated
- Ajax Co. Inc.
- Ajax Company Inc.
- Ajax Company
- Ajax Company (formerly Ajax Unlimited)
- etc

Does MarkLogic have any facility to query documents that have "similar" name as above? I'm not sure if there's a more technical term that I should be searching for. Preferably for either the node client API or server-side js.