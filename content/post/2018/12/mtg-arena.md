---
author: roy
categories: []
date: 2018-12-18 01:56:56
featuredImage: https://roytang.net/uploads/2018/mtgarena.png
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1074847827149365248/
tags:
- ccgs
- Magic the Gathering
- Gaming
title: MTG Arena
type: post
---

I've been playing [MTG Arena](https://magic.wizards.com/en/mtgarena) for a good while now, a little bit during the closed beta, and now I think we're still in open beta (?) because things still keep changing around. But I figured I could put in a little commentary about how this thing is going so far. I'm coming off the POV of a long-time [Magic the Gathering](/categories/magic-the-gathering/) player of course, with a little bit of comparison to [Eternal](/2018/11/review-eternal-or-eternal-primer-for-mtg-players/) and [Hearthstone](/2016/05/hearthstone-vs-mtg/), the two digital CCGs I'm most familiar with.

### Client, Ruleset, and Gameplay

![/uploads/2018/mtgarena.png](/uploads/2018/mtgarena.png)

Unlike the earlier Duels of the Planeswalkers game, it looks MTG Arena is a complete implementation of the paper MTG ruleset, but with a more limited card base. At the moment, only the cards from the [current standard](https://whatsinstandard.com/) are currently available (sets from the previous rotation were available during the closed beta.) Granted, the MTG ruleset is a complicated beast, so they probably have a few bugs hidden away there somewhere but for the most part it is a faithful conversion.

The client looks and feels great, a much more modern platform compared to the ugly rustbucket that is MTGO, they really built upon what they started with Duels. Some of the QoL improvements from both Duels and MTGO carry over (mostly Duels). Autotapping of lands and autopass of priority when you have nothing to play are enabled by default. I'm always worried that the autotapper will screw something up and leave me in a bad position, but so far that hasn't happened. You can add stops to opponent's upkeep, draw, first and second mains, and end step, same as MTGO. "Attack All" is available, though I wish it worked better with planeswalkers. When cards from your opponent's hand are revealed, they stay revealed (you can hover over the opponent's hand to zoom in) until they leave that zone.

There's a few issues with the presentation though: 

- triggered abilities could have more options to better handle when they trigger multiple times. One of the worst offenders is {{< card >}}Ajani's Pridemate{{< /card >}}, which is in one of the better starter decks. The triggered ability requires a player confirmation every time, which can be annoying when the Pridemate triggers multiple times on complicated boards. There should be an option like "Always take this action", similar to MTGO's "Always yield" for triggered abilities
- timeouts need a lot of work. The main issue is that the timers still count down while the client is animating effects and you can't do anything. That time really shouldn't count against you. 
- damage dealt to creatures and toughness penalties are presented the same way, as lowered red toughness numbers on the creature itself, even though rules-wise they are actually different - the main difference being indestructible doesn't prevent death due to 0 toughness or less. I've already seen at least one confused newbie on reddit trying to figure out how indestructibility works and being confused because of this.

### New Player Experience and Economy

NPE is okay. You get a bunch of starter decks, one for each color and color pair. Same as Eternal actually. The starter decks also provide some decent cards to start out your collection, with some mythics even. Some useful cards they provide include {{< card >}}History of Benalia{{< /card >}}, {{< card >}}Rekindling Phoenix{{< /card >}}, {{< card >}}Settle the Wreckage{{< /card >}} and {{< card >}}Vraska's Contempt{{< /card >}} IDK what they're going to do when there's a rotation and the starter decks don't work anymore. Well actually, I guess I don't know what they plan to do for rotation at all, so we'll just see what happens.

Same as Hearthstone and Eternal, there's daily quests to help you earn gold, and you can win gems from some events, so there's that. You also get a free pack every five wins, with a cap of three such packs per week. I haven't done the math but I'd say the rewards system is slightly more generous than Hearthstone, but way less generous than Eternal. You also get some rewards for each win for the day, but this drops off quickly.

The weird thing is they didn't go with a "dusting" system for extra cards, which is how other CCGs usually do it. Crafting is instead done using rarity-specific "wildcards" which you can open from booster packs. This leads to the so-called "fifth card problem", where whenever you open the fifth copy of a card from a booster pack, it literally has no use for you. They have scheduled a "duplicate protection" update to fix this sometime around 1Q2019, but I'm not sure if that'll work out. I hope they also think about some mechanism for "cashing out" your rotating cards since they need to implement rotations less than a year from now, but I'm even less hopeful about that.

### Limited Play

There's draft and sealed options available, with formats (the sets being opened) rotating every two weeks. When I started out I played mostly drafts (as soon as I had the gold, I would draft), since I didn't have enough of a collection yet to make a decent constructed deck. The draft experience isn't exactly the same as paper though. For one thing, you're drafting against bots, not actual humans. Eternal is able to make draft work vs actual humans, so Arena should be able to do it too. IDK how Eternal does it actually, one would presume the first few people to draft a format won't have other draft pools yet to be passed to them. Regardless, Arena should be passing you packs from real humans whenever possible and bots only when no such packs are available. Still, the draft experience is passable.

### Constructed Play

There's a ranked ladder which you can play for free, both Best of 1 (BO1) and Best of 3 (BO3) options are available. You can also play in Constructed Events, which have an entry fee and offer more prizes, and there's also BO1 and BO3 options there. They also often have "fun" events in different formats like Singleton or some strange format with custom rules. Kind of like Hearthstone's Tavern Brawl I guess?

The limiter for constructed play is your available wildcards. Getting rare wildcards is reasonable enough - you are guaranteed to get one every six packs you open. Mythics are another matter, you are only guaranteed to get one every thirty-six packs. So for a F2P player (that's me!) you will be likely constrained to decks with lower mythic counts, at least early on. For now, I've been playing [Monoblue Tempo](https://www.mtggoldfish.com/archetype/standard-mono-blue-tempo-60563#paper), a tier 2 deck (really has trouble against a resolved ) that has no mythics and has decent play value. I do love me some aggro control, so this is a fine choice for me for now. I've been playing it in BO3 Competitive Constructed Events (recently renamed to "Traditional Constructed"), and have a decent enough winrate that it has always made me profit. Standard is in a pretty good place right now actually - there's a ton of viable decks and quite a few other decks that are relatively easy to put together, like monored or Izzet Drakes, so it's a good time to be playing standard in Arena.

It's great to have an option for BO3 play. The complexity of competitive Magic shines through in BO3 play, although it takes much longer to play them out. Actually, Magic games in general, even BO1, take longer to play than Eternal (which is weird because Eternal has higher deck size and starting life), which means grinding out wins as a F2P player would be more exhausting. There was a recent outcry when they announced a tweak to constructed rewards that would have made BO3 events much less appealing, basically giving them the same rewards structure as BO1 events, which is ridiclous since BO3 games take so much more time. They walked back on that change though, but haven't announced a replacement yet, let's see if they do better next time. 

![/uploads/2018/mtgarena2.png](/uploads/2018/mtgarena2.png)

I also have this not-so-competitive BG midrange deck that I was building towards before I netdecked the MonoBlue one. I had already spent a few mythic wildcards towards it, kind of a bad choice really, because the ranked ladder does this weird matchmaking thing where you're more likely to fight against decks that have similar rare/mythic counts. So what usually happens is my unoptimized BG monstrosity gets roflstomped by tuned netdecks and such. After discovering this, I now mostly only play either the starter decks on ranked (to fulfill my daily quests) or Competitive Constructed with the Monoblue (in order to build up gold/cards). I still occasionally do break out the BG deck for fun.

I wrote most of the above paragraphs in a draft a week or two ago, and they just recently released a new patch that overhauled the rank system and matchmaking. I haven't explored it too much yet, I hope it's better.

### F2P, ESports, and Competitive Play

Wizards announced recently that [Arena will join the Pro Tour as part of their competitive play offerings and there will be a combined $10M prize pool for both paper Magic and Arena in 2019](https://magic.wizards.com/en/competitive-magic). This is exciting for me because it offers a more convenient avenue for competitive play. I'll be honest, I'm a bit older now and I'm not too fond of playing in big paper MTG tournaments anymore. You have to travel somewhere, and it's often hot and crowded and I have to shufffle with my sweat hands and you have to make sure your opponent's not cheating and so on. But if I'm playing from the comfort of my home computer, well that's a lot better for me! 

I was initially planning to play Arena same way I play other online CCGs - grinding it out as a F2P player. But I might be willing to change that depending on how the competitive landscape looks moving forward. It will probably be cheaper for me in the long run anyway - both paper Magic and MTGO are expensive options. So I'm hoping WOTC doesn't screw this up and provides a decent tournament experience for Arena. It's especially timely as there's no convenient Grand Prixs near me next year so I was planning to kind of lay low with paper Magic anyway.

### Summary

MTG Arena is still in open beta, and I assume the formal release will be around late 2019, when the next rotation comes in. I'll probably make a follow-up post at that time. I'm optimistic and hoping for the best and hopefully all the issues will be ironed out. Arena has the potential to trounce the online CCG scene, especially since Valve's Artifact hasn't been able to live up to its hype (though I might still try it). All Wizards has to do is to not screw things up!