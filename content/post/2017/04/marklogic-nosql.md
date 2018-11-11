---
author: roy
categories:
- Software Development
date: 2017-04-06 01:30:33
title: MarkLogic NoSQL
type: post
url: /2017/04/marklogic-nosql/
---

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="499pb-0-0">
  <span class="hardreadability"><span data-offset-key="95h4t-0-0">I recently attended a few training sessions for </span></span><a href="http://www.marklogic.com/"><span data-offset-key="95h4t-1-0">MarkLogic</span></a><span class="hardreadability"><span data-offset-key="95h4t-2-0"> held at an office in a nearby business center</span></span><span data-offset-key="95h4t-3-0">. Now, I'll forgive you for not knowing what MarkLogic is, as even I hadn't heard of it before six months ago. MarkLogic is (</span><span class="adverb"><span data-offset-key="95h4t-4-0">apparently</span></span><span data-offset-key="95h4t-5-0">) the leading Enterprise NoSQL provider.</span>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="gr26-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="gr26-0-0">
    <span data-offset-key="gr26-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="art97-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="art97-0-0">
    <span class="veryhardreadability"><span data-offset-key="art97-0-0">NoSQL is big and sexy right now because of the supposed advantages in handling big data, and large web companies like Google and Facebook use a lot of NoSQL in the backend</span></span><span data-offset-key="art97-1-0">. </span><span class="hardreadability"><span data-offset-key="art97-2-0">Most of the popular/well-known NoSQL solutions are open-source/free ones: MongoDB, Cassandra, CouchDB, and so on</span></span><span data-offset-key="art97-3-0">. </span><span class="hardreadability"><span data-offset-key="art97-4-0">But these aren't actually very popular on the enterprise side, hence &#8220;Enterprise NoSQL&#8221; isn't a very common phrase</span></span><span data-offset-key="art97-5-0">.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="b99to-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="b99to-0-0">
    <span data-offset-key="b99to-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="3a4hf-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="3a4hf-0-0">
    <span class="veryhardreadability"><span data-offset-key="3a4hf-0-0">One of the reasons NoSQL isn't currently very popular for enterprise projects is that the popular open-source solutions such as MongoDB don't guarantee ACID transactions</span></span><span data-offset-key="3a4hf-1-0">. </span><span class="veryhardreadability"><span data-offset-key="3a4hf-2-0">In fact, MongoDB has the concept of &#8220;eventual consistency&#8221; for their distributed servers, which implies that they don't have real-time consistency</span></span><span data-offset-key="3a4hf-3-0">.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="eg4ik-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="eg4ik-0-0">
    <span data-offset-key="eg4ik-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="26pou-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="26pou-0-0">
    <span data-offset-key="26pou-0-0">MarkLogic does guarantee ACID transactions, along with government-grade security. Both of these are things that enterprise clients love. So that's the market they're in. </span><span class="veryhardreadability"><span data-offset-key="26pou-1-0">Their highest-profile project to-date was the backend datastore for Healthcare.gov (also known as Obamacare/ACA)</span></span><span data-offset-key="26pou-2-0">. </span><span class="veryhardreadability"><span data-offset-key="26pou-3-0">That project involved consolidating data with different structures from </span></span><span class="complexword"><span data-offset-key="26pou-4-0">multiple</span></span><span class="veryhardreadability"><span data-offset-key="26pou-5-0"> sources and needed to scale up to a </span></span><span class="adverb"><span data-offset-key="26pou-6-0">ridiculously</span></span><span class="veryhardreadability"><span data-offset-key="26pou-7-0"> high capacity, so it seemed tailor-fit for a big data level NoSQL solution</span></span><span data-offset-key="26pou-8-0">.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="bkhkm-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="bkhkm-0-0">
    <span data-offset-key="bkhkm-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="gph9-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="gph9-0-0">
    <span class="veryhardreadability"><span data-offset-key="gph9-0-0">During the second-to-last day of the training, Jason Hunter, CTO of Marklogic for Asia-Pacific, dropped in to answer some questions</span></span><span data-offset-key="gph9-1-0">. </span><span class="veryhardreadability"><span data-offset-key="gph9-2-0">He talked a bit about how MarkLogic started and how they got him on board, and a bit about their competition (some disparagement towards MongoDB and Oracle) and about Healthcare.gov</span></span><span data-offset-key="gph9-3-0">.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="6pv85-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="6pv85-0-0">
    <span data-offset-key="6pv85-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="1bb2p-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="1bb2p-0-0">
    <span data-offset-key="1bb2p-0-0">He also had a </span><span class="adverb"><span data-offset-key="1bb2p-1-0">really</span></span><span data-offset-key="1bb2p-2-0"> good sales pitch about why NoSQL is </span><span class="qualifier"><span data-offset-key="1bb2p-3-0">just</span></span><span data-offset-key="1bb2p-4-0"> a better approach compared to RDBMS. </span><span class="hardreadability"><span data-offset-key="1bb2p-5-0">(Although it would have been more fun if he had given this talk with like an Oracle salesperson there to debate with him</span></span><span data-offset-key="1bb2p-6-0">.)</span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="kdo7-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="kdo7-0-0">
    <span data-offset-key="kdo7-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="718jd-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="718jd-0-0">
    <span data-offset-key="718jd-0-0">One of his points was that RDBMS restrictions such as limits on column size </span><span class="passivevoice"><span data-offset-key="718jd-1-0">are outdated</span></span><span data-offset-key="718jd-2-0">. </span><span class="hardreadability"><span data-offset-key="718jd-3-0">They were sensible in the old days when disk space was at a premium, but these days you don't need to limit how many characters you store in a last name field</span></span><span data-offset-key="718jd-4-0">. MarkLogic stores all records as documents with no file size limit (AFAIK) to avoid such an issue. </span><span class="veryhardreadability"><span data-offset-key="718jd-5-0">From experience developing web forms, there's the occasional client or system user who doesn't understand why we need to have character limits on fields</span></span><span data-offset-key="718jd-6-0">. </span><span class="hardreadability"><span data-offset-key="718jd-7-0">We also had this system where they wanted to be able to type unlimited-length rich text content (we stored it as HTML in the backend) in memoboxes</span></span><span data-offset-key="718jd-8-0">. </span><span class="hardreadability"><span data-offset-key="718jd-9-0">These were fields where they had to write stuff like notes and assessments and most of their data was pages of text</span></span><span data-offset-key="718jd-10-0">. </span><span class="qualifier"><span data-offset-key="718jd-11-0">I feel</span></span><span data-offset-key="718jd-12-0"> like that sort of thing would have been a great use for NoSQL.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="89k12-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="89k12-0-0">
    <span data-offset-key="89k12-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="dp52e-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="dp52e-0-0">
    <span class="hardreadability"><span data-offset-key="dp52e-0-0">Another point he raised was that RDBMS systems were very bad at allowing the user to search like three columns at random</span></span><span data-offset-key="dp52e-1-0">. You needed to know in advance which three columns to index. </span><span class="hardreadability"><span data-offset-key="dp52e-2-0">For document stores like MarkLogic, </span></span><span class="adverb"><span data-offset-key="dp52e-3-0">typically</span></span><span class="hardreadability"><span data-offset-key="dp52e-4-0"> the entire document </span></span><span class="passivevoice"><span data-offset-key="dp52e-5-0">is indexed</span></span><span class="hardreadability"><span data-offset-key="dp52e-6-0"> so that problem </span></span><span class="passivevoice"><span data-offset-key="dp52e-7-0">is avoided</span></span><span data-offset-key="dp52e-8-0">. Of course, that means that functions like &#8220;sorting by last name&#8221; need a bit more setup. You need to build a range index in MarkLogic to sort by a specific field. So it's kind of a trade-off either way.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="1nstr-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="1nstr-0-0">
    <span data-offset-key="1nstr-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="8v98d-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="8v98d-0-0">
    <span class="hardreadability"><span data-offset-key="8v98d-0-0">Now to be fair, Oracle does support indexed full-text search over any number of columns via Oracle Text</span></span><span data-offset-key="8v98d-1-0">. But it's not the default behavior and definitely not straightforward. </span><span class="hardreadability"><span data-offset-key="8v98d-2-0">I used to work with Oracle Text a lot in some of my older projects, and the amount of time it took to index any nontrivial amount of data often gave us a headache</span></span><span data-offset-key="8v98d-3-0">.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="f3j9b-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="f3j9b-0-0">
    <span data-offset-key="f3j9b-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="9d1rv-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="9d1rv-0-0">
    <span data-offset-key="9d1rv-0-0">I should do a test sometime to determine how well MarkLogic's indexing performs. </span><span class="hardreadability"><span data-offset-key="9d1rv-1-0">The story goes that MarkLogic started out as a document search application before they changed gears to become a database</span></span><span data-offset-key="9d1rv-2-0">. They even approached VC's with the intent of competing with Google. They've had a lot of time to get good at this, so I have high expectations.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="3dbt5-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="3dbt5-0-0">
    <span data-offset-key="3dbt5-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="abg4a-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="abg4a-0-0">
    <span data-offset-key="abg4a-0-0">The MarkLogic server itself is an interesting piece of engineering. </span><span class="hardreadability"><span data-offset-key="abg4a-1-0">It's </span></span><span class="adverb"><span data-offset-key="abg4a-2-0">basically</span></span><span class="hardreadability"><span data-offset-key="abg4a-3-0"> a document store, a search engine and an application server all rolled into one package</span></span><span data-offset-key="abg4a-4-0">. Upon installation you get some administrative web applications for configuration purposes. The admin interface seems robust and thorough. </span><span class="hardreadability"><span data-offset-key="abg4a-5-0">Contrast that with Oracle where you often find yourself needing to tinker around with configuration files and such</span></span><span data-offset-key="abg4a-6-0">. </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="dlss0-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="dlss0-0-0">
    <span data-offset-key="dlss0-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="814ui-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="814ui-0-0">
    <span data-offset-key="814ui-0-0">You can run web applications on the MarkLogic server itself. The supported languages are XQuery and server-side JavaScript. Odd choices I know. </span><span class="hardreadability"><span data-offset-key="814ui-1-0">I suspect due to historical reasons they started out with XQuery, but the SJS side has the same capabilities (or so we're told)</span></span><span data-offset-key="814ui-2-0">. If you're not a fan of either option, you can also expose the server's functionality via a REST interface. They also provide existing Java and Node.JS APIs on top of that REST interface. </span><span class="complexword"><span data-offset-key="814ui-3-0">All of</span></span><span data-offset-key="814ui-4-0"> this means you can deploy any kind of webapp in front of MarkLogic server.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="8nbca-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="8nbca-0-0">
    <span data-offset-key="8nbca-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="f4n2s" data-offset-key="atd2i-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="atd2i-0-0">
    <span class="hardreadability"><span data-offset-key="atd2i-0-0">The world is moving towards bigger data stores, so it's not unreasonable to think that NoSQL is on the way up and will be big players in the future</span></span><span data-offset-key="atd2i-1-0">. So </span><span class="qualifier"><span data-offset-key="atd2i-2-0">I think</span></span><span data-offset-key="atd2i-3-0"> the training was worth it (even if I did have to stay in Ortigas for a while). It's early still. MarkLogic might still turn out to be as painful to work with as Oracle was. </span><span class="hardreadability"><span data-offset-key="atd2i-4-0">But at the very least it's interesting to try a different approach to enterprise data storage</span></span><span data-offset-key="atd2i-5-0">. Looking forward to see what kind of applications we can build with this tech.</span>
  </div>
</div>