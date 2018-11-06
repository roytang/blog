---
title: Creating a WordPress Template Part 3
type: post
date: 2008-05-12T20:00:00+00:00
url: /2008/05/creating-a-wordpress-template-part-3/
categories:
  - Software Development

---
[
    
Part 1
   
][1] 
   
.

[
    
Part 2
   
][2] 
   
.

Moonglove Winnower template is currently live on
   
[
    
Roy on Magic
   
][3] 
   
.

I made several color and formatting changes since the last update. Relatively easy due to the stylesheet. I also had to scrap the CSS hack for implementing equal height columns, it was causing problems with anchors in the URL. I went with a 1-pixel high background image instead.

Currently most of the PHP logic/heavy lifting is done in sidebar.php while most of the formatting stuff is handled in the stylesheet. Since I&#8217;m copying from an existing template and not creating one from scratch, I didn&#8217;t actually need to learn much PHP. Most of it was moving code around.

I&#8217;m not releasing this source yet because:
 
  


  * The code is still very messy 
  * It still doesn&#8217;t work properly with WordPress Widgets 
  * I still have some improvements I want to make. The search box is missing for instance. 
  * I&#8217;d like to release some variations (featuring other Magic card art) at the same time. 
  * It&#8217;s not yet XHTML-valid. The autocard plugin in particular is causing problems. 


   
Still, the current one is functional enough that I don&#8217;t mind using it on the site.

Most of the difficulty so far has been the design part: thinking about colors, how things should be arranged, etc. As an engineer, it&#8217;s not one of the things I&#8217;m used to doing. I can&#8217;t imagine I would be able to do some of the fancy, complicated layouts anytime soon, though I might be able to create simpler, minimalistic ones first.

 [1]: http://roytang.net/blog/2008/04/creating-a-wordpress-template-part-1/
 [2]: http://roytang.net/blog/2008/05/creating-a-wordpress-template-part-2/
 [3]: http://roytang.net/magic/