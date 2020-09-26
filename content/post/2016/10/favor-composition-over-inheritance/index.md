---
author: roy
categories: []
date: 2016-10-20 01:30:10
syndicated:
- type: tumblr
  url: https://tumblr.roytang.net/post/152049049735/favor-composition-over-inheritance
- type: twitter
  url: https://twitter.com/roytang/statuses/788916969630212096/
tags:
- Software Development
title: Favor Composition Over Inheritance
type: post
url: /2016/10/favor-composition-over-inheritance/
dontinlinephotos: true
---

"[Composition over inheritance][1]" is an object-oriented programming principle that I'm sad to say many devs I've encountered aren't too familiar with. Composition provides greater flexibility, modularity, and extensibility in large software systems as compared to inheritance, especially for statically typed languages like Java that don't support multiple inheritance

The most common examples of the problems caused by too much inheritance involved generic object such as the game objects example in the wikipedia page linked above. I want to cite a more enterprise-y example I've encountered in past projects

Let's say in your system, you have a base class "ScreenController", which contains all the common behaviors for screens in your system. Behaviors could include startup behaviors, variables the screen needs to track, how to handle the actions when the user clicks buttons, that sort of thing. Then each dev working on a different screen in your system will just extend this base class for their own screen, and you have a type hierarchy that looks something like this:

{{< img src="fcoi1" >}}

Alright, that's fine, a perfectly acceptable use of inheritance. But then as your system grows larger, you notice some of the screens share some other behaviors could be refactored so that they aren't repeated. For example, some of the screens might be Search screens that have similar behavior. Or maintenance (CRUD) screens that share common action handlers. Using inheritance, you might extend ScreenController and add additional hierarchy levels to handle those common behaviors, and you end up with something like:

{{< img src="fcoi2" >}}

Okay, it's a bit more complicated now, but it's probably still manageable right? But then one of the devs realizes that your project needs some modal screens too, which have some additional behavior as well. An example would be a modal screen that allows the user to select some parameters (a "selection screen"). Some modal screens also need to be search screens or maintenance screens too. If you insist on using inheritance, you need to mix and match all the possible combinations and might start seeing a hierarchy similar to:

{{< img src="fcoi3" >}}

Okay, things are starting to get really unwieldy now, but hopefully there aren't any further complications right? Then your team starts to implement multiple subsystems with different domains, and some of the different domains have common behavior that they want to have in base classes too. So for example, the finance domain wants to have a FinanceScreen parent class they can use. But what about the existing hierarchy above? Should you duplicate it for each domain and up with ridiculous things like FinanceModalSearchScreen? I'm not even going to bother making an example of such a type hierarchy!

Now, you look at this mess and wonder how could it have been done better? Well, (as if the spoilers in the post title didn't make this obvious), one alternative would have been to use composition. Composition means creating objects to encapsulate behavior and attaching them to other objects as necessary.

In our example, if you still had the flat hierarchy from the start, you could have a base ScreenBehavior class, and the ScreenController could have an addBehavior() method. Your class hierarchy would end up similar to:

{{< img src="fcoi4" >}}

And each screen will just have to add the specific behaviors it needs like so:

```java
    public ScreenA() {
    		addBehavior(new SearchScreenBehavior());
    		addBehavior(new ModalScreenBehavior());
    		addBehavior(new FinanceScreenBehavior());
    	}
```

This setup is a lot more flexible and easily extensible, since you don't have to uproot entire type hierarchies when some new common behavior needs to be added. Such robust design is especially important for larger projects and systems that may have hundreds of screens. The only downside is that you have to implement support for this approach early in the project -- the longer you wait, the more complicated it becomes to adjust the existing code to the new paradigm. Definitely something to consider if you're a technical lead on a large project just starting out

&nbsp;

&nbsp;

 [1]: https://en.wikipedia.org/wiki/Composition_over_inheritance
 [2]: http://roytang.net/wp-content/uploads/2016/10/fcoi1.png
 [3]: http://roytang.net/wp-content/uploads/2016/10/fcoi2.png
 [4]: http://roytang.net/wp-content/uploads/2016/10/fcoi3.png
 [5]: http://roytang.net/wp-content/uploads/2016/10/fcoi4.png