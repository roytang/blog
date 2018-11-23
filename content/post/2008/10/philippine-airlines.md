---
categories:
- Software Development
date: 2008-10-21 06:44:00
title: Philippine Airlines
type: post
url: /2008/10/philippine-airlines/
---

My dad asked me to help book a flight from Manila to Boracay for my uncle who would be a balikbayan this weekend. The rates at PAL were better, so we decided to book using their website. I did the search for the flights, booked the seats, input my uncle's details, etc. When we got to the screen to input the credit card info, my dad went to call my uncle to confirm and to get his credit card. He can't have been gone five minutes. When he came back, I enter the credit card info in the form, click submit&#8230;and I get a session timeout error.

Wow. Their session timeout value is somewhere between five to ten minutes, closer to five. I'm not sure if this is reasonable, especially given that their website isn't that user-friendly to begin with and you may spend some time poring through the flight lists to get one that you want.

Anyway, I figure the credit card hasn't been charged yet since I timed out while entering the CC details, so I go to try again. Search for the flight&#8230;wait, the one with the cheap rate was no longer available!

I figure that while I was selecting dates the first time through their Online Booking application, the backend marked the last seat on that flight as "Reserved" under my uncle's name, but since I timed out before I could pay that seat may now be lost forever.

I figure they probably have some sort of cleanup if the booking hasn't been confirmed (i.e. paid for), so I leave the website for a bit then come back later. I search again, and the cheap flight is there! I get my dad's credit card and proceed to go through the steps again. I get to the credit card form and input the details and click submit. Yay, it's verifying! Checking the status bar though, it seems to be verifying against a MasterCard URL&#8230;but the card I used was a Visa!I was in such a hurry I forgot to tick MasterCard.

Unbelievably, the credit card verification was being done from my machine (since I could see the mastercard URL in the browser status bar), instead of on the server where it could be done more reliably.

Okay, this time it was my fault. No sweat, I'll wait for the website to fail the verification then re-input the credit card details. So I wait. Then wait some more. The website is taking forever and not doing anything. Firefox prompts that the website tried to show a popup. I right-click and enable pop-ups for the website, nothing though. I wait some more.

Damnit, I finally reload the page to find that "my session has expired." Sure enough, I tried to search for the cheap flight and it was no longer available AGAIN.

I give up. I'm not going to try again. Seriously this time. I'll give the credit card back to my dad and just tell him to book manually (and to double check that the card has not been charged.)

I always have a bad time with Airline websites -- I hate the Cebu Pacific one as well. These companies need to get better web developers.

## Comments

### Comment by noems on 2008-10-22 18:57:35 +0000
ayy nako. i'm hating the cebu pacific site right now.

i spent almost the whole afternoon booking and reloading pages. i haven't
  
passed the flight selection yet!

With the heavy traffic of Users specially with their frequent promos, they
  
really should improve the website.

If you can't serve it, don't sell it.