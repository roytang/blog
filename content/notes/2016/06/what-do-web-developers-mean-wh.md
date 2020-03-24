---
date: 2016-06-03 00:00:00
slug: what-do-web-developers-mean-wh
source: quora
syndicated:
- type: quora
  url: https://www.quora.com/What-do-web-developers-mean-when-they-say-back-end/answer/Roy-Tang
tags:
- answers
---

Someone on [quora](https://quora.com) asked:

> [What do web developers mean when they say back-end?](https://www.quora.com/What-do-web-developers-mean-when-they-say-back-end/answer/Roy-Tang)


<span class="ui_qtext_rendered_qtext"><p class="ui_qtext_para u-ltr u-text-align--start">The difference between front-end and back-end is on which side executes the relevant code. HTML, JS and CSS are all interpreted, rendered, and in the case of JS, executed by the client browser. These parts are the front-end. The code for those parts is basically meaningless to the server. The server program looks at these parts and only sees simple text and just sends it through to the browser (or whatever client program made the request)</p><p class="ui_qtext_para u-ltr u-text-align--start">For example in a *.php file, anything outside the &lt;?php ?&gt; brackets is not interpreted by the PHP runtime, they are just returned to the browser as-is. The server does not “load the HTML for the user”, it simply returns the HTML code to the browser and the browser loads that HTML and displays the rendered HTML.</p></span>