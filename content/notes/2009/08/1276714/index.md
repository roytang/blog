---
date: 2009-08-14 08:40:06
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1276714/invoking-java-code-across-application-server-cluster-nodes
tags:
- java
- java-ee
- cluster-computing
- questions
- stackoverflow
- software development
title: Invoking Java code across Application Server cluster nodes
---

Let's say I have a Java webapp deployed on some Application Server with clustering across a few nodes.

In the webapp, we maintain a cache of some values retrieved from the database, stored in-memory as static variables. Whenever a user performs an update in a particular screen, we clear the cache so that the cached values will be retrieved again the next time they are needed.

Now the problem: Since each node in the cluster is running on a separate JVM, how can I clear the cache across all nodes? Basically I want to call a static function on each cluster node. Is there some standard J2EE way to do this, or it depends on the Application Server software?