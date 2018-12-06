---
categories:
- Software Development
date: 2008-08-25 06:07:50
title: Poorly Implemented Combo Box
type: post
url: /2008/08/poorly-implemented-combo-box/
---

I was registering for an account at a local auction site (which shall remain nameless), the zip code combo box threw me off:

[<img class="alignnone size-medium wp-image-536" title="badcombo" src="/files/uploads/2008/08/badcombo-300x180.jpg" alt="" width="300" height="180" />][1]

 [1]: /files/uploads/2008/08/badcombo.jpg

## Comments

### Comment by Bry on 2008-08-26 00:55:11 +0000
It's actually displaying the ZIP codes of locations in Quezon City in
  
alphabetical order. I think the dev forgot to put the location name somewhere
  
there e.g.

Alicia (1105)

Amihan (1102)

Apolonio Samson (1106)

and so on... 

I'm still wondering how 801 got there, though.

### Comment by [Roy](http://roytang.net/blog) on 2008-08-26 07:52:22 +0000
Bakit alam mo ung alphabetical list of Quezon City locations :p

### Comment by Bry on 2008-08-27 01:15:59 +0000
Googled "manila zip codes". First hit has ZIP codes per municipality, arranged
  
by location alphabetically.

Wala lang...  nakakabobo kasi pag-draft ng prototypes. Tinopak ako last week at
  
linagay ko lahat ng country + country code sa mga country code dropdown list
  
ng screens ko instead of just putting 5-10 country codes. Kaya yun, familiar
  
yung pattern sa combo box sa pic sa taas.