---
date: 2009-06-16 07:38:33
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1000028/how-to-focus-radio-control-using-javascript-in-ie
tags:
- javascript
- internet-explorer
- questions
- stackoverflow
- software development
title: How to focus radio control using Javascript in IE?
---

Given the code below:

<!-- begin snippet: js hide: false console: true babel: false -->

<!-- language: lang-js -->

    function test() {
        document.forms[0].TEST[0].focus();
    }

<!-- language: lang-html -->

    <form>
        <input type="button" value="Test" onclick="test()" />
        <input type="radio" name="TEST" value="A">A
        <input type="radio" name="TEST" value="B">B
    </form>

<!-- end snippet -->

In IE6, clicking the button doesn't focus the control, unless I've already tabbed through the radio at least once, in which case it works. =/

Any idea how I should be focusing the control? The above works perfectly fine in FF of course.

Edit: I found that the control is being focused, except the highlight box around the radio button is not being rendered. (I can hit space to activate the radio button, and also use arrow keys to change the active button). So the question becomes: how can I force the focus highlighting box to render?