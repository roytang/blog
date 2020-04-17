---
date: 2020-04-17
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/104012199125124756
- type: twitter
  url: https://twitter.com/roytang/statuses/1251015056147410945/
tags:
- software development
- html
title: Pure HTML Toggles
---

Just last month, I wrote a method of implementing [element toggles using a pure CSS approach](/2020/03/pure-css-spoilers/). While that post was educational for me, it turns out there was an even simpler way of doing things. I found out about it when I read this [post by Jamie Tanna](https://www.jvt.me/posts/2019/05/19/html-toggle/). Apparently the `details` and `summary` tags already support HTML toggles, so we can do this with neither CSS or JS! 

I've updated the spoiler tags on this site to use this new method. I also used this method for the Table of Contents on certain posts (currently only the [Covid19 diary](/2020/03/covid19/)). Sample here:

{{% spoiler %}}This is some text!{{% /spoiler %}}

The post I linked above covers most of the technical details. My only issue with this is that's a relatively new feature. Even though browser support is near universal (minus the much-maligned and quite ancient Internet Explorer), I'm not sure if there will be issues or how it renders when viewed in an older browsers or in other contexts such as in a feed reader or a screen reader. I don't want to accidentally show spoilers! I suppose that's a minor concern at this point, and maybe I should just be confident that people who make those tools have taken the visibility toggle into account.

(I've also edited the CSS post to point to this one so anyone who sees it has better information!)