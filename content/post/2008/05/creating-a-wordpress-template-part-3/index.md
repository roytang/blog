---
categories: []
date: 2008-05-12 20:00:00
tags:
- wordpress
- Software Development
title: Creating a WordPress Template Part 3
type: post
url: /2008/05/creating-a-wordpress-template-part-3/
---

[Part 1][1]. [Part 2][2]. Moonglove Winnower template is currently live on [Roy on Magic][3].

I made several color and formatting changes since the last update. Relatively easy due to the stylesheet. I also had to scrap the CSS hack for implementing equal height columns, it was causing problems with anchors in the URL. I went with a 1-pixel high background image instead.

Currently most of the PHP logic/heavy lifting is done in sidebar.php while most of the formatting stuff is handled in the stylesheet. Since I'm copying from an existing template and not creating one from scratch, I didn't actually need to learn much PHP. Most of it was moving code around.

I'm not releasing this source yet because:
 
  


  * The code is still very messy 
  * It still doesn't work properly with WordPress Widgets 
  * I still have some improvements I want to make. The search box is missing for instance. 
  * I'd like to release some variations (featuring other Magic card art) at the same time. 
  * It's not yet XHTML-valid. The autocard plugin in particular is causing problems. 


   
Still, the current one is functional enough that I don't mind using it on the site.

Most of the difficulty so far has been the design part: thinking about colors, how things should be arranged, etc. As an engineer, it's not one of the things I'm used to doing. I can't imagine I would be able to do some of the fancy, complicated layouts anytime soon, though I might be able to create simpler, minimalistic ones first.

 [1]: /2008/04/creating-a-wordpress-template-part-1/
 [2]: /2008/05/creating-a-wordpress-template-part-2/
 [3]: /tags/magic/