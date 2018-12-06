---
author: roy
categories:
- Software Development
date: 2017-01-11 01:30:06
tags:
- python
title: The Simplest Code That Can Do The Job
type: post
url: /2017/01/the-simplest-code-that-can-do-the-job/
---

So the other day I was reworking a Python script that I had been using for years on my home PC to manage and categorize some downloaded files for me. This time I wanted to add some smarter behavior to make it more able to figure out when to group files into folders without constantly needing manual intervention from me. To do this, I needed to persist some data between runs -- so that the script remembers how it categorized previous files and is able to group similar files together.

Now since my software development career has largely been as an enterprise-y kind of developer, my first thought was to just use a database to store the data. I already had a MySql installation on my machine so that was fine, I just needed Python to interface with it. After looking up how to do it, I balked at having to install a new Python library just to connect to MySql and reconsidered.

As programmers, we have a tendency sometimes to over-engineer solutions because that's what we're used to doing. Did I really need a database for this? The data won't be very big, and I won't need to do any sort of maintenance on it, so maybe a simpler solution was in order.

I ended up just using pickle, which was already built-in to Python:

{{< highlight python >}}
def load_db():
	all_series = {}
	with open(DATABASE_FILE, 'rb') as handle:
		all_series = pickle.load(handle)
	return all_series

def save_db(all_series):
	with open(DATABASE_FILE, 'wb') as handle:
		pickle.dump(all_series, handle, protocol=pickle.HIGHEST_PROTOCOL)
{{< /highlight >}}

(Above code _probably_ gives you an idea what kind of files I'm sorting... )

As an added benefit, I didn't need to design any database schemas or tables or whatnot, pickle just lets me serialize the map as-is and reload it later from disk without any hassle.

I guess my lesson here was: don't over-complicate things when something simple will work fine. Write the simplest code that can do the job.