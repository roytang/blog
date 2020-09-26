---
author: roy
categories: []
date: 2016-12-01 01:30:53
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/153885002880/javascript-references-to-out-of-scope-variables
- type: twitter
  url: https://twitter.com/roytang/statuses/804136962735095810/
tags:
- javascript
- Software Development
title: 'Javascript: References to out-of-scope variables.'
type: post
url: /2016/12/javascript-references-to-out-of-scope-variables/
---

In JavaScript, referencing variables that are declared outside of a function's scope can be tricky. If you have code like this:

```javascript
  var btn = document.getElementById("BTN");
  var test = 1;
  btn.onclick = function() {
      alert(test);
  }
  test = 2;
```

The click handler above retains a reference to the test variable even though it falls out of scope as soon as the script block finishes execution. When you actually click the button, the alert will show the last value of the variable when the block finished execution (2) instead of the value at the time the function was initialized (1).

I thought about this because another developer raised a similar problem to me a few days ago. He had a loop that was initializing click handlers for an array of elements. Of course I can't replicate his example here, but let's say we wanted to add click handlers to an array of buttons that would show the result of multiplying an input value by different integers.

```javascript
    var btns = [];
    btns.push(document.getElementById("BTN1"));
    btns.push(document.getElementById("BTN2"));
    btns.push(document.getElementById("BTN3"));
    btns.push(document.getElementById("BTN4"));
    var input = document.getElementById("IN");

    for (var i=0; i<4; i++) {
      btns[i].onclick = function() {
        alert(input.value*(i+2));
      }
    }
```

This is kind of an analogous example for the problem. In this case, the expected behavior is that the first button outputs the input value times 2, while the second button outputs the input value times 3, and so on. But because each of the click handlers retains a reference to the loop counter i, what they will remember on execution is the last value of i after the loop exits, that is, i==4. All the buttons will show the same output.

There are several ways to correct the behavior. One way would be to build the click handlers using a utility function, like so:

```javascript
    var btns = [];
    btns.push(document.getElementById("BTN1"));
    btns.push(document.getElementById("BTN2"));
    btns.push(document.getElementById("BTN3"));
    btns.push(document.getElementById("BTN4"));
    var input = document.getElementById("IN");

    function getClickHandler(counter) {
      return function() {
        alert(input.value*(counter+2));
      }
    }
    
    for (var i=0; i<4; i++) {
      btns[i].onclick = getClickHandler(i);
    }
```


This way, the value for the local function variable "counter" is locked in once getClickHandler exits execution, and each returned function now has a reference to a different "counter", and the buttons will behave as expected.