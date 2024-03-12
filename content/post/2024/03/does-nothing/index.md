---
date: 2024-03-12 07:41:35
dontinlinephotos: true
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/112081670960878504
tags:
- software-development
- mobile
title: An Android App That Does Nothing
---

A couple of months or so ago, Google started nagging me about my inactive Play Store account:

> You have 31 days to fix issues with your Play Console developer account, Roy Tang.
> 
> More details about this issue can be found on the Policy status page in Play Console. View in Play Console
> 
> Your developer account is not in use. Play Console developer accounts are intended for developers who actively publish and maintain apps. To protect the safety of app users, developer accounts that aren't used are closed. 
>
> How to fix this
> 
> If you plan to publish or maintain apps in the future, prevent your account from being closed by completing the following tasks:
> 
>   - If you haven't done so yet, verify your email address and phone number on the Account details page
>   - Create and publish an app, or publish an update to an existing app on Google Play.
>

It's been a while since I published to the Play Store and I didn't really have any intention of using the account soon, but I didn't want to lose it either. Unlike the Apple Developer account which costs $100 a year, the Play store account is free to maintain but I had to pay a one-time fee of $30 to start it, so I didn't want to have to do that again.

So I decided to just publish an app. Specifically: an app that does nothing.

This also gave me a chance to try out creating a super basic Android app using Godot Engine, something I've never tried before. I prefered to use Godot rather than reinstall and use the clunky Android Studio IDE.

I made a super simple "game" that consisted of a two-frame animated sprite that I had made previously for some other project prototype that didn't push through. I didn't even bother resizing the canvas! 

I looked up [the tutorial instructions for exporting from Godot to Android](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html) and they were super straightforward to follow. The only thing that the documentation didn't explicitly specify was that for publishing on the Play Store, you need to export to Android App Bundle (AAB) format, and I had to hunt around for where that setting was. 

The Google Play Console was much more confusing to use, it's not a simple case of upload your file and submit. You need to set store listing details, upload screenshots, create a release, specify distribution details, etc. Once I was finally able to submit a new release, I found out I needed to wait up to 7 days for a review. 

I remember thinking before how lax the submission process was on Android compared to iOS, so I was expecting a quick turnaround and no problems. But after a few days I got a message saying my submission had been rejected! The reason given was "Violation of Minimum Functionality policy":

> Your app doesn't comply with the Minimum Functionality policy. It has no functionality.
> 
> Issue details
> 
> We found an issue in the following area(s):
> 
> Version code 1: In-app experience: Please see attached screenshot IN_APP_EXPERIENCE-1458.png
> 
> About the Minimum Functionality policy
> 
> You should ensure your app provides a stable, engaging, responsive user experience. 

I hadn't realized such a policy existed! The screenshot the reviewer had attached to the issue was exactly the same as one of the images I attached to the store listing, so I think they just thought the app had frozen or something. I found it hilarious.

So when I had some time, I updated the app and added some super simple interactivity: I added a button that when pressed, it would move the sprite to a different position and also show some text. I also changed the canvas settings so the scene would be more zoomed in to make the text readable.

{{% photos %}}

I submitted the new build late last week and finally the app was approved and [is now listed on the Google Play Store](https://play.google.com/store/apps/details?id=net.roytang.DoesNothing). The above screenshots are the same ones in the store listing. 

I decided to make this one a paid app, which a minimal fee, because it would be hilarious if someone went ahead and paid for it. Actually, you can buy it if you want to support me!

*(I would guess there is probably something to be said about adding to the deluge of trash apps on the Play Store, but at least my app is incredibly honest about what you're getting!)*