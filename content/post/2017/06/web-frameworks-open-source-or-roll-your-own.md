---
author: roy
categories: []
date: 2017-06-22 04:19:27
tags:
- Software Development
title: Web Frameworks -- Open Source or Roll Your Own?
type: post
url: /2017/06/web-frameworks-open-source-or-roll-your-own/
---

<div class="" data-block="true" data-editor="154rn" data-offset-key="2j7h7-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="2j7h7-0-0">
    <span class="hardreadability"><span data-offset-key="bk3q5-0-0">A while back I </span></span><a href="http://roytang.net/2016/10/coding-frameworks/"><span data-offset-key="bk3q5-1-0">wrote about my experience</span></a><span class="hardreadability"><span data-offset-key="bk3q5-2-0"> coding and maintaining an in-house web framework at a previous job</span></span><span data-offset-key="bk3q5-3-0">. It was a full-stack web framework. We had libraries for front-end Javascript up to server-side database connections. And the entire stack was </span><span class="adverb"><span data-offset-key="bk3q5-4-0">tightly</span></span><span data-offset-key="bk3q5-5-0"> coupled. </span><span class="hardreadability"><span data-offset-key="bk3q5-6-0"> But while the framework was serviceable, it was almost always behind modern trends in web development</span></span><span data-offset-key="bk3q5-7-0">. I always felt like we were playing catch-up. And as a developer I wanted to widen my horizons and try out more things. </span><span class="hardreadability"><span data-offset-key="bk3q5-8-0">So more than once I had discussions with higher management about using open source web frameworks in some projects</span></span><span data-offset-key="bk3q5-9-0">.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="154rn" data-offset-key="cf2ii-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="cf2ii-0-0">
    <span data-offset-key="cf2ii-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="154rn" data-offset-key="6qcr-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="6qcr-0-0">
    <span class="hardreadability"><span data-offset-key="6qcr-0-0">Unfortunately, our in-house web framework already had a long history and most of the devs in our company </span></span><span class="passivevoice"><span data-offset-key="6qcr-1-0">were used</span></span><span class="hardreadability"><span data-offset-key="6qcr-2-0"> to it</span></span><span data-offset-key="6qcr-3-0">. The company had tried using a different Java-based framework stack before. It was back in the days when things like Struts, Spring, Hibernate, etc were beginning to ramp up. It kind of ended in disaster -- that project ended up taking a lot of effort, had a lot of technical problems, and so on. </span><span class="qualifier"><span data-offset-key="6qcr-4-0">I believe</span></span><span class="hardreadability"><span data-offset-key="6qcr-5-0"> this gave the company leadership the impression that investing in other frameworks are not worth the risk and effort</span></span><span data-offset-key="6qcr-6-0">. It's a form of </span><a href="https://en.wikipedia.org/wiki/Not_invented_here"><span data-offset-key="6qcr-7-0">Not Invented Here</span></a><span data-offset-key="6qcr-8-0"> syndrome.</span>
  </div>
</div>

<div class="" data-block="true" data-editor="154rn" data-offset-key="kuc0-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="kuc0-0-0">
    <span data-offset-key="kuc0-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="154rn" data-offset-key="47ql9-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="47ql9-0-0">
    <span data-offset-key="47ql9-0-0">I admit there are some advantages to having your own in-house web framework. </span><span class="hardreadability"><span data-offset-key="47ql9-1-0">After all, all the popular web frameworks today started out in-house in some company and later they decided to release as open source</span></span><span data-offset-key="47ql9-2-0">. And many companies do fine using in-house frameworks. Using an in-house framework means full control over the behavior. And you can tailor the functionality and coding style to your internal processes. </span><span class="hardreadability"><span data-offset-key="47ql9-3-0">In fact it can be a good value add to your company if your in-house framework did something better or unique compared to open source ones</span></span><span data-offset-key="47ql9-4-0">. </span>
  </div>
</div>

<div class="" data-block="true" data-editor="154rn" data-offset-key="a8fn5-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="a8fn5-0-0">
    <span data-offset-key="a8fn5-0-0"> </span>
  </div>
</div>

<div class="" data-block="true" data-editor="154rn" data-offset-key="evq7f-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="evq7f-0-0">
    <span data-offset-key="evq7f-0-0">But there are also significant advantages to using open source frameworks. </span><span class="qualifier"><span data-offset-key="evq7f-1-0">Maybe</span></span><span data-offset-key="evq7f-2-0"> I should have used some of these during discussions when I was there:</span>
  </div>
</div>

<div class="" data-block="true" data-editor="154rn" data-offset-key="2e3mf-0-0">
  <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="2e3mf-0-0">
    <span data-offset-key="2e3mf-0-0"> </span>
  </div>
</div>

<ul class="public-DraftStyleDefault-ul" data-offset-key="8eoda-0-0">
  <li class="public-DraftStyleDefault-unorderedListItem public-DraftStyleDefault-reset public-DraftStyleDefault-depth0 public-DraftStyleDefault-listLTR" data-block="true" data-editor="154rn" data-offset-key="8eoda-0-0">
    <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="8eoda-0-0">
      <span class="hardreadability"><span data-offset-key="8eoda-0-0">With an open source framework, we wouldn't have to maintain the core functionality of the framework ourselves</span></span><span data-offset-key="8eoda-1-0">. We wouldn't have to maintain the full stack ourselves. We would only need to maintain any customisations and extensions we write for our own needs. </span><span class="hardreadability"><span data-offset-key="8eoda-2-0">For our in-house web framework, every so often we'd spend some effort to come out with a new version with incremental improvements</span></span><span data-offset-key="8eoda-3-0">. </span><span class="hardreadability"><span data-offset-key="8eoda-4-0">With an open source framework, we could instead redirect that effort to higher-value work</span></span><span data-offset-key="8eoda-5-0">.</span>
    </div>
  </li>
  
  <li class="public-DraftStyleDefault-unorderedListItem public-DraftStyleDefault-reset public-DraftStyleDefault-depth0 public-DraftStyleDefault-listLTR" data-block="true" data-editor="154rn" data-offset-key="8eoda-0-0">
    <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="8eoda-0-0">
      There's more learning material available online, and they don't have to be maintained in-house.
    </div>
  </li>
  
  <li class="public-DraftStyleDefault-unorderedListItem public-DraftStyleDefault-reset public-DraftStyleDefault-depth0 public-DraftStyleDefault-listLTR" data-block="true" data-editor="154rn" data-offset-key="8eoda-0-0">
    <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="8eoda-0-0">
      <span data-offset-key="241np-0-0">There's a wider base of experience to draw from. </span><span class="veryhardreadability"><span data-offset-key="241np-1-0">For our in-house framework if you encountered a problem requiring deep framework knowledge, there were only a handful of high-level experts in the company</span></span><span data-offset-key="241np-2-0">. </span><span class="hardreadability"><span data-offset-key="241np-3-0">For an open-source web framework, that expertise is </span></span><span class="adverb"><span data-offset-key="241np-4-0">widely</span></span><span class="hardreadability"><span data-offset-key="241np-5-0"> available on the internet through sites such as </span></span><a href="https://stackoverflow.com/"><span data-offset-key="241np-6-0">Stack Overflow</span></a><span data-offset-key="241np-7-0">.</span>
    </div>
  </li>
  
  <li class="public-DraftStyleDefault-unorderedListItem public-DraftStyleDefault-reset public-DraftStyleDefault-depth0 public-DraftStyleDefault-listLTR" data-block="true" data-editor="154rn" data-offset-key="8eoda-0-0">
    <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="8eoda-0-0">
      <span data-offset-key="cd6at-0-0">Having knowledge/experience in established frameworks means your company can get more contracts. You can take on projects that use those frameworks. </span><span class="hardreadability"><span data-offset-key="cd6at-1-0">You don't have to spend proposal space trying to convince clients that your in-house framework is great</span></span><span data-offset-key="cd6at-2-0">. With open source frameworks you can reuse marketing copy by someone else!</span>
    </div>
  </li>
  
  <li class="public-DraftStyleDefault-unorderedListItem public-DraftStyleDefault-reset public-DraftStyleDefault-depth0 public-DraftStyleDefault-listLTR" data-block="true" data-editor="154rn" data-offset-key="8eoda-0-0">
    <div class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr" data-offset-key="8eoda-0-0">
      <span data-offset-key="e2sor-0-0">Working on well-known, established frameworks is better for your developers career-wise. It gives them more knowledge that could be transferable to other jobs. While this isn't a benefit to the company per se, it will make the company more attractive to developers. It even allows the flexibility of hiring developers experience with that framework.</span>
    </div>
  </li>
</ul>

<div class="" data-block="true" data-editor="154rn" data-offset-key="cgdmp-0-0">
</div>

<div class="" data-block="true" data-editor="154rn" data-offset-key="4iqnk-0-0">
</div>

<div class="" data-block="true" data-editor="154rn" data-offset-key="86ifo-0-0">
</div>

There are some disadvantages too of course:

  * As mentioned above, there is time and effort involved in learning a new open source framework. This effort is mostly for the experienced developers -- for new hires they will need to learn something regardless
  * Having an in-house team developing your own framework means you have a core set of developers experienced in the full stack. Reliance on open source frameworks means most of your developers won't be familiar with the low level details.

In the end, there's no guarantee that using an open source framework will be painless or be better than developing one in-house. So I can understand the decision to stick with what you know. But for me as a developer, I feel that it's more rewarding to be exposed to different frameworks.

In fact I wrote this post because recently someone asked me what my "go-to web framework" was and I said I didn't have one. I'd rather be flexible enough to learn and work with any existing framework. In our industry where change happens quickly and can catch you by surprise, I think that flexibility is a much more valuable asset to have.