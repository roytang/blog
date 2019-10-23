---
date: 2009-06-26 03:07:21
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1047137/how-to-specify-the-word-breaking-conditions-in-ie
tags:
- css
- internet-explorer
- questions
- stackoverflow
- software development
title: How to specify the word-breaking conditions in IE?
---

Specifically, say I have a string like ABC-123-NNN. I would like the paragraph to have line breaks, but <b>not</b> to break at the dashes.

i.e. if my text is "The serial number ABC-123-NNN is not valid", I would like to keep together the entire serial number if it exceeds the container width. 

So the following is ok:

<pre>
  The serial number 
  ABC-123-NNN is not 
  valid
</pre>

But the following (which is the behavior of IE6) is not:

<pre>
  The serial number ABC-
  123-NNN is not valid
</pre>

Currently IE seems to break at dashes. Is there any applicable CSS or whatever I can apply to avoid it?