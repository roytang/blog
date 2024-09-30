---
date: 2008-12-08 16:08:43
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/349997/what-does-this-regular-expression-do
tags:
- php
- regex
- wordpress
- questions
- stackoverflow
- software development
title: What does this Regular Expression do
---

    $pee = preg_replace( '|<p>|', "$1<p>", $pee );

This regular expression is from the Wordpress source code (formatting.php, wpautop function); I'm not sure what it does, can anyone help?

Actually I'm trying to port this function to Python...if anyone knows of an existing port already, that would be much better as I'm really bad with regex.