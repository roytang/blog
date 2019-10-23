---
date: 2009-12-18 09:48:12
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1927273/applet-freezes-page-on-initial-load-mac-firefox
tags:
- firefox
- macos
- applet
- questions
- stackoverflow
- software development
title: Applet freezes page on initial load (Mac Firefox)
---

We have a web screen with a number of applets that has a problem on Mac OSX 10.5.7, Firefox 3.0.15, java 1.5.0_19. 

The problem is encountered on the user site.
On initial load of applets (with an empty applet cache), the screen locks up/hangs while loading the applets.
After refreshing the page, it loads normally. 
If the cache is cleared, same problem happens again.

Unfortunately, we're not encountering this on our local test machine (same OS, java and Firefox versions)

We were able to get a jstack thread dump, see below:
[http://pastebin.com/m527e05dd][1]

However, we're not sure how to interpret it. Any suggestions or advice?

Edit:
We were able to replicate in our testing machine by creating a new user (clean Firefox profile). If we clear the java cache then visit the problematic pages, the edit controls are disabled (we can't click them to focus them), the Firefox address bar and search box have the same behavior. The edit box controls only "unfreeze" when we access the "Help" menu entry, which has a Search edit box that *is* active.

  [1]: http://pastebin.com/m527e05dd