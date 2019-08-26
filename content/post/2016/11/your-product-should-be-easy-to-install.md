---
author: roy
categories: []
date: 2016-11-24 01:30:31
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/153581662850/your-product-should-be-easy-to-install
tags:
- Software Development
title: Your Product Should Be Easy to Install
type: post
url: /2016/11/your-product-should-be-easy-to-install/
---

This is a story of something I consider to be one of my worst mistakes in software product development.

Some years ago I was asked whether it was feasible to write software that would be integrated with Software X that allowed us to export that software's output into a format that was compatible with Standard Y. I took a look and after a while came back with "Well sure. We could use Programming Language M that has an API that lets us integrate into Software X so we can export the output data. Then we'll have to use Library N which lets us generate files in the format compatible with Standard Y. What project is this for by the way?"

"Oh, it's not a bespoke project. It's a product we're going to develop with a partner company."

"Oh." That set off some alarm bells, so I pointed out that Programming Language M and Library N required the client to install two different runtimes on the client machine. I suggested we consider itself writing our own conversion library so that we wouldn't have to require two different runtimes, but the cost estimates turned out to be prohibitive so of course we went with the more complicated stack with two runtimes.

It was a disaster. It turned out to be almost impossible to convince users to install and try out our software when the installation process included a step where the user needed to download and install a programming runtime from an external website (the licensing terms of the runtime did not allow us to package it together with our installer). In hindsight, it was probably a newbie mistake since this was the first time we were working on software product development. If this was our usual bespoke software project where users had IT staff to install software on their enterprise systems, it wouldn't be a problem.

I learned a lot of technical stuff from that project (there was a lot of math involved in the data export too), but the most important thing I learned was that the best software product in the world is going to fail if you make it difficult for your users to install it.