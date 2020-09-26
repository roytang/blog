---
author: roy
categories: []
date: 2017-12-28 01:00:38
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/169017917280/my-coding-approach
- type: twitter
  url: https://twitter.com/roytang/statuses/946186540031660032/
tags:
- Software Development
title: My Coding Approach
type: post
url: /2017/12/my-coding-approach/
---

I was thinking about my typical approach to coding. When writing a new feature, I tend to implement in the direction of where the data flows, starting from the user interface then to the backend and back to the frontend and wherever else that goes. I will build incrementally, using debugging tools or console printouts to ensure that each step is working correctly.

As an example, here's how I did a recent web-based function:

  1. The user needs to see a new button on the screen, so I add the HTML for that button and just have the click handler be an alert confirming the button has been clicked.
  2. The button needs to open a modal dialog. I write the HTML for the modal dialog, then add the code to the button to launch the modal.
  3. On load, the modal dialog needs to fetch some data from the server. I write the Javascript to make the ajax call on launch of the modal.
  4. On the backend, I map the URL route used by the above ajax call to a controller method. The controller method simply outputs a debug message to the console. I refresh the page on the front end, click the button to launch the modal and verify on my server's console that the controller method has been called.
  5. I modify the controller method to call a method on the relevant model. I write the stub method on the model with a dummy return value, which the controller method then outputs to the console. I verify the entire flow again.
  6. I write the retrieval logic in the controller method. I verify the entire flow again, using server console output to verify the correct data is being returned to the controller.
  7. I have the controller write the returned data to the response as JSON. I go back to the frontend and modify the success handler of the ajax call to log the response to the Javascript console. At this point, I also update the error handler to do whatever is appropriate. I verify the entire flow again, this time confirming that the correct data is displayed in the browser console.
  8. The user needs to see the data from the response, so I write the Javascript and HTML to render the response inside the modal dialog. I verify the entire flow again, this time confirming that the correct data is shown in the modal dialog.

I'm not sure if this is the best approach, but it works for me. It feels incremental, systematic, methodical, and easy to see where things go wrong (which they inevitably do). As kind of an upside, I also strangely feel compelled to not stop until I have working complete flow. Of course the downside is that if I have to stop at any point, I now have a nonworking UI component, but at least that's a clear indicator of where I need to pick up next time.

I realize that a lot of modern software engineering advocates recommend some kind of test-driven approach. I imagine with such an approach start with the smallest iota of functionality, write a test for it, then write the actual code, then work outwards from there, building more complexity on top. So for the example above, maybe I should have started with the retrieval logic on the backend then work my way outwards from there.

I do that sometimes but I find that as a full-stack engineer my natural tendency is work my way across a new feature in this manner -- from user interface to backend and back. Combined with the difficulty of writing code to test UI/HTML/JavaScript, this means I rarely get into the mindset of test-driven development. It's not something I ever got used to. Maybe someday a switch will click and I will get it and my mind will be blown.

My approach does have some benefits though, in that I'm defining the interfaces first before diving into the guts of the logic. In that sense it's kind of "test-driven" except all my testing is manual.

I do think having such a systematic, incremental method of implementation is a good skill for the junior programmer to learn though. My experience is that many younger programmers (especially those fresh out of college) tend to write huge chunks of code/logic/functionality then get surprised when the very first thing breaks down.

Recently when sitting down with a junior to help them walk through some problem I often show them how I debug problems this way. I trace the entire flow from start to end, adding debug messages as I go, to help identify at which step the process goes awry. I also try to describe my proposed approach for complex new functions this way. I'll prototype a small part of it from frontend to backend, writing debug messages all the way, and it conveniently leaves the junior with a template for writing the rest of the functionality. (Although I am as of yet unable to attest to the efficacy of this approach)

I've been writing code for a long time, and while I wasn't self-aware enough back when I started out to document how I was writing software, I like to think I've improved a lot since then. And for sure there's still a lot to learn. Maybe some years from now I'll look back on this blog post and chuckle about how naive I was and write a new blog post detailing an even better approach.