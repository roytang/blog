---
date: 2017-10-05 07:15:44
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/46579945/vis-js-shorter-edge-lengths-for-higher-edge-value
tags:
- javascript
- vis.js
- vis.js-network
- questions
- stackoverflow
- software development
title: vis.js - shorter edge lengths for higher edge value?
---

I'm trying out vis.js for generating graph visualization. For every edge in my graph, I have a number that describes the strength of the connection between two nodes. I'd like to render the vis.js graph such that the nodes that have stronger relationships (higher edge values) are closer together (edge length is shorter).

I've set the relationship strength (an integer) as the "value" attribute for each edge, but this only seems to make the edge lines slightly thicker for higher values.

What options should I be looking at? I'm not sure if this is supposed to be a function of vis's physics-based stabilization. 

Thanks for advice!