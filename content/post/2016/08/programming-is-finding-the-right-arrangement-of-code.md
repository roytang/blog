---
author: roy
categories:
- Software Development
date: 2016-08-18 01:30:21
title: Programming is Finding the Right Arrangement of Code
type: post
url: /2016/08/programming-is-finding-the-right-arrangement-of-code/
---

I like to say that software development is a challenging career because no two projects are ever the same and there are always new challenges to face and new concepts to learn, but the truth of the matter is a bit more complex.

**Writing software is about breaking down large problems into a series of very small technical problems for which we already have solutions.** Examples of small enough technical problems include list sorting, comparison, arithmetic operations, path traversal, string concatenation, returning a string as an HTTP response, rendering text to the screen, retrieving submitted parameters from an HTTP request, and so on. Any given non-trivial software project will be broken down into thousands, possibly hundreds of thousands of such small tasks, some occurring more often under different contexts.

The job of the software developer designed to implement such a program or some part of a program is to identify all those tiny tasks and the order in which they need to be done, then actually do it and put it all together in a way that satisfies the software's requirements. Finding out the proper arrangement of tasks is a form of design in and of itself, separate from the design of the software requirements. This is why many programmers will tell you that coding itself is both design and implementation -- the coder still has to make numerous small decisions, rearranging code and tasks until he finds the correct arrangement that works to satisfy your needs.

Invariably, practically all of these tiny tasks are either trivial to implement (based on knowledge the programmer already has), or have already been implemented somewhere else by some other programmer. This is why Q&A sites such as [Stack Overflow][1] are very useful for the modern programmer -- you simply dip your pool into the communal knowledge of the programming community and most of the time the programmers who have solved the same problem before will tell you how they did it.

"Practically all" means in the rare instance, you will still encounter problems that as far as you can tell have yet to be solved by anyone else in the world. I am unsure if there is anything quite as depressing to the programmer as finally finding a single Google hit about that one problem he was unable to solve only to find that it was a link to his own unanswered Stack Overflow question from months before.

Often this happens when you are doing something or some combination of things so obscure no one else has tried it before, or when you are legitimately blazing new ground. It largely depends on the field you are working in -- if you are using proven frameworks to build your 10th web application, most likely 999 out of every 1,000 problems you have are already solved. On the other hand, if you were maybe writing drivers for a new piece of hardware, or maybe writing a new framework to be used at the same time as the first application using it, that number shoots up considerably.

What to do when faced with such a situation where all the sources you consult -- mentors, experts, textbooks, the internet, and so on -- are unable to help you solve the problem and it stops you from moving forward? Well, if you can sense that trying to solve the problem on your own or brute forcing it in some manner may waste a lot of time that you can't afford, you should remember what I said above: **Writing software is about breaking down large problems into a series of very small technical problems for which we already have solutions. **This means your first choice should be to check first if there is an alternative arrangement of tasks for which that particular problem could be avoided (that is, "re-design your code to work around the problem"). You shouldn't box yourself into a particular sequence of steps, be willing to "think outside the box" to look for other solutions that while not immediately obvious, may be more feasible (i.e. "already solved")

This method of iterating the arrangements of parts until the software works might seem a bit clunky, but I've found it useful to think in this manner -- it makes even the impossible problems seem feasible. Now, if only problems with humans could be solved just be rearranging things... 

 [1]: http://stackoverflow.com/