---
date: 2016-04-19 00:00:00
slug: is-it-bad-to-use-regex-to-sift
source: quora
syndicated:
- type: quora
  url: https://www.quora.com/Is-it-bad-to-use-Regex-to-sift-through-JSON-data/answer/Roy-Tang
tags:
- answers
---

Someone on [quora]() asked:
> [Is it bad to use Regex to sift through JSON data?](https://www.quora.com/Is-it-bad-to-use-Regex-to-sift-through-JSON-data/answer/Roy-Tang)
<span class="ui_qtext_rendered_qtext"><p class="ui_qtext_para u-ltr u-text-align--start">Well, you probably know the famous quote:</p><blockquote><p class="ui_qtext_para u-ltr u-text-align--start">Some people, when confronted with a problem, think "I know, I'll use regular expressions." Now they have two problems. - Jamie Zawisnki</p></blockquote><p class="ui_qtext_para u-ltr u-text-align--start">That being said, regular expressions can be a good approach for particular problems. Sifting through JSON however, does not sound like one of them. Why not? JSON is already a structured format that has elements you can easily iterate through using normal programming constructs. I'm assuming you mean using regular expressions to search through JSON data by treating the entire JSON object as a string. If instead you're using regex matching on individual JSON elements, that's probably fine.</p></span>