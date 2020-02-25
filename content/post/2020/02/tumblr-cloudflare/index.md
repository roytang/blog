---
title: "Apparently Tumblr custom domains don't work well with Cloudflare"
date: 2020-02-26
slug: tumblr-cloudflare
tags:
- tech life
---

I used to host my tumblr blog on a custom domain at [tumblr.roytang.net](https://tumblr.roytang.net). That was working fine for a while.

Then recently I decided to play around with having [Cloudflare](https://www.cloudflare.com/) in front of my site (might be helpful on the off-chance I ever manage to go viral somehow). Not yet sure whether Cloudflare was a good idea, but apparently it doesn't play well with Tumblr's custom domains, so the above custom tumblr URL got turned off.

Now, I don't actually care about the tumblr blog anymore and have no intention of updating it further. All the content from that blog has already been [imported into this site](/source/tumblr) anyway. But those imported posts still have a link pointing back to the original URL. I'm not a fan of link rot on the web, and I want to minimize it as much as possible, so I was OC'ed into fixing it.

First idea was to just find-and-replace all the old links on this site to point to where the tumblr blog now lives. It would be super straightforward since it's just file updates. But other sources out in the wild may be pointing back to the original URL, and I don't want to give them link rot either.

I tried to figure out a solution with the Tumblr and Cloudflare DNS settings for around ten minutes before saying "screw it" and set up a redirector from [tumblr.roytang.net](https://tumblr.roytang.net) to [roytang.tumblr.com](roytang.tumblr.com), which is where the tumblr blog now lives. It was a simple `.htaccess` redirect like so:

`RewriteRule ^(.*)$ https://roytang.tumblr.com/%{REQUEST_URI} [R=301,L]`

(Someday when I migrate off shared hosting/apache, I will have to live with rewriting all of these .htaccess workarounds to work with Nginx or such.)

So now all the old links just automagically redirect to the appropriate post as expected. 

(Just for fun, I also changed the tumblr's theme, since I was already logged in to the dashboard anyway.)