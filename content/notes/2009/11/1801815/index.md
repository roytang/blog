---
date: 2009-11-26 06:07:40
reply_to:
  label: '''How do I change the location of index.jsp in a war file'' on stackoverflow'
  name: Ankur
  type: stackexchange
  url: https://stackoverflow.com/questions/1801787/how-do-i-change-the-location-of-index-jsp-in-a-war-file
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1801787/how-do-i-change-the-location-of-index-jsp-in-a-war-file/1801815#1801815
tags:
- java
- web-applications
- web.xml
---

The contents of WEB-INF aren't publicly accessible resources, why are you putting the other jsps there? Are those other jsps accessible?

If you want to hide the index.jsp, create a servlet mapped to the root path and have it forward to index.jsp.