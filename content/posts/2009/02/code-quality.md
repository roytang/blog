---
title: Code Quality
type: post
date: 2009-02-01T12:59:35+00:00
url: /2009/02/code-quality/
categories:
  - Software Development

---
I was doing code reviews on an interface file-processing framework to be used in one of our projects. The code was workable and already being used by several programs, and I didn&#8217;t see any major functional flaws. But design-wise I felt that it could stand for some improvements/refactoring to be &#8220;better object-oriented code&#8221; or &#8220;easier to maintain&#8221;. 

The current design required a lot of inheritance &#8211; the usual way of doing things in older Java code at work. I was thinking of a more dynamic, declarative design that would require a config file instead of more subclasses but eventually I decided against asking for it. It would have taken maybe a day or two to implement, and the client programs using the framework would need to be rewritten, et cetera. I felt that the improvement in maintainability didn&#8217;t justify the delay it would introduce.

I remembered this after reading [Joel Spolsky and Jeff Atwood&#8217;s discussion on unit tests and code quality][1]. The most relevant quote from their discussion is 

> And I find, sadly, to be completely honest with everybody listening, quality really doesn&#8217;t matter that much, in the big scheme of things&#8230;

It reminds me of a discussion I once had with the boss on one of his visits when he caught me doing code reviews. He asked me whether it was worth the effort for me to be doing these reviews. How many critical problems did I find on average? How many would have been caught by QA anyway? His point wasn&#8217;t to diss on code reviews, but was that although we want to have quality, sometimes we put too much effort into it, and the costs don&#8217;t always justify it. 

I guess part of working smart is knowing exactly how much quality your customers need. As developers, we feel a certain sense of &#8220;pride&#8221; that we want our code to be the best, optimized, et cetera. But polishing it up until you get a &#8220;perfect&#8221; design is also a form of [gold-plating][2] as well.

On a slight tangent, when I was reading about [how they write code at NASA][3], I was a bit put off at how much effort they put into building perfect code. They had lots of design meetings, going over every piece of code multiple times, et cetera. 

> And the culture is equally intolerant of creativity, the individual coding flourishes and styles that are the signature of the all-night software world. &#8220;People ask, doesn&#8217;t this process stifle creativity? You have to do exactly what the manual says, and you&#8217;ve got someone looking over your shoulder,&#8221; says Keller. &#8220;The answer is, yes, the process does stifle creativity.&#8221;

I understand that it&#8217;s the level of quality required for space shuttle software &#8211; literally perfect &#8211; and it makes me glad _I&#8217;m not_ writing space shuttle software because stifling creativity doesn&#8217;t sound fun to me. 

Back to the code review I was doing: I eventually shipped it back with a few minor comments to improve efficiency, but no major changes. I mentioned since the framework was already being used, we should treat the comments as optional. You have to weigh the costs of every change you ask for or every &#8220;Comment by Tester&#8221; you file in the name of code quality or better usability, et cetera. &#8220;If it ain&#8217;t broke, don&#8217;t fix it&#8221; is another form of [YAGNI][4] I guess.

 [1]: http://www.joelonsoftware.com/items/2009/01/31.html "From Podcast 38"
 [2]: http://www.codinghorror.com/blog/archives/000150.html "gold-plating blog post on codinghorror"
 [3]: http://www.fastcompany.com/magazine/06/writestuff.html?page=0%2C0 "The Write the Right Stuff"
 [4]: http://c2.com/xp/YouArentGonnaNeedIt.html "WikiWikiWeb entry for You Aren't Gonna Need It"

## Comments

### Comment by Aleks on 2009-02-04 00:25:24 +0000
Refactoring is an investment. You should be able to justify the effort to refactor the code on its long-term benefits. 

As for code reviews, I now think that its effectivity is largely dependent on when it's conducted. It's less effective when the developer is already done with the whole module/functionality and the QA team is about to do their thing. I think it's better to conduct the reviews when the developer has done a little coding and his design has been laid out.

### Comment by Aleks on 2009-02-04 00:44:54 +0000
That's supposed to be:
  
You \*will\* be able to justify the effort to refactor the code on its long-term benefits.

### Comment by roy on 2009-02-08 12:42:50 +0000
I know full well about the benefits of refactoring and code reviews. What I'm saying is, there are other factors to consider. 

As developers who take pride in our work surely you should want to refactor and have someone looking at your code almost all the time. But like all things, software is largely a product of compromise. 

Sure, it works out well in the long run. But sometimes you just want to make it through the short run, you have to realize that cutting back on these code quality measures and accepting the technical debt is a viable business option.