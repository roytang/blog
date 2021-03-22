---
date: 2016-04-14 00:00:00
slug: how-can-you-read-and-study-a-l
source: quora
syndicated:
- type: quora
  url: https://www.quora.com/How-can-you-read-and-study-a-large-software-project-source-code/answer/Roy-Tang
tags:
- answers
---

Someone on [quora](https://quora.com) asked:

> [How can you read and study a large software project source code?](https://www.quora.com/How-can-you-read-and-study-a-large-software-project-source-code/answer/Roy-Tang)


Attacking a large, existing codebase that you are unfamiliar with can be a daunting endeavor. Don't expect that you will be able to easily navigate the codebase quickly after just a few days of studying it. Familiarity will come with experience.

Some things that can help:</p><ul><li>Don't try to understand everything all at once. Figure out what is interesting to you and focus your efforts there</li><li>Follow the path of data. Easiest way to see how the program works. For example, if I were studying a web application that processes request parameters to generate a search result, I would trace how the program captures the parameters from the requests object, formulates it into a search query, sends it to the database, receives the results, formats the results, then sends it back to the browser. Looking at the typical paths through which data traverses the system can give you a good overview of where everything is.</li><li>Try to fix a bug or implement some sort of change. If it's an open source project, this is probably the best way to familiarize yourself with the codebase *and* get more involved at the same time. I'd suggest starting with minor UI bugs, those tend to be easiest to figure out since a text search of the source will often point you to where the correction needs to be made. For example, if the bug is that a particular error message is being shown under the wrong conditions, you can use a text search to find where the error message is declared, then trace all the code points that generate that message, figure out which one you need to update (probably by trial and error) and fix accordingly</li></ul></span>