---
date: 2009-12-02 07:05:32
reply_to:
  label: '''jQuery, how to call a function while passing a variable'' on stackoverflow'
  name: Ankur
  type: stackexchange
  url: https://stackoverflow.com/questions/1831116/jquery-how-to-call-a-function-while-passing-a-variable
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1831116/jquery-how-to-call-a-function-while-passing-a-variable/1831132#1831132
tags:
- jquery
- ajax
- parameter-passing
---

Try wrapping it in a new function object:

    $.get("InfoRetrieve", { },function() { addContent(data) });