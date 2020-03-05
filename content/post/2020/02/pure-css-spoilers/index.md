---
title: "Pure CSS Spoilers"
date: 2020-03-05
tags:
- software development
- css
---

I previously had some post that had some [content hidden via spoiler tags](/2018/10/october-2018-watching-lately), using a custom Hugo shortcode. Since I'm an [old-school developer](/2020/02/old-web/) I was previously doing this using some Javascript run on load:

{{% highlight javascript %}}
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
{{% / highlight %}}

This is the modern age however. We should really be trying to minimize our Javascript on the non-app public web as much as possible, so I decided to change it to a Pure CSS solution. Here's a quick demo:

{{% spoiler %}}This is hidden text!{{% /spoiler %}}

The Pure CSS solution uses the following HTML (including Hugo shortcode macros, should be easy to understand; .Inner is the actual spoiler content.):

{{% highlight html %}}
<div class="spoiler_container">
    <a class="spoiler_link" href="#spoiler-{{ $id }}">(Spoilers)</a> 
    <a class="spoiler_target" id="spoiler-{{ $id }}"></a>
    <div class="spoiler">{{ .Inner }} <a href="#" class="hide_spoiler">Hide Spoilers</a></div>    
</div>
<p />
{{% / highlight %}}

The CSS for this toggle is:

{{% highlight css %}}
.spoiler {
    display: none;
}
.spoiler_target:target {
    position: fixed;
}
.spoiler_target:target + .spoiler {
    display: inline;
}
{{% / highlight %}}

Basically, this takes advantage of the `:target` CSS pseudo-selector. The "(Spoiler)" anchor changes the URL hash to point to the id of the `spoiler_target` element, and we use the CSS `+` operator to display the actual spoiler content when the `:target` pseudo-selector is activated. I originally tried it with the id being assigned directly to the spoiler content, but this had the problem of "jumping around", i.e. clicking the "(Spoiler)" link would scroll the page to the anchor location. The workaround for this was separating the target anchor from the spoiler content, making the anchor hidden (no text) and adding `position:fixed` (to prevent the scrolling). The "Hide" link simply sets the URL hash location back to "#".