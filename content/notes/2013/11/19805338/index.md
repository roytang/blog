---
date: 2013-11-06 06:14:31
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/19805338/adding-event-handlers-globally-to-all-ckeditor-instances
tags:
- ckeditor
- questions
- stackoverflow
- software development
title: Adding event handlers globally to all CKEditor instances
---

I want to add focus and blur handlers to all CKEditor instances in our web application. I would like to add the handlers in one place, instead of hunting down every part where we instantiate a CKEditor. Can this be done, like maybe in the config.js editorConfig setup?

I can't do something like "on document ready, add handlers to all CKEditor instances on the page" either, since additional editor instances may be created dynamically.