---
title: "Google's LLM Hallucinations"
date: 2024-05-29T13:30:21+08:00
tags:
- tech
- llms
- ai
---

Previously: [Is Google Killing The Web?](/2024/05/google-vs-web/)

Since Google introduced their "AI overviews" feature, people have been showing how it can spit out misleading answers such as recommending putting glue on pizzas or that Obama was a Muslim or that geologists recommend eating rocks. In [a recently-uploaded interview](https://www.youtube.com/watch?v=lqikP9X9-ws&t=1999s), Sundar Pichai says such "hallucinations" are an unsolved problem, and that LLMs aren't the best approach for "factuality".

This [Forbes article has more detail on the issue](https://www.forbes.com/sites/siladityaray/2024/05/24/googles-ai-overview-appears-to-produce-misleading-answers/), but what stood out to me was the part under "What we don't know" when they say "It is unclear what exactly is causing the issue..."

My friends at Forbes, we know what exactly is causing the issue: LLMs are basically parrots [^1] that have no concept of factuality or reliability or context. It has no idea whether the source of the information is a satire site like the onion or a joke comment on a reddit post or whatever. In fact, LLMs have no concept of sources or documents or such things; the language models break down their training data sets into things like terms and words and tokens and probabilities and uses those to chain together sentences, but any concept of their source documents is lost along the way. This is why attribution can be challenging for an LLM.

The problem here is that Google has proposed that their "AI overviews" will "let us do the Googling for you"; that it is a replacement for checking various websites and sources to confirm information and understand the contexts check whether they are reliable and such, presenting a summary in a helpful package (all while deriving other websites of their traffic). This might involve things like reading through an entire reddit thread to get the context, maybe looking into the article's byline or the website's about page to figure out more about their motivations, etc.

So that got me thinking: can this problem actually be solved? In order for an LLMs to not hallucinate, their models need to include things like:

- whether the source document is reliable
- whether the source website is reliable
- the context in which the text was used (is it a joke? is it satire? is it sarcasm? is the author trying to sell you something? is the publication politically biased? is the author an expert on the subject?)
- are any claims grounded in science or are they just anecdotes? is there scientific consensus on the topics?
- are the views expressed in the document niche or wildly held?
- etc etc

All of which to say is that the LLMs have to have context of whether the source documents are likely accurate or reliable, and this is basically editorializing! Taking it upon themselves to use an LLM to provide "answers" means taking away the agency of users to make their own judgment calls! 

And while in theory we do have document classification models, good luck with that! We can't even get 100% of humans to agree on many basic facts! [^2] Such models would necessarily skew one way or another, probably disregarding minority opinions along the way (furthering political divides and marginalzation, etc). 

Besides, having Google (or any other big tech company) become an arbiter of whether something is believable/reliable or not seems like a slippery slope that can lead us to much worse outcomes for society. [^3] 

[^1]: I kind of want to have a browser extension that replaces words like "AI", "LLM", or "Chat-GPT" with "a parrot", then I would see headlines like "We asked a parrot what would the price of bitcoin be at the end of the year, you'll never guess what it said!"
[^2]: Something which should have become readily apparent since the age of "alternative facts" began, and even more emphasized by the COVID pandemic
[^3]: Looking forward to the Butlerian Jihad
