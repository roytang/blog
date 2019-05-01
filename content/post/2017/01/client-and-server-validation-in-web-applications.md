---
author: roy
categories: []
date: 2017-01-05 01:30:39
tags:
- Software Development
title: Client and Server Validation in Web applications
type: post
url: /2017/01/client-and-server-validation-in-web-applications/
---

Because of the nature of the web and the fact that you should [never trust user input][1], all the validation in a web application should be done on the server side. You can additionally provide validation on the client side (via JavaScript), but this is only a concession towards a better user experience and should not be used as a substitute for server-side validation.

One would think that anyone with a basic understanding of how HTTP works would understand the above easily and any failure to practice it should be considered amateur hour. But in shops where most of the testing is done manually, developers can easily fall into the habit of adding the client-side validations (since failing to do so would earn them a bug report) and forgetting the server-side validations altogether.

The main problems are that (a) HTTP requests can be spoofed, they do not need to have come from a form submitted via a browser; and (b) even for forms submitted via a browser, the Javascript validations may have been tampered with on the client-side.

For explicit validations for which you wrote out some logic (for example: email address must be so-and-so format), it is obvious that you need that on the server side. But for some classes of validation you may forget to handle them especially if they do not explicitly generate errors in the webpage on the client-side.

First example: when the contents of a drop-down list are dependent on some other value on the form. On the client-side you probably already restrict the choices such that the user is unable to select an invalid combination so it doesn't look like a check is needed. But on the server-side, you still have to check that the choice submitted for the drop-down field is a valid value given the other values submitted in the request.

Second example: when you hide or disable certain fields in the web page depending on some other value on the form. Same as above, you don't need to add a specific check on the client-side since the user is already prevented from doing so by the UI. But on the server-side, you have to make sure not to save or process any values from those hidden/disabled fields if the other values on the form indicate they shouldn't be processed.

Weak validations on the server side are dangerous because at the very least they will create bad data in your system and at the very worst may expose you to security vulnerabilities.

 [1]: https://www.owasp.org/index.php/Don't_trust_user_input