---
title: "Test"
date: 2020-05-01T19:02:58+08:00
---

An h1 header
============

Paragraphs are separated by a blank line.

2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists
look like:

  * this one
  * that one
  * the other one

Note that --- not considering the asterisk --- the actual text
content starts at 4-columns in.

> Block quotes are
> written like so.
>
> They can span multiple paragraphs,
> if you like.

Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex., "it's all
in chapters 12--14"). Three dots ... will be converted to an ellipsis.
Unicode is supported. ☺

https://roytang.net


- item 1
- item 2
- item 3

{{% spoiler %}}

https://roytang.net


- item 1
- item 2
- item 3
{{% /spoiler %}}

The quick brown fox jumps over the lazy dog.

### Latest post by tag

{{< latest tag="mtg" >}}

### syntax highlighting

```css
.lightbox {
	display: none;
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	z-index: 999;
	width: 100vw;
	height: 100vh;
    background: rgba(0,0,0,0.8);
}
.lightbox_overlay {
    position: fixed;
    z-index: 1000;
    bottom: 0;
    width: 100%;
    background: rgba(0,0,0,0.6);
    padding-bottom: 1rem;
}
.lightbox_overlay * {
    padding: 1rem;
}
.lightbox img {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;
    max-width: 100%;
    max-height: 100%;
}
.lightbox:target {
    outline: none;
    display: block;
}
```


### Footnotes

Test [^1]

Test 2 [^2]

Test 3 [^3]

{{< cardlist >}}

{{< cardgroup title="Lands" >}}
2 Crumbling Necropolis
9 Plains
1 Mountain
5 Forest
{{< /cardgroup >}}

{{< /cardlist >}}

{{< cardlist >}}

{{< cardgroup title="Lands" >}}
{{< /cardgroup >}}

{{< cardgroup title="Creatures" >}}
{{< /cardgroup >}}

{{< cardgroup title="Spells" >}}
{{< /cardgroup >}}

{{< cardgroup title="Sideboard" >}}
{{< /cardgroup >}}

{{< /cardlist >}}

{{< cardlist >}}

{{< cardgroup title="White" >}}
{{< /cardgroup >}}

{{< cardgroup title="Blue" >}}
{{< /cardgroup >}}

{{< cardgroup title="Black" >}}
{{< /cardgroup >}}

{{< cardgroup title="Red" >}}
{{< /cardgroup >}}

{{< cardgroup title="Green" >}}
{{< /cardgroup >}}

{{< cardgroup title="Others" >}}
{{< /cardgroup >}}

{{< /cardlist >}}

### Webmention Tests

https://webmention.rocks/test/1
https://webmention.rocks/test/2
https://webmention.rocks/test/3
https://webmention.rocks/test/4
https://webmention.rocks/test/5
https://webmention.rocks/test/6
https://webmention.rocks/test/7
https://webmention.rocks/test/8
https://webmention.rocks/test/9
https://webmention.rocks/test/10
https://webmention.rocks/test/11
https://webmention.rocks/test/12
https://webmention.rocks/test/13
https://webmention.rocks/test/14
https://webmention.rocks/test/15
https://webmention.rocks/test/16
https://webmention.rocks/test/17
https://webmention.rocks/test/18
https://webmention.rocks/test/19
https://webmention.rocks/test/20        
https://webmention.rocks/test/21
https://webmention.rocks/test/22
https://webmention.rocks/test/23/page


[^1]: A footnote
[^2]: Second footnote
[^3]: Third footnote
