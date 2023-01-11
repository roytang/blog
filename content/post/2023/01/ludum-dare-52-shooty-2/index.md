---
date: 2023-01-11 05:02:00
dontinlinephotos: true
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/109668986263351294
- type: twitter
  url: https://twitter.com/roytang/status/1613049440335691776/
tags:
- gamedev
- gamejam
- ludumdare
title: 'Ludum Dare 52: Untitled Shooty Game 2'
---

### The jam

An interesting way to start the year: For 2023, Ludum Dare decided to add a 3rd game jam to the year (they used to only have two a year), so this past weekend was the [the 52nd LUDUM DARE game jam](https://ldjam.com/events/ludum-dare/52). This is my 4th time participating in the Ludum Dare game jams!

Previously: [Ludum Dare 48](/2021/04/ludum-dare-48-diver/), [Ludum Dare 50](/2022/04/ludum-dare-50-shooty/), [Ludum Dare 51](http://localhost:8000/2022/10/ludum-dare-51-pizza/)

This jam started 4am (!!) local time on Saturday January 7th. Same as before, I chose to participate in the "Compo", the more challenging version, with a 48-hour time limit and restriction that you can only work solo and all assets must be created within the 48 hour period.

### The theme

The theme, announced when the jam started at 4am was **"Harvest"**. Not the best among the choices, I guess we can expect a lot of farming games for this one?

This time I wasn't struggling for the theme. I came in to the jam with an idea already in mind. I wanted to do a sequel to my [Ludum Dare 50](/2022/04/ludum-dare-50-shooty/) [Untitled Shooty Game](https://hungryroy.itch.io/untitled-shooty-game), which was a twin-stick bullet hell space shooter. There were a number of improvements I wanted to make to this game, but the most important was an upgrade system. It's something I noted from the previous game jams, some of the best ones I played had this feature, so I wanted to try it out myself.

Anyway, the weekend was packed. I still had a lot of my usual weekend activities, so I didn't have a lot of time for this jam, but I think I did manage to use my time wisely. By end of day Saturday, the basic enemies and composite enemies and the bare-bones upgrade system were in the game. Most of Sunday afternoon was spent adding more upgrades and enemies. Sunday evening was spent polishing and tweaking and balancing. Balancing turned out to be really hard; the upgrade system meant you got stronger as the game got longer, but if you didn't get the best upgrades early on, the early game was very challenging. I had to spend maybe an additional 2 hours on balancing runs but I still didn't feel like I got it right. I ended up submitting my entry around 2:30am on Monday, a bit more than an hour before the deadline. The weekend effort was surprisingly exhausting.

I definitely accomplished much more than I did back in LD40 though. Since this was a sequel, I had the advantage of being able to review the old code for reference. The rules of the jam meant I couldn't reuse the code directly (I think), but I had two IDE windows open side by side, one for each monitor, so that I could easily see how I did things the first time around.

I think I did maybe 18-20h of work over the weekend for this one, which honestly is a feat for me these days. I'm glad to know I can still pull off such focused work.

### The tools

Some new tools this time around, though I'm still using the same engine:

| <!-- -->    | <!-- -->    | <!-- --> |
|-------------|-------------|----------|
| Engine | Godot Engine 3.5 | I get my Godot from Steam, so I just use whatever version is there |
| Pixel Art | Aseprite | First used this during LD51, it's much better than the web-based one I was using before, but I had to re-build it again since I had a new PC. Was able to explore more of the features this time around! |
| Sound FX | https://sfxr.me/ | No notes. |
| BG Music | Medly app on iPad | I knew BGM was my weakness, so before the jam [I posted on the website](https://ldjam.com/events/ludum-dare/52/untitled-shooty-game-2-the-harvesting/music-tool-recommendations-for-someone-with-no-musical-talent) asking for BGM tool recommendations and got this one from there. It's pretty good, and felt better than what I was using before. |
| Font | Xolonium-Regular | From the Godot Dodge tutorial. Someday I'll find a better font that I like. |

I didn't bother making a cover art/splash screen for this one.

### The game

So the game is basically a twin stick shooter where your objective is to survive as long as possible. Enemy ships are periodically spawned and some of them have multiple modules that are randomly generated. Modules are just different variations of "guns". Some guns track you, some spread over the area, etc. The larger variant has many more modules and thus more challenging. I have smaller individual ships here that I didn't have in the previous entry.

I added back the bomb weapon from the previous game, but this time made it consume an "energy" meter that you have to fill up.

My gameplay wasn't super connected to the theme, so I added a feature where enemies drop resources (health/minerals/energy) that you "harvest". Health restores your ship health (another new feature - in the last game, your ship could only take 1 shot!), minerals are used to purchase upgrades, while energy powers your bomb weapon. I will admit the games adherence to the theme is very, very loose! I added a subtitle "The Harvesting" and some lore text with the word "HARVEST" in all caps to help lol.

You can play the game on itch.io: https://hungryroy.itch.io/untitled-shooty-game-2

Ludum Dare requires the source code be made available, I have it up here: https://github.com/roytang/ld52

And finally, the page for my entry on the Ludum Dare site itself: https://ldjam.com/events/ludum-dare/52/untitled-shooty-game-2-the-harvesting

Some screenshots of the game attached below!

{{% photos usg %}}

### In Summary

Overall, I was very happy with how this turned out and with the effort I put in. I was exhausted by the end. Honestly the past few game jams were a bit challenging for me because I felt like my gamedev skills weren't really getting better, but with this one I felt like i learned a lot. Not big things, but a lot of tiny implementation details that I never tried before.

I also had to cut a lot of features I wanted to get in, basically ran out of time. So many other weapons and upgrades and enemies and features I wanted to do! I think the submission is a really solid base though; I might work on it further and release some updates down the line. 

That will have to wait until after the review period though. Same as before: After submitting your game, you're supposed to review and rate other people's games, and you want to earn at least 20 ratings to get a "final score". The first USG from LD50 finished 435th overall, so I'm hoping this one at least does better than that!

Will update this post when the results come out!