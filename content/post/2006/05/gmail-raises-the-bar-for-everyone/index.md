---
categories: []
date: 2006-05-03 06:56:37
tags:
- Software Development
title: GMail raises the bar for everyone
type: post
url: /2006/05/gmail-raises-the-bar-for-everyone/
---

So I was at work, and one of the HK guys asks me if we can have a themed button for the file input control in one of our screens. So, I'm all "alpha geek" and stuff, and I go: "No we can't. We can't style the &#8216;Browse' button directly, and IE will throw an Access Denied error on submit if we invoke the click() method using Javascript."

But HK guy replies: "Gee, I wonder how GMail does it then."

I checked, and he's right. I never noticed before because I use Firefox all the time, but GMail in IE doesn't even show the freakin' file input control! It's just an "Attach a File" link that opens the "Open File" dialog on click! I took a look at it and I was like... "how in the world... "

So, being a developer, I of course attempt to get the source, analyze it, break it down, and get it to work for me. But from experience, I know that trying to figure out gmail's obfuscated javascript code would take me days. So I decided to take an alternative approach: I would let gmail execute it's weird javascript magic, then use javascript myself to extract the relevant HTML and Javascript code from the gmail window at the correct state.

My first attempt: I tried to load gmail in an iframe so I could read the document contents from window.top. Eh, no go. Gmail pops itself out of the frame easily.

My second attempt: I open gmail in a new window using javascript's window.open, then use the resulting window variable to access the document contents. Something like this:

```html
<html>
<body>
<script>
  var win;
  function doIt() {
  win = window.open(‘http://www.gmail.com’);
  }
  function getIt() {
  document.getElementById(“t”).innerHTML = win.document.body.innerHTML;
  }
</script>
<br/><input type=”button” onclick=”doIt()” value=”clickMe” />
<br/><input type=”button” onclick=”getIt()” value=”getContents” />
<br/><textarea style=”width:100%; height: 40%;” id=”t”></textarea>
</body>
</html> 
```

Wow, "Access is denied." Who knew IE actually had that much security?

I try a few other methods, mainly trying to navigate the properties of the "win" variable to find something I can actually use. I go through trees of frames trying to find something... but I get "Access Denied" and "Permission Denied" anytime I try to get near a document element.

Damn this is tough... I thought it would only take me a few minutes =/