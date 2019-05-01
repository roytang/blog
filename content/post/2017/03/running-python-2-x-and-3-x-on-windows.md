---
author: roy
categories: []
date: 2017-03-02 01:30:38
tags:
- python
- Software Development
title: Running Python 2.x and 3.x on Windows
type: post
url: /2017/03/running-python-2-x-and-3-x-on-windows/
---

I've been hesitant to try Python 3.x because it's not backward compatible with Python 2.x which I've been using for scripting since forever. But recently I found out that since Python 3.3, they've included a launcher in the Windows version that supports having both versions installed.

You can use the launcher to specify the Python version to use at the command line (it defaults to whichever version was installed first):

[<img class="aligncenter size-full wp-image-1816" src="http://roytang.net/wp-content/uploads/2017/03/py.png" alt="" width="664" height="272" srcset="https://roytang.net/wp-content/uploads/2017/03/py.png 664w, https://roytang.net/wp-content/uploads/2017/03/py-300x123.png 300w" sizes="(max-width: 664px) 100vw, 664px" />][1]

Even better, the launcher will recognize a header in your .py files that can specify which version of python to use:

> #!/usr/bin/env python3

If the launcher sees this header, it will automatically launch the appropriate python version. Handy!

 [1]: http://roytang.net/wp-content/uploads/2017/03/py.png