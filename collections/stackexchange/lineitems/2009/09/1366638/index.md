---
date: 2009-09-02 09:20:42
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1366638/embedding-videos-in-web-pages-firefox
tags:
- video-streaming
- questions
- stackoverflow
- software development
title: Embedding videos in web pages/Firefox
---

I'm writing a webapp that would run on a device using Firefox to display a bunch of videos. The videos can be huge, up to HD quality, and would be using a large display.

I would like to be able to queue videos, i.e. have them run one after another. I'll also have some ajax checking if there are new videos to be displayed, so I need to be able to dynamically load them. I also have some script that I need to run between videos, so I need to be able to respond to the end of each video.

Note that I'm in control of the environment, so I can make sure the needed plugin (Flash player or QuickTime, etc) and codecs re installed on the machine.

The question is: what's the best video format for me to use? FLV or MP4? What technologies should I look into?