---
date: 2010-12-17 14:25:54
reply_to:
  label: '''How many times can I have jQuery&#39;s document ready function declared
    on a page?'' on stackoverflow'
  name: Kev
  type: stackexchange
  url: https://stackoverflow.com/questions/4471349/how-many-times-can-i-have-jquerys-document-ready-function-declared-on-a-page
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/4471349/how-many-times-can-i-have-jquerys-document-ready-function-declared-on-a-page/4471375#4471375
tags:
- javascript
- jquery
---

As many times as you like. They fire in order of declaration.

`$(document).ready()` will fire when the document is ready (when it's all loaded by the browser). The other one will fire as soon as that part of the script executes.