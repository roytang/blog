---
date: 2010-09-12 16:14:28
reply_to:
  label: '''how to use jquery UI autocomplete 1.8.4?'' on stackoverflow'
  name: Ben
  type: stackexchange
  url: https://stackoverflow.com/questions/3695414/how-to-use-jquery-ui-autocomplete-1-8-4
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/3695414/how-to-use-jquery-ui-autocomplete-1-8-4/3695558#3695558
tags:
- javascript
- jquery
- user-interface
- autocomplete
---

If you want to use jquery ui autocomplete, your data must be "a simple Array of Strings, or it contains Objects for each item in the array, with either a label or value property or both". This is from the documentation at http://jqueryui.com/demos/autocomplete/ 

Your server response does not follow the expected data type, you should modify suggest.php to post-process the data into label-value pairs.

As I understand it, you also want to perform a custom action when an item is selected from the autocomplete, so you should also add a handler for the 'select' event.