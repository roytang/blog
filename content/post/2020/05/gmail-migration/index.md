---
title: "Migrating away from GMail"
slug: gmail-migration
date: 2020-05-27
tags:
- tech life
---

I've basically been using GMail as my main email account since I first got access in 2006ish. "Main email account" means I use it as the primary access point for all my other online accounts. GMail was certainly revolutionary when it came out, and had a lot of benefits: it was fast, easily searchable and had a lot of free storage. But in the modern day, there are significant disadvantages to using GMail:

- you don't control your account; it's rare, but anecdotally people have lost access to their GMail accounts for some perceived infraction, and when that happens you have no way of recovery or appeal
- you're fueling a surveillance capitalism machine
- it can [look unprofessional](/2020/05/1263160405737607170/) to be using free email, especially for official or business correspondence

The first bullet point is the biggie for me. One such story came across the Hacker News front page a while back and I can only imagine the nightmare it would be for me to lose access to my Google account. Since then, I've started a conscious effort to slowly but surely decouple myself from my dependencies on Google Services.

That meant migrating my online accounts to use another email, primarily one I control. I already had this domain [roytang.net](https://roytang.net), so there's no reason to not use emails with that domain. The only risk to using an email on your own domain is that if you forgot to renew your domain, or otherwise lose control, you are screwed. So... don't let that happen I guess?

The only question was what email service provider to use? I'm still on Webfaction hosting, and they do provide email accounts, but I'm planning to move away from them before the end of the year [due to the GoDaddy purchase](/2019/03/rip-webfaction/), so probably best not to be reliant on their email service. If I wanted more control over the risks, I could of course run my own mail servers, but I'm not ready to go that far yet.

The first one I tried was [ProtonMail](https://protonmail.com/) because yay, end-to-end encryption! I used it for a couple of months first before paying for anything (using a custom domain email requires a paid plan). Unfortunately, I felt like the additional security wasn't worth the trouble of not being super portable. Accessing via mobile required their app, can't use any generic email client. I also wanted to be able to access via a desktop client like Thunderbird or Mail on the Macbook Air, but that required some sort of SMTP bridge, and it seemed like a bother. Every time I set up a new machine I'd need it? I'm not super security-conscious, so I decided to keep the protonmail account as a secondary account, in case I did come to a situation where e2e encryption was absolutely critical.

I next tried [migadu.com](https://www.migadu.com) as an email provider, based on [this recommendation thread](https://cmpwn.com/@sir/102452352875414214) by Drew Devault over on Mastodon. Their web settings aren't super refined, but everything was relatively easy to setup. And their free tier includes support for custom domains and multiple mailboxes per domain, so that's a big plus. I've been using them now for a few months and am generally happy with the service. (They did have a short bout of server access issues around the time the covid19 thing started getting around, but they resolved it pretty quickly.)

After choosing an email service provider, the next step was setting up emails and shifting over all my online accounts. Migadu's support for unlimited mailboxes meant I could have separate email addresses for:

- contact email for other online accounts
- publicly accessible contact email on the website
- private email for communication with friends
- etc

I ended up updating over 50 online accounts to point to the new domain email. Not all in one go, as that's terribly boring, but a few at a time over the course of the last few months. That covers social media services, gaming services, financial services, dev tools, and so on. The upside of all this effort is I got to do a kind of audit of all my online accounts, which ones could be deleted/deactivated, which ones needed new passwords, which ones have poor security measures, and so on. 

Theoretically, I only need to do this once. An advantage to using custom domain emails is that if you're unhappy with your underlying email provider, you can switch to a different one while retaining the same email addresses, no need to update emails in all your other online accounts. 

Lastly, I had no intention of using webmail anymore, so I ended up installing Thunderbird (it's been a while old friend) for accessing these accounts, and also set up the Mail app on the Macbook Air. For the phone, I installed K-9 mail, although I'm having an issue with that currently where it doesn't seem to be doing background syncing of mails. Not a super critical issue, as I mostly don't want to be pinged real-time by email anyway.

I'm still keeping the GMail account of course, a lot of people still know me by that email address, but now I have a largely reduced footprint and dependency on it. And as mentioned, I'm also keeping the ProtonMail account for any security-conscious communications. So I ended up having to manage a lot more email addresses, but hopefully everything will be a bit more organized, with every account having a specific purpose.