---
date: 2016-04-20 00:00:00
slug: how-many-searches-does-it-take
source: quora
syndicated:
- type: quora
  url: https://www.quora.com/How-many-searches-does-it-take-on-average-to-find-a-row-when-not-indexed-in-MySQL-database/answer/Roy-Tang
tags:
- answers
---

Someone on [quora](https://quora.com) asked:
> [How many searches does it take on average to find a row when not indexed in MySQL database?](https://www.quora.com/How-many-searches-does-it-take-on-average-to-find-a-row-when-not-indexed-in-MySQL-database/answer/Roy-Tang)
<span class="ui_qtext_rendered_qtext"><p class="ui_qtext_para u-ltr u-text-align--start">When there is no index in use, you are essentially performing a sequential search (iterating through each row and testing it to see if it matches your criteria), which means the search performs at O(n). If you limit your results to the first hit (using TOP 1 as pointed out by Scott Berry), the average number of checks is n/2 where n is the total size of the sample set. If there is no limit, the average number of checks is n (since you check all rows)</p></span>