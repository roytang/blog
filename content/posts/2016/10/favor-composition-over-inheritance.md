---
title: Favor Composition Over Inheritance
author: roy
type: post
date: 2016-10-20T01:30:10+00:00
url: /2016/10/favor-composition-over-inheritance/
categories:
  - Software Development

---
&#8220;[Composition over inheritance][1]&#8221; is an object-oriented programming principle that I&#8217;m sad to say many devs I&#8217;ve encountered aren&#8217;t too familiar with. Composition provides greater flexibility, modularity, and extensibility in large software systems as compared to inheritance, especially for statically typed languages like Java that don&#8217;t support multiple inheritance

The most common examples of the problems caused by too much inheritance involved generic object such as the game objects example in the wikipedia page linked above. I want to cite a more enterprise-y example I&#8217;ve encountered in past projects

Let&#8217;s say in your system, you have a base class &#8220;ScreenController&#8221;, which contains all the common behaviors for screens in your system. Behaviors could include startup behaviors, variables the screen needs to track, how to handle the actions when the user clicks buttons, that sort of thing. Then each dev working on a different screen in your system will just extend this base class for their own screen, and you have a type hierarchy that looks something like this:

[<img class="aligncenter size-full wp-image-1506" src="http://roytang.net/wp-content/uploads/2016/10/fcoi1.png" alt="fcoi1" width="188" height="118" />][2]

Alright, that&#8217;s fine, a perfectly acceptable use of inheritance. But then as your system grows larger, you notice some of the screens share some other behaviors could be refactored so that they aren&#8217;t repeated. For example, some of the screens might be Search screens that have similar behavior. Or maintenance (CRUD) screens that share common action handlers. Using inheritance, you might extend ScreenController and add additional hierarchy levels to handle those common behaviors, and you end up with something like:

[<img class="aligncenter size-full wp-image-1507" src="http://roytang.net/wp-content/uploads/2016/10/fcoi2.png" alt="fcoi2" width="234" height="214" />][3]

Okay, it&#8217;s a bit more complicated now, but it&#8217;s probably still manageable right? But then one of the devs realizes that your project needs some modal screens too, which have some additional behavior as well. An example would be a modal screen that allows the user to select some parameters (a &#8220;selection screen&#8221;). Some modal screens also need to be search screens or maintenance screens too. If you insist on using inheritance, you need to mix and match all the possible combinations and might start seeing a hierarchy similar to:

[<img class="aligncenter size-full wp-image-1508" src="http://roytang.net/wp-content/uploads/2016/10/fcoi3.png" alt="fcoi3" width="269" height="391" srcset="https://roytang.net/wp-content/uploads/2016/10/fcoi3.png 269w, https://roytang.net/wp-content/uploads/2016/10/fcoi3-206x300.png 206w" sizes="(max-width: 269px) 100vw, 269px" />][4]

Okay, things are starting to get really unwieldy now, but hopefully there aren&#8217;t any further complications right? Then your team starts to implement multiple subsystems with different domains, and some of the different domains have common behavior that they want to have in base classes too. So for example, the finance domain wants to have a FinanceScreen parent class they can use. But what about the existing hierarchy above? Should you duplicate it for each domain and up with ridiculous things like FinanceModalSearchScreen? I&#8217;m not even going to bother making an example of such a type hierarchy!

Now, you look at this mess and wonder how could it have been done better? Well, (as if the spoilers in the post title didn&#8217;t make this obvious), one alternative would have been to use composition. Composition means creating objects to encapsulate behavior and attaching them to other objects as necessary.

In our example, if you still had the flat hierarchy from the start, you could have a base ScreenBehavior class, and the ScreenController could have an addBehavior() method. Your class hierarchy would end up similar to:

[<img class="aligncenter size-full wp-image-1510" src="http://roytang.net/wp-content/uploads/2016/10/fcoi4.png" alt="fcoi4" width="465" height="201" srcset="https://roytang.net/wp-content/uploads/2016/10/fcoi4.png 465w, https://roytang.net/wp-content/uploads/2016/10/fcoi4-300x130.png 300w" sizes="(max-width: 465px) 100vw, 465px" />][5]

And each screen will just have to add the specific behaviors it needs like so:

    
    public ScreenA() {
    		addBehavior(new SearchScreenBehavior());
    		addBehavior(new ModalScreenBehavior());
    		addBehavior(new FinanceScreenBehavior());
    	}
    

This setup is a lot more flexible and easily extensible, since you don&#8217;t have to uproot entire type hierarchies when some new common behavior needs to be added. Such robust design is especially important for larger projects and systems that may have hundreds of screens. The only downside is that you have to implement support for this approach early in the project &#8211; the longer you wait, the more complicated it becomes to adjust the existing code to the new paradigm. Definitely something to consider if you&#8217;re a technical lead on a large project just starting out

&nbsp;

&nbsp;

 [1]: https://en.wikipedia.org/wiki/Composition_over_inheritance
 [2]: http://roytang.net/wp-content/uploads/2016/10/fcoi1.png
 [3]: http://roytang.net/wp-content/uploads/2016/10/fcoi2.png
 [4]: http://roytang.net/wp-content/uploads/2016/10/fcoi3.png
 [5]: http://roytang.net/wp-content/uploads/2016/10/fcoi4.png