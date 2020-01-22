---
date: 2010-08-30 10:50:08
reply_to:
  label: '''jQuery - split() arrays with only one match = undefined'' on stackoverflow'
  name: Peter
  type: stackexchange
  url: https://stackoverflow.com/questions/3599620/jquery-split-arrays-with-only-one-match-undefined
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/3599620/jquery-split-arrays-with-only-one-match-undefined/3599669#3599669
tags:
- javascript
- jquery
- arrays
---

You already have the lines logging your values array, was it so hard to add lines logging the other vars?

    c1_arr = c1.split(';');  

The array created here is ['font-color:#ff0000', ''] - there is a blank second element since there's nothing after the ';' in the input string.

Then when you call:

    values[1][i]= c1_arr[i].split(':');

c1_arr[1] is empty string, so values[1][1] is an array with only one element, empty string.

values[1][1][0] -> empty string
values[1][1][1] -> undefined (no second element)