---
date: 2022-03-21 17:52:49+00:00
dontinlinephotos: true
reply_to:
  label: '''"Technology" is really not there and won''t be (for things you think are
    easy like ICR).'' on /r/MagicArena'
  name: stysiaq
  type: reddit
  url: https://www.reddit.com/r/MagicArena/comments/tj8ndx/technology_is_really_not_there_and_wont_be_for/
source: reddit
syndicated:
- type: reddit
  url: https://www.reddit.com/r/MagicArena/comments/tj8ndx/technology_is_really_not_there_and_wont_be_for/i1k2qwn/
tags:
- MagicArena
- replies
---

I've been meaning to comment on the whole "technology" meme, I guess this thread is fine for it. 

IIRC the original "technology" response in the stream was to the problem of cards being repeated across sets with different printings, i.e. your collection has 8 copies of each temple or 12 copies of Duress or whatever. People are saying why can't these just be cosmetics (card skins) or autodusted or whatever.

It seems pretty likely that this problem exists because they inherited their data structures from MTGO which mirrors the reality of paper, where each of a card's printings exists as a separate "card" object. Since MTGO doesn't care how many copies of a card exist in your collection and you can just sell your extras, this model just works for MTGO (the same way it does for paper).

On Arena it's problematic because you can't get rid of those extras, they just sit there taking up space and annoying the obsessive-compulsives among us. And this data structure probably influences how things like ICRs or duplicate protection works.

Because they're tied to this legacy data structure, they can't just easily treat different printings of the same card as the same. Most likely fixing this comprehensively requires an overhaul of the underlying data structure around cards, decks, collections, etc, and there are probably dependencies on the backend we can't even see. Going through all of these requires effort, so yeah, man-hours.

This is probably just one minor thing. From experience, technical debt in a large system tends to build up slowly but surely especially when the dev cycle is strained for resources, so most likely there are a lot of tiny things in the client and the backend that seem like minor problems but digging into them would break things somewhere else or otherwise require a lot of effort so they have to be really careful what they touch otherwise the whole house of cards might collapse. 

A lot of the "small" pain points attributable to "technology" probably boil down to "we can't afford to spend X manhours on this" - basically completely agreeing with the OP here. I would guess the guy being interviewed (was he a product guy or sth? IDK his name) didn't really know the technical details, or figured it would go over the head of the audience, so he just resorted to the "technology" shortcut. I think 

I'm not a fan of turning the "technology" response into a meme, as it can trivialize the dev work. Software development is hard. Maintaining and constantly updating a large system with thousands of interacting pieces and millions (?) of users is hard. Keeping software bug-free is hard. Even issues we experience that seem "minor" and could be easily fixed might have related issues or dependencies we aren't aware of that make it more complex to fix. 

Obviously WOTC could probably afford to pour more resources into Arena, but that won't necessarily mean problems would be resolved linearly faster (see: the Mythical Man Month). The problem (as it often is with software projects) is most likely with prioritization (and the fact that regular paper set releases means their dev cycle has an unchangeable cadence). Unfortunately, WOTC isn't a software company, so I don't expect them to communicate like a software company, their comms are largely driven by marketing concerns.

(I'm not arguing with the OP or anything, I largely agree with the thread here, just needed a place to post my thoughts lol.)