---
date: 2023-08-18 14:51:29
subtitle: Or "Don't Trust Lazada with your Payment Details"
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/110911426683108749
tags:
- tech-life
title: Stolen Phone Post Mortem
---

Previously: [What To Do When Your Phone Is Stolen](/2023/08/what-do-phone-stolen/)

I've been using Lazada for a while (more since the pandemic started), and knew enough to never link my credit cards to it and always do cash on delivery. However, in a moment of weakness, I paid for one transaction by linking my GCash account to Lazada (also because I wanted to spend the money in the GCash account).

Fast forward some time later, and [someone steals my phone](/2023/08/what-do-phone-stolen/). Sure enough, by the time I get home there is a notification that my Lazada password has been reset. At first I'm not too worried because I know I always do cash on delivery. But then I get a notification that a purchase was made using Lazada Wallet funds. What Lazada wallet funds, I didn't have any money in there?!? It actually took me a while to figure out that they were able to load my Lazada Wallet via the linked GCash account. I filed a support ticket with GCash to temporarily disable the account, but apparently it was too late by then.

I was able to recover and reactivate both my Lazada and GCash accounts a few days after getting a replacement sim and sure enough that's what happened. The point is: Lazada is super easy to breach because you can password reset using only the phone. (Even if you remotely locked your device like I did, they can just move your SIM to another phone.) 

I tried to contact Lazada support to see if they could reverse the transactions and recover the lost money, but apparently their process requires me to file a police report! I do not have a high regard of PH law enforcement and have managed to spend all my life not transacting with them in anyway, so I would rather not start now. The amount lost wasn't that large (much less than P1000) and for me was not worth the time and hassle of having to deal with the police, so I just gave up. Not before complaining to support about their lax security and stupid requirements; credit card companies can detect fradulent transactions themselves and reverse them easily without involving the police, so online stores like Lazada should be able (and even required) to do as well I reckon.

I spent a good part of that week unreasonably angry at the circumstances; at myself for being so careless that my phone got stolen; at Lazada for their lax security and stupid policies; and most definitely at the thief who stole my phone and took money from me. I even managed to gather some clues - I have the phone number, email address and phone model used by the thief. The first two were easily traced because they had to send their fraudulent digital purchases somewhere. The phone model I was able to find out from the access logs from the compromised email account I was able to recover. For a while I fantasized about using these clues to track down the perp and terrorize them in some manner. Of course it doesn't make sense to spend even more time on the matter, but it was nice to imagine.

I had also reported the fraudulent transactions to GCash support, but they were also unable to do anything. I wasn't too mad at them because it looks like the GCash account itself was never breached. Apparently attempting to access it without the MPIN requires both an SMS code and facial recognition, so GCash itself is more secure than Lazada. Also, I suspect the GCash account of the thief has been suspended; when I first got my GCash account back I was able to see their initials if I tried to send them money via the GCash app; today trying to send money to that number already raises an error.

Long story short: Don't link your e-wallets or bank accounts or other such payment platforms to insecure platforms like Lazada. I still use Lazada (it's super convenient, sigh), but strictly COD from now on.

My anger at the situation has largely subsided, and I am writing this post mostly so I can move on.