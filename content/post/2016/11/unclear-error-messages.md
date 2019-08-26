---
author: roy
categories: []
date: 2016-11-17 01:30:37
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/153281781825/unclear-error-messages
tags:
- Software Development
title: Unclear error messages
type: post
url: /2016/11/unclear-error-messages/
---

_"Button for non-service floor does not light up."_

For more than a decade I regularly went to an office building where the elevators verbally spouted this nonsense message whenever you tried to go to a floor that the current elevator car did not service. For context, the elevators in the building were zoned programmatically -- this means that they only service a particular subset of the floors that are provided on the elevator panel itself. They sometimes disable the zoning depending on the loading among the elevator cars so simply removing the buttons for the unsupported floors isn't a viable solution.

Back to that message: It's terrible. At least once a week, some clueless newcomer to the building would press the button and hear the message and totally be unable to relate it to what he just did or even understand what it was saying. (That the message audio did not have the best quality only compounded the problem.)

See, that error message doesn't make sense because it's telling you something you already see: when you press the button for an non-service floor, the button does not light up. It's the equivalent of submitting a web form and receiving an error message of _"Your form was not submitted."_

A good error message should do three things (none of which the elevator message do):

  * It should tell the user something went wrong.

The first one is easy and may immediately be made obvious by the nature of the error message itself. For a web platform, error messages are often displayed highlighted in a different colored font and with some sort of "X" or other icon indicating a mistake has been made. For the elevator message. For the elevator message, I've often observed that some people dismiss the verbal message as background noise unrelated to the button they just pressed, and some will even repeatedly press the button again, ignoring the message. An improvement would be to have some sort of high-pitched buzzing noise whenever the button for a non-service floor is pressed, before giving the verbal message. Pressing the button multiple times would reset to the buzzing noise, making it painfully obvious that "Hey, maybe I should pay attention."

  * It should tell the user what went wrong.

For a web platform this typically means some of the fields failed some validation, in which case you should list them out. Something like "The following problems were encountered: Name is a required field. Date must not be later than today. Amount must be greater than 0." and so on. One must also take care to use more plain language rather than technical, i.e. "The Name must be filled in." might be better than "Name is a required field."

For the elevator message, instead of describing what the user already sees when he presses the non-responsive button, more useful would have been a direct "This elevator does not go to that floor."

  * It should tell the user what he can do to correct it.

For web forms with validation errors, a simple "Please correct these errors and resubmit the form." should suffice. For the elevator message, it could simply say "Please try a different elevator."

Good error messages make a big difference in the usability of your product, be it a web form or an elevator or something else. It makes it easier for users to find and learn their own way forwards rather than needing someone to walk them through their actions.