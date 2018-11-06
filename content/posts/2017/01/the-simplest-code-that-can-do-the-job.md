---
title: The Simplest Code That Can Do The Job
author: roy
type: post
date: 2017-01-11T01:30:06+00:00
url: /2017/01/the-simplest-code-that-can-do-the-job/
wp-syntax-cache-content:
  - |
    a:1:{i:1;s:2299:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">def</span> load_db<span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>:
    	all_series <span style="color: #66cc66;">=</span> <span style="color: black;">&#123;</span><span style="color: black;">&#125;</span>
    	<span style="color: #ff7700;font-weight:bold;">with</span> <span style="color: #008000;">open</span><span style="color: black;">&#40;</span>DATABASE_FILE<span style="color: #66cc66;">,</span> <span style="color: #483d8b;">'rb'</span><span style="color: black;">&#41;</span> <span style="color: #ff7700;font-weight:bold;">as</span> handle:
    		all_series <span style="color: #66cc66;">=</span> <span style="color: #dc143c;">pickle</span>.<span style="color: black;">load</span><span style="color: black;">&#40;</span>handle<span style="color: black;">&#41;</span>
    	<span style="color: #ff7700;font-weight:bold;">return</span> all_series
    &nbsp;
    <span style="color: #ff7700;font-weight:bold;">def</span> save_db<span style="color: black;">&#40;</span>all_series<span style="color: black;">&#41;</span>:
    	<span style="color: #ff7700;font-weight:bold;">with</span> <span style="color: #008000;">open</span><span style="color: black;">&#40;</span>DATABASE_FILE<span style="color: #66cc66;">,</span> <span style="color: #483d8b;">'wb'</span><span style="color: black;">&#41;</span> <span style="color: #ff7700;font-weight:bold;">as</span> handle:
    		<span style="color: #dc143c;">pickle</span>.<span style="color: black;">dump</span><span style="color: black;">&#40;</span>all_series<span style="color: #66cc66;">,</span> handle<span style="color: #66cc66;">,</span> protocol<span style="color: #66cc66;">=</span><span style="color: #dc143c;">pickle</span>.<span style="color: black;">HIGHEST_PROTOCOL</span><span style="color: black;">&#41;</span></pre></td></tr></table><p class="theCode" style="display:none;">def load_db():
    	all_series = {}
    	with open(DATABASE_FILE, 'rb') as handle:
    		all_series = pickle.load(handle)
    	return all_series
    
    def save_db(all_series):
    	with open(DATABASE_FILE, 'wb') as handle:
    		pickle.dump(all_series, handle, protocol=pickle.HIGHEST_PROTOCOL)</p></div>
    ";}
categories:
  - Software Development
tags:
  - python

---
So the other day I was reworking a Python script that I had been using for years on my home PC to manage and categorize some downloaded files for me. This time I wanted to add some smarter behavior to make it more able to figure out when to group files into folders without constantly needing manual intervention from me. To do this, I needed to persist some data between runs &#8211; so that the script remembers how it categorized previous files and is able to group similar files together.

Now since my software development career has largely been as an enterprise-y kind of developer, my first thought was to just use a database to store the data. I already had a MySql installation on my machine so that was fine, I just needed Python to interface with it. After looking up how to do it, I balked at having to install a new Python library just to connect to MySql and reconsidered.

As programmers, we have a tendency sometimes to over-engineer solutions because that&#8217;s what we&#8217;re used to doing. Did I really need a database for this? The data won&#8217;t be very big, and I won&#8217;t need to do any sort of maintenance on it, so maybe a simpler solution was in order.

I ended up just using pickle, which was already built-in to Python:

<pre lang="python">def load_db():
	all_series = {}
	with open(DATABASE_FILE, 'rb') as handle:
		all_series = pickle.load(handle)
	return all_series

def save_db(all_series):
	with open(DATABASE_FILE, 'wb') as handle:
		pickle.dump(all_series, handle, protocol=pickle.HIGHEST_PROTOCOL)
</pre>

(Above code _probably_ gives you an idea what kind of files I&#8217;m sorting&#8230;)

As an added benefit, I didn&#8217;t need to design any database schemas or tables or whatnot, pickle just lets me serialize the map as-is and reload it later from disk without any hassle.

I guess my lesson here was: don&#8217;t over-complicate things when something simple will work fine. Write the simplest code that can do the job.