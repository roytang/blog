---
date: 2022-10-05 06:30:27
dontinlinephotos: true
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/109114411251923982
- type: twitter
  url: https://twitter.com/roytang/status/1577556644447551489/
tags:
- gamedev
- gamejam
title: 'Ludum Dare 51: 10 Second Pizza Delivery'
---

### The jam


This past weekend I participated in [the 51st LUDUM DARE game jam](https://ldjam.com/events/ludum-dare/51). This is my third time participating in Ludum Dare and 5rd game jam overall. I was looking forward to this one because [I failed my last game jam attempt](/2022/07/gmtk-jam-2022-failed/) and was hoping to get back into the groove.

Previously: [LD50](/2022/04/ludum-dare-50-shooty/), [LD48](/2021/04/ludum-dare-48-diver/)

The jam started 6am local time on Saturday April 2nd. Same as before, I chose to participate in the "Compo", the more challenging version, with a 48-hour time limit and restriction that you can only work solo and all assets must be created within the 48 hour period.

### The theme

I woke up around 6am to little sleep so I could see the theme when it was revealed and it was **Every 10 Seconds**, which I could easily predict from the theme elimination rounds earlier in the week.

I still needed more sleep, so I went back to bed and let my subconscious stew on the theme for a bit. After I woke up around lunchtime, I figured I would just keep it simple and landed on doing a platformer with 10-second long stages. I may have been overcompensating a bit because of struggling with theme in the GMTK jam, but really keeping it simple and easy to scope is a good thing.

### The Work

I settled on the "lore" of a pizza delivery guy who has to make pizza deliveries in 10 seconds.

Pretty simple. I'm still using Godot, same as every Game Jam attempt so far, because Unity feels like a heavy massive monolith by comparison.

This time though, I wanted to use a new tool for pixel art. Previously I had been using [Piskel](https://www.piskelapp.com/) but this time I wanted to use [Aseprite](https://www.aseprite.org/), which is a C++ program that ran locally on your own machine instead of via a webapp. It's open source, so some time before the jam, I had the exciting experience of compiling it myself. (I guess exciting for a programmer?)

Working with Aseprite instead of Piskel had some obvious immediate benefits in terms of being able to go back and update existing sprite sheets, setting up frames, layers, etc. Aseprite is also a lot more powerful I believe - it might take me a while to be able to use the app to the fullest. I do a feel a bit prouder of my pixel art this time around, despite how it looks!

I had a bunch of feature ideas for the platformer stages, basically stuff I wanted to try out. Things like wall jumping, dashing, rotating platforms, etc. Same as before, my todo-list for the jam is in the repo: https://github.com/roytang/ld51/blob/main/todo.txt. It is much simpler than [my list for the last Ludum Dare](https://github.com/roytang/ld50/blob/main/tss/todo.txt)!

By the end of Saturday I had most of the features I wanted and had implemented 5 stages and at this point the game was already playable start to end. I wanted to get to at least 10 stages (more than I've done for previous Ludum Dares), so I saved Sunday for the last 5 stages and testing and polish and stuff like that. After all the work on Saturday, I could already whip up a new stage in around 30 mins or so, as long as I had a rough idea in my head already. I also added some rudimentary SFX and banged some notes together for BGM (me with my no musical ability...)

I uploaded and published my submission around 1am on Monday morning, some 5 hours short of the deadline. I had a busy weekend with other stuff and I was sneaking work on this game in between everything else, so I was a bit exhausted! I think I ended up working for around 5h each on Saturday and Sunday, which wasn't a lot, but a fair amount of time to spend on a game jam over a weekend. (I'm too old for the stay-awake-all-weekend kind of jams!)

### The Tools

I basically used the same stack I've been using since LD48 ([read the previous post for descriptions](/2021/04/ludum-dare-48-diver/)), except for replacing Piskel with Aseprite.

    Engine: Godot 3.4
    Pixel art: https://www.aseprite.org/
    Sound FX: https://sfxr.me/ + https://convertio.co/
    BG Music: https://onlinesequencer.net/ + Audacity
    Font: Xolonium-Regular from the Godot Dodge tutorial

I didn't bother making a cover art/splash screen for this one. I did draw a pixel art pizza for the intro stage though.

### The Game

The game ended up being a super-straightforward platformer, you run and jump and try to get to the customer in 10s for each stage.

During playtesting, I was a bit bored that each stage was basically just "get to the finish line", so I decided to add (I think on Sunday) an additional collectible to each stage, a "Bonus Star", that was slightly out of the way, so you had to risk losing some time to get the Bonus Star. 

I had also initially implemented carrying over excess time - so that succeeding stages are much easier if you do well on previous stages. When I added the Bonus Stars, I also wanted a reward mechanic so I made it so that excess time is only carried over if you got the Bonus Star for that stage.

This made the game balance a bit weird - I added the Bonus Stars to give the player an additional thing to do in each stage, but if you wanted a challenge, it was actually better to NOT get the Bonus Stars so you wouldn't have extra time for later stages. I even added some extra dialogue in the ending screen for finishing the run without getting any Bonus Stars!

You can play the game on itch.io: https://hungryroy.itch.io/10-second-pizza-delivery

Ludum Dare requires the source code be made available, I have it up here: https://github.com/roytang/ld51

And finally, the page for my entry on the Ludum Dare site itself: https://ldjam.com/events/ludum-dare/51/10-second-pizza-delivery

### Lessons Learned

While I got some early feedback about the good tutorials for the game, I did purposely avoid explaining two things: enemies can be stomped, Mario-style (it is not really essential to the stages, and you can easily figure it out experimentally) and that Bonus Stars carry forward excess time (I felt like players could figure it out once they saw it happening, but I got questions about it anyway.) It would have probably been better to mention these explicitly.

Also, as mentioned the difficult balance is a bit weird. Because of the Bonus Stars mechanic, the later stages can be much easier than the earlier ones. And early on in development, some stages like stage 2 were sooo easy, so I tweaked and rebalanced it and apparently it is now one of the harder stages of the run. I need to get better at balancing my stages across the entire game!

My platformer jump arcs also aren't the best. Kind of floaty. The code here is kind of cobbled together and evolved from previous attempts, might be worth going through it to make it tighter and smoother and generally feel better.

Lastly: Now that I've started playing some of the other submissions, I want to note some ideas / concepts that I might want to incorporate into future jams. The main one is upgrades: it might be a good idea to have purchasable upgrades in the game, perhaps you can spend Bonus Stars to get upgrades? A lot of other submissions have this type of mechanic.

### Aftermath

Same as before: After submitting your game, you're supposed to review and rate other people's games, and you want to earn at least 20 ratings to get a "final score". I tend to be very competitive, so I want to rank highly, but I have low expectations. My entries for LD48 and LD50 ranked overall 265th and 435th respectively; if I can beat those, that would be great, but that seems unlikely. Honestly, while this one feels like a solid entry, I feel like the LD50 entry was my best one so far (but it was also lower rated than the previous one, so eh?)

Some screenshots of the game attached below!

{{% photos 10spd %}}

Will update this post when the results come out!