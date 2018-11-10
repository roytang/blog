---
author: roy
categories:
- Software Development
date: 2016-06-01 22:31:10
title: You Are Not Your Code
type: post
url: /2016/06/you-are-not-your-code/
---

I once had to advise someone who found himself irritated at receiving lots of comments during code review. I think my response was good enough to quote verbatim:

> <p class="qtext_para">
>   Remember: You are not your code. You are not the hundred or so lines of C or Java or JavaScript or whatever that you wrote today.
> </p>
> 
> <p class="qtext_para">
>   This problem arises because you are too attached to your code. Your ego is associated with the code you write and you feel that any comments or defects found reflect upon   you as a person.
> </p>
> 
> <p class="qtext_para">
>   You are not perfect. You will not write perfect software, and that&'s fine. It&'s not a flaw, it&'s just the way software is. It isn&'t written all in one go, magically perfect and elegant and satisfying all the requirements. Good software goes through multiple iterations and many eyes looking at it.
> </p>
> 
> <p class="qtext_para">
>   It is also important to treat it as a learning experience &#8211; learn what you can from each code review comment and try to apply what you learn to future code you write. This also helps you minimize review comments in the future. Instead of treating the large number of comments as a shortcoming on your part, treat it as a metric you can improve upon.
> </p>

<p class="qtext_para">
  It&'s probably true of any endeavor which results in creation &#8211; be it programming, arts, crafts or whatnot &#8211; that you need to be able to divorce yourself from your work so that you can accept and analyze and learn from criticisms objectively and without feeling terrible about yourself.
</p>

<p class="qtext_para">
  Fun fact: All programmers write terrible code. Yes, even the veterans, the rock stars, the elite, they have all written terrible code at some point in their careers and they will probably write more terrible code in the future. The key is to recognize those instances &#8211; either through introspection or being open to criticism &#8211; and learning from them and trying to minimize them in the future. Or at least correct them earlier!
</p>

## Comments

### Comment by Eric on 2016-06-02 15:18:42 +0000
This is very true. It also gets more difficult to write &#8220;correct&#8221;&#8216; code as you get older and gain more experience. The definition of &#8220;correct&#8221; is refined with experience and it becomes easy to get locked in analysis paralysis because you are much harder on yourself when reviewing your own code.

There is something to just sitting down and making something work as a newbie. The fact that something works provides motivation to continue&#8230; So much so that this has become my new approach to mentoring junior developers. Think about the problem, refine the high level design with input from others, and then code something that works. It&'s easier to refactor a working system than it is to try to design the perfect implementation up front.

### Comment by ExMicrosoftie on 2016-06-03 04:55:45 +0000
Of course this is the wise approach to this situation &#8211; but I&'ve been in more than one workgroup where managers penalized you based on numbers of CR comments &#8211; without ever reading any of them, of course. Ideally we&'d all improve over time and get less feedback and the system would work &#8211; and maybe outside of Redmond that&'s what the culture supports &#8211; but when everyone reviewing your code is in direct competition with you for raises, people tend to ramp up the feedback to take their competitors/coworkers down. (In my decade of experience in MS Office, Developer Division, and Windows, anyway) In that case, it&'s more than just ego attachment fueling the frustration, it&'s your career viability, your family&'s medical insurance, maybe your work visa status. Sometimes there&'s nothing wrong with your code, and a workplace is just hostile. That&'s not a problem you solve through detachment.

### Comment by [roy](http://roytang.net) on 2016-06-03 08:10:55 +0000
Of course not all workplaces are ideal, but I think even in those situations being overly attached to your code can hinder and not help. The idea is not that you don&'t defend your code but rather that you treat criticism with an open mind &#8211; that doesn&'t mean you accept it if it&'s BS though! 🙂