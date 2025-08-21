---
date: 2021-06-15 16:30:14
dontinlinephotos: true
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/106415843629803863
- type: twitter
  url: https://twitter.com/roytang/status/1404848304987394048/
- type: twitter
  url: https://twitter.com/roytang/status/1407542174384680960/
tags:
- gamedev
- gamejam
title: 'GMTK Game Jam 2021: Manananggal'
---

### The jam


A thing I did last weekend was to participate in [the 2021 GMTK Game Jam](https://itch.io/jam/gmtk-2021). This is my second game jam, after [my Ludum Dare 48 entry back in April](/2021/04/ludum-dare-48-diver/). I was a lot more anxious about this one, especially after rewatching the [video of the winners from the last year](https://www.youtube.com/watch?v=RGeAkU2wu4o). 

This post is mostly about how the game jam unfolded for me. If you just want to view the game I made [here's the link](https://hungryroy.itch.io/manananggal).

The theme for the jam was **"JOINED TOGETHER"**. The theme was announced 2am Saturday my time here, but I had stuff to do up to lunch time so I couldn't start on any actual jam work until after then. I did spend try to brainstorm game ideas before then, but I really struggled with this theme. 

I went through some number of ideas, though many of them were variants of "tandem side-scrolling platformer where you have to bring two characters to the end", but most of them felt pretty meh theme-wise. I also thought about things like, a guy with a ball and chain that limited his movements, but I didn't think I knew enough about Godot physics to implement the linked bodies correctly. 

I finally decided to do a game based on [the local Manananggal myth](https://en.wikipedia.org/wiki/Manananggal), since the whole detaching half of the body and rejoining fit the theme really well. I was imagining a puzzle platformer, but I was worried that mechanically I might not have enough for anything more than a couple of levels. I had a few ideas, but I was pretty sure I wouldn't have something close the 10 levels I had for Diver. The initial discussion from my support group suggested I play into the lore that manananggals ate babies, but I didn't want to make a baby-eating game!

{{< img src="manang1.png" >}}

### The tools

I'm basically using the same tech stack as last time: Godot Engine for the all the coding, [Piskel](https://www.piskelapp.com) for the pixel art and so on. I also decided to reuse a tileset I got from an [online platformer tutorial](https://www.codingkaiju.com/tutorials/beginner-godot-2d-platformer/) I was playing around with the previous week (with some modifications). I still had to do the character sprites and animation myself though.

### Saturday

Saturday was challenging, since I only had half the day to work with. I used up most of the time just doing spritework and implementing the basic detach / rejoin mechanic, implementing switches and gates. All of this was only good enough for an introductory level by the end of the day so I didn't feel like I had much progress done, especially compared to my progress with Diver at around the same mark. I was tired so I just went to sleep and hoped for a better Sunday.

One thing that helped me was being on the Discord for the jam, which was super active, and full of a lot of other people also having trouble with ideas and levels and coding. Ludum Dare had posts from the devs on their page, but that was nowhere near as active or interactive as this one. I found myself going through the Discord chat when I felt stressed or tired, reassured by the presence of my fellow game jammers.

### Sunday

Managed to start early Sunday. I started out by implementing a simple framework for easily transitioning between stages, which would allow me to easily add stages and change the order (great for debugging!). 

Then I needed to do the second stage. I implemented an enemy that I would need, a human villager out on patrol for monsters (which meant more sprite work). Basically adds a stealth component to the game - you could walk past the humans while joined together, but you can't let them catch you while detached. I also added a Pick Up / Drop mechanic where you can pick up items while flying in detached mode and drop them for different effects. In the second stage I made, one of the obstacles was you needed to drop a rock on a human in order to stun and get past him.

After the second stage, I worked on the last stage. I had decided early on to have an ending that subverts some elements of the manananggal myth, so I already knew what the last stage needed to be. And that included a bit more sprite work.

At this point, I had around half a day remaining, and I wanted to submit early to avoid any possible rush on itch.io during the submission time, so time was short. Aside from the actual stages, I still had a bunch of polish stuff to do. I originally had an idea for a third stage that involved a new dog enemy that could detect you even while merged. I didn't have time to do more sprite work though, so I decided to reuse some sprites and movement patterns from Diver to make a challenging spike level instead. (I would later get a lot of complaints about my playtester friends about how difficult the spike level was lol.)

After that, I needed to do all the polish stuff I was planning. Luckily my friend Jaime told me he had time to help me with BGM and SFX, so I asked him to provide some tracks and help me source some sound effects. This freed me up to do things like intro and ending dialogs, splash screen, add decorations and polish to the stages, add key input hints, etc. For the splash screen, same as for Diver, I used up one of my [sketchdaily](/collections/sketchbook/tags/sketchdaily) slots to draw the cover art / splash screen art for the game:

{{< photo "2021/06/1404039267685261332/" >}}

### Submission and aftermath

I made my submission around 4 hours before the deadline (since I also had other stuff to do). The game is here on itch.io: https://hungryroy.itch.io/manananggal.

In the end, I was happy I was able to finish and submit, despite all my doubts along the way. The game actually ended up more polished than I thought it would, though it is still very short (only 4 playable levels), but that's fine, as I was practically new to platformers anyway. Most importantly, I learned a lot of things along the way; among them: how to structure stages and transitions in Godot, making objects interact with a linked object, patrolling mobs with ledge/wall detection and sight radius, etc. This game is my documentation of those things I learned, although I'm thinking maybe I should log some of those lessons here on the blog so I have a set of notes online for Godot. We'll see!

After the submission time, there's a one week period for the games to be rated. I believe you only need an itch.io account to rate the games, but if you aren't a participant, you need to rate 25 randomly-selected games before you can rate specific games. You can rate my submission [here](https://itch.io/jam/gmtk-2021/rate/1082887). 

Not that I'm expecting to make the top 20 or even the top 100 mind you, as the game is very short and I feel very basic. My explanations are low and really I should just be satisfied with having finished. I have already received some encouraging comments on itch.io though, so that's a nice boost. 

I actually haven't touched the game itself or looked at the code or anything like that since submitting. All I've done was look at comments and get some feedback from friends. At that point I had played through it so many times I was kind of sick of it, so I stayed away from it since then. I really should rate some games though, just as a way to give back to the community. I'll try to get some reviews and ratings and comments in over the week.

This makes 2 out of 2 game jams where I've successfully been able to finish and submit. The discussions on the Discord chat seem to be implying it's not uncommon to fail to complete your game. I will happily take this as a testament to my ability to manage scope and keep it small. Although, it might also be an indication of playing it safe and not being willing to push the envelope - I might consider to be more aggressive in future jams. 

OTOH, I'm a lot older than many of the participants, so I need a lot more sleep. Some of them were talking about working on their submission for like 20-30 hours straight, and I'm like I can't even sit in my chair for more than two hours without needing to lie down for an hour afterwards. So I gotta work smarter to keep up with the young'uns.

For future jams, I'll probably also try to do some other genres instead of side-scrollers which I did for the first 2 jams. Maybe some kind of shooter thingy? Or a match 3? Or maybe I'll study how to do some of the ideas I passed over this time? We'll see! Looking forward to doing more game jams! I think the major one is the next Ludum Dare in October, though I'll also be looking out for other game jam opportunities before then.

**[2021-06-23]** The GMTK game jam results are out; my Manananggal game ended up ranked 717 overall out of 5800+ entries. Looks like my programmer art pulled me down in the presentation criteria lol. [Link to ratings page.](https://itch.io/jam/gmtk-2021/rate/1082887)