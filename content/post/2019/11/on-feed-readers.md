---
title: "On Feed Readers"
date: 2019-11-18
tags:
- tech life
---

I don't use [Inoreader](https://www.inoreader.com/) anymore, but a recent blog post of theirs recently appeared in my feeds that mentioned [they implemented "sort by magic"](https://blog.inoreader.com/2019/11/new-feature-sort-by-magic-and-article-popularity-indicators.html). This was a feature that [Google reader had 10 YEARS AGO](/2009/10/5149594629/)! There hasn't been much innovation in the feed reader space in the last decade it seems, which is totally understandable given they are mostly tools used by internet "power users", and mostly by older netheads, so the target market isn't very large.

---

When I talk about "feeds" and "feed readers", I'm not talking only about RSS and the associated readers, but anything that lets me aggregate contents from a set of sources. This includes most social media streams (Twitter, etc), I guess Indieweb microformats readers (though I haven't tried these a lot), and apps like [Flipboard](https://flipboard.com/) (which I typically use for my morning news). 

---

Recently I installed a self-hosted [Tiny Tiny RSS](https://tt-rss.org/) to take the place of my primary RSS feed reader. I also previously tried Inoreader and Feedly. The jump to TTRSS was mostly to avoid the free account limitations on those services. TTRSS is fine and it's serviceable, but there's still a lot of improvement I would like. I think about feed reader features a lot because (a) I like reading content from a wide variety of sources and feed readers help me do that; and (b) even back when Google Reader was still around I was kicking around the idea of writing my own feed reader. It's one of those side projects that I want to build for myself but never get around to it. I'll note down a couple of features I've been thinking about in the past decade.

---

The first flaw I find in most readers (including social media feeds) is that they typically treat all feeds the same way. In reality, I would like to be able to treat some feeds differently. I can think of at least two categories:

- feeds where I don't mind missing some of their content (since I don't always have time to read), and don't mind just browsing their latest content like a magazine. Flipboard is great for this. Most social media feeds on the other hand seem to want to pull you away from this model by having their feeds be "algorithmic". And for traditional RSS readers, having unread counts for this type of feed doesn't make sense, and only annoys me and my compulsive need for zero unread counts.
- feeds where I don't want to miss any of their content. Maybe because it's a particular source that I enjoy reading, or because it's a feed I set up for notification purposes or such, or maybe the source is an events page where I want to know all the events they set up. Basically feeds that have a high signal-to-noise ratio for me (although ideally all the feeds I follow have high S/N ratio.) For this kind of feed, the unread counts in traditional RSS readers make sense.

I imagine there could be some in-between categories as well, possibly customizable. Something like a feed where I have unread counts, but also automatically mark as read articles that are too old? IDK.

Facebook actually had something like you could add friends to a "Close Friends" list, and their posts would be prioritized for you and appear in your notification bar. I don't FB much anymore, so IDK if this feature is still around, but as I recall you can't use it with Pages.

---

Another feature I'd like is grouping posts by topic, or the ability to highlight "related stories" for an article from other sources that I'm also following. For example, if there's some breaking news story, and the article about this from NewsSourceA appears in my feed, I could maybe see a link to related articles about the same topic from NewsSourceB, NewsSourceC, and so on that I also follow. Or maybe choose to mark the topic as read or block further content about this topic.

This is one of my major grips when using Flipboard, especially for the "Latest news" sections. There'll be like 5 different articles about the latest Trump meltdown, and I encounter them at different points in the feed. I don't mind reading about Trump meltdowns, but it would be more efficient if I could have each instance only appear in my feeds once. I understand this may be a bit challenging since it involves some automated content analysis though.

---

I must admit I haven't explored too much the paid features of services like Feedly or Inoreader, so maybe they support something similar to these features already. (I feel like it's unlikely though.) In addition to traditional RSS readers though, I'd also like my reader to be able to support following other kinds of sources like social media, ActivityStreams-compliant streams (Mastodon, etc), microformats feeds, and so on.

Maybe someday I'll get around to finally building that feed reader I wanted for myself!