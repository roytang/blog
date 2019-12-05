---
date: 2011-04-07 00:00:00+00:00
reply_to:
  label: '''Multiple "until end of turn" effects. How do they work?'' on /r/magicTCG'
  name: ''
  type: reddit
  url: /r/magicTCG/comments/gkbb9/multiple_until_end_of_turn_effects_how_do_they/
source: reddit
syndicated:
- type: reddit
  url: https://www.reddit.com/r/magicTCG/comments/gkbb9/multiple_until_end_of_turn_effects_how_do_they/c1o61gw/
tags:
- magicTCG
---

The damage is removed and the giant growth is removed, both at the same time. The important thing is state-based effects (including the thing that checks whether your creature is dead due to damage > toughness) do not check in between; once all end of turn effects are cleaned up, that's the only time things are checked to see if they are alive or dead. So, the correct answer is (1)