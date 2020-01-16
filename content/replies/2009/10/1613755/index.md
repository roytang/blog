---
date: 2009-10-23 14:14:22
reply_to:
  label: '''How to stop a running *.JAR file with a batch script?'' on stackoverflow'
  name: Faizan S.
  type: stackexchange
  url: https://stackoverflow.com/questions/1563029/how-to-stop-a-running-jar-file-with-a-batch-script
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1563029/how-to-stop-a-running-jar-file-with-a-batch-script/1613755#1613755
tags:
- java
- batch-file
- jar
---

Have your app create a temp file on startup and periodically check if it still exists. Your batch script can just delete that file to terminate the app.