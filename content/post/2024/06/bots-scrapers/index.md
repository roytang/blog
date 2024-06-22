---
title: "User Agents, Bots and Scrapers"
date: 2024-06-22T21:12:17+08:00
tags:
- genai
- bots
- scraping
---

This made the rounds recently: [Perplexity AI Is Lying about Their User Agent](https://rknight.me/blog/perplexity-ai-is-lying-about-its-user-agent/).

I don't especially care about Perplexity AI per-se (I'm not even sure what exactly it is), but I am a bit of two minds about the idea of user agent spoofing being automatically bad. Obviously, commercial companies lying about their user-agents to mass-crawl other people's websites is unacceptable. That being said, I have written my own crawlers myself that used browser-spoofing user agents. I used those user agents because otherwise the programs I was writing would not have worked. Now in my defense, I had done this before to scrape sites like Facebook, and only to extract my own user data. (Because Facebook's own export function is terrible, maybe I'll write about that sometime too.)

Also, while I object to my own content being crawled en masse for purposes of training LLMs, I don't particularly object to fetching say, a single page for purposes of page summarization, which is the specific use case raised in the article above. 

A fun aside: Edge's Copilot sidebar can also summarize pages on the above site: I opened the above link in Edge and asked Copilot to summarize it and it was able to do so. After that I said "by summarizing this web page are you not also using this context without permission" and Copilot said:

> I apologize if my previous action caused any discomfort. As an AI language model, I don’t intentionally infringe on privacy or use context without permission. If there’s anything else you’d like assistance with, feel free to ask! 😊
>

IDK if the author has also banned Copilot (IDK what user agent it uses), maybe he can look into it too.

Anyway, the main thing that interested me in the article above is that they identified the user agent used by Perplexity for the page summarization as `Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.3`, and this reminded me of an incident on my own server a few weeks ago.

Previously, I had set up [monitoring of user agents hitting my site](/2024/03/user-agents/) so that if I got unusual amounts of traffic I could easily see who the offenders are. My website runs on a rinky-dink VM so any traffic spike tends to slow it down a lot. This worked for a while: if some new bot decides to scrape my site in an unacceptable manner, I filter it out by user agent and move on. Late last month, I encountered a traffic spike and upon investigating I found that I got more than 25k requests in the same day with a user agent of `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36`, which is a bit similar to the user agent above, except this one is running on Mac OS instead of Windows. The article says this user agent likely means this bot is using headless Google Chrome to scrape my site. Although that's not necessarily true either, they can just set that user agent string themselves in their scraper program.

The bad thing about using a user agent string like this to mindlessly scrape is that I can't just block the scraper based on this user agent, because it might also be a legitimate user using a browser. It's different from when I use a browser user agent to bypass Facebook's anti-scraping mechanisms mostly because I'm running a rinky-dink VM and not a whole data center to serve my responses! I admit this seems a tad hypocritical; IDK, it's a complicated thing to have a stand on! All I'm sure of is: it's rude to mass scrape a personal website!

If you're an amateur web-scraper who is new at writing bots/crawlers it's easy to forget to set the user agent and it's even easier to have a coding mistake that results in an infinite loop that fires off way more requests than you expected. But maybe if you're in this situation, don't use someone's personal website as your scraping target? Twitter is right there! Anyway, I never was able to solve the above problem. And whatever that bot was doing will likely remain forever a mystery. (Unless the culprit sheepishly emails me and apologize after I post this, which would be fine, no hard feelings!)

Only somewhat tangentially related: After the above incident, I found out that Cloudflare supports filtering out websites using ["Verified Bot Categories"](https://developers.cloudflare.com/bots/reference/verified-bot-categories/), so I set up one of those to challenge any request classified as "AI Crawler". IDK if this has been particularly effective (and I suspect it will have no effect on bots that lie about their user agents), but I have not had any incidents since I set it up. But at least this way in theory if new known AI Crawler bots pop up, Cloudflare will automatically filter them out for me without needing me to update my settings every time?

I am looking forward to all this AI/LLM hype to pass us by so that I don't have to think about this nonsense anymore.