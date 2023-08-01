---
title: "What To Do When Your Phone Is Stolen"
date: 2023-08-01T23:26:57+08:00
---

I promised some friends about the steps I took when [my phone was stolen](/2023/07/stolen-phone/). These also acts as my notes in a possible future incident as well (though of course I hope that does not happen). A lot of the details here are specific to when you have a postpaid line in my country with my particular telecom (Globe Philippines), though the broad strokes should be similar elsewhere I think.

### 1. Call the number

If you're like me and were in doubt as to whether the phone was actually stolen or maybe you just dropped or misplaced it somewhere, you should try calling the number first. I was at a Dunkin and asked the cashier if she could lend me a phone to dial my number and she helpfully agreed. If the number cannot be reached, it is almost definitely stolen - the thief will turn off the device as soon as he has it, in order to remove the sim.

### 2. Have the SIM/line disconnected (temporarily)

I should have done this immediately (since I was already in the mall near a Globe store when it happened); instead I waited until a few hours later.

For Globe, it can be done (I assume) via a Globe store, or you can just message them on Facebook Messenger; the bot menu will have a "Report Lost Phone/SIM" option. After a wait, they will connect you with a CSR and you can tell them to temporarily disconnect the line. I was told the turnaround time on this is 24 hours and that someone would call be between 9am to 6pm the next day to process the request. This isn't ideal, it gives the thieves like half a day to do shenanigans with your phone number.

The next day around 9:30 someone called me (via an alternate number I provided the CSR) and verified my request and my details and processed the temporary disconnection.

### 3. Remotely disable the phone

This was the first step I did after getting home after the device was stolen.

For Android, you can do this via Find My Device: https://www.google.com/android/find/

There should be a similar service for iOS.

Your options are to lock the device and leave a message notification on the screen, or remotely request a factory request.

In my case, Find My Device still last reported my device was around where I lost it, so that means it never went online again after that.

### 4. (Optional) Have the unit blacklisted

When I spoke to the CSR in step 2 above, they mentioned I can also have the unit blacklisted by the NTC so it can no longer be used in the country. I just needed the IMEI number which should be on the box I got the phone in. I found the box during the call but had trouble locating the IMEI number so I just did it later when I visited the Globe store (where it was immediately pointed out that the number was on the side of the box top instead of under the box bottom where the phone CSR told me to look.)

Marked this step as optional because it does absolutely nothing for you but it does render the unit unusable except for spare parts, so it's some version of vengeance. I was angry so I went ahead with it.

I have no way of knowing it really works, though a friend assures me it does. Since I got the phone from Globe a few years ago, having the IMEI was sufficient for them to have it blacklisted, but if you bought your phone yourself I'm told you can report it directly to the NTC but you need to have proof of purchase.

### 5. Disable use of the phone number for recovery of critical accounts

I should have done this immediately, instead I came home later to some email notifications that some of my accounts had their passwords reset using the phone number. This is especially important since the temporary disconnection may take a while to push through.

Examples of affected accounts:

- Facebook: Can reset password using the phone number only. They reset the password but did not bother changing the emails, so I just reset it again myself and recovered my account.
- GMail: May be able to reset password using the phone number for some accounts. In my case, one of my lesser used emails had the phone as a recovery number and they were able to reset it, but there's nothing of significance there. I was also able to recover it.
- Lazada: Lazada is very insecure since it's designed for mobile-first the password can easily be reset using the phone. And further, the web password reset seems to always throw an error for me, so I wasn't able to recover my account as of yet. Apparently I had some credits in my Lazada wallet from some promo that I forgot about, and they used that to buy some GCash load. AFAICT this was the only financial loss (other than the loss of the unit itself)
- Shopee: Same as Lazada, but my Shopee account has nothing, so nothing was lost.
- GCash: GCash doesn't seem to send notifications by mail. I emailed support to suspend my account that same night and I am still in the process of having it reactivated so I still don't know if they were able to access my account using only the phone or if anything was lost. Will update this post when I found out.
- Maya: I also got some password reset requests for Maya, but it looks like they didn't have access to my email so they were never able to reset it. I had also requested to suspend this account, but missed some emails from support so it never happened. Oops.

I also temporarily removed my phone as 2FA for my main GMail account as a precaution.

### 6. Request a replacement SIM

For Globe, the requirements for getting a replacement SIM (with the same number) are just to bring an Notarized Affidavit of Loss and some valid IDs. It can only be done in a Globe Store.

I was able to hunt down a notary public the next morning and get my affidavit {{% footnote %}}I do find the concept of asking a notary public to attest to this as amusing since she has no way of verifying my claim is true so it's basically the same as my say-so. A friend says it's a legal "cover your ass" by the telecom so in case of fraud, i.e. someone else recoved my sim for me, they can point to the affidavit and say what can we do, there's our due diligence! Basically security theater I guess.{{% /footnote %}}. Around lunch time went to the Globe Store to get the replacement SIM. I had to wait a while, but once I was called up it was a straightforward process. Had to fill out some forms and wait a while.

You will need to provide some information to verify you are the owner. That means stuff like your personal details, last payment details, account details (they asked me when I started the account but I could not remember as that was more than 10 years ago!) and some other stuff. Basically you have to provide as many details as you can remember so that the agent can assess whether you really are the account owner.

Someone told me that when they tried this process it took them more than a week to get a new SIM so I was expecting the worst, but after the process was done, the agent handed me a new SIM card and said it should be activated within 3 days, so yay!

I was able to borrow a loaner phone until I could get a new one; the SIM was active by the 2nd day.

### 7. (Optional) Reset account passwords

I marked this step as optional, because if you did step 3 promptly AND if the developers of the apps you use weren't storing passwords in plaintext on-disc (best practice), then this shouldn't be necessary. That being said, you should be resetting your passwords regularly anyway, so I went ahead and reset a bunch of important passwords that same night.

Notably I could not reset any online banking passwords since they all require 2FA, but I was confident that my banking accounts were relatively secure. Also, I only actually had one banking app on that phone. 

I also got a bit overzealous with my Steam account and logged myself out of all devices and could not log back in since I no longer have the authenticator. Oops. I emailed Steam Support about it and they were able to restore my account the next day.

I must note that this is why I don't like the concept of mobile banking apps and prefer to do my online banking via web on my desktop; it is much harder to lose!

### That's It

As of this writing, I am mostly recovered. I have a temporary replacement phone, my SIM and phone number are mine again, and I have already checked all of my banking accounts and found no issue. I suspect they simply moved the SIM to another phone (an OPPO phone, based on gmail logs) and got as much as they could using only the number and who knows what they did with the device, though it should no longer be usable now.

This is the first time I had to handle this sort of thing in the modern age of 2FA and authenticators and whatnot. A learning experience for sure, and a big stressful hassle. I also largely blame my own carelessness and have made some changes to where I habitually store my phone to make it much harder to be pickpocketed again in the future.