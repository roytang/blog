---
date: 2017-08-20 17:28:32
source: stackexchange
syndicated:
- type: stackexchange
  url: https://superuser.com/questions/1242765/unable-to-access-google-services-sporadically
tags:
- networking
- router
- questions
- superuser
- tech life
title: Unable to access Google services sporadically
---

For the past 2 weeks or so now, I've been having issues with my ISP (I'm not in the US, so it's not Comcast or whatever).

Specifically, I often lose access to Google-related sites/services: the search engine itself, Gmail, Google Docs/Drive, Youtube, Google Keep are the ones I use most often. I've restarted my router multiple times already over the past couple of weeks. Same issue is encountered on my desktop (wired), laptop, iPad, phone (when connected over wifi) etc.

I know it's related to my ISP because (a) I've read some other users experiencing similar issues on social media; (b) if I tether to my phone's data connection, the problem isn't encountered.

I don't have a proxy server configured. I used to be using Google DNS but I've also tried switching back to my ISP's default DNS with no luck.

What's the best way for me to figure out what the issue is? (Preferably in a way that I can bring it up to my ISP so that they know specifically what they need to fix - talking to their customer service is a tedious experience so I've decided to figure out as much as possible before going back to them)

Screenshot of the error from the browser:
[![enter image description here][1]][1] 


Sample tracert:
[![enter image description here][2]][2]

Pings seem ok right now (although if I leave ping -t running for a while, there's an occasional "Request timed out"):
[![enter image description here][3]][3]


  [1]: https://i.stack.imgur.com/cin58.png
  [2]: https://i.stack.imgur.com/PB5zP.png
  [3]: https://i.stack.imgur.com/VxB92.png