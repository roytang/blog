---
author: roy
categories: []
date: 2009-12-30 11:00:38
syndicated:
- type: twitter
  url: https://twitter.com/roy_mtg/statuses/7193308065/
tags:
- mtg
title: 'Nix Tix Alara Draft (Swiss): 3-0 and Draft Conversion Tools'
type: post
url: /2009/12/nix-tix-alara-draft-swiss-3-0/
---

Now, this is a bit awkward. One of the side projects that's been in my backlog for a long time has been to work on an improved version of the MTGO Draft Converter at [zizibaloob][1]. I thought I would get started on that today, and in fact already had quite a bit of javascript done for the draft widget when I read a [new post by Brian David-Marshall over on top8magic][2] and found out that there was already a new draft recorder website: [RareDraft][3]. I got myself an invite and tried it out, it has many of the features I was planning and more! Ah, now I don't know whether it's worth continuing my own project. =/

Anyway, here's the link to the unfinished, unrefined (but working!) [MtgStorm draft converter][4]. (if you've been following [me on twitter][5], you know that I created a new username ["mtgstorm"][6] for MTG-related stuff)

To see how far ahead RareDraft's offering is, here's a recent Alara block draft I 3-0'd on MTGO. The first output is by the MtgStorm draft converter, the second is by RareDraft.



<div class="draft_navmenu">
  Pack <a id="draft1262171203798_pack1" class="active" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPack(1)" href="#">1</a><a id="draft1262171203798_pack2" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPack(2)" href="#">2</a><a id="draft1262171203798_pack3" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPack(3)" href="#">3</a> Pick <a id="draft1262171203798_pick1" class="active" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(1)" href="#">1</a><a id="draft1262171203798_pick2" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(2)" href="#">2</a> <a id="draft1262171203798_pick3" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(3)" href="#">3</a><a id="draft1262171203798_pick4" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(4)" href="#">4</a><a id="draft1262171203798_pick5" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(5)" href="#">5</a><a id="draft1262171203798_pick6" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(6)" href="#">6</a><a id="draft1262171203798_pick7" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(7)" href="#">7</a><a id="draft1262171203798_pick8" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(8)" href="#">8</a><a id="draft1262171203798_pick9" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(9)" href="#">9</a><a id="draft1262171203798_pick10" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(10)" href="#">10</a><a id="draft1262171203798_pick11" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(11)" href="#">11</a><a id="draft1262171203798_pick12" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(12)" href="#">12</a><a id="draft1262171203798_pick13" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(13)" href="#">13</a><a id="draft1262171203798_pick14" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(14)" href="#">14</a><a id="draft1262171203798_pick15" onclick="mtgstorm.Draft.get(&quot;draft1262171203798&quot;).goToPick(15)" href="#">15</a>
</div>

<div id="draft1262171203798_wrapper">
  <img class="card" src="http://www.wizards.com/global/images/magic/ALA/resounding_thunder.jpg" alt="" /><br /> <img class="card" src="http://www.wizards.com/global/images/magic/ALA/jhessian_lookout.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/resounding_silence.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/dregscape_zombie.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/obelisk_of_jund.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/cathartic_adept.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/lightning_talons.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/naya_panorama.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/onyx_goblet.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/obelisk_of_esper.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/grixis_charm.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/bant_battlemage.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/etherium_astrolabe.jpg" alt="" /><img class="card pick " src="http://www.wizards.com/global/images/magic/ALA/sigil_of_distinction.jpg" alt="" /><img class="card" src="http://www.wizards.com/global/images/magic/ALA/island.jpg" alt="" />
</div>

Powered by [MtgStorm Draft Converter][4]



In hindsight, mine might be better in some cases because I'm using pure JavaScript, while theirs is using flash (and does not seem to resize to fit the containing column)... yeah, technical jargon.

 [1]: http://www.zizibaloob.com/
 [2]: http://www.top8magic.com/2009/12/crabs-for-christmas/
 [3]: http://raredraft.com
 [4]: http://mtgstorm.com/drafts/
 [5]: http://twitter.com/roytang
 [6]: http://twitter.com/mtgstorm