---
date: 2010-10-17 03:01:52
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/3951840/how-to-invoke-a-function-on-an-object-dynamically-by-name
tags:
- python
- questions
- stackoverflow
- software development
title: How to invoke a function on an object dynamically by name?
---

In Python, say I have a string that contains the name of a class function that I know a particular object will have, how can I invoke it?

That is:

    obj = MyClass() # this class has a method doStuff()
    func = "doStuff"
    # how to call obj.doStuff() using the func variable?