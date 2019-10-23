---
date: 2011-07-13 10:36:38
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/6677574/migrating-from-cvs-to-distributed-version-control-mercurial
tags:
- version-control
- mercurial
- questions
- stackoverflow
- software development
title: Migrating from CVS to distributed version control (Mercurial)
---

Some background: We're working on projects that involve projects across 2 different countries, and we've been using CVS. Developers in the country not hosting the CVS server will take forever to connect to the remote server, so we've set up this system to have 2 separate CVS servers in each country and have a sync job that keeps them in sync every hour or so.

Given this, we're looking at migrating to a distributed version control system, mostly because we've been having problems with the sync job failing and the limitation that for a given set of files only one side can have the writelock for it at a time.

We're currently looking at Mercurial for this purpose, so can anyone help tell us if:

a. Will Mercurial be a good fit for our use case above? How easy will it be for devs to make the transition, i.e. will they still be able to work the same way? etc

b. Can Mercurial support branching a specific folder only?

c. We also hold a lot of binary docs in version control, will they be suitable for Mercurial?

d. Is there support for getting the "writelock" of particular files? i.e. I want no other people to update these particular files while I'm working on them

Thanks!