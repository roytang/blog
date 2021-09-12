---
title: "Mobile and Tablet Browsing Annoyances"
date: 2021-09-13T06:54:13+08:00
tags:
- tech life
---

### 1 

There was this link that did the rounds a couple of weeks ago: [How I experience the web today](https://how-i-experience-web-today.com/). It's an accurate depiction of the many issues with the modern-day web.

Such issues are already annoying on desktop web, but are often exacerbated and hence much worse on platforms such as mobile or tablets, especially given the more limited screen real-estate.

Not just screen space, system resources are often scarce on these systems too. All of the popups and ads and whatnot inevitably tend to slow down the mobile / tablet experience. The worst case scenario has to be on iOS, where the aggressive OS resource management often means that if I haven't restarted the tablet in a while, browser tabs (including in-app browser) will often randomly just decide to crash rather than load any overly complex web pages.

The above is mostly a problem when I'm using Flipboard for browsing the morning news, since I find that a lot of news sites are the worst offenders when it comes to web annoyances. I've been [meaning to quit using Flipboard](/2021/01/goodbye-flipboard/) because of this performance issue, but I keep coming back because I can't find a good set of RSS feeds to replace the news I get from Flipboard.

### 2

Speaking of Flipboard, another major annoyance for me when browsing via non-browser apps on mobile and tablet is the use of in-app browsers instead of opening pages in my preferred browser (Firefox on both Android and iOS). 

The main problem with in-app browsers is that they don't share the session of your default browser, which means you have to sign-in again etc. Maybe that's something you want, but you know, the reason I like staying signed on in my devices is the convenience. 

I'm not subscribed to news sites with paywalls, but I always imagine that to be a disincentive to pay for a subscription, since my method of reading them (i.e. Flipboard)  will require me to sign in every time.

### 3

Relevant to the above problem is the "I have your app installed, why doesn't this link open in the app?" I encounter this mostly with Twitter or Reddit links, i.e. the links will load in browser (or the in-app browser) instead of the app which I have installed on my phone/tablet, and this often results in me being annoyed that I'm prompted to log in or worse, prompted to open the link in the app. Why didn't the OS do that already?

Anecdotally, iOS seems to be better at this than Android - I encounter this issue far more often on my phone. 

### 4

Another problem is apps that do launch external links in the browser will sometimes use the wrong one, i.e. the system default instead of what I've set as my primary browser. On Android, that means Chrome, while on iOS that means Safari. I installed Firefox on both my Android phone and my iPad specifically because I wanted to support it! And opening links on some other browser means that once again I don't have access to the session and such from my regular browser. And sometimes I don't even notice a link has opened in Chrome before I shift to a different app, so I end up having a lot of open tabs in my mobile Chrome app (I never keep a lot of tabs open on mobile). When I do notice, I make sure to close all of the pending tabs.

### 5

I also dislike sites having mobile-specific URLs. Like how if you open a link to a tweet in your browser it redirects to mobile.twitter.com instead of to the canonical URL at the root twitter.com domain. It makes link-sharing more complicated, since sharing links to the same thing from different platforms will have different URLs. 

This feels a bit nitpicky, but for example it matters when I share something to [pocket](https://getpocket.com) because the backend process that imports pocket links to the [links page](/links) on this site uses the URL as key to detect duplicates. So if I mistakenly share something twice but from different platforms and they have different URLs, I'll end up having a duplicate.

The same thing should have the same canonical URL! Facebook is another big offender in this regard, since IIRC the same Facebook post can be linked to in several different ways (including a mobile-specific subdomain as well). Not really a problem for me anymore since [I no longer use Facebook](/2020/06/quitting-facebook/).

Anyway, mobile-specific URLs are silly. If your server can detect that I am on mobile, you can certainly just serve me the mobile version of the site at the same URL, without needing to redirect me to a different subdomain!

### 6

Basically what I want my tablet / mobile browsing experience is:

- I can browse using my primary browser (Firefox) and any native apps I choose to use
- links opened anywhere open in the native app for the site in question, if it's installed, or in my primary browser otherwise
- I don't mind apps having an in-app browser

### Notes

- there was a great article / blog post I read recently also complaining about the problems with in-app browsers, which was part of the impetus for this post. Sadly, it looks like I failed to store the link anywhere and I couldn't find it anymore. Maybe some kind soul will read this and know what I'm talking about and send me a link
- I admit that it's possible many of these annoyances might have simple solutions or workarounds that I haven't found yet but I'm lazy so I thought I'd do the internet thing and just complain about them
- I've been meaning to construct an experiment to document exactly which apps on each platform have which problems but again, I'm lazy (see above) so I'll just write this blog post without experimental data
