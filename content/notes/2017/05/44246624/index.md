---
date: 2017-05-29 16:07:16
reply_to:
  label: '''Extending a long-lived (60 day) user access token'' on stackoverflow'
  name: James Walker
  type: stackexchange
  url: https://stackoverflow.com/questions/39882930/extending-a-long-lived-60-day-user-access-token
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/39882930/extending-a-long-lived-60-day-user-access-token/44246624#44246624
tags:
- facebook-graph-api
- facebook-login
---

From https://developers.facebook.com/docs/facebook-login/access-tokens/expiration-and-extension:

> Refreshing Long-Lived Tokens

> Even the long-lived access token will eventually expire. At any point, you can generate a new long-lived token by sending the person back to the login flow used by your web app - note that the person will not actually need to login again, they have already authorized your app, so they will immediately redirect back to your app from the login flow with a refreshed token - how this appears to the person will vary based on the type of login flow that you are using, for example if you are using the JavaScript SDK, this will take place in the background, if you are using a server-side flow, the browser will quickly redirect to the Login Dialog and then automatically and immediately back to your app again.

> After doing the above you will obtain a new short-lived token and then you need to perform the same exchange for a long-lived token as above.

So it looks like it's not possible to renew the long-lived token without getting a new short-lived one (which requires user interaction)

Auto-renewal on request is only available for native mobile apps (Android/iOS):

> Native mobile apps using Facebook's SDKs will get long-lived access tokens, good for about 60 days. These tokens will be refreshed once per day when the person using your app makes a request to Facebook's servers. If no requests are made, the token will expire after about 60 days and the person will have to go through the login flow again to get a new token.