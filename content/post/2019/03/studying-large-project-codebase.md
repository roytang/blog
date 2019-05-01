---
author: roy
categories: []
date: 2019-03-03 05:56:56
tags:
- quora
- Software Development
title: Studying a large project codebase
type: post
---

Given my [recent misgivings about Quora](/2018/12/quora/), I thought it might be a good idea to cross-post some of my answers from there into this blog, with some edits even. So here's the first one! (stuff in *italics* were added during the cross-post)

> How can you read and study a large software project source code?

Attacking a large, existing codebase that you are unfamiliar with can be a daunting endeavor. Don't expect that you will be able to easily navigate the codebase quickly after just a few days of studying it. Familiarity will come with experience.

Some things that can help:

- Don't try to understand everything all at once. Figure out what is interesting to you and focus your efforts there
- Follow the path of data. Easiest way to see how the program works. For example, if I were studying a web application that processes request parameters to generate a search result, I would trace how the program captures the parameters from the requests object, formulates it into a search query, sends it to the database, receives the results, formats the results, then sends it back to the browser. Looking at the typical paths through which data traverses the system can give you a good overview of where everything is. *this may be a problem if you're not familiar with the technology or framework the codebase is using, as some of the details may have too many layers of abstraction to trace. In that case, better to brush up and have a basic understanding of the tech first.*
- Try to fix a bug or implement some sort of change. If it's an open source project, this is probably the best way to familiarize yourself with the codebase *and* get more involved at the same time. I'd suggest starting with minor UI bugs, those tend to be easiest to figure out since a text search of the source will often point you to where the correction needs to be made. For example, if the bug is that a particular error message is being shown under the wrong conditions, you can use a text search to find where the error message is declared, then trace all the code points that generate that message, figure out which one you need to update (probably by trial and error) and fix accordingly

[Link to the original answer on Quora](https://www.quora.com/How-can-you-read-and-study-a-large-software-project-source-code/answer/Roy-Tang)