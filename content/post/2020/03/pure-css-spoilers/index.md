---
date: 2020-03-05
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1235416366804619265/
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/103768512364323509
tags:
- software development
- css
title: Pure CSS Spoilers
---

Edit 2020/04/17: A month and a half later, I found [a better way to do this](/2020/04/pure-html-toggles/)!

I previously had some post that had some [content hidden via spoiler tags](/2018/10/october-2018-watching-lately), using a custom Hugo shortcode. Since I'm an [old-school developer](/2020/02/old-web/) I was previously doing this using some Javascript run on load:

```javascript
    let elements = document.querySelectorAll(".spoiler_header");
    Array.prototype.forEach.call(elements, function(el, i) {
        el.addEventListener( 'click', function( event ) {
            let nextEl = el.nextElementSibling;
            let display = getComputedStyle(nextEl)['display'];
            if (display == 'none') {
                nextEl.style.display = 'block';
            } else {
                nextEl.style.display = 'none';
            }
        }, false);        
    });
```

This is the modern age however. We should really be trying to minimize our Javascript on the non-app public web as much as possible, so I decided to change it to a Pure CSS solution. Here's a quick demo:

{{% spoiler %}}This is hidden text!{{% /spoiler %}}

The Pure CSS solution uses the following HTML (including Hugo shortcode macros, should be easy to understand; .Inner is the actual spoiler content.):

```html
<div class="spoiler_container">
    <a class="spoiler_link" href="#spoiler-{{ $id }}">(Spoilers)</a> 
    <a class="spoiler_target" id="spoiler-{{ $id }}"></a>
    <div class="spoiler">{{ .Inner }} <a href="#" class="hide_spoiler">Hide Spoilers</a></div>    
</div>
<p />
```

The CSS for this toggle is:

```css
.spoiler {
    display: none;
}
.spoiler_target:target {
    position: fixed;
}
.spoiler_target:target + .spoiler {
    display: inline;
}
```

Basically, this takes advantage of the `:target` CSS pseudo-selector. The "(Spoiler)" anchor changes the URL hash to point to the id of the `spoiler_target` element, and we use the CSS `+` operator to display the actual spoiler content when the `:target` pseudo-selector is activated. I originally tried it with the id being assigned directly to the spoiler content, but this had the problem of "jumping around", i.e. clicking the "(Spoiler)" link would scroll the page to the anchor location. The workaround for this was separating the target anchor from the spoiler content, making the anchor hidden (no text) and adding `position:fixed` (to prevent the scrolling). The "Hide" link simply sets the URL hash location back to "#".