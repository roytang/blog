---
author: roy
categories:
- Software Development
date: 2016-09-29 01:30:42
title: Type Interfaces Matter
type: post
url: /2016/09/type-interfaces-matter/
---

&#8230;especially for strongly-typed languages.

In one of the bigger Java projects that I took over, I was often annoyed to find some devs had written method signatures like

> public void doTheThing(HashMap<K, V> params)

Which is silly &#8211; not because of the naming, that&'s obviously not a real-world function name. The silly part is requiring a particular implementation (HashMap) instead of the generic interface (Map). It unnecessarily restricts your API and makes it less flexible. Unless your function specifically cares about the hashing part, there&'s no reason the parameter isn&'t a Map instead

Since most Java libraries will perform proper encapsulation and give you a generic Map type, it adds some mismatch when you have to plug one of those types into your function; one would need to instantiate a new HashMap and copy the contents of the generic Map into it so that your function accepts it

**Use the generic interface as much as possible! Use the specific implementation type only when instantiating!**