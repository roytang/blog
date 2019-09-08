---
author: roy
categories: []
date: 2018-12-13 01:56:56
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1073035117860454400/
tags:
- devto
- Software Development
title: Adding Developers to a Late Project
type: post
---

For any nontrivial software project of at least moderate team size, there can be a significant cost to onboarding a new team member, especially at later stages when you are rushing to meet deadlines. 

The most signifiant cost is of course the communication overhead as described in [the Mythical Man Month](https://en.wikipedia.org/wiki/The_Mythical_Man-Month). Fun story, the CEO of a company once told me they would add more developers to a delayed project to meet the deadline and when I pointed out the increased overhead he said to me that it wasn't a problem because they would just assign modules to those devs that have minimal dependencies so they don't have to communicate so much. Ha! I just shrugged and let him think it was a good idea.

In my experience, it's never a good idea, especially late in the game. Even if you are somehow able to minimize any domain overhead (which I seriously doubt), there is also the nontrivial matter of technical overhead that any new developer intake needs to go through. I'm not just talking about learning the programming language or the technical stack - presumably if you are adding someone to the team, he is either already familiar with the stack or you have factored in his being a newbie and needing training time. 

No, I'm talking about things like templates, UI standards, coding standards, devops processes, configuration, libraries in use, data dictionaries, and so on. Most projects will have "preferred ways of doing things", and the more work that has been done on the project, the more such "tribal knowledge" is often undocumented and you will need to bother someone to figure the stuff out. And if the project is behind schedule and everyone is trying to catch up, it's more likely people are going to forget to tell you stuff.

Slightly related side note: If there is very little in the way of standards or tribal knowledge global to the project, that might be a warning sign. I once worked with a client who had several subcontractors to work on the different modules in their system. Each module/subcontractor worked more or less independently from the others, with very little documentation or standards in place. The result was a weird hodgepodge system where one module did things one way, and the next module did things a completely different way, and so on. 

As an example, I was once asked to help in a project with a relatively large codebase and significant deadline pressure and I was coming in hot with no knowledge of the domain and minimal experience with the framework in use. I told them I wasn't sure I could hit the target given I had to learn a bunch of stuff, but they were in desperate need and so ok we proceeded anyway. Now, I'm an experienced developer, so pulling me in was a better option than pulling in some newbie since there's a lot of stuff I can figure out myself, but off the top of my head, I had to explicitly bother other people about:

- proper access rights to the repo
- proper access rights to the google drive with all the documents
- CRLF problems when I use windows to clone the repo
- database credentials for the provided dev VM
- errors encountered due to undocumented steps missing from the setup document
- where should I put new configuration options
- where should I put my new module in the menu
- how to map data in other tables to my new tables
- the proper HTML markup and CSS classes needed to conform to the way they layouted pages
- how to implement form validations the same way as other screens
- standard methods for displaying messages/errors
- how to setup role permissions for my new screens
- preferred library for making third party API calls
- JS errors encountered when using a particular component
- problems with dynamically created reccords not behaving properly when the page redirects on error

... and probably a lot more I'm unable to recall anymore, and that's not accounting for any comments that would be later logged by QA because I was unfamiliar with how other screens usually behaved.

If you're adding developers to a late project, you have to account for these onboarding costs, in addition to the increased communication overhead. That means sounding the alarm and asking for help earlier. If there's a module that's estimated by your devs to take say, one sprint, you can't ask for help one sprint before the needed delivery - you need to look for help maybe one or two sprints earlier. (Of course, the best approach would be to avoid painting your project into this corner at all, but as we all know in this industry, sometimes things just happen!)