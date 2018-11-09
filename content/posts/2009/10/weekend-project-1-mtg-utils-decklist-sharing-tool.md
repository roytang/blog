---
categories:
- Software Development
date: 2009-10-03 18:18:03
title: 'Weekend Project #1: MTG Utils Decklist Sharing Tool'
type: post
url: /2009/10/weekend-project-1-mtg-utils-decklist-sharing-tool/
---

I&#8217;ve been meaning to write a nontrivial app using [Google App Engin][1]e for a while, and here&#8217;s my first weekend project: [Decklist Sharing Tool][2], an tool for MTG players to share decklists online. 

I had the decklist parsing and autocarding code available for a while (and used on my MTG related posts), so that part was fairly easy, I got it done under 3 hours I think. The rest of the time (around 5-ish hours) was spent on glue logic, fixing minor bugs, working on HTML layout, cleaning up text, etc. It feels pretty good for a one manday effort, let&#8217;s see if it breaks down. Not the best code I&#8217;ve ever written though (until the latest upload the main class was named &#8220;hello.py&#8221;)

Some notes:
  
&#8211; the Django template engine included with GAE seems to be earlier than version 1, as the escapejs filter wasn&#8217;t available and I had to write it myself. Still, being familiar with the Django template engine helped a lot
  
&#8211; WordPress.com blogs don&#8217;t allow Javascript inside the posts, so the blog sharing code I provide won&#8217;t work there. It works on Blogger though. I&#8217;ll look for a workaround&#8230;(iframes?)
  
&#8211; I&#8217;ve yet to try using memcache, so the current version doesn&#8217;t cache anything, I mean to try it in a future version
  
&#8211; yes, I put adsense ads there. I was like, why not? 😀

 [1]: http://appengine.google.com/
 [2]: http://mtg-utils.appspot.com/deck/

## Comments

### Comment by Some anonymous person on 2009-10-04 11:26:11 +0000
"Posted by by roytang on Sat 03 Oct 2009 as a deck for Standard"