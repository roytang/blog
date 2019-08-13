---
categories: []
date: 2009-02-01 12:59:35
tags:
- Software Development
title: Code Quality
type: post
url: /2009/02/code-quality/
---

I was doing code reviews on an interface file-processing framework to be used in one of our projects. The code was workable and already being used by several programs, and I didn't see any major functional flaws. But design-wise I felt that it could stand for some improvements/refactoring to be "better object-oriented code" or "easier to maintain". 

The current design required a lot of inheritance -- the usual way of doing things in older Java code at work. I was thinking of a more dynamic, declarative design that would require a config file instead of more subclasses but eventually I decided against asking for it. It would have taken maybe a day or two to implement, and the client programs using the framework would need to be rewritten, et cetera. I felt that the improvement in maintainability didn't justify the delay it would introduce.

I remembered this after reading [Joel Spolsky and Jeff Atwood's discussion on unit tests and code quality][1]. The most relevant quote from their discussion is 

> And I find, sadly, to be completely honest with everybody listening, quality really doesn't matter that much, in the big scheme of things... 

It reminds me of a discussion I once had with the boss on one of his visits when he caught me doing code reviews. He asked me whether it was worth the effort for me to be doing these reviews. How many critical problems did I find on average? How many would have been caught by QA anyway? His point wasn't to diss on code reviews, but was that although we want to have quality, sometimes we put too much effort into it, and the costs don't always justify it. 

I guess part of working smart is knowing exactly how much quality your customers need. As developers, we feel a certain sense of "pride" that we want our code to be the best, optimized, et cetera. But polishing it up until you get a "perfect" design is also a form of [gold-plating][2] as well.

On a slight tangent, when I was reading about [how they write code at NASA][3], I was a bit put off at how much effort they put into building perfect code. They had lots of design meetings, going over every piece of code multiple times, et cetera. 

> And the culture is equally intolerant of creativity, the individual coding flourishes and styles that are the signature of the all-night software world. "People ask, doesn't this process stifle creativity? You have to do exactly what the manual says, and you've got someone looking over your shoulder," says Keller. "The answer is, yes, the process does stifle creativity."

I understand that it's the level of quality required for space shuttle software -- literally perfect -- and it makes me glad _I'm not_ writing space shuttle software because stifling creativity doesn't sound fun to me. 

Back to the code review I was doing: I eventually shipped it back with a few minor comments to improve efficiency, but no major changes. I mentioned since the framework was already being used, we should treat the comments as optional. You have to weigh the costs of every change you ask for or every "Comment by Tester" you file in the name of code quality or better usability, et cetera. "If it ain't broke, don't fix it" is another form of [YAGNI][4] I guess.

 [1]: http://www.joelonsoftware.com/items/2009/01/31.html "From Podcast 38"
 [2]: http://www.codinghorror.com/blog/archives/000150.html "gold-plating blog post on codinghorror"
 [3]: http://www.fastcompany.com/magazine/06/writestuff.html?page=0%2C0 "The Write the Right Stuff"
 [4]: http://c2.com/xp/YouArentGonnaNeedIt.html "WikiWikiWeb entry for You Aren't Gonna Need It"