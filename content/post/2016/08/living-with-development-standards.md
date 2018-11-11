---
author: roy
categories:
- Software Development
date: 2016-08-11 01:30:02
title: Living With Development Standards
type: post
url: /2016/08/living-with-development-standards/
---

I was originally going to write a post about the problems development teams face as they get larger, but the section on development standards was long enough by itself so here we are.

Having some sort of development standard in a project development team becomes a lot more important as project size goes up (for obvious reasons). There are different kinds of standards to consider, but generally I break them down into design standards and coding standards. Standards are important not only to ensure consistency among the development team, but to ease transitions both for new team members coming into the project late, or team members moving laterally to other positions or sub-teams within the same project

Design standards are generally UI and functionality related. UI standards can refer to what kind of controls are preferred to be used, where screen elements are expected to be placed, how error messages are presented, that sort of thing.

Functionality standards are more to establish similar user expectations as to how the program works. When I click Save, can I continue editing the same record or does it send me back to a listing screen? When I delete a record, is it reversible or will the system warn me that the deletion is permanent? When I enter a search criteria, is it case-sensitive? Having similar behavior throughout the system makes it more intuitive for users to navigate large, complex systems.

Coding standards refer to standards that developers follow, and will typically encompass:

  * Naming conventions. Applicable to variables, files, database tables and fields, and so on. This can be difficult to enforce, as some part of it is subjective. But it's important that the same things are always named the same way in different parts of the code. It can be more difficult in larger development teams that are split among different domains. A simple example is one sub-team might name their reference number database field REF\_NO while another sub-team sues REF\_NUM. At the very least having consistent naming will make it more intuitive for developers reaching across different domains to link fields to each other
  * Speaking of database fields, another thing to consider is data types and field length. It can be unpleasant to find out later on in the development process that one sub-team has used VARCHAR(35) for all their email fields while another one has used VARCHAR(70). Or maybe some tables have a reference number field as an integer while others have it as a string. Such inconsistencies can lead to integration problems later on
  * Code formatting. Generally covers indentation, bracket placement, spacing, etc. This is generally only an aesthetic choice, but may cause religious wars with some developer groups (&#8220;tabs vs spaces!!!&#8221;), but generally someone should just choose a standard and the developers follow it. Luckily, modern IDEs support autoformatting options that can be exported and distributed for all the developers to use, eliminating most such issues. If not enforced in this manner, it may create some issues though if different developers have different autoformat settings. For example, in one project I was on a certain developer had an autoformat setting to automatically declare as final any function parameters in Java files. This was an ok practice on its own, but he was the only one with that setting, so when he would make a change to a Java file written by someone else, those &#8220;final&#8221; keywords would be added automatically. It wasn't an issue most of the time, but when I had to check changes in source control, it would often be troublesome trying to isolate what change he had made in large files since there were all these other irrelevant changes found by the diff. Enforcing a standard formatting eliminates such issues
  * File organisation &#8211; a software project will typically have hundreds if not thousands of different files of varying types. Some sort of scheme is necessary for developers to follow to ensure order. For example in a web development project, HTML templates should be placed in a specific folder, CSS files in a different folder, JavaScript files in a different folder, and so on. Often there will also be subfolders either by domain or functionality
  * Implementation standards &#8211; typically in my projects I've found a need to standardize the approach for similar types of functions. For example, all search screens should be implemented a certain way, etc. Can be enforced by either language constructs or code templates
  * Best practices &#8211; many organisations will have their own set of coding best practices designed to help avoid common problems
  * Other, program-specific standards. For example, your Java project may require that all classes of a certain type use a particular form of constructor. If you're lucky, such standards can be enforced using language constructs such as interfaces, but that is not always the case

Ideally, all of the above standards are codified in some sort of standards document that the development team can reference on a regular basis. But due to the constantly evolving nature of software projects, most teams will find that the typical documentation problems arise for standards documentation:

  1. You often won't know ahead of time all the kinds of standards you need. Often later in the project new situations will arise that need standards but either the team may not recognize it or will not have time to document
  2. Standards will often become out of date or irrelevant. Updating these documents will often not be a priority as schedule pressure mounts
  3. As the problems from 1 and 2 mount up, more and more knowledge that should be codified as standards instead become unwritten tribal wisdom that can only be learned by experience or consultation with the experts
  4. After a certain point, adding new things to the standards document becomes counter-productive. When there are too many standards to follow, it becomes a challenge to even be aware of them all much less enforce them

It is a difficult problem to solve, and probably impossible to solve completely. I believe we will have to live with all of the problems above to some degree. There are a few ways to mitigate the effects:

  * Automate whenever possible. There are now many modern tools to automate checking for code formatting issues and so on
  * Prepare standards documents/bibles for the most common cases
  * Prepare step-by-step implementation guides and code templates for commonly-done tasks/functions. (Examples: &#8220;How to implement search screens&#8221;, &#8220;How to integrate our workflow library&#8221;, etc) &#8211; guides and templates don't guarantee adherence, but they should help reduce incidents of standards not being followed
  * Mentoring for new team members or those transitioning to new roles
  * Recognize and accept that as project teams get larger, there will be a greater overhead spent on ensuring standards are followed and that the team is aware of them

All of the above are my own thoughts arising from my own project experience. I haven't read much outside literature on this subject or other approaches within the industry at large, so I'd be happy to get more information on this matter