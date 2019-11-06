---
title: "The Perils of Handover Documentation"
slug: handover-documentation
date: 2019-11-06T20:07:37+08:00
tags:
- software development
---

A while back I found myself having to figure out how to compile/build/run a mobile application. The developers previously assigned to the project were no longer available to consult with, but they did leave behind some documentation. However, their documentation quality left a lot to be desired. The instructions they left basically amounted to:

1. `npm install`
2. `ionic serve`
3. `ionic codrova run android`/`ios`

Okay, first sign of trouble is that their instructions were basically commands that anyone who knew the app used Ionic would be able to Google. But ok, I gave this a shot, even though I had not used Ionic/Cordova before, I assumed the simple documentation meant it would be straightforward (spoiler: it was not).

- First problem: `npm install` fails. Okaaaay. I dig around for a bit and figure out there's an incompatibility between one of the packages and my node version (12). Some more digging around tells me that the previous developers likely were using Node 8. I switch to Node 8 and `npm install` finishes successfully, somehow.
- Second problem: `ionic serve` throws an error from one of the dependencies. A bit more digging around. Reading ionic docs. Stackoverflow. Turns out there was some extra configuration needed to be added if you're doing this stuff on Windows. (I later found out the previous developers had used Ubuntu.)
- Third problem: `ionic serve` throws a whole bunch of typescript errors. Why? After facepalming for a bit, I dig around again. And dig some more. Looks like dependency issues. But the `package.json` has dozens of dependencies, it would take me forever to figure out the problem. I find myself digging through the repository's commit history trying to figure out if there was a recent change to the `package.json` that would cause the issue. What I notice instead is that a couple of weeks before the handover, someone deleted `package-lock.json` from the repository for some unknown reason. Deciding to try it out, I restore the old version of `package-lock.json`, do the whole `npm install` dance again, and sure enough the typescript errors vanish. But we're not yet done.
- Fourth problem: `ionic serve` no longer throws an error, but when it launches the browser, there's a cyclic error stacktrace shown. Some stackoverflow answers tells me this is because something can't be serialize it, and I trace the problem to a generic error handler that just calls `console.log`. I comment this out so that I can see the actual error, which is "cordova doesn't exist" (or something to that effect). I realize this means that the mobile app uses some native-specific things, so Cordova is required and it's not going to work when served via web, so why did they include this step?
- So instead I do `ionic cordova run android` (after installing the necessary Android Studio/SDK things...this was after my [recent computer troubles](/2019/09/two-backups/), so I had a fresh OS install.) And yes, long story short, I am finally able to get the Android app running in an emulator (and eventually in a device, and then the iOS version as well).

I recounted this because I could use it as lesson to note that even when you do have documentation, there are so many ways the documentation can be insufficient. In this case:

- the dependencies/requirements were not specified
- they did not have someone actually go through these steps from a fresh install to verify things would work

A case could also be made that they should have just had something like a Docker setup available, but they actually did have a `docker-compose.yml` in the repository! Sadly, it wouldn't have worked either because it referenced some environment variables that I had no idea what the value needed to be. And besides, my PC doesn't support Docker (silly Windows Home), but looking at the docker image did clue me in to what Node version to use.

In this instance, it was also a problem was that the old team was asked to provide the documentation only after the handover (due to circumstances beyond our control). Ideally, a handover would have them available for consultation should there be problems found with their documentation, and the documentation would only be cleared for acceptance after such review. (Realistically, a lot of documentation like user manuals wouldn't even be looked at, but in this case, the ability to build the application was kind of crucial!)