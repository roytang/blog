---
date: 2009-09-29 09:43:10
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1491562/loading-and-resizing-images-dynamically
tags:
- javascript
- html
- css
- questions
- stackoverflow
- software development
title: Loading and resizing images dynamically
---

HTML/Javascript - I want to load images dynamically, and the images I'm going to load can be of varying aspect ratios.

I want the images to fit into a specific area of the containing div - an area 40% of the containing div's width and 80% of its height. Since they have varying aspect ratios, of course they will not always use up this entire area, but I want to resize them such that they don't exceed the bounds. But I don't know ahead of time whether I should specify the width or the height (and the partner attribute to auto) since I don't know what the aspect ratio of the images will be ahead of time.

Is there a CSS way to do this? Or I need to compute the required widths using javascript?

PS I only need to do this in Firefox 3.5!