---
date: 2009-07-14 04:23:32
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1123415/styling-a-disabled-combobox-in-internet-explorer
tags:
- html
- css
- internet-explorer
- questions
- stackoverflow
- software development
title: styling a disabled combobox in internet explorer
---

Say I had the following:

    <select disabled="disabled" style="border: 1px red solid; color: black;">
    <option>ABC</option>
    </select>

Firefox renders the above with a red border and black text as I expect; but IE does not, it seems to be using native colors for the border and the disabled text. Is there any way for me to be able to style it?

For edit boxes my workaround was to use readOnly instead of disabled so that I can style it, but it seems for combo boxes the readOnly attribute has no effect.

Note: I only need this to work in IE (it's for an intranet webapp where users must use IE), so IE-specific solutions are fine.