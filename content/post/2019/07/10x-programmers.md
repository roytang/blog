---
author: roy
categories: []
date: 2019-07-16 05:56:56
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1151010066574843905/
tags:
- software development
title: 10X Programmers
type: post
---

The topic of the mythical ["10x programmer"](https://softwareengineering.stackexchange.com/questions/179616/a-good-programmer-can-be-as-10x-times-more-productive-than-a-mediocre-one) has been the topic of discussion recently on tech twitter, due to [a thread](https://twitter.com/skirani/status/1149302828420067328?s=19) listing out the supposed signs of being such a mythical beast.

{{% twitter 1149302828420067328 %}}

The thread received a lot of negative responses, mainly because several of these items can be considered red flags indicating someone who doesn't play well with others - hates meetings, prefer irregular hours, poor mentoring ability, disdain for documentation, find process miserable, works alone to produce great code, etc. These attributes remind me of Steve McConnel's description of programming heroics in *Professional Software Development*:

> Combine a shortage of skilled workers with the common tendency to set overly optimistic schedules, and the stage is set for the programming hero. Programming heroes take on challenging assignments and write mountains of code. They work vast amounts of overtime. They become indispensable to their projects. Success, it seems, rests squarely on their shoulders.
> 
> Project managers both love and fear hero programmers because they are smart, temperamental, and sometimes a little self-righteous, and because the managers don't see any way to complete the project without them. In a tight labor market, replacing them isn't an option.
> 
> Unfortunately, the reality is that for every programming hero who is capable of monumental coding achievements, there are other pathological programming disasters who just don't know how to work well with others. They hoard design information and source code. They refuse to participate in technical reviews. They refuse to follow standards established by the team. The sum total of their actions is to prevent other team members from making potentially valuable contributions. A significant number of programming heroes don't turn out to be heroes at all; they turn out to be prima donna programming ball hogs.

Despite the negative feedback, I found myself relating to the list in the thread above because most if not all of these items could have been used to describe myself at some point or another in my career. Especially in my earlier years, I had a profound dislike for meetings and documentation and process. I think this sort of attitude stems from the transition from being a solo developer (which you largely are in school) who enjoys the act of coding to being part of a team tasked to deliver the software. The first-time team member may find it difficult to appreciate having to do all these non-coding things (meetings, mentoring, documentation) because he doesn't yet have an appreciation of how they can make things smoother for the entire team. 

Not all of the items in the list are bad habits. Luckily, I think I grew out of most of the bad ones as my career went on and I became part of different teams and filled different roles. Not all of these are bad habits though. Going through the list:

> - 10x engineers hate meetings. They think it is a waste of time and obvious things are being discussed. They attend meetings because the manager has called for a "Staff meeting" to discuss the features and status.

I'm still wary of too many unnecessary meetings, but I also understand how getting people away from their IDEs and together for a discussion can be necessary to bring a project back on track. 

> - Timings in the office for 10x engineers is highly irregular. They tend to work when very few folks are around. If there is a crowd or all-hands meeting, they are not visible. Most of them are late-night coders and come late to the office.

I think locally, people tend to come in later during the day instead of earlier, due to Metro Manila traffic. I knew that if I wanted some focused time, I could come in early and not much people would bother me. I think this is generally an ok practice, as long as you're still available during core hours when your team needs you.

> - 10x engineers laptop screen background color is typically black (they always change defaults). Their keyboard keys such as i, f, x are usually worn out than of a, s, and e (email senders).

This one is just straight-up cargo-cult nonsense. Different people have different preferences. (Okay, I do prefer dark background IDEs). 

> - 10x engineers know every line of the code that has gone into production. If a QA or support folks alert an issue, they know precisely where the fault (or bug) is and can fix the same in hours vs days

I have been in this kind of situation, although I guess it's a bit of an exaggeration. Typically if you're working in a team with a nontrivial codebase and you "know everything", some of your knowledge may be shallow, and some other devs who spent more time with each module may have more in-depth knowledge of how a particular module works. Having one guy with good oversight into the codebase can be handy for the team - for the reason cited above, they may easily be identify the cause of an issue, but the team should make sure he's not the only guy familiar with everything. Some redundancy is needed so that you aren't always dependent on the same person everytime. It's also bad for you as the developer who knows everything about the codebase, as it can be very hard to go on vacation, you'll have a tendency to get calls such as "Hey, just a really quick question, do you know where is the code that does XYZ?"

> - Most of the 10x engineers are full-stack engineers. For them code is code, they don't care whether it is front-end, back-end, API, database, serverless, etc. I have rarely seen them doing UI work.

This is still true for me. And just the other day during a call I had to give a disclaimer that my UI work isn't the best lol. I don't think this is indicative of disdain for specialists, there should be room in a team for both [generalists and specialists](/2016/12/generalists-and-specialists-in-dev-teams/).

> - 10x engineers can convert "thought" into "code" in their mind and write it in an iterative fashion. Given a product feature, they can write that entire feature in one or two sittings of 4 to 6 hours with a caffeinated drink without distraction.

I mean, this is just describing a developer who's in the zone. It's true that developers who can get into the zone on a regular basis are likely to be much more productive, that's a tautology.

> - 10x engineers rarely look at help documentation of classes or methods. They know it in memory and can recall from memory. They write code at the same ease as writing English. No breaks, no pauce, just type.

This one is a bit of BS, especially in modern software development where we have the meme of developers coding by stackoverflow. It might have been true in the older days when there weren't a billion and one APIs and frameworks to know and learn.

> - 10x engineers are always learning new frameworks, languages ahead of everyone in the company. They are not afraid of anything new. If there is something new (e.g. blockchain) they gobble up, setup, experiment before anyone is getting started.

This one is still true for me as of now. I still enjoy exploring new frameworks, languages and technologies, though I don't always have the time for it. I think this is a good trait for a developer to have, but at the same time it may be dangerous to expect or require this of developers when putting together a team. Not everyone enjoys coding, and developers shouldn't be penalized for not wanting to do software stuff outside of work hours.

> - 10x engineers are poor mentors as they can't teach others on what to do OR parcel the work. They always think "It takes too long to teach or discuss with others, I would rather do it myself." They are also poor interviewers.

I'm sure I have uttered some variation of that quote more than once in my career. The tendency to try to carry all the load yourself is not only a disservice to yourself, it's a disservice to your team as you're not helping them grow. I will admit my mentoring skills in the early years wasn't very good - I'm the type of mentor who tends to throw you into the deep end so you can quickly learn to swim. This is because that's my personal learning style as well, I learn more from trying stuff than from a lecture or a book. I understand that not everyone learns the same way, so I do actively try to spot opportunities for me to learn to explain things better (I like to think writing in a blog helps!) and for [better mentoring](/2018/10/mentoring-in-software-development/). And I think my interviewing skills have improved a bit through the years as well.

> - 10x engineers don't hack things. They write quality code and know exactly how the code has to evolve, and have a mental model of overall code structure. They write at most one design document, and the rest is in the code.

The idea of the most productive engineers not hacking things can only come from an idealist who hasn't experienced schedule pressure. While of course quality code is an ideal, the best engineers know when it is necessary to make tradeoffs and workarounds to meet requirements and schedules. And they will write as many documents as needed to make sure things can be understood. 

> - 10x engineers rarely job hunt or move out of the company. They move out because you make their life miserable with the process, meetings, training, and other non-value-added activities. If you come across them, hold on to them. Celebrate them.

This was true for me for the longest time, I stayed with my first company for 15 years before deciding to move on. I would suspect this tends to be true for the type of engineer I described who enjoys the coding part and not so much the dealing with people part of the job. Moving companies means a lot more noncoding work: meeting new people, learning new processes and procedures, more meetings and trainings and interviews and what not. Laziness is probably also a factor. 

The items listed here remind me of the type of programmer stereotype where one programmer goes into his office, tells nobody not to bother him, then comes out after three days having written all the code and solved all the company's problems. It's a ridiculous, dangerous stereotype that doesn't mesh well with how modern software development teams work. 

I'm not claiming that 10x engineers don't exist, I'm sure they do, and I know from experience many of the above stereotypes can be true. But stereotypes are just that - stereotypes. Every programmer has had a different path and there can be superproductive programmers who also know how to well work with teams and can be great mentors and write great documentation.

I'm also not necessarily claiming to be a 10x programmer even though I claim to relate to the items here (false humility?). I would appreciate being paid a 10x salary though. :D

A second thread on 10x programmers I like, from Alan Cooper:

{{% twitter 1150215587978596353 %}}