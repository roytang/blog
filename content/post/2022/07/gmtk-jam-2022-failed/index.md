---
date: 2022-07-20 04:57:21
dontinlinephotos: true
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/108678223565537693
- type: twitter
  url: https://twitter.com/roytang/status/1549640622859902976/
syndication_attachments: false
tags:
- gamejam
- gamedev
title: 'GMTK Game Jam 2022: Failed'
---

I signed up for this year's GMTK Game Jam, a 48-hour game jam which was held last weekend. I joined [this game jam last year as well](/2021/06/gmtk-game-jam-2021-manananggal/). My entry there [finished in the top 800 overall](https://itch.io/jam/gmtk-2021/rate/1082887) (out of 5000+ entries), which I felt was pretty good for a solo dev with minimal gamedev experience. So I was hoping to be able to complete the same jam this year and maybe even rank a little higher?

Unfortunately as you can tell by the title of this post, I failed to complete and/or submit an entry for this jam. It feels weird to be writing about failing to do something, but there are lessons to be learned whether you succeed or fail at something. This was the first time I failed to submit out of 4 game jams I've tried participating in so far, so it made me a bit sad.

#### Saturday

First problem I had was with the theme. The theme was revealed at 1am my time Saturday, and it was "Roll of the Dice". I stayed up for the theme reveal then went to sleep, hoping I would wake up with a good idea to implement. No such luck. I tried thinking going through some ideas with some friends but most ideas seemed irrelevant to the theme or just something similar to what everyone else would be doing. It's probably just a lack of creativity on my part, but I couldn't find any interesting approaches to the theme.

It was late afternoon before I even decided to make my first attempt at prototyping an idea: Slay the Spire with dice. Basically replacing the deck-building part of SoS with drawing dice from a bag, where each dice has faces that do stuff like attack, defend or heal, etc. It seemed a good idea at the time and I doubt few people would do something similar.

However, once I started planning out how the prototype I felt a bit overwhelmed with how much stuff I needed to do: I needed to design a bunch of different dice, draw sprites/icons for each face, draw sprites for the player and each enemy, implement the whole dice-bag building loop, implement a rudimentary AI, implement the "map" with different battles and other kinds of nodes, etc etc. On top of that, since dice have 6 faces that makes them 6 times harder to grok than a card with a single face; I knew that I had to have a really good UI so that a player deciding which dice to add to his bag can easily evaluate different dice. 

Ultimately, I spent a lot of time being paralyzed and progress on this was superslow. For the first day, my prototype didn't get far beyond implementing the dice rolling and a pop-up window UI for showing the dice details:

{{% img src="dice-rolling.gif" %}}

That is... not a lot! One of the problems was that my previous game dev games had been more arcade-y things like platformers or shooters where you just controlled a character directly via keyboard. The UI for this idea required a lot of mouse interactions, which I had to figure out first (not that it was hard, but I definitely started the wrong way.) At this rate, I figured I'd be lucky to finish just a simple battle scene by the end of the 48 hour period.

Another problem was time management: I had some other stuff scheduled for the weekend for example. Like I had some stuff to do Saturday evening, so that was out. I had a chance to defer the appointment, but I figured it would be fine. I didn't anticipate that I'd be starting so late! All in all, I think I only managed to do 2-3 hours of work on this prototype (including planning it out and being overwhelmed).

I also had a bit of a tools issue: I was using [Piskel](https://www.piskelapp.com/) for making pixel art for the dice face icons and such, but that required a lot of repeating icons across dice faces, and I couldn't find an easy way to copy-paste areas of the pixel art from one image to another using piskel. In hindsight, I probably should have done this via composition in code, since I'm more a programmer than an artist! I also wanted bigger sprites for the player and the enemies, and it seemed like a lot of effort to do so in Piskel. I actually spent some time looking for good and free pixel art tools for iPadOS (so I could use my Apple Pencil to draw). I tried a couple but didn't end up too happy with any of them. Here's a fighter sprite I made with one of them though:

{{% img src="fighter.PNG" %}}

By the end of Saturday, I was even less motivated to work on the game jam; the lack of progress made everything worse.

#### Sunday

Early morning Sunday, I had trouble sleeping because I was still thinking about the jam. I thought to myself maybe I still had time to pivot to a much simpler approach: I could do a "pushing blocks around" puzzler, where the blocks were dice hence the number changed every time you pushed it around, and you had to move the blocks to a target area. Since I couldn't sleep anyway, I got up and spent an hour or so on a quick prototype:

{{% img src="dice-blocks.gif" %}}

This seemed fine and easily something to build upon! However by then it was almost morning, and I'm not young enough to pull off the "work all day without sleep" thing anymore, so I went to sleep. 

By the time I woke up it was around noon. I quickly evaluated what else I would have to do to get this prototype to a state where I'd be happy to submit it. The actual levels would need to have more obstacles and possible more dice of course, to make things more challenging. Designing puzzle levels takes time, and not something I have a lot of experience with. I figure I would need at least 5 levels to properly showcase the possibilities, ideally 10-15. On top of that, I'd want to polish the game some before I submit, meaning making the sprites animated and probably adding some sound. 

Combined with me needing to do some other stuff on Sunday (see: time management above), I assessed that it wasn't likely I could finish and submit the game, so I decided to tap out early instead of stressing over it. If I already had this idea Saturday, it might have been a different matter, but alas.

#### Aftermath

I was of course sad to not be able to submit and failing a game jam for the first time. And for a while I questioned why I was doing all this gamedev stuff anyway and whether it was worth it and whether I had the capability to be successful at it. (A normal reaction for anyone with any form of anxiety!)

After the short period of being sad, I buckled up. Getting into game dev has been a long running dream of mine since college, and even if I'm getting nowhere, there's no reason to set it aside, so one setback would not be enough to derail me.

Some lessons I learned:

- when picking game ideas for a jam, should lean to my strengths:
    - favor genres I'm more experienced in like platformers etc
    - prefer ideas that are narrower in scope and can require less art assets
- need to do more prep outside of the game jam times, so that I don't waste jam time on them:
    - practice more on genres / features I'm not familiar with
    - look for better tools / workflow where possible
    - review past winning jam entries (for more/better ideas on what kind of games to make during the jam)
    - have a template ready for the game project beforehand
    - should practice designing puzzle levels
- better time management during the jam:
    - map out blocks of time where I can work on the jam and try to have more focused work during those periods
    - reschedule things where possible
- in general, more gamedev practice:
    - I found that every jam there's some things I keep having to relearn about coding in Godot (although I guess this is true whenever I start a new programming project even outside of gamedev)
    - I'm not super-focused on gamedev because I'm doing a lot of other stuff, so I usually only do big jams like GMTK or Ludum Dare. I might want to try participating in smaller, less stressful (longer jam time) jams in between to help improve/hone my skills

While I do this mainly for fun, there's also a part of me that wants to be "successful" at it, and for me the immediate next goal would be to have one of my submissions do well at a game jam. And in the long term, I would want to be able to build upon one of the jam submissions into some kind of commercial release. While commercial success for a solo dev is a very long shot, it's not unheard of - my favorite example is puzzle game [Baba is You](https://en.wikipedia.org/wiki/Baba_Is_You) being originally a demo from a game jam and now released commercially on multiple platforms.

Most likely a very long way to go still, but onwards we go on this gamedev adventure. The next big jam is Ludum Dare in October!