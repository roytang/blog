---
date: 2020-03-24
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/103875831680911288
- type: twitter
  url: https://twitter.com/roytang/statuses/1242287539836162048/
tags:
- tech life
- software development
title: Browsers and HTTP
---

Drew Devault wrote a great post/rant about [the reckless limitless scope of modern web browsers](https://drewdevault.com/2020/03/18/Reckless-limitless-scope.html):

> I conclude that it is impossible to build a new web browser. The complexity of the web is obscene. The creation of a new web browser would be comparable in effort to the Apollo program or the Manhattan project.

For the past year or so, I've been thinking about contributing to an open source project. Haven't gotten around to it yet, but I have looked at a few projects of interest. Preferably it's something I use on an every day basis, so Firefox was one of my candidates since it was my web browser of choice. I decided to try it out last month; I followed the instructions on their site for checking out the source and building the code. I assumed there would be a lot of code, and that the build would be a nontrivial amount of time, but just checking out the source and creating a build took the better part of a day; I believe the build itself took somewhere around 4-6 hours (I didn't really record how long it took, just left it running while I went out and did stuff.) I haven't actually tried hacking on the code itself yet, because with that kind of build time, I don't see how one can be productive. (I decided to run the build a second time as I write this post, maybe it speeds up on successive builds?) It's kind of intimidating to get into.

The point is: Drew is right, and modern browsers are massive pieces of software. The comparison to the Apollo or Manhattan programs may even be understated; even though your browser isn't taking people to the moon or testing nuclear weapons, it's probably using way more memory than those programs combined!

Somewhat related: Great post recently over on the Cloudflare blog about the [History of the URL](https://blog.cloudflare.com/the-history-of-the-url/). One can't talk about the history of the URL without talking about the history of the internet of course, and this post let me learn a lot more about those early days of the internet. One of my key takeaways is that a lot of the design decisions around URLs and the early internet made by people like Tim Berners-Lee largely intended the web and the HTTP protocol to be used for serving text-based documents. It's even in the name of the protocol: hyper*text* transfer protocol.

And that's what it was in the early days. People put up documents and web pages, and other people read them and maybe posted comments or other input and that was it. But the modern web (and thus modern web browsers) have tacked on so much functionality onto the presumably text-based protocol. First we added the ability to serve images and videos, then whole applications, formerly the domain of native apps. Just looking at my commonly-used websites, the web browser is used these days for:

- full-featured email applications (GMail, ProtonMail)
- a complicated social media interface with multiple streams that automatically update (Tweetdeck)
- watching videos, tv shows and movies (Youtube, Netflix)
- instant messaging with groups and voice chat (Messenger, Discord)
- rss feed reader (Inoreader)
- note taking and productivity (Trello, Notion)

With systems like Google Stadia, you can even play AAA games via the web browser now!

In the early days of the internet, all of those would still be native apps running outside the browser but these days we overload the poor HTTP protocol to handle all of these functions. The modern browser these days is almost comparable to an entire operating system (and there are of course already ChromeOS and FirefoxOS to drive home this point). 

I understand full well the benefits of overloading the browser and the HTTP protocol to handle all of these applications, but the scope creep is definitely unsustainable. The high resource usage of modern browsers and web pages even moreso. Imagine a new web browser that cuts off support for the evolving W3C specs at a certain point to compete on performance and stability instead. 

How about one that's "just a browser", literally just for browsing documents. Maybe one without JavaScript support completely, if you open a page that has SCRIPT tags, it will prompt you to open the OS-level browsers like Firefox or Chrome? Many modern applications could probably work without JavaScript, except users would have to do without many of the bells and whistles we've come to expect from modern webapps. i.e. clicking "Refresh" instead of timelines auto-updating, clicking "Next" instead of having infinite scroll, and so on.

The never-ending scope creep reminds me of the never-ending growth pursued by late-stage capitalism; it can't be sustainable in the long run, and maybe we need to start looking for different models other than "the browser does everything and will eventually become the OS." (At that point, everything will have been subsumed by JavaScript)!