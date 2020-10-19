---
date: 2019-11-18 16:54:16
reply_to:
  label: a comment by [deleted] on 'How to you prevent a RPG from ending up into a
    mess of copy pasted if else statements?' on /r/gamedev
  name: ''
  type: reddit
  url: https://reddit.com/r/gamedev/comments/dy4omz/how_to_you_prevent_a_rpg_from_ending_up_into_a/f7ybonm/
source: reddit
syndicated:
- type: reddit
  url: https://www.reddit.com/r/gamedev/comments/dy4omz/how_to_you_prevent_a_rpg_from_ending_up_into_a/f7yj706/
tags:
- gamedev
---

Decision trees like "which starter pokemon do you pick" aren't things that should be embedded into your code as if/else statements. These should be data that your code loads.

For this specific example, you could have a data file that has a list of all the available starter pokemon. How many are available to choose from? Your code will read these data files and present them as choices. The data files could include the dialog text and say, an ID string to indicate which pokemon would then be added into your party, something like this (JSON format, because it's easier for me:

`starters: [` 

`{ "dialog": "I choose Charmander!", "pokemon_id": "0001"},` 

`{ "dialog": "I want Bulbasaur!", "pokemon_id": "0002"},` 

`{ "dialog": "I want Pikachu!", "pokemon_id": "0003"}` 

`]`

(I forgot who the 3rd starter was supposed to be, I'm not big on Pokemon. Also I'm guessing those aren't the actual pokedex IDs)

Each item on the list could also contain some other info. For example in dialogue trees, you might have NPCs react differently depending on what you say, so in that case each node would have an id pointing to the specific NPC response.

The idea is to separate the data from your code, since those are totally separate concerns. This is a general programming principle not specific to game development. In this way, you make it easier to modify your data (like decision trees) without necessarily having to rebuild your code. For example, you could change the dialog message for each pokemon starter choice, or maybe you could add more choices, or make the starter pokemon be Snorlax, MewTwo and Ekans for some reason (those are pokemon right? Lol). Bigger game studios will have separate tools to maintain those data files so that even nonprogrammers can help change those kinds of things in the game.