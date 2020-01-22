---
date: 2010-06-30 02:29:40
reply_to:
  label: '''how to detect incoming chat message?'' on stackoverflow'
  name: Hristo
  type: stackexchange
  url: https://stackoverflow.com/questions/3146067/how-to-detect-incoming-chat-message
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/3146067/how-to-detect-incoming-chat-message/3146107#3146107
tags:
- php
- mysql
- ajax
- chat
- ajax-polling
---

You have to use polling, but you can use a technique called Comet which involves long-polling, i.e. sending out an ajax request that will be held by the server until a chat request comes in.

http://en.wikipedia.org/wiki/Comet_(programming))