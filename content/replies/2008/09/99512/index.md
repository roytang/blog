---
date: 2008-09-19 04:02:11
reply_to:
  label: '''Would it be useful to include the class name and variable name in any
    NullPointerException message?'' on stackoverflow'
  name: James A. N. Stauffer
  type: stackexchange
  url: https://stackoverflow.com/questions/99302/would-it-be-useful-to-include-the-class-name-and-variable-name-in-any-nullpointe
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/99302/would-it-be-useful-to-include-the-class-name-and-variable-name-in-any-nullpointe/99512#99512
tags:
- java
---

Yes, that would be useful. Especially if you have a mechanism where the error message (`exception.getMessage()`) is displayed on-screen but the actual stacktrace gets hidden away in log files which you can't access immediately.