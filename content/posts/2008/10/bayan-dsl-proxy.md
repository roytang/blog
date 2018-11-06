---
title: Bayan DSL Proxy
author: Roy
type: post
date: 2008-10-05T15:45:04+00:00
url: /2008/10/bayan-dsl-proxy/
categories:
  - Tech Life

---
If you&#8217;ve been having trouble with Bayan DSL web connections to some websites (which we have for the past few weeks or so), you may be surprised to know that they have an HTTP proxy server you can use. Strange, considering that when reporting such problems to their trunkline, they never ask whether you&#8217;re using that proxy server or not. I don&#8217;t recall ever being told about it by the Bayan DSL staff.

My brother found out about it last night and lo and behold! The websites we&#8217;ve previously had trouble accessing, such as Yahoo Mail, Multiply, Flickr, etc. have become accessible and Youtube videos now stream well, etc.

The settings are:

HTTP proxy server: proxy.skyinet.net

Port: 3128

You can set these in the options dialog of Firefox, under Advanced -> Network -> Settings.

<div class="flockcredit" style="text-align: right; color: #ccc; font-size: x-small;">
  Blogged with the<br /> <a style="color: #999; font-weight: bold;" title="Flock Browser" href="http://www.flock.com/blogged-with-flock" target="_new"><br /> Flock Browser<br /> </a>
</div>

## Comments

### Comment by Chry Cheng on 2008-10-12 23:13:44 +0000
Had to turn it off because my Mac's Software Update program kept timing out
  
when downloading. 🙁

### Comment by [Roy](http://roytang.net/blog) on 2008-10-12 23:23:35 +0000
You should be able to set the proxy server only for HTTP.

### Comment by Chry Cheng on 2008-10-13 01:36:13 +0000
It was set for HTTP only. Apparently, that's the protocol used by Software
  
Update.