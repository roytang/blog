---
title: 'Javascript: References to out-of-scope variables.'
author: roy
type: post
date: 2016-12-01T01:30:53+00:00
url: /2016/12/javascript-references-to-out-of-scope-variables/
wp-syntax-cache-content:
  - |
    a:3:{i:1;s:1672:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="javascript" style="font-family:monospace;"><span style="color: #339933;">&lt;</span>script<span style="color: #339933;">&gt;</span>
      <span style="color: #000066; font-weight: bold;">var</span> btn <span style="color: #339933;">=</span> document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;BTN&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
      <span style="color: #000066; font-weight: bold;">var</span> test <span style="color: #339933;">=</span> <span style="color: #CC0000;">1</span><span style="color: #339933;">;</span>
      btn.<span style="color: #660066;">onclick</span> <span style="color: #339933;">=</span> <span style="color: #000066; font-weight: bold;">function</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
          alert<span style="color: #009900;">&#40;</span>test<span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
      <span style="color: #009900;">&#125;</span>
      test <span style="color: #339933;">=</span> <span style="color: #CC0000;">2</span><span style="color: #339933;">;</span>
    <span style="color: #339933;">&lt;/</span>script<span style="color: #339933;">&gt;</span></pre></td></tr></table><p class="theCode" style="display:none;">&lt;script&gt;
      var btn = document.getElementById(&quot;BTN&quot;);
      var test = 1;
      btn.onclick = function() {
          alert(test);
      }
      test = 2;
    &lt;/script&gt;</p></div>
    ";i:2;s:4309:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="javascript" style="font-family:monospace;">  <span style="color: #339933;">&lt;</span>script<span style="color: #339933;">&gt;</span>
        <span style="color: #000066; font-weight: bold;">var</span> btns <span style="color: #339933;">=</span> <span style="color: #009900;">&#91;</span><span style="color: #009900;">&#93;</span><span style="color: #339933;">;</span>
        btns.<span style="color: #660066;">push</span><span style="color: #009900;">&#40;</span>document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;BTN1&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        btns.<span style="color: #660066;">push</span><span style="color: #009900;">&#40;</span>document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;BTN2&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        btns.<span style="color: #660066;">push</span><span style="color: #009900;">&#40;</span>document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;BTN3&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        btns.<span style="color: #660066;">push</span><span style="color: #009900;">&#40;</span>document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;BTN4&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        <span style="color: #000066; font-weight: bold;">var</span> input <span style="color: #339933;">=</span> document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;IN&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    &nbsp;
        <span style="color: #000066; font-weight: bold;">for</span> <span style="color: #009900;">&#40;</span><span style="color: #000066; font-weight: bold;">var</span> i<span style="color: #339933;">=</span><span style="color: #CC0000;">0</span><span style="color: #339933;">;</span> i<span style="color: #339933;">&lt;</span><span style="color: #CC0000;">4</span><span style="color: #339933;">;</span> i<span style="color: #339933;">++</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
          btns<span style="color: #009900;">&#91;</span>i<span style="color: #009900;">&#93;</span>.<span style="color: #660066;">onclick</span> <span style="color: #339933;">=</span> <span style="color: #000066; font-weight: bold;">function</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
            alert<span style="color: #009900;">&#40;</span>input.<span style="color: #660066;">value</span><span style="color: #339933;">*</span><span style="color: #009900;">&#40;</span>i<span style="color: #339933;">+</span><span style="color: #CC0000;">2</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
          <span style="color: #009900;">&#125;</span>
        <span style="color: #009900;">&#125;</span>
      <span style="color: #339933;">&lt;/</span>script<span style="color: #339933;">&gt;</span></pre></td></tr></table><p class="theCode" style="display:none;">  &lt;script&gt;
        var btns = [];
        btns.push(document.getElementById(&quot;BTN1&quot;));
        btns.push(document.getElementById(&quot;BTN2&quot;));
        btns.push(document.getElementById(&quot;BTN3&quot;));
        btns.push(document.getElementById(&quot;BTN4&quot;));
        var input = document.getElementById(&quot;IN&quot;);
    
        for (var i=0; i&lt;4; i++) {
          btns[i].onclick = function() {
            alert(input.value*(i+2));
          }
        }
      &lt;/script&gt;</p></div>
    ";i:3;s:4894:"
    <div class="wp_syntax" style="position:relative;"><table><tr><td class="code"><pre class="javascript" style="font-family:monospace;">   <span style="color: #339933;">&lt;</span>script<span style="color: #339933;">&gt;</span>
        <span style="color: #000066; font-weight: bold;">var</span> btns <span style="color: #339933;">=</span> <span style="color: #009900;">&#91;</span><span style="color: #009900;">&#93;</span><span style="color: #339933;">;</span>
        btns.<span style="color: #660066;">push</span><span style="color: #009900;">&#40;</span>document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;BTN1&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        btns.<span style="color: #660066;">push</span><span style="color: #009900;">&#40;</span>document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;BTN2&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        btns.<span style="color: #660066;">push</span><span style="color: #009900;">&#40;</span>document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;BTN3&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        btns.<span style="color: #660066;">push</span><span style="color: #009900;">&#40;</span>document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;BTN4&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        <span style="color: #000066; font-weight: bold;">var</span> input <span style="color: #339933;">=</span> document.<span style="color: #660066;">getElementById</span><span style="color: #009900;">&#40;</span><span style="color: #3366CC;">&quot;IN&quot;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    &nbsp;
        <span style="color: #000066; font-weight: bold;">function</span> getClickHandler<span style="color: #009900;">&#40;</span>counter<span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
          <span style="color: #000066; font-weight: bold;">return</span> <span style="color: #000066; font-weight: bold;">function</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
            alert<span style="color: #009900;">&#40;</span>input.<span style="color: #660066;">value</span><span style="color: #339933;">*</span><span style="color: #009900;">&#40;</span>counter<span style="color: #339933;">+</span><span style="color: #CC0000;">2</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
          <span style="color: #009900;">&#125;</span>
        <span style="color: #009900;">&#125;</span>
    &nbsp;
        <span style="color: #000066; font-weight: bold;">for</span> <span style="color: #009900;">&#40;</span><span style="color: #000066; font-weight: bold;">var</span> i<span style="color: #339933;">=</span><span style="color: #CC0000;">0</span><span style="color: #339933;">;</span> i<span style="color: #339933;">&lt;</span><span style="color: #CC0000;">4</span><span style="color: #339933;">;</span> i<span style="color: #339933;">++</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
          btns<span style="color: #009900;">&#91;</span>i<span style="color: #009900;">&#93;</span>.<span style="color: #660066;">onclick</span> <span style="color: #339933;">=</span> getClickHandler<span style="color: #009900;">&#40;</span>i<span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
        <span style="color: #009900;">&#125;</span>
      <span style="color: #339933;">&lt;/</span>script<span style="color: #339933;">&gt;</span></pre></td></tr></table><p class="theCode" style="display:none;">   &lt;script&gt;
        var btns = [];
        btns.push(document.getElementById(&quot;BTN1&quot;));
        btns.push(document.getElementById(&quot;BTN2&quot;));
        btns.push(document.getElementById(&quot;BTN3&quot;));
        btns.push(document.getElementById(&quot;BTN4&quot;));
        var input = document.getElementById(&quot;IN&quot;);
    
        function getClickHandler(counter) {
          return function() {
            alert(input.value*(counter+2));
          }
        }
        
        for (var i=0; i&lt;4; i++) {
          btns[i].onclick = getClickHandler(i);
        }
      &lt;/script&gt;</p></div>
    ";}
categories:
  - Software Development
tags:
  - javascript

---
In JavaScript, referencing variables that are declared outside of a function&#8217;s scope can be tricky. If you have code like this:

<pre lang="javascript"></pre>

The click handler above retains a reference to the test variable even though it falls out of scope as soon as the script block finishes execution. When you actually click the button, the alert will show the last value of the variable when the block finished execution (2) instead of the value at the time the function was initialized (1).

I thought about this because another developer raised a similar problem to me a few days ago. He had a loop that was initializing click handlers for an array of elements. Of course I can&#8217;t replicate his example here, but let&#8217;s say we wanted to add click handlers to an array of buttons that would show the result of multiplying an input value by different integers.

<pre lang="javascript"></pre>

This is kind of an analogous example for the problem. In this case, the expected behavior is that the first button outputs the input value times 2, while the second button outputs the input value times 3, and so on. But because each of the click handlers retains a reference to the loop counter i, what they will remember on execution is the last value of i after the loop exits, that is, i==4. All the buttons will show the same output.

There are several ways to correct the behavior. One way would be to build the click handlers using a utility function, like so:

<pre lang="javascript"></pre>

This way, the value for the local function variable "counter" is locked in once getClickHandler exits execution, and each returned function now has a reference to a different "counter", and the buttons will behave as expected.