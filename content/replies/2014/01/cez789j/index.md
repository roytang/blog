---
date: 2014-01-26 00:00:00
reply_to:
  label: '''Probably a dumb question about Rakdos, Lord of Riots, by a noobie building
    his first Standard deck.'' on /r/magicTCG'
  name: ''
  type: reddit
  url: https://reddit.com/r/magicTCG/comments/1w6kxn/probably_a_dumb_question_about_rakdos_lord_of/
source: reddit
syndicated:
- type: reddit
  url: https://www.reddit.com/r/magicTCG/comments/1w6kxn/probably_a_dumb_question_about_rakdos_lord_of/cez789j/
tags:
- magicTCG
---

That last ability isn't like a spell effect that is only determined when the creature spell resolves. It's a static continuous effect that is in effect all the time as long as Rakdos, LOR is on the battlefield. The expression "life your opponents have lost this turn" is thus evaluated continuously, instead of based on a fixed time. 

Unfortunately, this wording is not addressed directly in the comprehensive rules, mostly because the term "this turn" is most commonly used on spells and abilities instead of continuous effects. I suggest trying the Judge chat (http://chat.magicjudges.org/mtgrules/) to see if they could cite any gatherer rulings from similar cards (the gatherer page for Rakdos, LOR does not have anything relevant)

It should be noted that the alternative (that the reduction is only determined at casting time) would probably be implemented using counters, i.e. something like "Rakdos, Lord of Riots enters the battlefield with X evil counters, where X is the amount of life your opponents lost this turn. Creature spells you cast cost 1 less to play for each evil counter on Rakdos, Lord of Riots." The counters are needed because without them, there would be memory issues with such an effect.