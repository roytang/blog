---
title: "2024 Site Update"
date: 2024-04-04T22:38:04+08:00
tags:
- changelog
- css
toc: true
---

Previously: [2021 Site Update](/2021/03/2021-site-update/)

I've had "Site redesign" on my to do list since [at least January 2023](/2023/01/2023-checklist/) so today I am finally deploying something. Seemed to be an appropriate thing to do right after Easter?

It took me a while because honestly I kept changing my mind on what exactly I wanted (typical user!), so the fact that I am willing to commit to something and deploy it is... a thing I guess?

### Changelog

#### Layout and Sidebar

My main reason for wanting a layout change was I wanted to have a sidebar again (on desktop at least). Which is a bit ironic because in the last site update post (linked above), I said:

> Removed sidebar. Most of the sidebar links for my own use/benefit anyway, and not for the potential blog reader.
> 

It's true; the site does look more cluttered with a sidebar there. But as I often say, I myself am the prime consumer for this site and I often use the navigation links that were previously in the footer to get around quickly and having them at the bottom was very inconvenient.

A [recent blog post on Rubenerd](https://rubenerd.com/making-my-blog-easier-to-use/) echoed the sentiment of wanting a sidebar back:

> Modern blogs aren’t as fun as old ones because fewer people are doing it, but also because modern web design trends have stripped away a lot of what made blogs interesting, discoverable, and accessible. Superficial minimalism has meant people don’t include archive links, metadata, blogrolls, or even RSS icons. And you know what? I’m as guilty of this as anyone.
>

...

> So I brought mine back :). Kinda. My new theme is a riff on one I tried out back in 2004, complete with a sidebar containing all my archives and silly buttons of yore, and metadata under each post. 

Also, having the sidebar be easily visible means I can put things there to promote them or direct people to parts of the site that may be of interest. I have not yet actually updated the sidebar contents that much. The menu is slightly updated, but those are still the same menus that were in the footer before. I am still thinking about what things to put on there. 

Lastly, none of this applies to mobile; the mobile layout remains largely the same, with the sidebar content in the footer.

#### Floating TOC and Back to Top

This one is more help for navigating the site, especially longer blog posts. For such posts I used to enable a TOC that allows the reader to quickly jump to specific sections, but once you're down there, there was no easy way to jump to other sections instead. 

I made the TOC section floating (using CSS `position: fixed`) on the top left, kind of modeled after the Contents Menu in the latest Wikipedia Design. I also added a floating "Back to Top" link on the bottom-right to quickly get back up there, especially handy on mobile when I don't have a home button. One might argue I could put the "Back to Top" link inside the TOC, but not all posts/pages have the TOC.

I tried to find a way to make it so that the "Back to Top" link only appears if you have scrolled the page by some amount, but I could not find a JS-free way to do it. I may add JS for it in the future.

You can see both features on this very page.

#### Webfonts

The fact that I am considering adding more JS for site features is a big deal, as for the longest time I was following a very minimalist site philosophy of "as little JS as possible", mainly to keep the total page size down. I am now a bit more willing to stretch on that end. I do not have a rationale, other than the site is very lightweight anyway especially compared to most of the rest of the modern web. 

To that end, I have been experimenting with using Webfonts. As is typical, I tried a bunch of different fonts and had trouble settling on one. For now I am using [Menlo](https://en.wikipedia.org/wiki/Menlo_(typeface)), this may change in the future.

#### Background Image and Custom Styles for Tags

Mostly for nostalgia reasons I decided to bring back a 2-pixel green and black background image I used in one of the earliest versions of the site I had on the internet. I like the "scanlines" feeling it gives.

I have also added support for adding custom page styles depending on tags; this is mostly because I wanted to have a visual indicator that a post was related to a specific topic. My first attempt is setting different background images depending on the tag. I am not sure how much I am going to customize this - currently you can see it in posts tagged [comics](/tags/comics/) or [software-development](/tags/software-development/). The background images have been reduced in quality to be lightweight.

#### Other minor changes

- New CSS Reset implemented
- Updated menu contents
- Cleaned up and re-styled comment/feedback section
- Re-styled meta block at the bottom of each post, adding badge styles to tags etc
- Added some skew to image gallery thumbnails (this was just a fun thing I wanted to try!)
- Added an indicator to external links: this has been there for a while, just including this in the changelog
- More compact list format for the blog: again, this has been implemented for a while. Some blogs will have the entire post contents in the listing screens, and I can see how that might be nice for an "instant and continuous reading" kind of feel, but it makes it more challenging for me to quickly find a specific blog post if I'm skimming the list. Again, serving my needs first. I may find a different place to put a "full post listings" page elsewhere though.
- Various other small UI tweaks here and there

### To Do List

i.e. things I haven't gotten around to yet. Honestly I had a much bigger scope in mind, but here are some other things I wanted to do that will have to wait. Might try to get around to them within the year. Might not. 

Also, the site has a lot of content, so I almost certainly did not test the new design very thoroughly and so some things or pages here or there may be broken. We'll handle them as we go along.

As always we are [perpetually under renovation](/2019/08/perpetually-under-renovation/).

- Pages to update: front page, now page, about page, etc
- Improvements to how image galleries are presented. 
- Improvements to the media diet listing pages
- Content organization update: I've had some ideas about this for a while now; the site has a LOT of stuff, almost 2000 blog posts and over 10000 notes and 1500 shared links. I've been toying around with some approaches mainly revolving around surfacing and highlighting some older content, but I have yet to settle on a good approach.
- Theme/Color scheme switching. I actually already have theme switching more or less implemented, except (a) for some reason my cookie keeps getting cleared; and (b) I'd have to make actual different themes to switch between, and I it took me a while to just settle on this new one. In the end I even settled on just keeping the color scheme from the last major update! On the other hand, having this functionality available did make it a lot easier to test the new theme locally while the old one was still live on the site.

### CSS Notes

Some CSS stuff I used for this update.

- Reset CSS https://set.studio/some-simple-ways-to-make-content-look-good/
- Responsive font size https://jameshfisher.com/2024/03/12/a-formula-for-responsive-font-size/
- Smallest CSS https://robinrendle.com/notes/the-smallest-css/ (I didn't end up using this, but it was interesting to read)
- Styling external links https://www.paritybit.ca/blog/styling-external-links.html

### That's It

Let's see how long before I get tired of this design! (Honestly I used to change layouts much more often in the Wordpress days!)

This post turned out to be about twice as long as the last one, which may or may not be an indication of how verbose I have become. As is my wont, I have also attached some images of the new site design below.