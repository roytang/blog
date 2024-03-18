---
title: "User Agents"
date: 2024-03-18T21:42:27+08:00
tags:
- web
- bash
- meta
---

I sometimes get resource usage spikes on my site's server and it is almost always some kind of SEO or LLM-related crawler sending copious amounts of requests. The debugging process and remedy is often the same: check the access logs to determine the offending user agents and either block them via [robots.txt](/robots.txt) or the stronger penalty of blocking them via Cloudflare.

### Extracting the User Agents

But that first step of determining the offending user agents can take some work. The first few times I paged through the access logs manually to see visually which user agents were sending too many requests. After too many instances of remembering the commands to parse the log files every time, I decided to write a bash script to periodically generate the user agents list for the past 24 hours and save it as a text file that I can just access via the browser. 

After some searching and experimentation the actual script to generate the file turned out to be something like:

`awk -F\" '{print $6}' [access log file] | sort | uniq -c | sort -nr > [tempuseragentsfile.txt]`

Breaking it down:

- `awk` extracts the 6th term from each line of the access log
- then it's sorted and `uniq -c` gets the count for each unique user agent string
- `sort -nr` sorts by a numeric column (the count from the last command) in reverse order, so that the most frequent user agents are listed first
- the final output is piped to a text file that I then move to a location I can access via web

The script runs once a day on the previous day's access log file. THe generated text file looks something like this:

<pre>
   6725 Mozilla/5.0 (compatible; DataForSeoBot/1.0; +https://dataforseo.com/dataforseo-bot)
   1346 Mozilla/5.0 (compatible; AwarioBot/1.0; +https://awario.com/bots.html)
   1176 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
    823 Mozilla/5.0 (Macintosh; Intel Mac OS X 12_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15
    721 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36
    460 Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0
    451 python-httpx/0.26.0
    335 Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
</pre>

When they are arranged in this way it becomes obvious which are the offending bots! This sample was already from the day when I had updated my robots.txt to block the DataForSeoBot, it was much worse the day before!

### Some other interesting data

#### RSS User Agents

Aside from the convenience of making it easy to spot offending user agents, having this report gave me some fun facts.

First is the sheer number of RSS readers still in use these days, even if only the ones that subscribe to my blog! A cursory pass through the most recent user agents list shows the following feed readers:

- [CommaFeed](https://github.com/Athou/commafeed)
- [Unread RSS Reader](https://www.goldenhillsoftware.com/unread/)
- [Feedbin](https://feedbin.com/)
- [NetNewsReader](https://netnewswire.com/)
- [NewsBlur](https://www.newsblur.com/)
- [FreshRSS](https://freshrss.org)
- [Tiny Tiny RSS](https://tt-rss.org/)
- [Feedly](http://www.feedly.com/)
- [Reeder](https://www.reederapp.com/)
- [Inoreader](http://www.inoreader.com/) (my feed reader of choice!)
- SpaceCowboys Android RSS Reader
- [Liferea](https://lzone.de/liferea/)
- [Newsboat](https://newsboat.org/)
- [RSS Parrot](https://rss-parrot.net)
- [MiniFlux](https://miniflux.app)
- Roy and Rianne's Righteously Royalty-free RSS Reader v 0.1 (I approve of this name, but I couldn't find a website)

Those are just the ones that had at least 10 hits in the file I checked, there were a bunch more later on but my list is already far too long. It's refreshing to see so many active RSS readers still in use!

Many of the more popular readers such as Feedly, Inoreader, Feedbin, Newsblur, etc all include the subscriber counts in their user agents, so you can also parse your access logs to get some idea of how many subscribers you have, if that tickles your fancy. Reference: [article by JeffTK](https://www.jefftk.com/p/looking-at-rss-user-agents)

#### Mastodon versions

Another interesting data point I've seen is the sheer number of Mastodon servers and versions accessing my site. Whenever I share a link to the site on Mastodon, a bunch of Mastodon servers will ping my server (this is also known as the [Mastodon Stampede](https://www.jwz.org/blog/2022/11/mastodon-stampede/)). I can use the access log data to see how far my posts manage to reach on the Fediverse.

Here is a count of the number of different servers and their Mastodon versions:

- Mastodon/4.3.0 versions: 53 servers
- Mastodon/4.2.8: 312 servers
- Mastodon/4.2.7: 109 servers
- Mastodon/4.2.6 to 4.2.0: 19 servers
- Mastodon/4.1.x: 37 servers
- Mastodon/4.0.x: 12 servers
- Mastodon/3.x: 3 servers

That is way more servers than I would have expected! It's nice to see.

#### Anon user agents

There's a whole bunch of requests from scrapers that don't even bother with proper user agents and are just something like `python-httpx` or `Go-http-client` or some version of PHP. It would be nice to have more info but it's hard to complain since I've written my own share of toy scrapers that don't identify themselves. I should do better!

#### Worst User Agent

The file I'm checking had one hit from a user agent "Expanse, a Palo Alto Networks company, searches across the global IPv4 space multiple times per day to identify customers&#39; presences on the Internet. If you would like to be excluded from our scans, please send IP addresses/domains to: scaninfo@paloaltonetworks.com". I thought about blocking it, but eh, one hit a day it's fine.

### In Conclusion

Maybe I enjoy parsing data too much.