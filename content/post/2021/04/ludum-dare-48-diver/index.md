---
title: "Ludum Dare 48: Diver"
date: 2021-04-27T13:49:23+08:00
tags:
- gamedev
---

### The jam


A thing I did last weekend was to participate in [the 48th LUDUM DARE game jam](https://ldjam.com/events/ludum-dare/48). Doing gamedev has been a long-time elusive dream of mine, all the way back to my college years. I've had a number of failed attempts to get into gamedev, both solo and with other people.I've also played around with things like PyGame, [Unity](https://roytang.net/2017/01/10155238560218912/), [DragonRuby](https://roytang.net/2020/11/1326919888472956928/), etc.

I read about the LD48 game jam this April and signed up to participate. My expectations weren't very high and I was anxious going on; I was pretty sure I was not going to do well and doubted I could even put things together. I had never done a Ludum Dare or a game jam before, heck I haven't even made anything I consider a "real game" before!

The game jam has two modes you can choose to submit to. The 72-hour version (called the "Jam") was easier, as you could have a team of people working together, and you could use any assets you had legal access to. The 48-hour version, called the "Compo" (which I guess is short for competitive?), is much more challenging. You can only work solo, and all assets must be created within the 48 hour period (with a few exceptions like fonts etc).

I had no intention of working with a team; in fact I didn't tell anyone I planned to participate until after the jam started last Saturday at 9AM local time. I figured I would try my best and if I finished within 48h, I would submit for the jam. If I didn't, I had an extra 24h to try for the compo, and I could even ask for help! 

That meant I would be working alone, which meant I would have to do things like art and sounds and music! I didn't have any experience doing pixel art for games or anything like that, so I figured I could get by on "programmer art". For sound effects, I knew there were online generators I could use, I've tried some before. Background music was the real challenge: I have no musical talent at all, so even if I could find tools to do it, I wouldn't know how to put anything together. These were problems for me 48h into the future though. When the jam started, I just dove in to code.

Okay, not really. I woke up late and had to do some errands so I missed the start time by a couple of hours. Still, I dove right in as soon as I was free!

### The tools

For the gamedev/programming part, I decided to use the Godot Engine game development framework. I had been trying it out since earlier this year, and I was pretty happy with it compared to Unity. The IDE was a lot lighter, the APIs felt more intuitive, and basically it made it easier for me to get into the guts of a game. Unity is great, but it always seemed geared towards 3D gamedev. Godot makes 2D gamedev feel like a first class citizen. I prefer working on 2D because I feel like that's something more achieveable for me as an indie. Doing sprites and such is more in my wheelhouse than 3D models.

For the art, I've never tried any pixel art creation tools before, so I just searched online. I settled on [Piskel](https://www.piskelapp.com) which had the advantages of (a) being free; and (b) running entirely in-browser, without needing me to create an account. Very low friction! I haven't tried such tools before so I was impressed with how mature they were. There were functions similar to what you'd find in paint, plus support for layers and export to various formats, including into spritesheets. It was perfect for what I needed.

For sound effects, I used another free online site [JSFXR](https://sfxr.me/). Basically just kept rolling one of the settings until I got a sound I like. Godot's AudioStreamPlayer didn't seem like it accepted WAVs, so I used [convert.io](https://convertio.co/wav-ogg/) to convert the files to OGG.

For background music, a friend suggested I tried [Online Sequencer](https://onlinesequencer.net/). I tried it out for a while, banging out random notes since I knew nothing about how to compose music. I looked at a few interesting ones created by other people and tried to adjust the random notes I was banging out to better follow the patterns I saw. I still don't understand, but I was able to create a couple of tracks I was fairly happy with (they sounded like music!) which I used as BGM in the game.

I also used one of my [sketchdaily](/tags/sketchdaily) attempts to generate some [splash screen/cover art](https://roytang.net/2021/04/1385956018509664263/) for the game. The final game used a slightly cleaned up and modified version of that one.

I also needed a Dynamic font, since using Godot's built-in fonts didn't allow me to resize text. The Compo rules allow you to use fonts you didn't make during the jam, so I just used Xolonium-Regular from one of the Godot tutorials.

### The game

The theme of the jam was **DEEPER and DEEPER**, so I figured I'd go the easy route and do something with digging or undersea exploration. I felt like digging would be the more common approach, so I went the other way, since I'm a contrarian. I decided to do something inspired by things like the underwater level in TMNT (NES) or the underwater level in Earthworm Jim (SNES). These were the frustrating underwater levels I grew up with, so I wanted to replicate that experience a bit. Basically moving around underwater, with a time limit and trying to avoid obstacles. 

So the idea was to have a deep-sea diver exploring underwater. But for some reason the ocean is full of spikes, so he has to keep moving and swimming to avoid them. All the while trying to go deeper and deeper. I added in a few enemies like jellyfish that acted as moving obstacles, and seeker fish that actively tried to chase you.

I also added an oxygen tank mechanic to serve as the timer. The tank would be getting depleted constantly as you kept breathing and you had to avoid running out. There would be little things that generate air bubbles you can pick up to increase your oxygen level (this part was inspired by the 3d mario games). Initially the bubble generator was just a jar, but later I changed the sprite to a clam.

I also decided to add a collectible in the form of gems that you can pick up on your way down. Basically to add more things to do in each stage. And it added a bit of risk-reward mechanics: should I waste time trying to get this gem, when I might run out of air or get hit by enemies? When I added it I wasn't sure how the gems would be relevant in the game. I eventually decided to have the player earn extra lives whenever he collects 5 gems. The initial gem sprite was a diamond but later changed to a pearl.

That's the basic gameplay: Avoid obstacles, collect gems, avoid running out of air, try to get as deep as possible. 

The controls were simple: 

- your diver is constantly sinking
- you can move left or right using arrow keys
- you can swim up (or bounce, in my internal terms) by pressing space bar. 
 
The bounce was kind of a flappy bird bounce: you hit spacebar and you go up by a fixed amount after which you begin sinking again. I wanted the controls to be not too smooth so that you needed to know the bounce distance really well to navigate tighter corridors.

Once I had something basic working, I showed it to some friends to get some feedback, and got some good ideas and bug reports from them. (I figured showing it to other people and getting suggestions was fine within the compo rules, as long as I did all the actual creation work myself!)

By the end of Saturday (around 16h after jam start, 32h before compo deadline), I was mostly done with all the mechanics and gameplay and such. But content was lacking: I only had five screens ("stages") for the player to navigate through, which I felt was too short. Creating levels was fairly straightforward though once I had all the components ready. The feedback from my friends was also pretty good. By this point I was fairly confident I could finish in time, and probably wouldn't lose too much sleep.

I spent Sunday working more on the game, in between a bunch of family errands. I added another five levels, and fixed a lot of bugs. By the end of day Sunday (around 9h before compo deadline), I was ready to submit. Godot lets me export both to web and to Windows binaries. I could have also exported to other OSes, but I didn't have time to test them. I was originally planning to host the game here on this site, but I couldn't decide how / where to put them in the site structure. Instead I went ahead and deployed the game to itch.io, as I already had an account there. This was a relatively easy and straightforward process (though I did have to answer some tax-related questions). 

So the game is here on itch.io: https://hungryroy.itch.io/diver

Ludum Dare requires the source code be made available, I have it up here: https://github.com/roytang/diver

And finally, the page for my entry on the Ludum Dare site itself: https://ldjam.com/events/ludum-dare/48/diver

### Aftermath

After submitting your game, you're supposed to review and rate other people's games, and you want to earn at least 20 ratings to get a "final score". Coming in, I didn't really aim to "win" the compo or anything like that, I just wanted to finish a game. But after submitting and checking out a few of the other submissions, I felt a bit more confident about my chances and am hoping for a decent finish. The "play, review, and rate" period lasts for 21 days after the jam ends, so it'll be a while before I know the outcome of that! I am doing my part by playing through some of the entries and rating them and leaving helpful comments where I can.

Overall, very impressed with how Ludum Dare works. The more ratings and quality feedback you give, the higher your game appears in the listings. This makes it more likely for you to receive ratings and feedback yourself, thus incentivizing the same and creating a positive feedback loop!

My biggest takeaway is that I learned how to build something with as small a scope as possible. In many of my past attempts, scope creep was always one of the bigger problems. I was used to playing big, epic games like grand strategy or long RPGs or open world games, so I often wanted to make games like those. The 48h limit helped me narrow my focus and reject stuff that would endanger that deadline. I had to discard some other ideas for enemies and stage elements because they would make things more complicated.

I did enjoy the experience, no matter the outcome, I've already exceeded my own expectations. I expect to try my hand at game jams again moving forward. Building experience by making a series of small games might be a better way for me to find a path into "real" gamedev. That is, as opposed to "hobbyist" gamedev, which is the new level I consider myself at now that I've completed a Ludum Dare!

Some screenshots of the game attached below!