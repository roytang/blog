---
title: "The AI Ouroboros"
date: 2023-09-28T15:53:11+08:00
tags:
- tech
- ai
---

Link dump of AI <del>nonsense</del> stuff incoming!

#### Intellectual sharecropping

[NYT (archive link): The Internet Is About to Get Much Worse](https://archive.li/vjiJL):

> We have commons on the internet, too. Despite all of its toxic corners, it is still full of vibrant portions that serve the public good — places like Wikipedia and Reddit forums, where volunteers often share knowledge in good faith and work hard to keep bad actors at bay.
> 
> But these commons are now being overgrazed by rapacious tech companies that seek to feed all of the human wisdom, expertise, humor, anecdotes and advice they find in these places into their for-profit A.I. systems.

[Tracy Durnell: Generative AI is intellectual sharecropping](https://tracydurnell.com/2023/09/25/generative-ai-is-intellectual-sharecropping/):

> Generative AI companies steal our intellectual property then license it back to us. We can’t be compensated reasonably for our individual contributions to the model because they’ve stolen from so many of us and each individual’s work represents a miniscule portion of the entire model. Whatever we generate with their models can’t be copyrighted and used to make money for *us* without significant human contributions — but generated works are in direct competition with the creators whose works built the model. These powerful, well-funded companies want businesses to fire their employees and pay them instead, making businesses reliant on an opaque, unpredictable service that demands vast amounts of natural resources that may be in short — and shortening — supply.
>

One of the things one can try to resist our new AI overlords farming our hard-written (?) blog content would be to [try to ban them using robots.txt](/2023/08/2023-week-32/#site-updates) but [Manuel Moreale's investigation tells us that's futile](https://manuelmoreale.com/bots-spiders-and-crawlers-the-results):

> So, what's the takeaway here? I guess that the vast majority of crawlers don't give a shit about your robots.txt.

Probably the next step to try (if you really wanted to), would be to set up your server/software to filter out those scraping bots based on their User-Agents, or maybe even return garbage data to pollute their models. But that seems like it would lead to an escalation where they will just lie and use different User-Agent strings. Like Manuel, I am tempted to just give up, mostly because I believe that the open web should be welcoming to scrapers anyway (I have written my own share of web scrapers, mostly for archival purposes). The sharecropping is bad, but the alternative seems to be closed systems? IDK, it feels like we have to choose between evils here. (I am keeping my `robots.txt` though.)

#### A snake eating its own tail

I will admit I have been using AI for some stuff. Not for content generation (outside of [one small experiment](/2022/12/chatgpt/)), but rather for asking programming questions, via the ChatGPT-powered Bing Chat in Microsoft Edge. I literally will sometimes have an Edge window open just to ask mundane Python/Django/JavaScript questions about things I don't bother memorizing even though I have done them many times over the years, such as "how do I filter Django queries based on child table counts?" It used to be that I would just use web search (DDG, not Google) and click on StackOverflow links to get these answers, but this seems a bit more convenient, if not pretty bad for StackOverflow and similar sites. 

Anyway, I'm not sure how long this sort of usage will remain useful, given AI-hallucinated misinformation is now affecting search results. 

See: [Ars Technica: Can you melt eggs? Quora’s AI says “yes,” and Google is sharing the result](https://arstechnica.com/information-technology/2023/09/can-you-melt-eggs-quoras-ai-says-yes-and-google-is-sharing-the-result/).

Caitlin Dewey tells us about how [Google glitches hit different in an AI-filtered world](https://linksiwouldgchatyou.substack.com/p/already-seen-it-thank-you):

> A funny thing happens when you search the phrase “Roe v. Wade overturned” on Google: The search engine assumes “Roe v. Wade Overturned” is … a deeply unpopular TV show.
>
> A Google Knowledge Box invites you to watch the trailer. A prominent yellow button supplies dozens of “reviews.” You can even bookmark “Roe v. Wade Overturned” to watch later. (Already seen it, thank you!)
>

...

> But Knowledge Graph glitches also hit different at a moment when Google and its competitors are seeking to filter more information through AI. Since May, Google has experimented with a generative AI feature, called Search Generative Experience, that summarizes the results of users’ queries and answers questions in real time. That may multiply these types of errors; it will almost certainly change our relationship with the wider internet.
> 

It's not like Google Search has always been 100% accurate anyway. It's a garbage-in / garbage-out sort of deal, with a lot of internet queries poisoned by two decades of SEO practices and an ad-driven economy that encourages low quality content farms and spammers pestering bloggers like me with proposals for guest posts or asking me to link to their articles.

It leaves me wondering: what happens to these content forms and advertising revenue when AI misinformation becomes so prevalent that people start to avoid using search engines? Or when LLM content generation starts enabling large volumes of content farms at scale? The more AI-generated content/nonsense that exists out there on the internet, the harder it becomes to earn eyeballs for advertisers. And with search engines (read: Google) not even sending users to your website anymore, can the advertising-driven web economy survive? And what happens when future generations of LLM start hoovering up all of this low-quality LLM-generated content as their own training data? 

[Maggie Appleton writes about The Expanding Dark Forest and Generative AI](https://maggieappleton.com/ai-dark-forest):

> You thought the first page of Google was bunk before? You haven't seen Google where SEO optimizer bros pump out billions of perfectly coherent but predictably dull informational articles for every longtail keyword combination under the sun.
>

...

> We're about to drown in a sea of pedestrian takes. An explosion of noise that will drown out any signal. Goodbye to finding original human insights or authentic connections under that pile of cruft.
> 
> Many people will say we already live in this reality. We've already become skilled at sifting through unhelpful piles of “optimised content” designed to gather clicks and advertising impressions.
>

...

> After the forest expands, we will become deeply sceptical of one another's realness. Every time you find a new favourite blog or Twitter account or Tiktok personality online, you'll have to ask: Is this really a whole human with a rich and complex life like mine? Is there a being on the other end of this web interface I can form a relationship with?
> 

In this (as-yet theoretical?) internet drowning under endless automatically-generated content, being genuinely human and being able to convey genuine human thoughts and form human connections becomes rarer, scarcer, and perhaps more valuable. 

#### Recent related links from the linkblog

- [I'm a Spotless Giraffe. | Ben Myers](https://benmyers.dev/blog/spotless-giraffe/): 

    > "It is something of an amusing curiosity that some AI models were perplexed by a giraffe without spots. But it's these same tools and paradigms that enshrine normativity of all kinds, "sanding away the unusual." As tech continues to charge headfirst into AI hype, this is going to have far-reaching, yet largely invisible to the mainstream, consequences to anyone on the wrong side of that normativity. Better hope you have spots."

- [AI is killing the old web, and the new web struggles to be born - The Verge](https://www.theverge.com/2023/6/26/23773914/ai-large-language-models-data-scraping-generation-remaking-web)

(The linkblog is [here](/links/).)