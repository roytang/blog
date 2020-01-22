---
date: 2010-08-07 22:28:39
reply_to:
  label: '''how i can i change the content of a page without refreshing'' on stackoverflow'
  name: djd
  type: stackexchange
  url: https://stackoverflow.com/questions/3432273/how-i-can-i-change-the-content-of-a-page-without-refreshing
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/3432273/how-i-can-i-change-the-content-of-a-page-without-refreshing/3432287#3432287
tags:
- php
- javascript
---

If you use a hidden frame, the content won't be displayed (hence "hidden"), I think you just mean to use an iframe. But this doesn't fit your description of "without refreshing", since you have to refresh the frame.

When loading the PHP file inside the frame, your PHP file just needs to generate HTML the same way you would generate a normal page. It's the same whether the PHP file is loaded inside a frame or not.