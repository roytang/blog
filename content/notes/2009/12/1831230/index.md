---
date: 2009-12-02 07:37:51
reply_to:
  label: '''Is there a tuple data structure in Python'' on stackoverflow'
  name: Priyank Bolia
  type: stackexchange
  url: https://stackoverflow.com/questions/1831218/is-there-a-tuple-data-structure-in-python
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1831218/is-there-a-tuple-data-structure-in-python/1831230#1831230
tags:
- python
- tuples
---

You can have an array of 3-item tuples.

    arr = [ (1,2,3), (4,5,6), (7,8,9)]
    for (k, v, x) in arr:
      # do stuff