---
date: 2017-11-10 06:11:10
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/47216649/vis-js-network-is-there-a-setting-to-make-the-node-labels-stay-the-same-size-o
tags:
- javascript
- vis.js
- vis.js-network
- questions
- stackoverflow
- software development
title: vis.js network - is there a setting to make the node labels stay the same size
  on zoom?
---

Basically the title. The client is complaining that when he zooms in, the text labels for the nodes are quite large. Is there a way to keep the node labels at a fixed font size even when zooming in or out?

From the nodes documentation (http://visjs.org/docs/network/nodes.html), there's a scaling.label option, but it doesn't seem to work. I think this is only relevant if I'm using values to scale the nodes.