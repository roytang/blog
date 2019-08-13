---
author: roy
categories: []
date: 2016-06-14 01:30:08
tags:
- Tech Life
title: Password Security for Dummies
type: post
url: /2016/06/password-security-for-dummies/
---

Around the first week of June 2016, [Mark Zuckerberg, well-known nerd and founder of Facebook, was hacked][1]. If even the founder of the world's largest social network can be hacked, anybody can! So it might be a good idea to review how you manage and secure your online passwords

&nbsp;

* * *

&nbsp;

**Avoid using short, simple, or commonly-used passwords! **These are subject to so-called "brute force" attacks where bad actors just try a whole lot of passwords until they find one that works. You don't _actually_ have to use numbers or special characters (unless the service requires you to do so). What can really hamper password attackers is password length, the longer the better, since the length of the password increases the computational time needed for a brute-force attack. For the most important services, I would suggest a password length of at least 20 characters (although some services won't allow you to have passwords this long, which deserves a glare from me). If not required to use numbers or special characters, you can simply use a pass phrase composed of multiple English words. This has the pleasant side effect of being easy to remember. As with many things, this is best illustrated by XKCD:

[<img class="alignnone" src="http://imgs.xkcd.com/comics/password_strength.png" width="740" height="601" />][2]

Take note that it's important to choose passwords or phrases that are not related to common personal information such as birthdays, names of relatives, or anniversaries. This is all information which any attacker might be able to acquire from other sources. This is how Michael Caine's character in _Now You See Me_ got hacked by the Four Horsemen!

* * *

**Avoid using the same passwords for every service!** This is one of the cardinal rules that Zuck broke causing the hack. A few years back, data from LinkedIn was accessed by hackers including passwords, and the hackers were able to use Zuck's LinkedIn password to log in to his Twitter and Pinterest accounts

You probably don't have to use unique passwords for _every _service -- I have a few "low-security" passwords that I use whenever I don't care about the account being compromised. Most common usage for me is when I need to ask a question on some programming forum (for the rare case that [StackOverflow does not suffice)][3]

You need to identify which services are critical to you -- the ones you can't afford to have compromised. Typically (for me at least), this includes financial services (online banking websites), email and social media accounts you use on a regular basis, and probably government services (I don't have any of those at the moment). For these services you should use different passwords for each one, to protect the other accounts in case one of them gets compromised

In the past few years many major services such as LinkedIn have had their password data exposed _(If the programmers were doing their job right, the hackers wouldn't have been able to decrypt the password data even if they accessed it -- but that's material for another post)_, so if you're using a lot of online service, the odds of some of your data getting hacked at some point is quite high

The problem is: most people have trouble remembering one password, how can they be expected to remember multiple passwords and match them to the corresponding service? There are a few of strategies:

  1. **Use a password manager program **such as [LastPass][4]. These programs will randomly generate and store a new password for you for each service you use. A lot of commenters online swear by this, but I'm not a fan of it because (a) I need my passwords everywhere, anywhere, any time. LastPass has an option to sync passwords across the cloud, but it requires a premium account; (b) additional steps when you need to create or store or remember a password; (c) if you lose access to the password manager, you also lose everything else
  2. **Use a procedurally-generated password for each service**. This is my preferred option. It means that for each service, you construct a password using a fixed set of rules, with the rules taking into account the service itself. A simple example would be using a base password + the service name: with a base password of "horseradish", you would use "horseradishYahoo" for Yahoo mail and "horseradishFacebook" for Facebook and so on. Of course, if your Yahoo mail account is compromised the hacker can still easily guess your Facebook password, so it needs to be more complicated than that. A better example would be: base password + your favorite Transformer whose name starts with the third letter of the service: for Yahoo it would be "horseradishHound" and for Facebook it would be "horseradishCliffjumper"
  3. **Keep a list of password hints written down**. Either on paper or on a softcopy document somewhere you can access all the time. Now obviously, if you keep a list of the passwords themselves you risk someone finding that list and accessing all your services. What I like to do is maintain a list of cryptic password hints that really only make sense to me
  4. **Memorize them! **For the most important accounts (probably the ones that allow access to other services via forgot password mechanisms), you should generate a unique password and eventually memorize them

I use some combination of #2 and #3: for most social media services I use #2 but for more critical services like online banking I use some variation of the procedural rules and maintain a list of cryptic hints that describe how I varied the rules. #2 works fine for social media accounts since I can reconstruct the passwords mentally wherever I am without need to reference a list. For online banking services, I don't use them that often but they need to be more secure so it's okay for me to have to reference a list if I forget the passwords. For my primary email accounts, I have a very strong password that I have committed to memory with no hints anywhere

* * *

Some random other tips:

  * **Change your passwords on a regular basis. **Regularly changing passwords means older passwords can't be used against you in case they are hacked. It can be as simple as changing your password when you log into a service for the first time in a new year
  * **Don't share passwords with anybody!** Well okay, maybe you can share some passwords with select family members as necessary. But basically don't give your passwords to anyone you wouldn't confess murder to. There are still scammers who pretend to be authorities in order to collect passwords and other information from you. Be wary of strangers!
  * **Don't use any browser feature that remembers the passwords for you.** I suggest typing out your passwords every time. Typing them out makes it easier for your brain to remember your passwords. But more importantly, if your machine is compromised by malware, your passwords can be accessed from the browser's data store
  * Not really password-related but you should take note anyway: **Use two-factor authentication whenever it is available**. This is where whenever you login to a service, it will also send you a secret code via another channel such as SMS or email. You then need to input that secret code in the service in order to proceed. This is so that even if your password is compromised, hackers still can't access your account. This is starting to become more and more common among the widely used services: Google, Facebook, Twitter, and Steam all provide 2FA. Modern online banking services will even **require** you to use two-factor authentication. (Sadly not all local banks do so)

* * *

Well, that post turned out longer than I expected! It might seem like overkill to have overly complicated passwords or password management schemes. If you use any online services which contain important data you can't afford to have compromised, it's a necessary evil and well worth the effort

 [1]: http://uk.businessinsider.com/mark-zuckerberg-twitter-pinterest-accounts-hacked-linkedin-hack-facebook-passwords-2016-6
 [2]: http://imgs.xkcd.com/comics/password_strength.png
 [3]: http://stackoverflow.com/
 [4]: https://lastpass.com/