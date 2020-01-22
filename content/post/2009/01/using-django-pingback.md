---
date: 2009-01-04 07:22:20
tags:
- royondjango
- python
- software development
title: Using Django Pingback
type: post
url: /2009/01/using-django-pingback/
---

I actually had some trouble using [django-pingback][1] on my custom blog engine; the [django-pingback documentation][2] is mostly fine, but there were some caveats that I had to discover myself through a bit of debugging:

  * The URL specified for the XML-RPC endpoint in the HTML head needs to be a full absolute url including domain, i.e. http://roytang.net/xmlrpc/, which gave me trouble when I was trying to test using localhost pinging to an online server. I eventually just decided to set it up, deploy on webfaction and test it online before I redirected the domain name.
  * The documentation mentioned that the pingback handler needs to have the same arguments as the detail view for the post, so I wrote it as follows: <div class="hl_wrap">
      <table class="sourcetable">
        <tr>
          <td class="linenos">
            <pre>1
2
3
4</pre>
          </td>
          
          <td class="code">
            <div class="source">
              <pre><span class="c"># exactly same arguments as 'details' view.</span>
<span class="k">def</span> <span class="nf">pingback_blog_handler</span><span class="p">(</span><span class="n">catslug</span><span class="p">,</span> <span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">slug</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
    <span class="n">cat</span> <span class="o">=</span> <span class="n">Category</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">slug</span><span class="o">=</span><span class="n">catslug</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">Post</span><span class="o">.</span><span class="n">pub_objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">date__year</span><span class="o">=</span><span class="n">year</span><span class="p">,</span> <span class="n">date__month</span><span class="o">=</span><span class="n">month</span><span class="p">,</span> <span class="n">slug</span><span class="o">=</span><span class="n">slug</span><span class="p">,</span> <span class="n">category</span><span class="o">=</span><span class="n">cat</span><span class="p">,</span> <span class="n">published</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</pre>
            </div>
          </td>
        </tr>
      </table>
    </div>
    
    But it wasn't exactly working for me, for some reason the function wasn't being called. After some debugging I found that I needed to use named parameters for catslug, year, month, slug in the URLConf for the post permalink in order for this to work. I'm not sure if this was because I was doing it wrong or it's some sort of undocumented requirement.</li> 
    
      * The pingback client was throwing a KeyError whenever a post I made would have anchor tags without an href attribute. Granted that there isn't much point in having an <a>anchor tag without the href</a>, but the code shouldn't just choke on it. I modified the following line in client.py: <div class="hl_wrap">
          <table class="sourcetable">
            <tr>
              <td class="linenos">
                <pre>1</pre>
              </td>
              
              <td class="code">
                <div class="source">
                  <pre><span class="n">links</span> <span class="o">=</span> <span class="p">[</span><span class="n">a</span><span class="p">[</span><span class="s">'href'</span><span class="p">]</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">soup</span><span class="o">.</span><span class="n">findAll</span><span class="p">(</span><span class="s">'a'</span><span class="p">)</span> <span class="k">if</span> <span class="n">is_external</span><span class="p">(</span><span class="n">a</span><span class="p">[</span><span class="s">'href'</span><span class="p">],</span> <span class="n">url</span><span class="p">)]</span>
</pre>
                </div>
              </td>
            </tr>
          </table>
        </div>
        
        Adding the check for the href attribute:
        
        <div class="hl_wrap">
          <table class="sourcetable">
            <tr>
              <td class="linenos">
                <pre>1</pre>
              </td>
              
              <td class="code">
                <div class="source">
                  <pre><span class="n">links</span> <span class="o">=</span> <span class="p">[</span><span class="n">a</span><span class="p">[</span><span class="s">'href'</span><span class="p">]</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="n">soup</span><span class="o">.</span><span class="n">findAll</span><span class="p">(</span><span class="s">'a'</span><span class="p">)</span> <span class="k">if</span> <span class="n">a</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="s">'href'</span><span class="p">)</span> <span class="ow">and</span> <span class="n">is_external</span><span class="p">(</span><span class="n">a</span><span class="p">[</span><span class="s">'href'</span><span class="p">],</span> <span class="n">url</span><span class="p">)]</span>
</pre>
                </div>
              </td>
            </tr>
          </table>
        </div></ul> 
    
    Those are all the changes I made to get pingbacks working. I hope they're still working now, as I haven't received any pingbacks since the django version of this blog went live >.

 [1]: http://code.google.com/p/django-pingback/
 [2]: http://hg.piranha.org.ua/django-pingback/file/6ca8eadcd22d/README.md#l1