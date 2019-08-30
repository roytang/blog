---
author: roy
categories: []
date: 2016-06-16 01:30:02
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/743255093370290176/
tags:
- Software Development
- Tech Life
title: Password Security for Application Developers
type: post
url: /2016/06/password-security-for-application-developers/
---

In the modern era of online services and applications, it is getting more and more common to hear of databases and systems being hacked and user data being exposed. The most dangerous of this data is the user's password since it may allow access not only to your own service but to other services as well. As an application developer, the below is probably the bare minimum you need to know when handling user passwords:

* * *

**Never store passwords in plain text!** This is the most important rule. It means that if your database is ever compromised, the password information will not be exposed

This is true even if your application doesn't contain sensitive data or would not otherwise cause any problems if compromised. This is because many users will tend to re-use the same password across different services (although they really shouldn't!)

**Use a strong one-way cryptographic hash function to store the passwords.** One-way hashes can still be brute-forced, but the idea is that the computational effort to do so will be so large to make it not worth the effort. The most commonly used/recommended algorithms are [bcrypt and PBKDF2][1]. One of these should suffice, but take note to check every few years or so if better cryptographic hash algorithms emerge; as technology and hardware evolves and computational power increases, at some point in the future stronger algorithms may be needed (it might take a while though, bcrypt has been good since 1999)

Cryptographic hash functions are designed to be collision-resistant, meaning the result of the hash function will almost certainly be unique. When the user submits a password for authentication, you simply hash it using the same method and compare the hash against the one stored in the database

**Use a unique salt per password before hashing. **Salting means that you don't hash the password by itself, you instead combine it with another string before hashing. Not only does this increase the length and complexity of the hashed string, but reduces vulnerability to so-called [dictionary attacks][2] and [rainbow table attacks][3]. The salt should be different for each user, probably some combination of personal data like the username and a key like the user id stored in your system

**Never send passwords in plain text either. **You may be tempted to send out an email with the password in plain text on a password reset request. The common practice now is to just generate and send a unique user-specific link to allow the user to set his own password manually

* * *

**Force good password practices on your users**. This means requiring sufficiently strong passwords. Many modern services provide quick feedback on how strong the input password is. Optionally you can also require that the password contains a varied amount of lower case letters, upper case letters, numbers, and other special characters, but this is not really necessary if the passwords are of sufficient length. Also consider requiring users to change their passwords after a set period

**You should disallow the most common passwords.** A list of the most commonly used passwords (such as "password" and "123456") are available from previously leaked password hacks. Microsoft has recently started to roll out this sort of check now in their services. Actually, one good idea I've heard of before is to have a uniqueness check on the password field -- disallow users from having the same password as any other user, but this may not be feasible depending on how you hash the passwords

* * *

If your application has a large number of users or is especially critical (anything involving money transactions is a good candidate), you should also consider implementing some sort of **two-factor authentication**. Most common implementations these days use email, SMS or a mobile application as the second factor

* * *

These practices won't prevent your application from being hacked. In truth, probably nothing can really prevent hacks 100% especially against determined hackers. These are simply mitigation practices you need to be aware of as the application developer to protect your users in case your application does get hacked. Other methods of securing your system may be the responsibility of other roles such as system administrators/engineers or dev ops

 [1]: http://security.stackexchange.com/questions/4781/do-any-security-experts-recommend-bcrypt-for-password-storage/6415#6415
 [2]: https://en.wikipedia.org/wiki/Dictionary_attack
 [3]: https://en.wikipedia.org/wiki/Rainbow_table