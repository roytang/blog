---
date: 2009-10-10 08:46:00
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1547415/how-to-handle-ie-select-onchange-and-ajax-requests
tags:
- javascript
- internet-explorer
- questions
- stackoverflow
- software development
title: how to handle IE select onchange and ajax requests
---

Let's say I attach a javascript "change" event handler to a select element, something that dispatches an ajax request to load some stuff from the server.

This is fine in Firefox. However, in IE, the change event will fire every time you scroll rapidly through the combo box options using a mouse wheel. This is troublesome because it spams the server with requests, and there's no guarantee the requests come back in the correct order, hence the client-side state may become inconsistent.

Now, our previous workaround was that we would introduce a timeout to the change handler, such that it would wait a fraction of a second before actually dispatching the request. If in that short time, another change event comes in, we cancel the previous timeout and start a new one, thus preventing spamming multiple requests.

Now, while this seems to be working, it's a bit hackish and I'm wondering if there's any better approach. Is there a different event we can hook to so that it doesn't fire repeatedly when scrolling with the mouse? Or should we just disable mouse-wheeling altogether (onmousewheel="return false;")? Firefox does not seem to support mouse-wheeling thru combo boxes, but I'm not sure if disabling mouse wheeling is a serious usability no-no or something.

Can anyone recommend other solutions?