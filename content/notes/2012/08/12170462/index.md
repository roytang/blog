---
date: 2012-08-29 03:24:13
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/12170462/how-to-assess-the-risk-of-a-java-version-upgrade
tags:
- java
- questions
- stackoverflow
- software development
title: How to assess the risk of a java version upgrade?
---

I'm being asked to assess whether we can safely upgrade the java version on one of our production-deployed webapps. The codebase is fairly large and we want to avoid having to regression test everything (no automated tests sadly), but we've already encountered at least one problem during some manual testing (XmlStringReader.getLocalName now throws an IllegalStateExeption when it just used to return null) and higher-ups are pretty nervous about the upgrade.

The current suggested approach is to do a source compare of the JDK sources for each version and assess those changes to see which ones might have impact, but it seems there's a lot of changes to go through (and as mentioned the codebase is kinda large). Is it safe and easier to just review the java version changes for each version? Or is there an easier way to conduct this assessment?

Edit: I forgot to mention the version upgrade being considered is a minor version upgrade, i.e. 1.6.10 to 1.6.33