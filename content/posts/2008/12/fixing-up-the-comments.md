---
title: Fixing up the comments
type: post
date: 2008-12-01T04:58:00+00:00
url: /2008/12/fixing-up-the-comments/
categories:
  - Software Development
tags:
  - royondjango

---
I played around with the built-in comments app today, trying to clean it up.

Some findings:

1. Some of the moderation views, such as flagging a post or deleting a post, accept a next parameter that determines where the view will redirect to after the operation. However, the way the url&#8217;s are set up, there&#8217;s no easy way to pass this parameter normally, even through query strings. THis lovely bug is documented in
  
[
  
http://code.djangoproject.com/ticket/8968
  
][1] 
  
. I wasn&#8217;t confident enough to try patching it, so as a temporary workaround, I overrode the flag and delete templates and placed the following inside the form:

<input type=&#8221;hidden&#8221; name=&#8221;next&#8221; value=&#8221;{{ comment.get\_content\_object_url }}&#8221; />

_
  
Edit: Wow that was stupid. Blogger didn&#8217;t want to render the HTML code above!
  
_ 

I also replaced the URL in the &#8220;cancel&#8221; links for both pages. For some reason, {{ comment.permalink }} wasn&#8217;t giving me anything useful.

2. Took me a bit of work to figure out how the moderation part works. Apparently I have to hook on some of the signals to add my moderation logic. I&#8217;m not sure yet how to handle this, or whether I should try customizing the comment form with something like a captcha to prevent comment spam.

3. I have a pending problem now that submitting comments from the preview or error page does not redirect to the correct place. (i.e. the post page). I tried adding the next parameter to the form, but apparently comment.get\_content\_object_url returns an empty string here because the comment has not yet been saved to the database. I think the content object should be provided in the context for the preview page. This would be handled by
  
[
  
http://code.djangoproject.com/ticket/9268
  
][2] 
  
, except apparently no one&#8217;s paying attention to it yet.

4. Some random features I added: Gravatar support (the Gravatar for the email address used to post the comment will be shown), and Markdown support in the comment body. Easy stuff.

5. Cleaned up an refactored the templates that render the comments, separating them from the parts that render the blog posts. This makes it easier if I want to have comments for other non-Blog post objects later.

Non-comment related:

1. Added simple search!

2. The script to import from WordPress has some problems. Since I&#8217;m storing the post body in markdown format, I use
  
[
  
html2text
  
][3] 
  
to convert the HTML body from old posts into markdown, but nice stuff like image alignments and tables are lost. I think I have to make do with editing straight HTML for old posts imported from WordPress, and just clean them up later as needed.

My code is rather messy now (especially from the HTML side). I should clean it up sometime soon.

 [1]: http://code.djangoproject.com/ticket/8968
 [2]: http://code.djangoproject.com/ticket/9268
 [3]: http://www.aaronsw.com/2002/html2text/