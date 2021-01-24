---
categories: []
date: 2007-08-11 08:29:20
tags:
- Software Development
title: Announcing PyMTG
type: post
url: /2007/08/announcing-pymtg/
---

I couldn't sleep, so obviously, I had to start a new personal project.

[PyMTG][1] 

I was inspired after forum-browsing lead me to look at existing MTG open-source software. I've been thinking of starting a true-blue personal software project for a while now, and the idea of PyMTG appeals to me for several reasons:

(a) It's related to one of my current hobbies
   
(b) Allows me to become familiar with a new language (Python)
   
(c) It's moderately to insanely difficult (depending on how well I set my targets), i.e. it's of a scale large enough to be challenging.

The wiki page contains the target features for the first release at the end of the year. Quite modest I think, despite my tendencies to underestimate. I hope I can follow through with this project and have enough time for it.

The success of the project would be determined by how much of the existing MTG cardbase it could support. Ultimately, I would want it to be open-source and have people help me to obtain 100% cardbase support. But that's obviously very far away.

Wish me luck 🙂

Update: This project is on-hold, not surprisingly. It turns out I don't actually have time to learn a new language. :( 

Update Jan 2021: Since the wiki link above is obsolete, I've rescued the text below for archival purposes. _This is not an active project!_

---

pyMTG is a Python-based Magic: The Gathering game engine. It is currently in the initial stages of development.

Project started middle of August 2007.

The next milestone is version 0.1, target for release at the end of 2007.

Target feature list for v0.1:

1. Provide a console gui for playing MTG against a computer AI

    I currently have no interest in writing GUI stuff, only logic, so the bare-bones console will be the first release.

2. Provide a working game engine, supporting only basic lands and vanilla creatures

    Really the minimum to get a game working. With this I already need to handle: playing lands, playing creatures, turn order, attack phases, passing priority, dealing damage, drawing cards, etc. I assume I will become familiar with Grizzly Bears :D

3. Provide a basic, extensible AI interface

    The idea for #3 is that I can provide a basic interface and maybe implement some simple AIs, namely Goldfish (never does anything) and AlwaysAttacks (plays any creatures it can and always attacks), and other people can contribute more complicated AIs.

    pyMTG design philosophy: Everything must be easily extensible. Ideally I can implement the base source and other people can extend it by adding new cards to data files, or even implement their own python classes.


 [1]: http://roytang.pbworks.com/w/page/7977434/pyMTG