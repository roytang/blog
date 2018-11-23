---
author: roy
categories:
- Software Development
date: 2010-07-21 07:00:55
title: 'Weekend Project: Stack Bragger'
type: post
url: /2010/07/weekend-project-stack-bragger/
---

<img class="alignnone" title="Sample Post" src="http://stackfb.appspot.com/static/sample-post.png" alt="" width="488" height="141" />

Stack Bragger lets you brag to your Facebook friends whenever you ask new questions or earn new badges at StackOverflow, SuperUser or ServerFault.

I was looking for a weekend project and found out that stackoverflow api was released so I thought I'd make a small facebook app. I originally just wanted to post to FB whenever I got a badge, something like how PSN accounts automatically post Trophies to FB. It also posts questions you ask so that any friends you have on facebook not already using stackoverflow might want to help answer 😀

It turned out to take a bit more than a weekend (mostly because my weekend was busy), but at least it gave me a chance to try out a few things:

1. Facebook's Graph API
  
2. Google App Engine
  
3. DVCS

I've toyed around with Google App Engine before, but now was the first time I got to use it for something more useful than following tutorials or writing random "Hello World". I pretty much got to try all of the relevant services: cron jobs, tasks, memcache, GQL, etc. Everything was well-documented and easy to follow.

Facebook on the other hand&#8230;this whole thing with their Graph API that they want to release the old REST API with makes things a bit confusing when searching for tutorials, as most of them will be referring to the old REST API, including the python facebook wrapper libraries available. It took me a while to get the authentication and setting up permissions thing going. The great thing is I don't need to go through that again for future facebook apps!

This project also gave me a chance to create a [bitbucket][1] account and use a DVCS. I picked bitbucket over github because I prefered to have a private repository and mercurial just seemed a lot easier to use than git.

Here's the [StackApps entry][2]. Originally, I wanted to win their [contest][3], but to be honest that seems a bit far-fetched now. My app comes in late to the game and there was already a facebook app listed there before but it's not ranked too high. Besides, we all know [@codinghorror][4] isn't a fan of Facebook haha.

Am I releasing the source? I dunno yet. I'd have to create a public repo on Github, decide on a license, scrub out my API keys from the code and other stuff, so maybe later.

 [1]: http://bitbucket.org
 [2]: http://stackapps.com/questions/1163/stack-bragger-facebook-app-to-post-questions-badges "StackApps entry"
 [3]: http://blog.stackoverflow.com/2010/05/stack-exchange-api-contest/
 [4]: http://twitter.com/codinghorror