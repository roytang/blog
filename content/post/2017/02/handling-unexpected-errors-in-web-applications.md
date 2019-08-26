---
author: roy
categories: []
date: 2017-02-02 01:30:25
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/156694527375/handling-unexpected-errors-in-web-applications
tags:
- Software Development
title: Handling unexpected errors in web applications
type: post
url: /2017/02/handling-unexpected-errors-in-web-applications/
---

So after so many months of development you deployed your webapp to production and it's up and running and everything is fine and you celebrate and your work is done right?

Not really.

Two days later you get an urgent support call in the middle of the night. (Your clients are halfway across the world.) They're asking why the website is inaccessible. You check via your browser and sure enough there's an error 500. You have to ssh into the server. Half-asleep, you have to quickly comb through the log files to figure out if there's something you can do about it right now or you have to sadly tell the client that the team has to handle it in the morning.

Nobody expects software errors. And nobody can predict how they will happen. (If we could do that, there wouldn't be any errors!) But in general you should stay ahead of future headaches during development time by having robust error handling and reporting principles in place for your development team to follow.

There are two classes of errors:

  * Validation errors -- checks on user inputs. These errors are expected, and the most important thing here is to [present clear error messages that tell the user what was wrong and how they can correct it][1].
  * Everything else is an unexpected error, which we can breakdown further according to how the development team would react: 
      * "That shouldn't happen!" -- the broadest category, usually caused by human errors in coding/configuration or hardware problems. Examples include: database failure, typos in configuration files, different data formats used by different developers, unexpected system crashes and so on.
      * "Hmm, oh yeah, we didn't think of that." -- i.e., design flaws or unhandled cases. These are errors caused by program flow or usage that was not anticipated in the program's design but are considered valid use.
      * "That can't possibly happen!", also popularly known as "We have no clue how that happened." Most unexpected errors start out under this category then after some detective work (some developers use the term "debugging"), it transfers to one of the above categories.

Unexpected errors may also be either recoverable (the user can either attempt to repeat the operation to continue or use other functions in the system) or catastrophic (the entire system or subsystem is completely unusable.)

Ideally, what happens when an unexpected error occurs? There's a number of things that probably need to be considered:

  1. The user needs to be aware that it's not an error on his part and that the problem needs to be reported to support or the system administrator.
  2. The user needs to be presented with enough information to give to the support team to allow them to determine the cause and fix the error.
  3. The program needs to capture what information it can to help the support team find and fix the error.

For client-side errors (typically JavaScript problems, but can also be problems in HTML/CSS rendering), all of the above are difficult, since the mechanisms by which you present #1 and #2 and by which you can do #3 may be compromised by the error. Typically for any client-side errors, you are almost entirely reliant on the user's description of the error and the steps that led to it -- not the most reliable source of information, but you make do with what you have. If you are unable to reproduce the error during debugging, you are in for a whole lot of speculation and trial and error.

For server-side errors, it's a bit easier than client-side errors. The first two items are typically handled by having a catch-all error page in the application that gives an error code and message for unexpected errors.

For the last item, it generally means logging, either to a file or a database-backed audit trail (the file is more reliable). Generally we log the error/exception encountered, including the stack trace, and some log messages on each request/page access. A majority of the time, having the stack trace is sufficient. The access logs allow us to back-trace previous steps which might have contributed to the problem. Any special conditions encountered in the code should also be logged -- this helps to identify errors that can only happen under some combination of special conditions.

You don't want to log too much information (what to log might need to be a separate post all on its own), but just enough to help the support team determine the cause of the problem.

Sometimes, the error is specific to the data being used by the users, or happens only in the environment they are using. And the support team investigating the problem will often not have access to that data or that environment, so your logging and the error reports have to be good enough to allow them to deduce the conditions that caused the error.

Error handling for deployed systems is already hard -- so make sure not to make it harder on the future support team by having standard error handling and logging mechanisms.

 [1]: http://roytang.net/2016/11/unclear-error-messages/