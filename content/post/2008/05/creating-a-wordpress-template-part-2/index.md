---
categories: []
date: 2008-05-04 08:21:00
tags:
- wordpress
- Software Development
title: Creating A WordPress Template Part 2
type: post
url: /2008/05/creating-a-wordpress-template-part-2/
dontinlinephotos: true
---

Part 1 of this series is [here][1].

Creating a WordPress template is harder than I thought. Luckily I'm modifying the default template instead of starting from scratch. The one I'm creating is rather simple but after spending almost 8 hours on it so far, I'm still far away from completing it. I'm guessing the more complicated layouts take more than two weeks of full-time work.

Here's my current WIP:

{{< img src="screenshot.png" >}}

Changes since the last part:

<!--more-->

  1. I moved the blog title and blog name into the header image. For this I had to darken the image a bit using the Gimp so that the white text isn't difficult to read against the header image. 
  2. Changed the layout to use CSS and divs instead of the previous table-based layout. I solved the "columns with equal heights" problem using a hack I found from several websites. Basically: for each column you add a large amount of padding to the bottom of each column, then apply a negative margin so that the padding isn't actually visible on-screen. This will create a scrollbar in the containing div though, so you need to hide the overflow. Sample CSS for this is:

    {{< highlight css >}}
    .content {
    overflow: hidden; /* Part of equal heights column hack */
    }
    .column {
    margin-bottom: -20000px; /* Part of equal heights column hack */
    padding-bottom: 20000px; /* Part of equal heights column hack */
    }      
    {{< / highlight >}}


  3. Centering the main div was something I didn't know how to do either. The solution was to set left and right margin to auto in the divs. But this is ignored by IE6 so in addition to that, you need to set text-align: center in the body. 
  4. Set the background color of the page to be the same as rightmost column. 
  5. Modified index.php by removing the while loop to iterate over the posts. This is so that only the latest post appears in the leftmost column. 
  6. Added the "recent posts" listing in the center column. Relevant code inserted into sidebar.php:

  {{< highlight php >}}
    <table class="recent-posts" >
    <?php
    global $post;
    $recentposts = get_posts('numberposts=5&amp;offset=2');
    foreach($recentposts as $post) {
    ?>
    <tr>
    <td rowspan="2" class="date-cell"><?php the_time('d M Y', '', '') ?></td>
    <td><a class="recent-title" href="<?php the_permalink() ?>"> <?php the_title() ?> </a></td>
    </tr>
    <tr>
    <td class="recent-cats">Filed under <?php the_category(', '); ?></td>
    </tr>
    <?php
    }
    ?>
    </table>
  {{< /highlight >}}

  7. I don't want the about info hardcoded into the right column, so I modify it instead to display the contents of any page titled "about". The code shown below is cribbed from Hemingway Reloaded WordPress theme:

  {{< highlight php >}}
    <?php query_posts('pagename=about'); ?>
    <?php if (have_posts()) : ?>
    <?php while (have_posts()) : the_post(); ?>
    <?php the_content(); ?>
    <?php endwhile; ?>
    <?php endif; ?>
  {{< /highlight >}}


  8. Changed the standard font used to Arial 12px 


   
The above changes took me around half the day today (well, there were naps and videogames in between, et cetera) and the theme is starting to look decent, but there's still a lot to do: navigation links, search pages, category lists, archive page, single post page, page template are the ones I can name off the top of my head right now.

Still, WordPress has turned out remarkably easy to customize, the PHP functions exposed as template tags are usually enough for whatever you plan to do, and the documentation on [codex.wordpress.com][3] is pretty thorough as well.

The hard part turned out to be figuring out CSS-related problems. Luckily, CSS and browser-specific issues are well-discussed problems online so I could easily find the solution to the problems via the internet.

I'll continue working on this whenever I have time, and hopefully can have the theme live on the Roy on Magic blog soon.

 [1]: /2008/04/creating-a-wordpress-template-part-1/
 [3]: http://codex.wordpress.com