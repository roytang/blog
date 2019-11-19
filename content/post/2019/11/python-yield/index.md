---
date: 2019-11-07
slug: python-yield
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1192280118468792321/
tags:
- software development
- devnotes
title: 'DevNotes: Python''s yield'
---

I've been using Python for well over 10 years, and I still don't have an intuitive mastery of one of its keywords: `yield`. Everytime I see it in someone's code I need to stop and mentally remind myself what it does. I figured I'd write a devnote to help improve my recall.

Typically, `yield` is used in a function with a loop, like so:

{{< highlight python >}}
def some_func(lim):
    for i in range(0, lim):
        yield i
{{< / highlight >}}

``yield`` means the function returns a "generator" that can be used as an iterable in a loop:

{{< highlight python >}}
for val in some_func(5):
    print(val)
{{< / highlight >}}

You can also straight up convert the generator into a list via something like `list(some_func(5))`.

The equivalent function, without using ``yield`` would be something like:

{{< highlight python >}}
def some_func(lim):
    result = []
    for i in range(0, lim):
        result.append(i)
    return result
{{< / highlight >}}

This is definitely the kind of function I've written often! Now that I've actually written it down, ``yield`` is rather straightforward, and hopefully it can help me shorten some of the python code I'll be writing in the future!