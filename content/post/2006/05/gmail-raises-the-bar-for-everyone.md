---
categories:
- Software Development
date: 2006-05-03 06:56:37
title: "GMail raises the bar for everyone"
type: post
url: /2006/05/gmail-raises-the-bar-for-everyone/
---

So I was at work, and one of the HK guys asks me if we can have a themed button for the file input control in one of our screens. So, I'm all "alpha geek" and stuff, and I go: "No we can't. We can't style the &#8216;Browse' button directly, and IE will throw an Access Denied error on submit if we invoke the click() method using Javascript."

But HK guy replies: "Gee, I wonder how GMail does it then."

I checked, and he's right. I never noticed before because I use Firefox all the time, but GMail in IE doesn't even show the freakin' file input control! It's just an "Attach a File" link that opens the "Open File" dialog on click! I took a look at it and I was like&#8230;"how in the world&#8230;"

So, being a developer, I of course attempt to get the source, analyze it, break it down, and get it to work for me. But from experience, I know that trying to figure out gmail's obfuscated javascript code would take me days. So I decided to take an alternative approach: I would let gmail execute it's weird javascript magic, then use javascript myself to extract the relevant HTML and Javascript code from the gmail window at the correct state.

My first attempt: I tried to load gmail in an iframe so I could read the document contents from window.top. Eh, no go. Gmail pops itself out of the frame easily.

My second attempt: I open gmail in a new window using javascript's window.open, then use the resulting window variable to access the document contents. Something like this:

> <html>
  
> <body>
  
> <script>
  
> var win;
  
> function doIt() {
	  
> win = window.open(&#8216;http://www.gmail.com');
  
> }
  
> function getIt() {
	  
> document.getElementById("t").innerHTML = win.document.body.innerHTML;
  
> }
  
> </script>
  
> <br/><input type="button" onclick="doIt()" value="clickMe" />
  
> <br/><input type="button" onclick="getIt()" value="getContents" />
  
> <br/><textarea style="width:100%; height: 40%;" id="t"></textarea>
  
> </body>
  
> </html> 

Wow, "Access is denied." Who knew IE actually had that much security?

I try a few other methods, mainly trying to navigate the properties of the "win" variable to find something I can actually use. I go through trees of frames trying to find something&#8230;but I get "Access Denied" and "Permission Denied" anytime I try to get near a document element.

Damn this is tough&#8230;I thought it would only take me a few minutes =/

## Comments

### Comment by [advanced](http://advanced-webhosting.net) on 2007-10-31 17:12:52 +0000
Better late than never?

You bumped into IE's "Same Origin Policy" security protocol.

If you use .hta (Microsoft's HTML Application extension) you can bypass it.

You'll need to crawl the microsoft dev center a bit to find out how to
  
properly initialize an .hta in a chromeless IE browser window.. but it's worth
  
the effort for future reference.

Otherwise you can use firefox tamper data plugin or a greasemonkey hack to
  
bypass firefox's SOP, but I don't think that's what you're looking for.

As a side note you can use prototype event handlers to stop the framebuster
  
"beforeunload" but gmail still won't load in a frame for some reason or
  
another (both the original and the new interface update exhibit this
  
behaviour, I don't know if it's intentional or just lucky).

Anyways.. they use javascript browser detection and it's not really obfuscated
  
in the newest version, just stop the page load on the "Loading&#8230;" screen and
  
view source.

Personally I'd use PHP to snoop the browser type in the header
  
$\_SERVER["HTTP\_USER_AGENT"] and then use an if statement to server the correct
  
HTML.

Alternatively you could check if the user agent will accept xml applications
  
since mozilla and opera will but IE still doesn't load them as true
  
applications:

if ( stristr($\_SERVER["HTTP\_ACCEPT"],"application/xhtml+xml")

BETTER still.. (K.I.S.S.) theme an input button using CSS and IE ONLY switches
  
and skip all the guess work and iffy browser detection routines.

Seeing as it's been well over a year since you posted this I hope you got it
  
sorted ..)