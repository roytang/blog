---
categories: []
date: 2008-02-10 15:18:23
tags:
- wordpress
- Software Development
title: MTG Autocard WordPress Plugin
type: post
url: /2008/02/mtg-autocard-wordpress-plugin/
---

I had been planning to do this for a while: it's my first WordPress Plugin! Over at [Roy on Magic][1], I often have to write out decklists and such, so I wanted to have an autocard feature similar to the one used at MTGSalvation. After a quick five-minute search I couldn't figure out how they did it, so I just wrote the plugin myself. Actual effort was around 3.5 hours, most of it struggling with PHP and Regular Expressions. :p

Details and download are at [http://roytang.pbworks.com/w/page/7977432/MTG-Autocard-WP][2]. Hopefully someone else will find it useful.

Update Jan 2021: Since the wiki link above is obsolete, I've rescued the text below for archival purposes. _This is not an active project!_ The download link below should be working, but I make no guarantees as to whether it will still work with current wordpress versions.

___

*MTG Autocard for Wordpress*

What: Wordpress Plugin

Plugin Name: MTG Autocard for Wordpress

URI: http://www.roytang.net/wiki/index.php/MTG_Autocard_WP

Description: For Magic: The Gathering bloggers, a plugin that will automatically convert [CARD] and [DECK] tags to autocard links.

Author: Roy Tang

Version: 1.1

Author URI: http://roytang.net

Revision 12-Oct-2008 (v1.1): Changed the algorithm that splits the card list into columns; can now potentially split into more than two columns.

Revision 13-Apr-2008: Fixed a bug where two [CARD] tag pairs in the same line/paragraph won't be converted correctly.

#### Installation Notes

Download the latest version file from /files/autocard.1.1.zip

Extract autocard.php

Upload autocard.php into your wp-content/plugins folder

Activate the plugin in the Wordpress Admin interface

#### Usage Notes

When posting, use `[CARD](cardname)[/CARD]` to generate an autocard link to a single card.

When posting a decklist, use a format like

```
[DECK]
Header1
4 Cardname1
4 Cardname2

Header2
12 Cardname3
8 Cardname4
[/DECK]
```

The above will generate a two-column table with autocard links. The program will try to break the list into two columns at the first header that exists after the midpoint.

To change the style of the decklist table, add a CSS definition for "autocard_table" in your style.css, for example:

`.autocard_table {border: 1px red solid; background-color: yellow;}`

Todo list

- Create a settings page to allow the user to select the URL opened by the autocard links. (Currently always uses http://magiccards.info/autocard.php)
- More options for formatting the autocard_table, i.e. more columns, etc.


 [1]: /tags/mtg
 [2]: http://roytang.pbworks.com/w/page/7977432/MTG-Autocard-WP