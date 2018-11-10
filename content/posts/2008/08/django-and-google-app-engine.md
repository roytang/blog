---
categories:
- Software Development
date: 2008-08-25 04:37:43
title: Django and Google App Engine
type: post
url: /2008/08/django-and-google-app-engine/
---

In my continuing quest to become better than everybody else, I spent some time today learning
   
[
    
Django
   
][1] 
   
(a Python webapp framework) and the
   
[
    
Google App Engine
   
][2] 
   
.

I tried following the tutorials included in the
   
[
    
Django Book
   
][3] 
   
for a while, but I've never taken too well with just typing up examples from a book, so I decided to write something from scratch. I decided to write a simple message board application.

I wrote the message board pretty quickly using Django; it took me about 2-3 hours to have a bare-bones message board up and running. (I was watching Speed Racer at the same time.) The UI is horrendous of course, but it's functional, with categories and topics, etc.

Now to deploy the message board app somewhere. After a bit of searching around, I couldn't find any suitable free Django webhosting. So I went with the backup plan: I'd upload the project to the Google App Engine.

I've had a Google App Engine account for a while now, but haven't done anything with it yet. Unfortunately, a Django app can't be ported directly to GAE as Google has their own datastore implementation which won't work with Django's models. So I spent the rest of the day porting/rewriting the message board app for use with GAE. Google has their own guide for this sort of porting here:
   
[
    
Running Django on Google App Engine
   
][4] 
   
.

Some problems encountered when porting:
 
  


  * Can't seem to use the list_detail generic view; I get errors about undefined user attribute on the request 
  * Sometimes after editing a view, I get random &#8220;NoneType has no attibute get&#8221; errors. Restarting the dev_appserver fixes this. 
  * Unlike Django, GAE models don't have an &#8220;id&#8221; primary key. Instead, you must use object.key() which returns some sort of hash string (making for very inconvenient urls) 
  * I'm having
    
    [
     
    errors raised during 404s
    
][5] 
    
    ; the problem is mentioned in
    
    [
     
    this thread
    
][6] 
    
    which should already be fixed but I'm still encountering it. I'll investigate it later. 


   
The final product is here:
   
[
    
Random Encounters Message Boards
   
][7] 
   
. I don't know who would actually use the site, but I think there's some people I know reading this blog who wouldn't be able to resist testing it!

The next step would be to improve the UI of the app!

 [1]: http://www.google.com.ph/url?sa=t&ct=res&cd=1&url=http%3A%2F%2Fwww.djangoproject.com%2F&ei=x6OySMHXJYvQ6gP-t93-Dw&usg=AFQjCNGfxYhHSLrgk6aVrm5Bbc2ozc89rA&sig2=6Zd2UWQL7gEYK7d6SsY2Hg
 [2]: http://code.google.com/appengine/
 [3]: http://www.djangobook.com/en/1.0/
 [4]: http://code.google.com/appengine/articles/django.html
 [5]: http://random-encounters.appspot.com/forum/cat/CxIIQ2F0ZWdvcnkYAww/
 [6]: /forum/cat/CxIIQ2F0ZWdvcnkYAww/
 [7]: http://random-encounters.appspot.com/forum/home/