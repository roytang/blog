---
date: 2008-10-23 02:57:06
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/228386/how-to-get-command-line-arguments-for-a-running-process
tags:
- apache-flex
- flexbuilder
- questions
- stackoverflow
- software development
title: How to get command line arguments for a running process
---

In my program, I have been receiving an error when I use a
command-line compile command for mxmlc. The error is related to an
embedded font name not being correctly identified by flex in the
system fonts list.

However, on a whim, I decided to copy the code to Flex Builder and
compile it there. To my surprise, it worked, and it found the proper
font using the same system name I had given (PMingLiU).

I suspected my problem may be a locale one, and that my system cannot
correctly identify the font name because of locale considerations.

I've tried setting the locale of the compile code to en_US, to no
avail. So I would like to ask if anyone here knows how exactly Flex Builder invokes the MXML compiler and what differences there are compared to running mxmlc directly? We know it's not using the mxmlc.exe directly, since we tried replacing mxmlc with our own executable to capture the command line parameters. 

If it matters, the OS used is Windows XP.