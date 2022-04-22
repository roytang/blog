---
date: 2022-04-06 04:31:14
dontinlinephotos: true
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/108083498854289749
- type: twitter
  url: https://twitter.com/roytang/status/1511578251633717248/
- type: twitter
  url: https://twitter.com/roytang/status/1517614791245795328/
- type: twitter
  url: https://twitter.com/roytang/status/1517615047547129856/
- type: twitter
  url: https://twitter.com/roytang/status/1517615190287601664/
tags:
- gamedev
title: 'Ludum Dare 50: Untitled Shooty Game'
---

### The jam


This past weekend I participated in [the 50th LUDUM DARE game jam](https://ldjam.com/events/ludum-dare/50). This is my second time participating in Ludum Dare and 3rd game jam overall. My last attempt was [Ludum Dare 48 last year](/2021/04/ludum-dare-48-diver/). I had to skip Ludum Dare 49 due to [a hospital stay](/2021/10/covid-experience/), so I was looking forward to this one.

The jam started 9am local time on Saturday April 2nd. Same as before, I chose to participate in the "Compo", the more challenging version, with a 48-hour time limit and restriction that you can only work solo and all assets must be created within the 48 hour period.

### The theme and the struggle

The theme, announced when the jam started at 9am was **"Delay the Inevitable"**. (A few hours before the jam the leading theme was actually "Folklore" and I thought I would be able to do [something about PH mythology](/2021/06/gmtk-game-jam-2021-manananggal/) again.)

Now, I actually had to sleep and couldn't start working on the jam as soon as it started at 9am, so I was only able to start working and thinking over the theme a few hours later. Even then, it turned out to be a struggle. Typically you want to find a good innovative approach to the theme that works both thematically and mechanically. I tossed around a few ideas with some friends, but none of them seemed good. All my implementable ideas were variants of "survive as long as possible", where apparently the "inevitable" being delayed was a game over.

{{% img src="struggle.png" %}}

I ended up deciding to do a simple twin-stick shooter. The initial concept was that you were trying to flee from a horde of zombies; you would have to bomb walls to make an escape path before you got overwhelmed by the swarm. I made some mockup "art" and did a simple prototype with spawn points generating the zombies that try to swarm you and blocks you could bomb. Here's a WIP video: https://www.youtube.com/watch?v=dCXmzl2bn_k

I had a bunch of feature ideas for this concept:

{{% img src="struggle2.png" %}}

But I was thinking about generating the map/landscapes and infinite scroll and such and that felt like a lot of work and together with all the other stuff, it all seemed very overwhelming. By the end of the day I wasn't very happy with the theme and was thinking to shifting to some kind of boss rush space shooter. My prototype graphics didn't look like a guy shooting zombies anyway!

I went to sleep earlier hoping I would feel better about the jam in the morning but I woke up early and still wasn't into it. For some reason, I wasn't into it as much as earlier game jams. And I'm not very young so I don't really have the energy to do like 18 hours of work in one day (unless maybe I'm getting paid lol); I was worried that I wouldn't have time to do everything I wanted to do.

I finally managed to get over the slump after lunch and I did this by doing one of the most effective motivation methods: I made a list. Basically I opened up a text file and listed all the things I thought would be doable within the day. By this point I had already decided to switch to the boss-rush space shooter thing.

Making lists is great! It clarifies your thinking and gives you a good overview of the scope and makes everything less overwhelming. The list I made is actually in github: https://github.com/roytang/ld50/blob/main/tss/todo.txt

The initial list I made was around 32 items, and I did a high-level estimate of 15 mins per item, which meant I had 8h of work to do for Sunday, which seemed reasonable. After doing the list I immediately dug into the first few items, and I was able to manage the first 8-10 items in around an hour, which put me ahead of schedule! 

By this point I was able to generate complex enemy ships with randomly generated components: https://www.youtube.com/watch?v=Q1COUzluwcs

Had to take a break mid-afternoon to entertain some guests and was able to resume late afternoon. By early evening I had added the gameplay and ship generation loops: https://www.youtube.com/watch?v=1jq9DvP7eMA

After that it was mostly just polish work. Testing and tweaking and fixing bugs. I added SFX and splash and restart screens and random UI stuff. I had to make a BG music track myself, but I have literally no musical ability at all. I ended up mashing some random notes together on online sequencer then splicing it together with some older tracks via Audacity. 

By late night I was pretty happy with what I had. It's not the best theme-wise and not the most innovative, but a pretty good outcome given how miserable I was feeling about the whole thing the previous day. 

There were still a number of features I had put in the todo list that I didn't get around to, but I felt that was fine and didn't want to lose sleep over it. I did the last few tasks (documentation, uploading, etc) before going to bed. There were still 9 hours left in the jam, but I needed to sleep. 

I ended up working for around 6h on the second day and around 4h on the first day, which wasn't a lot (I think the last LD I did around 16h of work over two days).

### The tools

I basically used the same stack as last time, you can [read the previous post for descriptions](/2021/04/ludum-dare-48-diver/):

    Engine: Godot 3.4
    Pixel art: https://www.piskelapp.com
    Sound FX: https://sfxr.me/ + https://convertio.co/
    BG Music: https://onlinesequencer.net/ + Audacity
    Font: Xolonium-Regular from the Godot Dodge tutorial

I didn't bother making a cover art/splash screen for this one.

I really should find a better pixel art program than Piskel though. While it's perfectly functional, they recently disabled creating an account, which meant it was no longer possible to save stuff to the cloud. (I think you can still save locally in your browser?) I usually just end up exporting to PNGs and just never editing them. I should probably get a pixel art program that runs natively on Windows and saves to files, that would make it easier to edit the files as needed.

### The game

So the game is basically a twin stick shooter where your objective is to survive as long as possible. Enemy ships are periodically generated, and each of them has multiple modules that are randomly generated. These are just different variations of "guns". Some guns track you, some spread over the area, some generate "swarmer drones" that chase you down (these were repurposed from the "zombie horde"). I was able to make smaller and larger enemy ship variants. The larger variant has many more modules and thus more challenging.

To help you along, I retained the bomb weapon/pickup. I reworked it so it can destroy bullets and hits every enemy full-screen. Basically an emergency escape when the field gets too tough. 

I honestly gave up on trying to think of a good title so **"Untitled Shooty Game"** ended up being the final one. I promise I will think of a better title for the next one!

The game is super simple, very arcad-y kind of shooter. But I'm happy just to be able to finish.

You can play the game on itch.io: https://hungryroy.itch.io/untitled-shooty-game

Ludum Dare requires the source code be made available, I have it up here: https://github.com/roytang/ld50

And finally, the page for my entry on the Ludum Dare site itself: https://ldjam.com/events/ludum-dare/50/untitled-shooty-game

### Aftermath

Same as before: After submitting your game, you're supposed to review and rate other people's games, and you want to earn at least 20 ratings to get a "final score". I tend to be very competitive, so I want to rank highly, but I have low expectations. The [last entry](https://roytang.net/2021/04/ludum-dare-48-diver/) had an overall ranking of 265th, so if I could just beat that, I would already be happy. Well, I'm already happy I was able to finish.

Some screenshots of the game attached below!

{{% photos screen %}}

Will update this post when the results come out!

<time id="1517614791245795328">[2022-04-23 05:22] </time> Ludum Dare 50 results came out yesterday morning! Unfortunately, Untitled Shooty Game did not do as well as my last Ludum Dare attempt. Ratings are out of 805 compo submissions total. 

{{< photos 1517614791245795328 >}}

<time id="1517615047547129856">[2022-04-23 05:23] </time> Still, relatively happy with the result and for the experience, and I did get some good feedback. Honestly, USG feels a lot more solid as a foundation for a later release compared to my earlier game jam attempts. Looking forward to LD51 later this year!

<time id="1517615190287601664">[2022-04-23 05:23] </time> Side note: The top LD50 games look great, I'm thinking of streaming them next week.