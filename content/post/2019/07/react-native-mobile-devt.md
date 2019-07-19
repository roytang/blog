---
author: roy
categories: []
date: 2019-07-20 05:56:56
tags:
- software development
- react native
- mobile
title: 'Upgrading a React Native Project'
type: post
---

I have a small mobile app that I wrote using React Native (henceforth RN) back in 2017, currently deployed on the Google Play Store and Apple App Store. Shortly before my US trip, I got an email from Google telling me about a required action:

> By August 1, 2019, all apps that use native code must provide a 64-bit version in addition to the 32-bit version in order to publish an update. This past January, we reiterated that this is required in order to make way for innovation and in anticipation of future Android devices that only support 64-bit code.
> 
> As the deadline approaches, we wanted to remind you that at least one of your apps* uses native code but does not currently offer a 64-bit variant

This illustrates for me one of the big problems with mobile development: that app was perfectly fine when I last deployed it in 2018 and now even though I haven't changed anything, there's additional work that needs to be done. I guess I'm too used to web development where we just deploy the app on a server and the server architecture doesn't suddenly change for no reason. With mobile apps, the platforms and APIs and frameworks change quickly, leading to situations where even if your app doesn't have any pending changes, you need to do some work on it anyway. (Granted, this can also happen with webservers due to security patches and such, but with managed hosting, that's not something you worry about as often, and the resolution is often straightforward!)

As I was about to be out of the country on vacation for more than a month, I put this off and only started looking at it when I got back. Luckily, I did actually also have some minor revisions to do on the app, so I would do all the work in one go.

As it turns out, the version of RN I was using was too old and did not support providing the 64-bit version. I had to upgrade to a later version of RN, and after reviewing the process, it seemed like a nontrivial amount of work. There was an upgrade tool, but because I was so many versions behind, it couldn't work directly. The problem seems to be in the initial boilerplate created by `react-native init` for the ios and android subprojects; the older boilerplate was out of date and needed to be updated, which was not straightforward given that you may have modified that boilerplate afterwards. I had to use some kind of diff tool to manually find the differences in the boilerplate and merge the changes manually.

That seemed like a lot of work, and the app wasn't that large and didn't have that much code, so I figured it was more straightforward to just create a new RN project from scratch, which would be using the latest version of RN (0.60.3, from 0.50.4). Afterwards, I port over the project code into the new project, them swap the new project back into the old project's repo. That way I only had to update the few dependencies I was using in the project itself. 

It was still a nontrivial amount of work, but I eventually got everything working through many iterations of trial-and-error.

- I went ahead and upgraded the dependencies to the latest versions as well, to make sure there was no conflict with the new RN version
- ReactNavigation had some backward incompatible changes:
  - needed to [initialize the gesture handler](https://reactnavigation.org/docs/en/getting-started.html#installation) in the java class 
  - new function `createStackNavigator` instead of just `StackNavigator` constructor
  - needed to use `createAppContainer` to initialize the navigator
- some components such as WebView and AsyncStorage were no longer part of RN core and had to be imported accordingly
- Android now requires that I explicitly prompt for the `READ_EXTERNAL_STORAGE` permission when trying to access the camera roll 
- Google now recommends that I provide an upload key for encryption, but since I reset the project, I also accidentally deleted the signing key I was using before. Oops! Momentary panic until I have the sense to do a search and realize that past me was wise enough to backup the file elsewhere. 
- Test that I can create the app bundle successfully.
  
By this point I more or less had a working Android build, then shifted over to iOS. Since I only [recently got a Macbook Air](/2018/12/macbook-air-2017-model/), I actually hadn't tried creating and publishing the iOS build, someone was helping me with that part before. Because of reasons, I wanted/had to do it myself this time around, so a bit of a learning curve and trial-and-error again.

- clone the project from repo, `npm install`, try `react-native run-ios`, oops missing dependencies
- find out about CocoaPods. Clone a fresh copy of the project, `npm install` then `pod install` (took a while), then try `react-native run-ios` again
- needed to fix some dependencies I was using by manual linking and updating
- camera roll also needed to be added to the podfile (a config I possibly lost when I reset the project)
- fix a bunch of configs before I can actually run and test the app in the simulator
- Success! 

At this point, I make my other app changes and test on both my Android phone and the iOS simulator. The changes are easy, so now to try publishing.
 
- Try to publish and upload to iTunesConnect. Takes me a few tries to figure out that I need to be updating stuff like bundle identifier, version number, etc. 
- iTunesConnect has some new requirements too (like the iPad version needs to support all orientations) which causes a couple more iterations
- more screenshots are now required when submitting the app!
- I set up TestFlight and verify everything is ok with the published app. (I only tested using the simulator before)
- iOS app now submitted and "Waiting for Review". I anticipate they will have some ridiculous request and it might take me a couple more submission rounds before I can publish
- Google Play is more straightforward. `gradlew releaseBundle` is already working after my previous effort, so I just upload the bundle and distribute.

I see no indication that I have satisfied Google's action item, but it let me publish the update without complaints, so I'm done!

My initial estimate that the work was nontrivial ends up correct, I spent way more manhours than I expected on the upgrade. Part of it was learning how to do the iOS deployment, so hopefully that ends up easier in the future.

