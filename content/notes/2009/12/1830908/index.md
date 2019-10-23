---
date: 2009-12-02 05:52:26
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1830908/css-rendering-list-items-in-2-rows
tags:
- html
- css
- css-float
- questions
- stackoverflow
- software development
title: CSS Rendering List Items in 2 rows
---

Let's say I have a series of <li> elements designed to render via float:left inside a fixed-width container as follows:

    Item 1 | Item 2 | Item 3 | Item 4
    | Item 5 | Item 6

This is fine, Item 5 and Item 6 are pushed to the second row because the container has a fixed width.

Now, is it possible to have something similar to above, except that majority of the items will render in the second row? Something like:

    Item 1 | Item 2 
    | Item 3 | Item 4| Item 5 | Item 6

Basically, I want to render a list of items horizontally, wrapping to the second row as needed, but with majority of the items on the second row if it exists. The number of items to be generated may vary, but will not exceed 2 rows' worth of items.