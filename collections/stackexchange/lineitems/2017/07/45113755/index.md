---
date: 2017-07-15 02:04:29
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/45113755/jsplumb-scroll-the-canvas-when-node-dragged-outside-visible-area
tags:
- javascript
- css
- jsplumb
- questions
- stackoverflow
- software development
title: jsplumb - scroll the canvas when node dragged outside visible area
---

I'm trying out jsplumb. I have a copy of this demo: https://jsplumbtoolkit.com/community/demo/statemachine/index.html

In this demo, when I drag one of the nodes outside of the canvas boundary, a scrollbar appears to indicate the canvas area has expanded. However, I still have to manually scroll the view to see the dragged node. 

I would like the view to automatically scroll when I drag a node beyond the edge. Same thing when dragging a new connector, I would like to automatically scroll the view - so I can choose to connect to a node currently outside the visible area. Any advice on how to do this?

Secondary question: In the demo above the scrollbars appear as expected when I drag elements off the right or bottom of the canvas, but not when I drag them off the left edge or off the top edge. That is, if I drag a node upward off the canvas and drop it there, I no longer have any way of viewing that node or dragging it back down. Is there a way around this?