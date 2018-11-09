---
categories:
- Software Development
date: 2009-02-14 14:17:32
tags:
- royondjango
title: Stylesheet Switcher using Django
type: post
url: /2009/02/stylesheet-switcher-using-django/
---

You may have noticed the new color scheme and new &#8220;Theme Switcher&#8221; widget in the sidebar. I had done some CSS work during the past month in the office and it made me want to tweak the stylesheets on this site a bit. I figured I might as well make it easy to switch stylesheets, so I wrote a small Theme Switcher django app. (Well, it&#8217;s more of a stylesheet switcher I guess)

The model is simple:

<div class="hl_wrap">
  <table class="sourcetable">
    <tr>
      <td class="linenos">
        <pre>1
2
3
4
5
6
7</pre>
      </td>
      
      <td class="code">
        <div class="source">
          <pre><span class="k">class</span> <span class="nc">Theme</span><span class="p">(</span><span class="n">models</span><span class="o">.</span><span class="n">Model</span><span class="p">):</span>
    <span class="n">slug</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">SlugField</span><span class="p">()</span>
    <span class="n">title</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">CharField</span><span class="p">(</span><span class="n">max_length</span><span class="o">=</span><span class="mf">250</span><span class="p">)</span>
    <span class="n">css_path</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">CharField</span><span class="p">(</span><span class="n">max_length</span><span class="o">=</span><span class="mf">500</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">title</span>
</pre>
        </div>
      </td>
    </tr>
  </table>
</div>

I only needed one view &#8211; to switch the current theme.

Added the ff to urls.py:

<div class="hl_wrap">
  <table class="sourcetable">
    <tr>
      <td class="linenos">
        <pre>1</pre>
      </td>
      
      <td class="code">
        <div class="source">
          <pre><span class="p">(</span><span class="s">r'^theme/([a-zA-Z0-9\-]+)/'</span><span class="p">,</span> <span class="s">'themer.views.switch'</span><span class="p">),</span>
</pre>
        </div>
      </td>
    </tr>
  </table>
</div>

The view code simply stores the selected theme as a cookie:

<div class="hl_wrap">
  <table class="sourcetable">
    <tr>
      <td class="linenos">
        <pre>1
2
3
4
5
6
7
8
9</pre>
      </td>
      
      <td class="code">
        <div class="source">
          <pre><span class="k">def</span> <span class="nf">switch</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">theme_slug</span><span class="p">):</span>
  <span class="sd">""" Sets a cookie to specify the new theme, then redirects to the referer or root url """</span>
  <span class="n">theme</span> <span class="o">=</span> <span class="n">get_object_or_404</span><span class="p">(</span><span class="n">Theme</span><span class="p">,</span> <span class="n">slug</span><span class="o">=</span><span class="n">theme_slug</span><span class="p">)</span>
  <span class="n">referer</span> <span class="o">=</span> <span class="s">"/"</span>
  <span class="k">if</span> <span class="s">"HTTP_REFERER"</span> <span class="ow">in</span> <span class="n">request</span><span class="o">.</span><span class="n">META</span><span class="p">:</span>
    <span class="n">referer</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">META</span><span class="p">[</span><span class="s">"HTTP_REFERER"</span><span class="p">]</span>
  <span class="n">resp</span> <span class="o">=</span> <span class="n">HttpResponseRedirect</span><span class="p">(</span><span class="n">referer</span><span class="p">)</span>
  <span class="n">resp</span><span class="o">.</span><span class="n">set_cookie</span><span class="p">(</span><span class="s">"theme"</span><span class="p">,</span> <span class="n">theme_slug</span><span class="p">,</span> <span class="mf">100000</span><span class="p">)</span>
  <span class="k">return</span> <span class="n">resp</span>
</pre>
        </div>
      </td>
    </tr>
  </table>
</div>

To load the stylesheet, I set up a [context processor][1] to pass both the current theme and the list of themes to the context. I wanted to do this using template tags, but I couldn&#8217;t figure out how to extract a cookie from within a template tag.

<div class="hl_wrap">
  <table class="sourcetable">
    <tr>
      <td class="linenos">
        <pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15</pre>
      </td>
      
      <td class="code">
        <div class="source">
          <pre><span class="kn">from</span> <span class="nn">themer.models</span> <span class="kn">import</span> <span class="n">Theme</span>
<span class="k">def</span> <span class="nf">context_processor</span><span class="p">(</span><span class="n">request</span><span class="p">):</span>
    <span class="n">theme_list</span> <span class="o">=</span> <span class="n">Theme</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">all</span><span class="p">()</span>
    <span class="k">if</span> <span class="s">"theme"</span> <span class="ow">in</span> <span class="n">request</span><span class="o">.</span><span class="n">COOKIES</span><span class="p">:</span>
        <span class="n">slug</span> <span class="o">=</span> <span class="n">request</span><span class="o">.</span><span class="n">COOKIES</span><span class="p">[</span><span class="s">"theme"</span><span class="p">]</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">theme</span> <span class="o">=</span> <span class="n">Theme</span><span class="o">.</span><span class="n">objects</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">slug</span><span class="o">=</span><span class="n">slug</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">Theme</span><span class="o">.</span><span class="n">DoesNotExist</span><span class="p">:</span>
            <span class="n">theme</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">theme_list</span><span class="o">.</span><span class="n">count</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mf"></span><span class="p">:</span>
            <span class="n">theme</span> <span class="o">=</span> <span class="n">theme_list</span><span class="p">[</span><span class="mf"></span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">theme</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="k">return</span> <span class="p">{</span><span class="s">"current_theme"</span> <span class="p">:</span> <span class="n">theme</span><span class="p">,</span> <span class="s">"theme_list"</span> <span class="p">:</span> <span class="n">theme_list</span><span class="p">}</span>
</pre>
        </div>
      </td>
    </tr>
  </table>
</div>

Then in my base template file, I add the following to the head section:

<div class="hl_wrap">
  <table class="sourcetable">
    <tr>
      <td class="linenos">
        <pre>1</pre>
      </td>
      
      <td class="code">
        <div class="source">
          <pre><span class="nt">&lt;link</span> <span class="na">rel=</span><span class="s">"stylesheet"</span> <span class="na">href=</span><span class="s">"{{ current_theme.css_path }}"</span> <span class="na">type=</span><span class="s">"text/css"</span> <span class="nt">/&gt;</span>
</pre>
        </div>
      </td>
    </tr>
  </table>
</div>

And add the list of themes into the sidebar.

<div class="hl_wrap">
  <table class="sourcetable">
    <tr>
      <td class="linenos">
        <pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12</pre>
      </td>
      
      <td class="code">
        <div class="source">
          <pre><span class="nt">&lt;h2&gt;</span>Theme Switcher<span class="nt">&lt;/h2&gt;</span>
<span class="nt">&lt;ul&gt;</span>
            {% for theme in theme_list %}
            <span class="nt">&lt;li&gt;</span>
            {% ifequal theme.slug current_theme.slug %}
            {{ theme.title }} <span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"note"</span><span class="nt">&gt;</span>(current)<span class="nt">&lt;/span&gt;</span>
            {% else %}
            <span class="nt">&lt;a</span> <span class="na">href=</span><span class="s">"{% url themer.views.switch theme.slug %}"</span> <span class="na">title=</span><span class="s">"Switch to {{ theme.title }} theme"</span><span class="nt">&gt;</span>{{ theme.title }}<span class="nt">&lt;/a&gt;</span>
            {% endifequal %}
            <span class="nt">&lt;/li&gt;</span>
            {% endfor %}
            <span class="nt">&lt;/ul&gt;</span>
</pre>
        </div>
      </td>
    </tr>
  </table>
</div>

And we&#8217;re done!

Of course, I&#8217;m still not particularly strong in web design, so the two current &#8220;themes&#8221; really just switch around the color scheme. The light blue theme is named Azorius, while the old black and green theme is named Golgari, both named after the respective color guilds in Magic: The Gathering&#8217;s Ravnica block.

Hopefully this gives me a chance to whip up more interesting themes and polish the old CSS skills some more. Enjoy!

 [1]: http://www.b-list.org/weblog/2006/jun/14/django-tips-template-context-processors/ "Django tips: Template context processors by James Bennet"

## Comments

### Comment by Radek on 2011-12-16 19:38:11 +0000
Hi,

Nice do you have working example or download that I can try and look how it works?

### Comment by [roy](http://roytang.net) on 2011-12-18 08:03:56 +0000
Hi Radek, unfortunately I&#8217;m unable to find the original source code for this; I had previously been running a Django-backed blog but have since migrated it and the posts over to WordPress