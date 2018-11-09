---
author: roy
categories:
- Software Development
date: 2016-12-29 01:30:36
title: Cleaning up your Code
type: post
url: /2016/12/cleaning-up-your-code/
---

In one of my most recent projects, a large system that had gone through a relatively long and unstable period of many, many changes due to sales demonstrations, different clients and whatnot, one of the &#8220;fun buffer tasks&#8221; I always kept around for devs was code cleanup. Because of the unstable nature of the project, there was always a lot of duplication, unused/unnecessary/obsolete classes/functions/files and so on. Unnecessarily large CSS files where most of the selectors were no longer really needed or JS libraries that weren&#8217;t actually used. That kind of thing.

It&#8217;s one of those things that you&#8217;ll never get official approval from management to do, so you have to somehow sneak it in during your daily tasks. But it&#8217;s important for a couple of reasons:

  * Having too much cluttered code makes your system a lot harder to grok. That means new developers will have a much higher learning curve, and existing developers will find it difficult to be assigned tasks in modules and functions they&#8217;re not familiar with. Lower understanding means more bugs, lower quality and so on.
  * Having a lot of unused files, classes, functions, etc. bloats the build process (making build times longer, extending development cycles) and makes build files bigger (extending deployment times)

A lot of developers prefer not to throw away old code, for fear that &#8220;we might need it later&#8221;. They would prefer to just comment them out in large blocks (making the code a lot more unreadable) or just leaving dangling functions/classes unused. The reason is hogwash of course, since you should be using source control, and source control means never being afraid to delete old code. (Of course, you should make sure what you&#8217;re deleting is really no longer in use!)

&nbsp;