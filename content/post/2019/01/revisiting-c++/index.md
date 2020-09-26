---
author: roy
categories: []
date: 2019-01-05 05:58:22
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1081599258204213249/
tags:
- c++
- Software Development
title: Revisiting C++ after a decade
---

This year I had the dubious privilege of having to work with a C++ project again. Although my college education was in C, that was a completely different animal. I did self-study C++ for a bit back even before I was working, mostly because I was interested in game development even back then. I remember trying some OpenGL and/or DirectX stuff back with good old Borland Turbo-C++ during the DOS days and using the [Dev-C++ IDE][1] when I shifted to Windows. Professionally, I think there was at least one project where I had to work on a Windows-based application using C++ on Visual Studio 6 (before all this .NET nonsense), but for the life of me I can't even remember which project it was anymore. I do remember struggling more with the compiler and the IDE and the layouting of Windows components more than the language itself. And even then, I mostly used the language as an extension of C and not really taking advantage of the more advanced features.

Although I knew about the language features in theory, I didn't have much experience back then with using features like templates, generic types, or the STL. That was remedied this year when we had a project that required us to adapt an existing open source C++ project and modify it for our needs. This was a full blown project, somewhere in the neighborhood of 175 kloc, and it involved complex stuff like cryptography, encryption, signing, networking, and so on. I didn't even know about the Boost library back then. A huge challenge for me at that time, given my little to no C++ experience. Luckily it was a service process that we planned to compile and deploy on Linux, so at least we didn't need to worry about Windows and UI shenanigans.

One of our senior developers (who was not available full-time for the project) *did* have C++ experience though, and he used to train new hires in C++ at his old company. So he dug out some of his old training slides and gave us a C++ refresher/crash course in the span of an afternoon. A bit too much info crammed into too little time, but still informative. Especially for me, since it's been so long since I touched the language, the slides reminded me of a few things I had already forgotten.

{{< note "2018/08/1035019095287189504/" >}}

Some notes:

- having worked almost exclusively with dynamic languages the past few years, I haven't had the chance of use the [old XKCD "compiling" excuse][2] in a while. When we first tried compiling the project, we were seeing build times in the 10-15 minutes range, which was worrying for our coding cycles. And since we were "relearning" C++, as it were, we were bound to have more iterations than normal. Luckily we found that the build process tended to be a bit faster on succeeding builds, I guess it does some kind of incremental build? Later on, compiling would take around 2-3 minutes.
- makefiles are something I've never had to deal with before (that sort of thing used to be handled by an IDE during my last go-around with C++). But I had to figure them out early on in this project, otherwise we couldn't add our own new files to the codebase!
- I still don't fully understand linking, but we eventually figured out where to correctly place our files so that we wouldn't have any referential errors during linking. (Figuring this out also sped up the build process a bit.)
- As I mentioned, I didn't have much experience with C++ features like templates and generic types, so one of the challenges we faced early on was making heads or tails of the usage of this third party library called [JSON Spirit][3], which was used for representing JSON objects. The library uses a lot of generics and templates and typedefs, so it took a bunch of code tracing and a bit of trial and error for us to get the hang of it.
- one thing we discovered early on was that the use of deeply-nested templates and generic types led to a lot of quite obtuse error messages, a bit of a challenge for us who didn't have much C++ experience. This problem is succinctly described in the following tweet:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">In C++ we don&#39;t say &quot;Missing asterisk&quot; we say &quot;error C2664: &#39;void std::vector&lt;block,std::allocator&lt;_Ty&gt;&gt;::push_back(const block &amp;)&#39;: cannot convert argument 1 from &#39;std::_Vector_iterator&lt;std::_Vector_val&lt;std::_Simple_types&lt;block&gt;&gt;&gt;&#39; to &#39;block &amp;&amp;&#39;&quot; and i think that&#39;s beautiful</p>&mdash; mcc (@mcclure111) <a href="https://twitter.com/mcclure111/status/1002648636516282368?ref_src=twsrc%5Etfw">June 1, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

So there were a lot of challenges along the way, but this is fairly typical for developers coming into a project with an existing large codebase. And on the upside (my usual upside), I learned a lot, and I felt like a C++ genius a few weeks in. When you climb a learning curve quickly, it can make you feel amazing:

![HOHOHO I DID IT][4]

In the end I think we did pull it off and were able to implement and integrate the needed changes well, without any major issues. Given C's challenges with memory management and so on, I was kind of expecting we would encounter things like crashes, memory leaks, and such, but it turns out using the STL and Boost largely alleviates that problem. The project is still ongoing and has a bunch of requirements-related issues, but I think the C++ side turned out relatively well. Unfortunately, I don't think I'll have much use for C++ knowledge outside of this project, the language isn't really appropriate for the sort of personal projects I like to take on. 


[1]: https://www.bloodshed.net/dev/devcpp.html
[2]: https://xkcd.com/303/
[3]: https://www.codeproject.com/Articles/20027/JSON-Spirit-A-C-JSON-Parser-Generator-Implemented
[4]: /uploads/hohohoidiit.jpg