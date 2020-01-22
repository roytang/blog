---
date: 2011-12-13 03:03:22
reply_to:
  label: '''How to redirect to specified page after session timeout'' on stackoverflow'
  name: palAlaa
  type: stackexchange
  url: https://stackoverflow.com/questions/8483809/how-to-redirect-to-specified-page-after-session-timeout
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/8483809/how-to-redirect-to-specified-page-after-session-timeout/8483836#8483836
tags:
- java
- jsp
- session
- servlets
- redirect
---

How are you redirecting to the login page? At that point you should store the originally requested URL somewhere (can be in session, or request param that you pass around) such that you can redirect back there after he logs in again