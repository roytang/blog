---
title: "Location, Location, Location"
slug: location-location-location
date: 2020-05-26
tags:
- tech life
- meta
- changelog
---

A while back I got an export of my Foursquare/Swarm data. If you're not familiar, these were a pair of apps that were used for "checking-in" to particular locations, with a sort of gamification system where if you checked in at a place often enough, you would earn points and eventually become "Mayor" of the venue. The idea being that owners of those venues might give some benefits to those who check-in often at those locations (AFAIK, this never really caught on in the Philippines). I wasn't a super active user of Foursquare/Swarm, I had maybe 500ish check-ins from 2010-2017 when I stopped using it. Some people are still using it up to now and have thousands of check-ins, although as far as I can tell it's no longer very popular in the Philippines.

Anyway, I thought having this data would be handy so I put it up as location data on this site. It also gave me an excuse to figure out how to render OpenStreetMap. (The location pages are one of the few pages that have JavaScript on this site.) The [locations page](/locations/) shows a map of all the visited locations and a listing of the locations grouped by country, and for the Philippines, by city (where available). You can click through to individual locations to see how often I've checked in there. 

For example, one of the venues with the most number of check-ins for me is [BBQ Chicken](/locations/4d27f36c8292236a41e814bb/), a now-closed Korean-themed BBQ chicken place in Ortigas near where I used to work. Another one with a lot of check-ins would be [Murphy's in Makati](/locations/4bbbfea5ed7776b032413f51/) where we did a lot of quiz nights from 2011-2013. Obviously, the location data isn't complete and doesn't capture all my visits, since I didn't use Foursquare/Swarm that religiously anyway. I'm certain I've eaten at BBQ Chicken more than the 18 times I checked in!

### What about privacy?

Actually telling the internet where you are all the time might seem a bit anathema to the more privacy-conscious modern world, but I do like having a history of where I've been. I even have location tracking enabled on my phone via Google Maps so that I can have a timeline of where I am on a day-by-day basis. I've used it more than once to answer queries like "do you know if we went to <place> in <month> of last year?" or "When did you last go to <store> ?" Obviously it's not for everyone and I fully understand the privacy ramifications of Google having all my location data and feeding the mightly global surveillance capitalism machine, but for me right now it's an acceptable tradeoff. As for the foursquare data, I was using foursquare back when I was less privacy-conscious that I am now, so I my attitude is like, that particular dataset has been out in the world for years, I can't put the toothpaste back in the bottle.

That being said, I did scrub some old check-ins from this data (and the corresponding data on Swarm and on Twitter if it was cross-posted)) that was a bit too close to home. I know this data potentially allows bad guys or assassins or whatnot to figure out where I live, so I thought I'd at least make it a tiny bit more difficult. 

### What now?

This is just a neat little thing that probably only I will care about, as it lets me see some of the places I've been to. And I probably won't be using 4sq/Swarm again, so the dataset probably won't be growing. That being said, I do want to add some future features like grouping the check-ins according to trips, so I can see all the particular places where I went to on particular trips. Many of my trips are missing data though; for example, my only check-in in France was in the airport, and not at any of the touristy places we went to. I may try to supplement this data with selected extracts from my Google Maps location history (hopefully it's easy to figure out!).

I also don't know where to put the locations page in the menus lol. I'll figure it out sooner or later!

