---
author: roy
categories: []
date: 2018-11-07 05:06:56
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1060037520895959045/
tags:
- Software Development
title: Version Issues
type: post
url: /2018/11/version-issues/
---

SCM (Software Configuration Management) doesn&#8217;t just refer to version control for the software you&#8217;re building. It also means controlling the versions of software you depend on. This includes operating system and programming runtimes. Sometimes even minor version differences can cause issues in running your software. I have two example stories to share:

  1. One of our clients asked us for help with an upgrade their production servers from CentOS 6.4 to 6.9. It was supposed to be a straightforward yum upgrade, which meant of course there would be a problem. The problem turned out to be one of the SOAP calls to a third-party service. After a bunch of retries and log checking, we found that OpenSSL was complaining that the third party&#8217;s certificate didn&#8217;t have enough bits in the Diffie-Hellman (DH) parameters. Complaining to the third party would have taken forever, so we had to find a workaround ourselves. I had previously been told that OpenSSL was the same version before and after the upgrade, but after we did our own checking, we found that there was a minor version difference. That led to a lot of searching until I managed to [find release notes from Red Hat][1] (which was upstream of CentOS). The release notes linked us to [this bug][2] which gave us the workaround we needed.
  2. I had been working on a Python script that would fetch JSON from an external URL and process it. Local dev environment was running Python 3.6. Everything worked well. When I went to deploy it to my server, I found that my host only supported Python 3.5. I was like surely there wouldn&#8217;t be a problem, so of course there was. It turns out the [json load functions added support for binary inputs in 3.6][3], which I had been using all this time. I ended up using a codecs workaround from [this Stackoverflow post][4] which happened to work well in both versions.

 

 [1]: https://access.redhat.com/errata/RHBA-2017:0660
 [2]: https://bugzilla.redhat.com/show_bug.cgi?id=1335921
 [3]: https://docs.python.org/3/whatsnew/3.6.html#json
 [4]: https://stackoverflow.com/questions/6862770/python-3-let-json-object-accept-bytes-or-let-urlopen-output-strings