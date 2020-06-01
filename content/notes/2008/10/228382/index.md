---
date: 2008-10-23 02:54:03
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/228382/c-html-font-tag-parsing
tags:
- csharp
- parsing
- questions
- stackoverflow
- software development
title: C# HTML Font Tag Parsing
---

I need to parse a large amount of text that uses HTML font tags for formatting,

For example:

    <font face="fontname" ...>Some text</font>

Specifically, I need to determine which characters would be rendered using each font used in the text. I need to be able to handle stuff like font tags inside another font tag.

I need to use C# for this. Is there some sort of C# parser class to make this easier? Or would I have to write it myself?

Thanks!