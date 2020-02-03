---
title: "Tales of the Old Browsers"
slug: old-browsers
date: 2020-02-04
dontinlinephotos: true
tags:
- software development
---

There was this great (and long!) [article that came out recently about the history of CSS](https://eev.ee/blog/2020/02/01/old-css-new-css/). It reminded me a lot of the old days when I started out in web development. So join me in a walk down memory lane as I reminisce about the trials and tribulations of early web development. (This one isn't about CSS as much as that linked article.)

<!--more-->

I started out with web applications during the heyday of the much-maligned Internet Explorer 6, and pretty much the start of the age of webapps. Most of our projects during this time involved government agencies wanting to upgrade from their old existing client-server style systems. Those were often written in programming languages/tools like Delphi, Oracle Forms, PowerBuilder and such. That meant there was a lot of pressure on the web applications we developed to be able to match most of the client-side functionality available in those kinds of programs, which was often a challenge due to the limitations of the HTTP model.

### ActiveX

Typically, the government agencies at that time used only Internet Explorer in their workstations, so we could write our web applications to target just IE specifically. This meant we could use things like ActiveX to attempt to do things browsers normally can't do. Some of it was for security purposes, like confirming the user's authentication matches the current workstation user, or for Single-Sign On purposes, things like that. There were also some for interfacing with things outside the web browser, like document scanners.

We also had to use some ActiveX to get around browser quirks. For example, IE6 had this problem with combo boxes/select elements where the width of the drop window would always match the width of the `select` element, but this means if the `option` text was longer than that width, they would not be readable. We had to make an ActiveX component just to fix this, by making the drop window wider on document load! Sample screenshot recovered from the vaults:

{{< img src="combo.jpg" >}}

Some other ActiveX uses were to do things that would later on become standard features in browsers. Some other examples I can recall:

- spellchecking. We used an ActiveX component from a company called [WinterTree software](https://www.wintertree-software.com/dev/wspell/info.html). I was surprised to find this particular product of theirs is still available, when practically all modern browsers have spellcheck support! I suppose it's still useful for legacy environments maybe?
- we had this one project that needed a complicated graphing diagram. Think about those pinboards with pictures and documents connected by wires that conspiracy theorists use in memes, something like that. These days that kind of thing can be done using modern HTML+Javascript only, but during the IE6 days we were still pretty limited. We used another third-party ActiveX (can no longer recall the component name), that we wrapped in our own Delphi program for customization purposes.

As far as I can tell, we ended up using ActiveX in some projects up to the early 2010s.

### GMail and Ajax

Our initial webapps also did the thing where we would reload the page whenever doing something like going to the next page of results. This was pretty bad user experience-wise, especially compared to the client-server programs of old, which felt a lot more snappy since they were only loading the database results via the database driver, instead of an entire HTML page. By 2005, we were already using Ajax/XMLHttpRequest to get around these limitations in IE6. ([The wikipedia entry](https://en.wikipedia.org/wiki/XMLHttpRequest) says XHR didn't officially exist in IE6, so I'm not sure how we did that, but I'm pretty sure we did). Our main use was for paging search result grids, but we weren't even fetching XML or JSON back then, the XHR response would be the grid HTML itself, which we just plop right where the previous page was. 

I remember I was talking to the SA for the project about ajax, he asked what it was and why we were using it, my explanations was:

> Ajax is "Asynchronous Javascript and XML"; it's a method of using
Javascript and XML data that allows us to make server-side (database)
calls without having to resubmit the entire page.
> 
> We use it because it's cool =p With Ajax, we can do something like allow
the user to re-sort a grid of records without reloading the rest of the
page. It is easier for us to meet the performance reqt.
> 
> If you've seen the Google Maps or GMail webapps, they both use Ajax.

The response was:

> I've used Gmail.  AJas is client side library??? Seems they process very
fast.

(I would later kind of [regret using Gmail as a comparison](/2006/05/gmail-raises-the-bar-for-everyone/)!)

### Cross-browser development

Most of our projects were for internal systems where the workstations had controlled environments so we were free to target a single browser only (usually IE). Some projects also had a public-facing portal though, and that required we do some cross-browser frontend stuff. Early on, the typical targets other than IE where Netscape and Firefox. This is where the IE6 compatibility headaches come in. It was usually a game of write the code for IE first, then let the testers find any NS/FF issues, then quash accordingly.

We started checking in Firefox around the quirks mode era, as described in the article linked at the start of this post. The biggest challenge really was getting everything pixel-perfectly the same between brwosers. The typical problems were:

- browser differences in CSS models (the famous box model issue)
- differences in native controls (typically the `select` and `input type='file'` controls were the more problematic ones)
- for cases where we needed ActiveX plugins for IE6, we would also need to develop corresponding FF add-ins, usually targeting Firefox 2.x (It's fun to think about how the current version of Firefox is 70 major versions ahead of that!)

We did very little cross-browser work at the start, with the proportion accelerating in tune with Firefox/Chrome's rise in marketshare. By around 2010, it was common for projects to be testing across at least 2 versions of IE (6 and 7), 2 versions of Firefox (2 and 3), Google Chrome, and often Safari as well. (We didn't really start thinking about Mac users until around 2007ish).

Google Chrome came out in 2008, I found some old comments I made to our internal tech team when it came out:

> I have an installer in t:\roy
> 
> It's not an OS, but it runs browser tabs in separate processes (literally...each one has a different PID), such that a single webapp won't crash everything else.
> 
> More info here: t:\keis\Google_Chrome.pdf
> 
> If it gets widespread adoption, it may affect the webapps we develop - it uses Webkit as a rendering engine (used by Safari), so it's different from Firefox and IE. Haven't encountered any problems yet though.

I also tested the memory usage of Chrome vs FF back then:

> Try this:
> 
> Firefox - open 9 tabs. Check the memory consumption. Close 8 tabs. Check
the memory consumption. (Remains around the same as previous one)
> 
> In Chrome, the memory usage of closed tabs is 0.

This is a far cry from Chrome's modern reputation as a memory hog! (Although I guess that reputation is probably related to people keeping too many tabs open.)

Side story: while looking up old files for this post, I came upon a thread where we were discussing printing issues across browsers, and there was a problem in printing some pages from the browser because of limitations in IE6, and some management higher-up chimed in with a suggestion to "just tell the client to use IE7" as if the client will magically upgrade all their workstations for that one problem. :shrug:

### jQuery

As the linked article mentioned, jQuery raised the bar when it came out, allowing developers to easily paper over cross-browser JavaScript concerns and providing an API that became so prevalent, years later parts of it would become built-in to modern browsers (i.e. `document.querySelector`).

I shared the link to [jQuery via delicious](/2006/01/jquery-new-wave-javascript/) in 2006, but for sure we weren't using it yet in our projects at that time. Based on my own CV, the first time I used it in a project was in 2009. It quickly became part of our standard libraries. I still remember in one particular project I spent some time thrashing out a bunch of issues because we needed to upgrade from like jQuery 1.3 to 1.4? Or something like that. Normally we'd fix to a certain version, but I think we needed to upgrade because of a jQuery plugin we needed. This was before the modern frontend development frameworks where you already have dependency management tools, so we had to make sure none of our other third-party JS components would break with the upgrade. The company ended up using jQuery as a standard in projects up to the time I left in 2015. (I'm told they later on switched to Vue.js, so more power to them.) 

I identify as a "full stack developer", but these days the "frontend" half of that usually implies usage of one of the modern frontend frameworks: Angular, React, or Vue. While I am cognizant of those frameworks and have tried them all in some form or another over the past few years, my frontend development experience is still largely defined by the jQuery era. So when setting up personal projects or quick prototypes that's still what I default to.

### CSS

The linked article was about CSS, so I figured I should have some CSS stories too, but I find that I don't have much, other than the cross-browser compat above. My main issue with CSS back then was that in a large project with a nontrivial amount of developers each working on separate screens, the CSS style sheets tended to get longer and denser with time. And with bug fixes and whatnot, it would tend to be full of hacks and workarounds like randomly placing `!important` in so many places. I just assumed we had a whole bunch of CSS selectors that were no longer necessary but no one would bother cleaning up the style sheets because who knows what you'll break? Basically a whole chaotic mess. IDK if modern tooling handles this because I haven't been on larger projects since leaving the company, but I suppose the stronger delineation/specialization between frontend and backend dev work means less people to mess up the stylesheets, and those who do handle the styles are more aware of such pitfalls.

### That's it (for now)

Well, this was a fun trip down memory lane. This post is already longer than I thought it would be, but those are all the old-timey stories I can recall right now. There's a good chance there's some more of them lodged in my brain somewhere that will come out sooner or later, so maybe there's a part 2 sometime in the future.