---
title: My history in text editors
author: roy
type: post
date: 2018-11-10T05:07:22+00:00
url: /2018/11/my-history-in-text-editors/
categories:
  - Tech Life
  - Software Development

---
Text editors (and by extension IDEs) are a programmer&#8217;s best friend. I thought I&#8217;d look back at a number of text editors I&#8217;ve used over the years. (I grew up with Windows, so I won&#8217;t list vim/emacs/nano here, even though I&#8217;m at least a bit proficient with vim by now. That is, I know how to exit vim.)

  1. Notepad &#8211; of course, the default editor in Windows. The one we turn to when all else fails. It used to be pretty bad at handling UTF-8 and probably just gives up on large files, but for quick and dirty work, it&#8217;s sufficient.  
    
  2. [Crimson Editor][1] &#8211; relatively useful. First editor I used with multiple tab support and find in files. The first team lead I worked with (who I affectionately call "boss&#8221; to this day), recommended this to me mostly because she thought the dog icon was cute.
  3. [UltraEdit][2] &#8211; a very powerful editor, lots of features. We mostly used it back then for the superior UTF-8 handling and for the ability to open very large files. However, it has one glaring flaw that prevented me from using it too much: It&#8217;s not free.
  4. [Notepad++][3] &#8211; I think this had roughly the same if not slightly larger feature set as Crimson Editor. But it was well-maintained and received regular updates, even up til now. (The latest update was a few weeks ago.)
  5. [Eclipse][4] &#8211; ok, I&#8217;ll include IDEs in this list. Most of my early career was in Java web development, and our IDE of choice was Eclipse. Slow-as-hell, always-compiling, unforgiving Eclipse. It had a rich features set, but again, hella slow, even among Java IDEs. Still, I spent enough hours with it to become fairly proficient with it and I even published a few internal blog posts on the most useful shortcuts and how to get the most out of the IDE.  
    
  6. Visual Studio .NET &#8211; I actually had experience with the older Visual Studio versions, since we had a few legacy VC++ programs we had to maintain, but that was minimal at best so I don&#8217;t have much familiarity there. But then we had a C# project and I used VS.NET for a while. I didn&#8217;t care much for the C# language, but I did enjoy that VS.NET was way faster than Eclipse and especially enjoyed how good the Intellisense feature was.
  7. [Atom][5] &#8211; when I left my long-time job and started considering other directions to take my career, I considered using Atom because it was open source and I had long wanted to get into open source, and I figured what better way to get involved than to help improve your own tools right? Sadly, while I liked Atom&#8217;s feature set, I was turned off by its incredibly poor performance and loading times.
  8. [Sublime Text][6] &#8211; Sublime is so good. Extensive feature set, good performance. Only downside is that it&#8217;s not free, although it was so good I considered actually paying for version 3 at one point. Luckily I didn&#8217;t before deciding to try out my current text editor of choice:
  9. [VS Code][7] &#8211; VS Code is great. It&#8217;s free and it&#8217;s open source and it&#8217;s cross-platform. It has a good feature set. It&#8217;s super extendable and it has a vibrant extensions ecosystem. It performs reasonably well. I&#8217;d say not as fast as Sublime on startup, but way more tolerable than Atom. Once it&#8217;s loaded it&#8217;s blazing fast. It also inherited my favorite feature from VS.NET, Intellisense! Microsoft did a good job with this one. And I was able to have my [first pull request for VS code][8] merged into the codebase a few weeks ago! (I can now officially claim to be an open source contributor? Lol) I&#8217;ve only been using VS Code for a short while (less than half a year) so I&#8217;m sure I have yet to tap into its full potential, but I feel it&#8217;s deep enough that it will greatly improve my workflows as I gain more mastery over it.

 [1]: http://www.crimsoneditor.com/
 [2]: https://www.ultraedit.com/
 [3]: https://notepad-plus-plus.org/
 [4]: https://www.eclipse.org/
 [5]: https://atom.io/
 [6]: https://www.sublimetext.com/
 [7]: https://code.visualstudio.com/
 [8]: https://github.com/Microsoft/vscode/pull/61206