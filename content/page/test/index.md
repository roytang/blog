---
title: "Test"
date: 2020-05-01T19:02:58+08:00
toc: true
submenu: "stats"
---

### HTML Elements

# H1 header
## H2 header
### H3 header
#### H4 header
##### H5 header
###### H6 header

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

A link: https://roytang.net

An external link: https://example.com


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

### Site Features

#### Syntax Highlighting

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

#### Footnotes

Test [^1]

Test 2 [^2]

Test 3 [^3]

#### Card List

{{< cardlist >}}

{{< cardgroup title="Lands" >}}
2 Crumbling Necropolis
9 Plains
1 Mountain
9 Forest
1 Swamp
{{< /cardgroup >}}

{{< cardgroup title="Creatures" >}}
4 Dark Confidant
4 Savannah Lions
4 Grizzly Bears
{{< /cardgroup >}}

{{< cardgroup title="Spells" >}}
4 Lightning Bolt
4 Giant Growth
4 Harrow
{{< /cardgroup >}}

{{< cardgroup title="Sideboard" >}}
4 Wrath of God 
{{< /cardgroup >}}

{{< /cardlist >}}

#### Images

##### Single Image

{{% photos test1 %}}

##### 2 Images

{{% photos test2 %}}

##### 3 Images

{{% photos test3 %}}

##### 4 Images

{{% photos test4 %}}

### Webmention Tests

Used to test with webmention.rocks

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
