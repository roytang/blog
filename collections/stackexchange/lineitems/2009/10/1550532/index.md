---
date: 2009-10-11 11:58:13
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1550532/trimming-whitespace-from-html-content
tags:
- java
- javascript
- html
- html-parsing
- questions
- stackoverflow
- software development
title: Trimming whitespace from HTML content?
---

I have a CRUD maintenance screen with a custom rich text editor control (FCKEditor actually) and the program extracts the formatted text as HTML from the control for saving to the database. However, part of our standards is that leading and trailing whitespace needs to be stripped from the content before saving, so I have to remove extraneous &amp;nbsp; and &lt;br&gt; and such from the beginning and end of the HTML string.

I can opt to either do it on the client side (using Javascript) or on the server side (using Java) Is there an easy way to do this, using regular expressions or something? I'm not sure how complex it needs to be, I need to be able to remove stuff like:

    <p><br /> &nbsp;</p>

yet retain it if there's any kind of meaningful text in between. (Above snippet is from actual HTML data saved by the tester)