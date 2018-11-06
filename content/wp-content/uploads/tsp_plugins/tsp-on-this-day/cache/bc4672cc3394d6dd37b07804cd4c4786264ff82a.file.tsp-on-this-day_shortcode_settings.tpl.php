<?php /* Smarty version Smarty-3.1.14, created on 2018-02-11 17:02:44
         compiled from "/home/roytang/webapps/blog/wp-content/plugins/tsp-on-this-day/templates/tsp-on-this-day_shortcode_settings.tpl" */ ?>
<?php /*%%SmartyHeaderCode:10143825445a807734aa7c00-69377232%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'bc4672cc3394d6dd37b07804cd4c4786264ff82a' => 
    array (
      0 => '/home/roytang/webapps/blog/wp-content/plugins/tsp-on-this-day/templates/tsp-on-this-day_shortcode_settings.tpl',
      1 => 1486429437,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '10143825445a807734aa7c00-69377232',
  'function' => 
  array (
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.14',
  'unifunc' => 'content_5a807734b03471_98535777',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_5a807734b03471_98535777')) {function content_5a807734b03471_98535777($_smarty_tpl) {?><p>Changing the default post options below allows you to place <strong>[tsp-on-this-day]</strong> shortcode tag into any post or page with these options.</p>
<p>However, if you wish to add different options to the <strong>[tsp-on-this-day]</strong> shortcode please use the following settings:</p>
<ul style="list-style-type:square; padding-left: 30px;">
	<li>Title: <strong>title="Title of Posts"</strong></li>
	<li>Max Words in Title: <strong>max_words=10</strong></li>
	<li>Show Event Data: <strong>show_event_data="Y"</strong>(Options: Y, N - Requires The Event Calendar plugin &amp; fpost_type="tribe_events")</li>
	<li>Show Author: <strong>show_author="Y"</strong>(Options: Y, N)</li>
	<li>Show Publish Date: <strong>show_date="Y"</strong>(Options: Y, N)</li>
	<li>Show Quotes: <strong>show_quotes="Y"</strong>(Options: Y, N)</li>
	<li>Show Private Posts: <strong>show_private="N"</strong>(Options: Y, N)</li>
	<li>Show Posts with No Media Content: <strong>show_text_posts="N"</strong>(Options: Y, N)</li>
	<li>Keep Formatting: <strong>keep_formatting="N"</strong>(Options: Y, N)</li>
	<li>CSS Style tags: <strong>style="color: red;"</strong> (CSS tags seperated by semicolon)</li>
	<li>Number Posts: <strong>number_posts="5"</strong></li>
	<li>Read More Text: <strong>read_more_text="Continue Reading <span class="meta-nav">&rarr;</span>"</strong></li>
	<li>No Posts Text: <strong>no_posts_msg="<em>No Posts Found On This Day</em>"</strong></li>
	<li>Excerpt Length (Layouts #0 & #3): <strong>excerpt_min="60"</strong></li>
	<li>Excerpt Length (Layouts #1, #2, #4[Slider], #5): <strong>excerpt_max="100"</strong></li>
	<li>Post Class: <strong>post_class=""</strong>(Example: columns1_3, columns1_2)</li>
	<li>Post Type: <strong>fpost_type="post"</strong>(Options: post, varies)</li>
	<li>Slider Width: <strong>slider_width="865"</strong></li>
	<li>Slider Height: <strong>slider_height="365"</strong></li>
	<li>Layout: <strong>layout="0"</strong>(Options: 0, 1, 2, 3, 4, 5)
		<ul style="padding-left: 30px;">
			<li>0: Left: Image - Right: Title, Text (Thumbnail)</li>
			<li>1: Top: Title - Left: Image - Right: Text (Featured-Medium)</li>
			<li>2: Left: Title, Image - Right: Text (Featured-Large)</li>
			<li>3: Left: Image - Right: Text (Thumbnail/No title)</li>
			<li>4: Slider: Title, Image - Right: Text (Featured-Large)</li>
			<li>5: Top: Image, Bottom: Title, B ottom-Last: Text</li>
		</ul>
	</li>
	<li>Order By: <strong>order_by="DESC"</strong>(Options: rand,title,date,author,modified,ID)</li>
	<li>Show Thumbnails: <strong>show_thumb="Y"</strong>(Options: Y, N)</li>
	<li>Thumbnail Width: <strong>thumb_width="80"</strong></li>
	<li>Thumbnail Height: <strong>thumb_height="80"</strong></li>
	<li>HTML Tag Before Title: <strong>before_title="&lt;h3&gt;"</strong></li>
	<li>HTML Tag After Title: <strong>after_title="&lt;/h3&gt;"</strong></li>
</ul>
<hr>
A shortcode with all the options will look like the following:<br><br>
<strong>[tsp-on-this-day title="Title of Posts" keep_formatting="N" style="color: red;" max_words=10 show_quotes="N" show_thumb="Y" show_event_data="N" show_author="Y" show_date"N" show_private="N" show_text_posts="N" number_posts="5" excerpt_max=100 excerpt_min=60 post_class="" fpost_type="post" slider_width="865" slider_height="365 layout="0" order_by="DESC" thumb_width="80" thumb_height="80" read_more_text="more..." before_title="" after_title=""]</strong>
<?php }} ?>