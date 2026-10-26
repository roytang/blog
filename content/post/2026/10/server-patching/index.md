---
date: 2026-10-26 09:03:49
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/117507407460760692
tags:
- tech-life
- cybersecurity
- tech
- server-management
title: Server Patching Notes
---

Previously: [Server Setup Notes: Ubuntu, Nginx, Django, MySQL](/2020/11/server-setup-notes/)

I spent some time last week trying to patch and update my rinky-dink little webserver over here. This was mostly because of the PHP-related vulnerabilities that kind of ran roughshod over the cybersecurity sector last week. For a more detailed discussion of that incident, I found [this post](https://www.garfieldtech.com/blog/php2shell) useful.

Anyway! I took some notes because I suspect in our current GenAI-powered dystopia this will not be the last such incident so I should get used to patching my server.

### Patching PHP

Now, my server uses *some* PHP but not a lot. There was an odd Wordpress instance on a subdomain, and small one-off pages I use for various tasks. I disabled the whole lot of them (or at least tried to, I didn't actually get them all) while I tried to figure out how to do the upgrade. My server was on something like PHP 8.3.x, where x < the "safe" patched version number. But for some reason I found that even when I tried to do the instructed `sudo apt update && sudo apt upgrade -y`, that 8.3.x version number did not budge!

I found out later (after trying many things, some noted below), that the reason the version number wasn't updating is that Ubuntu maintains the same version number of PHP in its repositories, and instead backports important security fixes into it. So I think I already had the fix at the start of the process, I just didn't know it!

So, this part is for future me: you can verify if a CVE has been fixed in your installation using `pro fix`, i.e.:

```bash
root@ubuntu-main:~# sudo pro fix CVE-2026-109619

CVE-2026-109619: PHP vulnerabilities
\- https://ubuntu.com/security/CVE-2026-109619

1 affected source package is installed: php8.5
(1/1) php8.5:
A fix is available in Ubuntu standard updates.
The update is already installed.

✔ CVE-2026-109619 is resolved.
```

That would have been good to know at the start of the process!

### Upgrading Ubuntu

As you can see above, I ended up upgrading to PHP 8.5 as well. This was because one of the many things I tried along the way was to do a upgrade to newer versions of Ubuntu. When I started, I was still on the 20.4 release, which was apparently out of long-term support coverage, so I thought maybe the reason I wasn't getting updated PHP versions was because my Ubuntu version was too old, so I tried doing a release upgrade. I basically did not do a release upgrade since I first set up this server in 2020!

I ran into various errors trying this, which I found out later was because the version was out of LTS coverage, so `do-release-upgrade` wouldn't work automatically. Instead I would end up having to update `/etc/apt/sources.list` myself and do the upgrade manually. 

I found this post on Medium helpful: [How to Duct-Tape, euh I mean, Manually Upgrade an End-of-Life (EOL) Ubuntu System](https://medium.com/aimonks/how-to-duct-tape-euh-i-mean-manually-upgrade-an-end-of-life-eol-ubuntu-system-7d7440ddc027). (Referencing this with a bit of distaste because the author is "AImonks", apparently an AI-Educational publication, whatever that means. Well, the writer claims to be proficient in machine learning, so maybe that's good AI and not GenAI slop?)

I eventually managed to upgrade all the way to version 26.04, which is the current LTS release. I suspect it's better to stay on the most recent version as much as possible, given the likelihood of more vulnerabilities popping up.

### Updating Python and UWSGI and NGINX

With a new Ubuntu version came a new baseline version of Python 3. I decided to install a new venv using the new Python version for my deployed applications. I suspect this was not at all necessary; the whole point of a venv is that my apps can happily keep chugging along with their old Python version despite having a different version than the system-wide Python, but again I figured, better to be on the newer versions.

Setting up the new venv mostly went smoothly, but I had trouble getting the webserver running under UWSGI. I had to dig through logs to find the issue, and it turned out that system-wide UWSGI was still somehow using the old Python version even though our venv was on the newer one, causing problems loading dependencies. 

So it turns out that I needed to uninstall UWSGI and reinstall it again system-wide (overriding a message that told me not to do that), and after that the web application was once again working correctly.

For NGINX, I just had to go through my enabled sites and make sure they were pointing to the updated version of PHP-FPM.

### Enabling PHP again

After all of that was done, I did not restore all the PHP functionality again yet. Only a specific application that I used often and a few PHP pages that were needed. But the Wordpress instance remains down, not sure if I want to bring it back up since it hasn't been used in like a decade. I might decide to convert it to a static site for safety.

### Is running a server still worth it?

Throughout all of this I was seriously considering just giving up on having and maintaining my own webserver. If we expect a flood of more GenAI-powered exploits in the future, it would be annoying trying to keep up. It is super handy for me to have certain functionality available to me over the internet, but there's nothing I can't live without. I can still have a website (purely static and hosted on Netlify or something) even without my Python webapps. But all things considered, I kind of love tinkering around with this website, and I'm not sure I'm at the point where I want to surrender that little pleasure to our GenAI dystopia, so for now we soldier on.

(I must note that having the previous blog post about the server setup available was super helpful for figuring out how I set all of this up in the first place!)