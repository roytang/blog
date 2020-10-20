---
categories: []
date: 2019-07-30 03:06:26
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1156241920361938950/
tags:
- hugo
- Meta
- Tech Life
- changelog
title: Move Fast, Break Things
dontinlinephotos: true
---

As is my wont, I'm almost never satisfied with a website's layout, so I've been tinkering with this blog's layout on the backend. To make a long story short, I decided to start working on [a Hugo theme](https://github.com/roytang/hugo-theme-exhale). It's still largely a work in progress, as there's a bunch of things I wanted to implement. But it was good enough to replace the old one so I went ahead and deployed it, so maybe some bugs here and there on some pages. And I'm still tinkering, so probably some minor/major changes as we go along in the next few weeks. Or months. Who knows how long it will take? There were some conflicts with the old theme and the new theme which meant I had to modify some of my main blog files to support the new theme and the amount of uncommitted changes I had was getting unwieldy, so I figured I'd just "move fast and break things", as it were. (I realize that a more sensible programmer would have done the theme work on a branch to avoid this nonsense, but we are who we are.)

Anyway, here's a snapshot of the current appearance, for posterity:

{{% img src="hugo-theme-2019" %}}

I've also back-updated some of the older posts where I updated the site theme/layout with a tag [changelog](/tags/changelog/), so that I can reference them when I update the about page sometime soonish.

Aside from my general finnickiness about wanting a new theme approximately every 17 days, another reason I wanted to change the layout was I wanted to try out CSS grid layouting, as it seemed neat and boy I wish this existed back in the IE6 days. Would've made things a lot easier.

I've also kind of gone down the rabbit hole of [Indieweb](https://indieweb.org/) stuff. The core message of having your own website that contains all your content appeals to me and also aligns with some things I've been thinking about implementing like importing all of my off-site content into this site as a central repository. Those things are yet to come but with the theme change I've also started looking into stuff like microformats (should be supported as of now), webmentions, POSSE, and so on. Might be a while before those other things get done though.

I full technical breakdown of the theme features belongs in [the theme's README](https://github.com/roytang/hugo-theme-exhale/blob/master/README.md) and probably in a separate colophon post later on, but we're not there yet and we'll get there when we get there.

For now, enjoy if you will my obsession with the color green.