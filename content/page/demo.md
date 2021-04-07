---
title: Demo stuff
date: 2020-09-16
---

An h1 header
============

Test {{< footnote >}}A footnote{{< /footnote >}} 

Test 2 {{< footnote >}}Second footnote{{< /footnote >}} 

Test 3 {{< footnote >}}Third footnote{{< /footnote >}} 



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

Definitely, we are using Django templates but there is still one problem though. We are still hardcoding raw HTML inside our views. Creating templates for a large HTML page in this way would be very cumbersome and tedious. It would be much better if we could write the HTML in an external file. Let's do this.

```go-html-template
Latest blog posts:
{{ $pages := first 5 (where site.RegularPages "Type" "post") }}    
{{ range $pages }}
- [{{ .Title }}]({{ .Permalink }}){{ end }}

[View all posts]({{ .Permalink }}blog)
```

{{< video width="320" height="180" src="https://video.twimg.com/tweet_video/CKKiqvPXAAAaE5A.mp4" >}}

The quick brown fox jumps over the lazy dog.

{{< latest tag="movies" >}}


{{< cardlist title="Test card lists" >}}

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