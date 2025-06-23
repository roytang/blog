---
date: 2021-08-18 14:57:02
dontinlinephotos: true
like_of: https://twitter.com/JoelBurgess/status/1428008041887281157/
repost_source:
  name: JoelBurgess
  type: twitter
  url: https://twitter.com/JoelBurgess/
source: twitter
syndicated:
- type: twitter
  url: https://twitter.com/JoelBurgess/status/1428008041887281157/
tags:
- skyrim
- gamedev
- gaming
title: 'JoelBurgess: The Skyrim Fox'
---

Alright, so inspired by [@NPurkeypile](https://twitter.com/NPurkeypile/)'s bee post yesterday, here is one of my favorite bits of Skyrim oral history - the myth of the treasure fox.



I've told this story before in talks/etc, but I don't think I've shared it with twitter.  Here goes. 

{{< photos 1428008041887281157 >}}

<time id="1428008043556622336">[22:57]</time> Among Skyrim players, you'll occasionally see this tip: if you see a wild fox, follow it and you'll be led to treasure.



Sometime shortly after shipping, we saw this going around online, and an informal investigation started.  Who made foxes do this?!

<time id="1428008045012004866">[22:57]</time> The usual suspects got interrogated - myself, 

[@jean_simonet](https://twitter.com/jean_simonet/) [@Jonahlobe](https://twitter.com/Jonahlobe/) and [@Markiepo0](https://twitter.com/Markiepo0/) , among others.  Nobody confessed.  



I got curious and started digging around in the scripts - nothing.



So if nobody MADE this behavior, what's up?



Jean figured it out.  (as usual)

<time id="1428008052314234887">[22:57]</time> Skyrim uses something called 'navmesh' for AI navigation.  



For non-dev folks, this is an invisible 3D sheet of polygons that is laid over the world, telling AI where it can and cannot go.



This red stuff is navmesh.  You can read about it here: https://creationkit.com/index.php?title=Category:Navmesh 

{{< photos 1428008052314234887 >}}

<time id="1428008060946194433">[22:57]</time> In most situations, you're seeing AI decide what do to (run at player, hide in cover, etc), use navmesh to make a path, and navigate along that path.



Foxes are no different.  But their AI is very simplified: they basically can *only* run away.  



If you spook a fox, it flees. 

{{< video width="320" height="187" src="https://video.twimg.com/tweet_video/E9FNwoHXsAcerKq.mp4" >}}

<time id="1428008062913327111">[22:57]</time> So foxes flee.  Why would they flee towards treasure?

🦊👑💰

This is where it gets interesting.  



If you're close to an AI, it's in "High Process", or the most fancy, cpu-intensive pathfinding.  It uses the full navmesh and will do things like line of sight and distance checks.

<time id="1428008064737742856">[22:57]</time> To contrast, there's also "Low Process" - used for stuff like NPCs walking a trade route across the world. 

 These are only updated every several minutes, and position is tracked very loosely.



The bandit stabbing your face, however, is running nav stuff many times per second.

<time id="1428008066444926982">[22:57]</time> So [@jean_simonet](https://twitter.com/jean_simonet/) knew something that I didn't (as usual) 



There is a sort of "Medium Process" for characters nearby, but who didn't need the complex pathing of combat.  



Because of the way the fox's AI worked (always be fleeing!) it's basically ONLY using this process.

<time id="1428008074233753603">[22:57]</time> This is where understanding of how Skyrim uses navmesh comes in.



Swaths of the outdoor world have simple navmesh.  You don't need to add lots of detail in a space with basic topography, little clutter, or a low chance of combat.  



So wilderness = small number of big triangles. 

{{< video width="320" height="178" src="https://video.twimg.com/tweet_video/E9FNxZfXoAAc0TQ.mp4" >}}

<time id="1428008083909906434">[22:57]</time> When you stumble across something like a camp, however, navmesh gets way more detailed.  Added visual detail means added navmesh detail, and if we're placing NPCs of any kind, we also tend to add even more detail.  



So Points of Interest = big number of small triangles. 

{{< video width="320" height="371" src="https://video.twimg.com/tweet_video/E9FNx87XIAIasb7.mp4" >}}

<time id="1428008092218925059">[22:57]</time> You see where this is going?



The Fox isn't trying to get 100 meters away - it's trying to get 100 *triangles* away.



You know where it's easy to find 100 triangles?  The camps/ruins/etc that we littered the world with, and filled with treasure to reward your exploration. 

{{< video width="320" height="177" src="https://video.twimg.com/tweet_video/E9FNychXIAIN4n5.mp4" >}}

<time id="1428008094064332806">[22:57]</time> So foxes aren't leading you to treasure - but the way they behave is leading them to areas that tend to HAVE treasure, because POIs w/loot have other attributes (lots of small navmesh triangles) that the foxes ARE pursuing.



To players, however, it's the same thing.

<time id="1428008102457139206">[22:57]</time> It's a nerdy little story, but I love it.  



Emergent Gameplay is often used to describe designed randomness, but this is a case of actual gameplay that NOBODY designed emerging from the bubbling cauldron of overlapping systems.



And I think that's beautiful. 

{{< video width="320" height="180" src="https://video.twimg.com/tweet_video/E9FNzANXMAcDs5P.mp4" >}}

<time id="1428008104457818115">[22:57]</time> BTW ICYMI ETC - here's the post from [@NPurkeypile](https://twitter.com/NPurkeypile/) that I mentioned at the top.  Fun read if you like criminal bees.





{{% quoted url="https://twitter.com/NPurkeypile/status/1427650365558857728?s=20/" label="NPurkeypile's tweet" %}}

So, I have a story about the Skyrim Intro and how hard game development is.



That intro is famous now, but back then, it was just that one thing that we had to keep working and working on forever. I lost track of how many times I've seen that cart ride. Easily hundreds. (thread) 

{{< video width="320" height="212" src="https://video.twimg.com/tweet_video/E9AIG_pWEAAiznV.mp4" >}}

{{% /quoted %}}