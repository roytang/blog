---
author: roy
categories:
- Software Development
date: 2017-02-09 01:30:50
title: Working with Client-Server Programs
type: post
url: /2017/02/working-with-client-server-programs/
---

Back when I was starting out as a software developer, webapps weren't really a thing. Not as much as they are now anyway. My company provided training to new hires, but I didn't get any web development training at the time, even though they already had a few web development projects in play at the time.

Instead my initial training involved mostly development of so-called client-server software. This was software that was installed and run on the client machine but they would connect to a remote database server. Up until the early 2000s most enterprisey-type systems used these kinds of program.

I was trained in using mostly two tools:  Borland Delphi and Oracle Forms and Reports. These were the sort of tools that would have been billed as reducing the need for specialized programmers or developers. They featured drag and drop user interfaces to design forms or report layouts. The Oracle tools featured robust database integration that let you drag and drop to associate form fields to database tables and fields. Supposedly even people with minimal training would be able to do the work of application programmers.

In practice of course, the only people patient enough to work with these tools in-depth were the programmers themselves. And client requirements always eclipsed the capabilities of these tools, such that expert programmers were still needed to push the tools to their limits and beyond.

Tools like Oracle Forms and Reports had a lot of problems with modern software development practices. For one thing, the "source" files weren't actually text files. They were mostly binary format files with some PL/SQL interspersed, and could only be opened in the proprietary IDE that only Oracle provided.

Binary formats meant that while they could reap some of the benefits of source control (namely version history and such), actually figuring out the differences between revisions involved opening up both versions in the IDE and comparing each item/script/setting in the two files. Doing things like global find and replace were also a pain in the ass, especially in systems that had hundreds of forms. It was so bad I remember spending some time trying to reverse engineer the binary format so that I could attempt to make some of this work easier. No dice.

Another issue was that Oracle's IDEs were notoriously buggy. Their Reports IDE in particular often had me incensed. If you dragged the wrong thing to the other wrong thing, you would crash the IDE entirely. In fact, we had a list of things to avoid doing that would crash the entire IDE entirely. The built-in text editors were so bad, I often had a entirely separate text editor open in a separate window so I could copy-paste PL/SQL code there for any complicated edits. (Back then we were for some reason fond of [Crimson Editor][1] although it wasn't as full-featured as [UltraEdit][2] or as reliable with updates as [Notepad++][3]) This was actually also sometimes a problem as some versions of the Reports IDE also had a crash on paste.

Most of my first two years of work involved maintenance of Oracle Forms-based systems (with some Delphi work thrown in occasionally). I didn't get an introduction to web development until late into the second year of my career. I was so impressed with web development I made a mock-up of one of the really complicated screens from one of our Oracle Forms projects and it seemed so pretty. I secretly hoped we could convince our clients to port them over to a web application. (1) No dice again; and (2) I probably would have regretted such a thing.

I know I would have regretted it because some number of years later, we got a project to migrate an existing client-server system to a web application. The original application was written in Powerbuilder. I figured it was a fairly straightforward reverse-engineer and implement as a webapp, but nooooo. One of the higher-ups decided that to save on costs, we should look into attempting to automate the porting process somehow. We were to write translation software that would take the Powerbuilder source and convert it into the appropriate web application screens.

This was ridiculous for a good number of reasons, but as a tech lead, I had to look into it and had to prove it was in fact not viable (Spoiler alert: it was not). The first concern was that Powerbuilder also had a binary format. This was solved when I found that someone had already written a tool to export Powerbuilder binaries into some kind of text format. It was a bit crude, but it was a way forward.

The second concern is that client-server form behaviors do not map well to web applications. My favorite example of this is editable grids. These are some kind of excel-like grids that were commonplace in client-side systems. And when users upgrade their legacy systems to web apps, they inevitably expect that their editable grids should work the exact same way on the web as they did on the client-side forms.

Back then Javascript-backed editable grids were still in their infancy, and each one we tried had their own sets of problems and limitations which would lead to some number of client complaints. Some clients even wanted editable grids that could accept copy-pastes from excel! Yeah, we had to develop Google Sheets! I personally had to roll my own editable grid framework from scratch at least once too. I ranted so often against client's editable grid requirements that a few developers often quoted something I said in one of our internal chat rooms:

> <jaeger> you say "editable grid" i hear "problems"

Anyway yeah, porting client-side behavior to a web framework would not have been straightforward. At least not to the way our internal web development framework liked to do things. In order to have any kind of reasonable mapping, I would have needed to build some kind of Javascript rich-client framework (or see which ones of the emerging ones we could use). That also meant rewriting a lot of the backend code to support a bunch of new operations. It was a lot more work than the expected output of "a series of steps to easily or automatically migrate PowerBuilder source code to web applications."

When I raised that the idea was not viable, I was asked to give a more detailed explanation. This involved taking one of the more complex Powerbuilder source files, putting it into an Excel, and line-by-line explaining how and why that line could or could not be translated into a web application. As an alternative option to an automated porting program they wanted a guide or process so simple that even junior developers with minimal experience could follow the guide and port the programs quickly. I think they eventually went with this approach. (Which was closer to our normal reverse-engineer-and-reimplement methodology.)

These days web applications are the norm and client-server programs are a thing of the past. They were relics of a different age. The browser is our universal client now, on the desktop at least. On mobile, "apps" are effectively client-server programs, though they have a different set of advantages and limitations. Maybe in the future mobile apps will converge as well, into a unified browser client -- although probably mobile browsers need to be more feature-rich before this convergence can take place. My historical disdain for client-server programs carries over to mobile apps though -- I don't like to use too many of them, although that is a story for another blog post.

 [1]: http://www.crimsoneditor.com/
 [2]: http://www.ultraedit.com/
 [3]: https://notepad-plus-plus.org/