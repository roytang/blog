---
date: 2009-11-26 06:01:39
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1801804/applets-failing-to-load
tags:
- java
- applet
- questions
- stackoverflow
- software development
title: Applets failing to load
---

While testing our setup for user acceptance testing, we got some reports that java applets in our web application would occasionally fail to load. The envt where it was reported was WinXP/IE6, and there were no errors found in the java console.

Obviously we'd like to avoid it. What sort of things should we be checking for here? On our local servers, everything seems fine. There's some turnaround time when sending questions to the on-site guy, so I'd look to cover as many possible causes as possible.

Some more info:
We have multiple applets, in the instance that they fail loading, all of them fail loading. The applet jar files vary in size from 2MB to 8MB. I'm told it seems more likely to happen if the applet isn't cached yet, i.e. if they've been able to load the applets once on a given machine, further runs on that machine go smoothly. I'm wondering if there's some sort of network transfer error when downloading the applets, but I don't know how to verify that.

Any advise is welcome!