---
date: 2009-07-07 03:13:37
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1090202/using-javascript-to-open-a-maximized-window-in-ie6
tags:
- javascript
- internet-explorer
- questions
- stackoverflow
- software development
title: Using Javascript to open a "maximized" window in IE6?
---

Any idea for this? 

Problems encountered: Using screen.availHeight and screen.availWidth as the height and width params in window.open causes the browser size to include the taskbar, and positioning at (0, 0) ignores the possibility of the taskbar being up there.

What I want is to open a new window with the size as if it was "maximized" by the user, i.e. it shouldn't cover the windows taskbar.

(Oh, and no need to remind me that users don't like Javascript interfering with their browser windows, etc. This is for an internal intranet webapp...)