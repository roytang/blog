---
date: 2011-10-24 04:17:49
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/7871245/css-menu-wrapping
tags:
- css
- questions
- stackoverflow
- software development
title: CSS Menu wrapping
---

I'm trying to build a CSS-based menu. I want it to be able to adjust when the browser resizes so I'm using floats to wrap the menu items to the next line as needed. However, I want to have an extra buffer cell at the end to round out the menu appearance, see the sample image below (this an image the designer made from photoshop). 

![Example here][1]


I can set the background image of the containing div to fake it (using the clearing floats trick I found at http://quirksmode.org/css/clearing.html), but then I have the additional problem of having extra space on the right side because I the cited trick says I should set the width to 100% on the container. (see image below)

![enter image description here][2]

I also don't have any borders on that extra area after the last item. So, what's the proper way to go about this? Can anyone suggest any good online implementations I can check?

Thanks!

  [1]: https://i.stack.imgur.com/yWkZj.png
  [2]: https://i.stack.imgur.com/1LKIQ.png