---
author: roy
categories: []
date: 2017-03-02 01:30:38
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/157884428980/running-python-2x-and-3x-on-windows
- type: twitter
  url: https://twitter.com/roytang/statuses/837115319877533698/
tags:
- python
- Software Development
title: Running Python 2.x and 3.x on Windows
type: post
url: /2017/03/running-python-2-x-and-3-x-on-windows/
dontinlinephotos: true
---

I've been hesitant to try Python 3.x because it's not backward compatible with Python 2.x which I've been using for scripting since forever. But recently I found out that since Python 3.3, they've included a launcher in the Windows version that supports having both versions installed.

You can use the launcher to specify the Python version to use at the command line (it defaults to whichever version was installed first):

{{< img src="py.png" >}}

Even better, the launcher will recognize a header in your .py files that can specify which version of python to use:

> `#!/usr/bin/env python3`

If the launcher sees this header, it will automatically launch the appropriate python version. Handy!