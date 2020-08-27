---
title: "On Mobile App Development"
slug: mobile-app-dev
date: 2020-08-26T12:09:32+08:00
draft: true
tags:
- software development
- tech life
---

love hate relationship

My first exposure to mobile app development when I got pulled to help my then-company's then-fledgling mobile team with cleaning up the codebase for their iOS app. This was back in maybe 2011? It was one of those projects where some devs built a quick proof-of-concept demo using new technology, then management liked it and asked for new features and they kept adding new features haphazardly until there was just this huge unmaintainable mess of code. This isn't a knock against Objective-C or iOS development specifically or the dev team; the fact is they were new to the stack and were learning as they went while still trying to meet deadlines. I also spent some time reviewing the corresponding Android team's code as well. This was the bulk of my exposure to native mobile dev on iOS/Android. (This was before Swift, so I never got to experience that. Language looks neat though.)

Coming from a web dev background, I've always found the fragmentation of platforms annoying. Basically your effort gets multiplied by the number of platforms you have to support, and what would work well on iOS may not work well on Android and vice versa.

Later on, this concern was alleviated a bit with the rise of common frameworks that could publish to both iOS and Android. The first one I tried of these was React Native. I tried it for a small mobile project I did around 3-ish years ago. I wasn't tremendously happy with the experience. My mistake was probably diving head-first into React Native, when this was my first experience with React and front-end frameworks in general (something new to someone with [my jQuery background](/2020/02/old-web/)!), so a lot of concepts were new to me. 

To make matters worse, the React Native docs at that time seemed to assume some familiarity already with React, or at least similar frameworks like Angular. I had a bit of confusion with whether I should be using Expo or not, and how to eject, and it resulted in having to restart the project a couple of times. It was also my first encounter with NPM's dependency management, and that annoyed me a lot. A lot of the third-party dependencies I used back then were still immature too, so I often had problems with things like accessing the camera roll and so on. 

Nevertheless, it was experience, and the ability to publish cross-platform to iOS and Android was invaluable. I went on to use React Native as my go-to mobile framework I would recommend for other projects afterwards.

history
- objective c (convene)
- android
- react native (maroon)
- flutter (ap)

good:

bad:

- native apps
    - different platforms
    - no universal binary
    - app store controls/review

- companies wanting to unnecessarily make mobile apps for everything, when web is perfectly fine

- api backward compatibility
  - compare to windows
  - see how many of my old ios purchases got delisted