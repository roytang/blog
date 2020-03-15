---
date: 2020-03-09
dontinlinephotos: true
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/103826055094956762
- type: twitter
  url: https://twitter.com/roytang/statuses/1239101838978191368/
tags:
- philippines
title: How to Make Voluntary SSS Payments
---

Since I stopped being a full-time employee at the end of 2015, I've missed around four years of monthly SSS payments. This isn't really that big a deal, since I've already paid more than 10 years of premiums, I'm already guaranteed to get a pension from SSS when I reach retirement age. However, this past January I decided to resume making SSS premium payments on a voluntary basis. I had to research a bit and ask some friends about the whole process, so I thought I'd document it here both for my own recollection and in case someone finds it useful.

The SSS pension isn't a lot, which is why I've never really prioritized making the payments, but making voluntary payments will slightly increase the actual pension I can get from SSS in my old age. The computation for SSS pension amounts is outside the scope of this post (it's [easy to search for](https://duckduckgo.com/?t=ffab&q=sss+pension+computation)) but AFAIK each additional year of payments I make (with the maximum contribution amount) will increase my monthly pension by around 320 pesos, and this is the maximum possible bracket. A pitiful amount really; whether it's worth it or not depends on how long you intend to live past retirement age. By my computation if you live around 8 years past retirement age, you come out ahead.

**First step: Create an account**. If you want to transition from monthly payments made by your employer to voluntary payments, the first thing you need is an account on the [SSS online website](https://www.sss.gov.ph/). There are several methods to register an account, but all of them will require your SSS No. plus a secondary set of information to verify your identity. 

The secondary info can be something a mobile number or savings account number already registered with SSS, or a Payment Reference Number (PRN) previously used (more on PRNs later). If you're like me and you've had zero interactions with SSS in the past, the easiest way is to get the SSS Employer number for your last employer. (If you don't have a previous employer, I suspect you have to go to the SSS office and ask for advice there.) Hopefully you haven't burned your bridges and can just ask them for this information.

{{< img src="sss-registration.png" alt="SSS Registration Options" >}}

Ok, so I signed up by providing this information, so now I have an account. 

**Next step: Generate a PRN.** A PRN is a Payment Reference Number, basically a record of the payment you want to make. after you log in to the SSS web application, click the "Payment Reference Number (PRN)" tab and click "Generate PRN". You get the following form:

{{< img src="sss-2.png" alt="SSS Generate PRN Form" >}}

Input the following fields:

- Membership Type: Voluntary. By fulfilling this payment for the first time, your membership type will be changed to "Voluntary"
- Applicable Period: You can choose to pay for 1 month at a time or multiple months. I haven't tried paying for multiple months yet, IDK if there is a limit as to how far in advance you can pay.
- Contribution: When your SSS premiums are paid automatically by your employer, the actual contribution amount is determined by your salary. But the highest bracket is for salaries of only P16,000 or more a month, so chances are you were in the highest bracket already if you were in IT. This corresponds to the highest possible contribution amount of P2400 per month. You can choose to pay less if you want.
- Total Amount: This will be computed automatically when you click "Submit Request"

After you submit the request, your PRN will be generated in the succeeding page:

{{< img src="sss-3.png" alt="SSS Generated PRN" >}}

My own PRN is redacted in the screenshot for privacy reasons, but it's a string of two letters followed by twelve numbers. A payment due date is also provided. I'm not sure how this is determined, I think it's the end of the month after the current quarter? No idea really. You can also go back to the PRN list or click the PRN tab again to view the list of your outstanding PRNs.

**Next: How to actually pay the premium?** You can actually do it online directly from the PRN list, there will be a "PAY" button. This is currently through a service called ["Moneygment"](https://moneygment.ph/), but I've never tried it myself so I have no feedback other than that is a terrible name for an app. 

The SSS website also [claims that it is possible to pay via BancNet or Unionbank](https://www.sss.gov.ph/sss/appmanager/pages.jsp?page=eservices). When I checked the Unionbank web application, there was no option to pay to SSS as a biller, so I guess that's out. BancNet Online is only available to [accounts in certain banks](https://www.bancnetonline.com/BancnetWeb/view/goToUserPreRegistrationPage.do), none of which apply to me, so I can't do that either.

Instead, what I've tried is I go and make a payment at the nearest Bayad Center. Yes, I need to go out and interact with people like this was the 1990s.

Anyway, you go to the Bayad Center and you ask for a form for SSS member contribution. You fill up the form, including the PRN number you want to pay, and make the payment. It's relatively painless, aside from the having to go to the Bayad Center in the first place. 

About a week after making the payment, I suggested logging in to the SSS website again and checking your account details to see if the payment was recognized, just to make sure everything went fine. IDK how it could go wrong, but this is the government, so better safe than sorry!

Note: I was using the old SSS webapp for this (and the screenshots above). They also have a publicly-accessible beta of their [new member portal](https://portal.sss.gov.ph/member/). It uses the same account as the old webapp, and it looks *slightly* less dated. However, I could not find a screen in the beta member portal for generating the PRNs, so you might be stuck using the old webapp.