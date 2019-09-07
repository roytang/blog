---
categories: []
date: 2019-08-28 00:00:00
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1166502708343390210/
tags:
- software development
- python
title: 'Python: Markov Chains'
type: post
---

Back when I was still learning Python in 2008, one of the first "fun" scripts I wrote was a text generator using [Markov chains](https://en.wikipedia.org/wiki/Markov_chain). I'd run it against all the chat logs I had with people at work and serve the results from a webserver on my computer. THe results were often amusing and sometimes hilarious.

Since I've been going through my old scripts lately, I thought I'd update that script to Python 3 (read: add parentheses around print params and use [pathlib](/2019/08/devnotes-python-pathlib/)) and run it against all the posts on this here site. I added the script to my deploy script for this site (thus further worsening my build times), so it should generate a new page every hour or so. I also added the generated markdown file to gitignore so it never gets saved to the repo. Every output of this script will be fleeting and ephemeral!

You can view the output [here](/demos/markov). You can view the script source [here](https://github.com/roytang/blog/blob/master/utils/markov.py).