---
categories:
- Software Development
date: 2007-10-29 02:19:40
title: How to Solve Technical Problems
type: post
url: /2007/10/how-to-solve-technical-problems/
---

One of the qualities that I think make a really good software developer is the ability to solve difficult technical problems. Unless you're the sort of software developer who just sells the same piece of software over and over again, at some point in time you'll to need to find out how to implement some feature you've never tried before. Or you'll hit a problem that's not documented in any official docs and you need that critical functionality.

Typically, there are two approaches: Research and Experimentation. Today I'll talk about Research.

Research means the internet of course, but what part of it exactly? At first of course you should search for the information yourself, using Google usually. But often if the technology is new or the problem is esoteric enough, you won't be able to find what you need (or you would need very precise keywords). The second step is to ask for expert help.

As an example, some recent postings of mine on a Microsoft-related forum (I was trying to figure out how to do an addin for Microsoft Office) elicited a mail from someone with the subject "Hello, I need ur help". I was feeling a bit helpful, so I gave him a reply. I'm not sure if it was smarmy or anything, but I also gave him some additional advice, and I quote:

"Also I have some additional free advice for you:
   

   
1. Your email looks like SPAM. I was about to mark it as spam when I happened to spot the phrase "MSWord Addins" in the body. Learn to write better email subjects.
   

   
2. Sending personal emails to people asking for help isn't a very good way to solve technical issues. Most people are likely to ignore such requests.
   

   
3. You might want to read this: http://catb.org/~esr/faqs/smart-questions.html"

I'm not trying to deride him or anything, god knows I've sent my own share of personal email requests for help before. And it's correct that they are often ignored, so it's not very effective. I think the most effective way, as mentioned in the ESR link above, is to use forums. Specifically, don't look for forums where newbies like us ask questions; use forums where experts congregate. By forum, I'm not strictly referring to bulletin boards, it also includes mailing-lists.

How to find the best forums? It depends on what you're looking for.

The best thing is if your subject matter of choice has an active community of developers interested or passionate about the product. Google about the subject matter and see what forums or mailing lists are popular. An example would be [Adobe Flex][1], which I started reading up on a while back for a work-related issue. Finding help on Adobe Flex is really easy. There's [a very active mailing-list][2], where you can even expect replies from some of the guys who actually made Flex. If you visit some of the active blogs about Flex (there are a lot), many of them will reference the flexcoders mailing list so you know you can get a lot of good help there.

Non-official forums are better because people are more likely to be passionate than paid reps. One problem I often encounter when researching is Microsoft. Whenever I search for Microsoft-related stuff inevitably sources dry up -- there are literally hundreds of unofficial forums where many newbies ask questions. Now, what to recognize about Microsoft is that they have hundreds (maybe thousands?) of experts called MVPs in every different Microsoft technology. These MVPs are recognized by Microsoft for providing unofficial support to the community. So, the trick is to figure out where you can post such that a good number of MVPs will see your question and possibly respond.

I'm not sure what the best place would be, but the one that I have gotten the most results from would be [Google Groups][3]. Any of the microsoft.public.* ones. I guess Google Groups would be pretty good for non-MS topics as well, but I find that inevitably my MS searches lead me here. For Office-related questions at least there are often one or two MVPs who reply.

Another resource I have used on occasion: the forums at [Joel on Software][4]. A lot of very good developers frequent those forums, so even if no one can answer your questions, they might be able to point you in the right direction.

Beyond forums, well good luck. At this point you might need to resort to personal emails, although I have personally never gotten any success from such a method. Or you probably have to resort to detailed experimentation or even -- god forbid -- giving up.

 [1]: http://www.adobe.com/products/flex/
 [2]: http://tech.groups.yahoo.com/group/flexcoders/
 [3]: http://groups.google.com/
 [4]: http://www.joelonsoftware.com/

## Comments

### Comment by [advanced](http://advanced-webhosting.net) on 2007-10-31 17:37:02 +0000
Hmm.. you've overlooked the motivational force of money and the power of sub-
  
contracting.

Rome was not built in a day, nor was it built by a single pair of hands.

If you know what the problem is or at very least the desired objective, you'll
  
find skilled people lining up to work on your project at most of the various
  
freelance developer sites.

Of course if you're asking someone to build the next super web framework
  
they'll expect a kings ransom and most likely never finish.

But if you can narrow it down to a simple and exact task such as "I need a
  
themed input button that is cross-browser compliant" you'll find people
  
willing to provide top notch solutions practically for free (minus a good
  
review and the associated freelancer site fees ~$5).

Even wasting an hour googling the answer probably won't be as cost effective.
  
Most of the time you can even request demo examples to make sure they're not
  
just trying to run a scam.

### Comment by [Roy](http://roytang.net/blog) on 2007-10-31 21:21:42 +0000
That's probably a good idea, but not really something that's an option with
  
the company I'm in. You know the deal -- I'd need all sorts of authorizations
  
to be able to subcontract someone, it's not worth it, especially for a simple
  
task that would take me an hour or two to figure out.

Besides, the post isn't really about how to get things done, but rather the
  
value of technical problem-solving skill to a software developer, and my own
  
usual approaches to it.

I wrote this because I was doing performance assessments on several junior
  
developers and noticed that some really had no idea how to go about solving
  
such issues.