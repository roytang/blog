---
title: COM Surrogate Has Stopped Working Error in Vista
author: Roy
type: post
date: 2009-01-01T18:16:48+00:00
url: /2009/01/com-surrogate-has-stopped-working-error-in-vista/
categories:
  - Software Development

---
For the past few months, I&#8217;ve been encountering the COM Surrogate Has Stopped Working Error in Windows Vista, as described [here][1]. Unfortunately, most of the recommended fixes on this page didn&#8217;t work for me. (I had neither DivX nor Nero installed, etc.) Eventually, I had to download [InstalledCodec][2] and use trial and error disabling of all the codecs in my system to trace the problem. I narrowed it down to the Xvid Codec and ended up having to disable it.

 [1]: http://www.howtogeek.com/howto/windows-vista/fix-for-com-surrogate-has-stopped-working-error-in-vista/
 [2]: http://www.nirsoft.net/utils/installed_codec.html