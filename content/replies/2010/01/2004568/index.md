---
date: 2010-01-05 06:39:39
reply_to:
  label: '''How can I make JavaScript make (produce) new page?'' on stackoverflow'
  name: M. A. Kishawy
  type: stackexchange
  url: https://stackoverflow.com/questions/2004555/how-can-i-make-javascript-make-produce-new-page
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/2004555/how-can-i-make-javascript-make-produce-new-page/2004568#2004568
tags:
- javascript
- html
- web
- printing
---

    var w = window.open("");
    w.document.writeln("<the html you wanted to write>")