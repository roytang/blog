---
categories:
- Software Development
date: 2008-05-04 08:21:00
title: Creating A WordPress Template Part 2
type: post
url: /2008/05/creating-a-wordpress-template-part-2/
---

Part 1 of this series is
   
[
    
here
   
][1] 
   
.

Creating a WordPress template is harder than I thought. Luckily I'm modifying the default template instead of starting from scratch. The one I'm creating is rather simple but after spending almost 8 hours on it so far, I'm still far away from completing it. I'm guessing the more complicated layouts take more than two weeks of full-time work.

Here's my current WIP:

[
  
<img class="aligncenter size-thumbnail wp-image-489" title="screenshot" src="/files/uploads/2008/05/screenshot-150x150.png" alt="" width="150" height="150" />
  
][2] 

Changes since the last part:

<!--more-->



  


  1. I moved the blog title and blog name into the header image. For this I had to darken the image a bit using the Gimp so that the white text isn't difficult to read against the header image. 
  2. Changed the layout to use CSS and divs instead of the previous table-based layout. I solved the &#8220;columns with equal heights&#8221; problem using a hack I found from several websites.</p> 
      * Basically: for each column you add a large amount of padding to the bottom of each column, then apply a negative margin so that the padding isn't actually visible on-screen. This will create a scrollbar in the containing div though, so you need to hide the overflow. Sample CSS for this is:</p> <div class='hl_wrap'>
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
8</pre>
              </td>
              
              <td class="code">
                <div class="source">
                  <pre>     .content {
overflow: hidden; /* Part of equal heights column hack */
}
.column {
margin-bottom: -20000px; /* Part of equal heights column hack */
padding-bottom: 20000px; /* Part of equal heights column hack */
}
    
</pre>
                </div>
              </td>
            </tr>
          </table>
        </div>

  3. Centering the main div was something I didn't know how to do either. The solution was to set left and right margin to auto in the divs. But this is ignored by IE6 so in addition to that, you need to set text-align: center in the body. 
  4. Set the background color of the page to be the same as rightmost column. 
  5. Modified index.php by removing the while loop to iterate over the posts. This is so that only the latest post appears in the leftmost column. 
  6. Added the &#8220;recent posts&#8221; listing in the center column. Relevant code inserted into sidebar.php:</p> <div class='hl_wrap'>
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
15
16
17
18</pre>
          </td>
          
          <td class="code">
            <div class="source">
              <pre>   &lt;table class="recent-posts" &gt;
&lt;?php
global $post;
$recentposts = get_posts(&#39;numberposts=5&amp;offset=2&#39;);
foreach($recentposts as $post) {
?&gt;
&lt;tr&gt;
&lt;td rowspan="2" class="date-cell"&gt;&lt;?php the_time(&#39;d M Y&#39;, &#39;&#39;, &#39;&#39;) ?&gt;&lt;/td&gt;
&lt;td&gt;&lt;a class="recent-title" href="&lt;?php the_permalink() ?&gt;"&gt; &lt;?php the_title() ?&gt; &lt;/a&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
&lt;td class="recent-cats"&gt;Filed under &lt;?php the_category(&#39;, &#39;); ?&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;?php
}
?&gt;
&lt;/table&gt;
  
</pre>
            </div>
          </td>
        </tr>
      </table>
    </div>

  7. I don't want the about info hardcoded into the right column, so I modify it instead to display the contents of any page titled &#8220;about&#8221;. The code shown below is cribbed from Hemingway Reloaded WordPress theme:</p> <div class='hl_wrap'>
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
              <pre>   &lt;?php query_posts(&#39;pagename=about&#39;); ?&gt;
&lt;?php if (have_posts()) : ?&gt;
&lt;?php while (have_posts()) : the_post(); ?&gt;
&lt;?php the_content(); ?&gt;
&lt;?php endwhile; ?&gt;
&lt;?php endif; ?&gt;
  
</pre>
            </div>
          </td>
        </tr>
      </table>
    </div>

  8. Changed the standard font used to Arial 12px 


   
The above changes took me around half the day today (well, there were naps and videogames in between, et cetera) and the theme is starting to look decent, but there's still a lot to do: navigation links, search pages, category lists, archive page, single post page, page template are the ones I can name off the top of my head right now.

Still, WordPress has turned out remarkably easy to customize, the PHP functions exposed as template tags are usually enough for whatever you plan to do, and the documentation on
   
[
    
codex.wordpress.com
   
][3] 
   
is pretty thorough as well.

The hard part turned out to be figuring out CSS-related problems. Luckily, CSS and browser-specific issues are well-discussed problems online so I could easily find the solution to the problems via the internet.

I'll continue working on this whenever I have time, and hopefully can have the theme live on the Roy on Magic blog soon.

 [1]: http://roytang.net/blog/2008/04/creating-a-wordpress-template-part-1/
 [2]: /files/uploads/2008/05/screenshot.png
 [3]: http://codex.wordpress.com