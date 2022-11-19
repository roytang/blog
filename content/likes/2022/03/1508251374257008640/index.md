---
author:
  name: amasad
  url: https://twitter.com/amasad/
date: 2022-03-28 01:15:24
dontinlinephotos: true
like_of: https://twitter.com/amasad/status/1508251374257008640/
source: twitter
syndicated:
- type: twitter
  url: https://twitter.com/amasad/status/1508251374257008640/
- type: twitter
  url: https://twitter.com/amasad/status/1508251376123490304/
- type: twitter
  url: https://twitter.com/amasad/status/1508251377956388865/
- type: twitter
  url: https://twitter.com/amasad/status/1508251379634085896/
- type: twitter
  url: https://twitter.com/amasad/status/1508251381458608132/
- type: twitter
  url: https://twitter.com/amasad/status/1508251383195074561/
- type: twitter
  url: https://twitter.com/amasad/status/1508251385048969217/
- type: twitter
  url: https://twitter.com/amasad/status/1508251386823143424/
- type: twitter
  url: https://twitter.com/amasad/status/1508251388681195521/
- type: twitter
  url: https://twitter.com/amasad/status/1508251391374106630/
- type: twitter
  url: https://twitter.com/amasad/status/1508251393286545413/
- type: twitter
  url: https://twitter.com/amasad/status/1508251395056541697/
- type: twitter
  url: https://twitter.com/amasad/status/1508251396851699714/
- type: twitter
  url: https://twitter.com/amasad/status/1508251398667874307/
- type: twitter
  url: https://twitter.com/amasad/status/1508251400379113472/
- type: twitter
  url: https://twitter.com/amasad/status/1508251402060980225/
- type: twitter
  url: https://twitter.com/amasad/status/1508251403742982147/
- type: twitter
  url: https://twitter.com/amasad/status/1508251405420687362/
- type: twitter
  url: https://twitter.com/amasad/status/1508251407144534016/
- type: twitter
  url: https://twitter.com/amasad/status/1508251408901935110/
- type: twitter
  url: https://twitter.com/amasad/status/1508251410642587652/
- type: twitter
  url: https://twitter.com/amasad/status/1508251412420984833/
- type: twitter
  url: https://twitter.com/amasad/status/1508251414207770629/
- type: twitter
  url: https://twitter.com/amasad/status/1508251416044859392/
- type: twitter
  url: https://twitter.com/amasad/status/1508251417844150273/
- type: twitter
  url: https://twitter.com/amasad/status/1508257103764344835/
- type: twitter
  url: https://twitter.com/amasad/status/1508482175695425539/
- type: twitter
  url: https://twitter.com/amasad/status/1508489965683978240/
tags:
- amasad
- bloombergbeta
---

Going into startups, no one tells you that fighting is part of the job.



At Replit, the toughest people we have to fight are dark web hackers.



One time we went head-to-head against an underground group doing really bad things on our service -- this is the story:

<time id="1508251376123490304">[09:15]</time> It's Nov 2018. Replit is super small, 4 people at the time but usage growing superexponentially.



Because we provide free compute in the cloud we built a lot of tech to run containers cheaply.



Thanksgiving eve, I get an alert that we're spending $10k a day, up 20x  😱

<time id="1508251377956388865">[09:15]</time> All emergencies tend to happen around holidays -- is it a coincidence?



I get on my computer and find that a repl is getting forked 10s of thousands of times and sending insane amount of traffic.



I ban the user and alert the team. No Thanksgiving for us this year.

<time id="1508251379634085896">[09:15]</time> Another user comes back, does the same thing, and another and another -- we are bleeding money.



It's obviously automated. So what are they running? Look at the contents of the repl, nothing is there. What the hell?

<time id="1508251381458608132">[09:15]</time> Working under pressure is a hard-earned skill. Years of competing in extreme coding where you have to solve hard problems on the clock for 24 hours helps. Years of competing in esports. And of course incident response at startups, all trained me for this moment.

<time id="1508251383195074561">[09:15]</time> As a leader, you need to remain calm... to radiate confidence. Our team is A+ hackers, and I know we can handle this.



We strap in, teeth clinched, anxious and excited for what's to come.

<time id="1508251385048969217">[09:15]</time> The first thing we have to do is.... wait. We have to wait for the next attack so we can debug live.



Finally next attack is up, go look at the running containers.



There is a binary in there -- how do they get it in?



Anything else? No, no source code, nothing. Just the binary.

<time id="1508251386823143424">[09:15]</time> Okay, what is it sending over the network? It's all UDP and we don't have logging of UDP. Damn.



Just in time for the next attack, we have UDP logging deployed.



Looking at the logs, they get a payload from an external server. That server is maybe the "command and control."

<time id="1508251388681195521">[09:15]</time> The payload is likely the running binary we saw before. We strace and network trace it.



An IP address for an external server. Could this be the command-and-control server running the attacks?



We take the IP and match it against other access logs -- it's a match. Nice!

<time id="1508251391374106630">[09:15]</time> What is the CnC server doing?



Reconstructing from logs: it scraps our websites, creates repls and gets tokens, connects to the repls, sends them the payload.



Essentially they reverse-engineered our protocol to create thousands of repls that do... what exactly?

<time id="1508251393286545413">[09:15]</time> Okay, we obviously need to make it harder to create repls programmatically. But before we do that, let's see what we can find out from their CnC server.



In security, your instinct is to go fix things, but you have to fight that so you can know more. Leave the honeypot.

<time id="1508251395056541697">[09:15]</time> nmap scan the server, plenty of ports open, most important is an HTTP and telnet servers.



Go to the webserver, it looked like a custom server. Maybe it has some vulnerabilities?



In other words, what if we reverse the game and we go on the offense -- we HACK them instead.

<time id="1508251396851699714">[09:15]</time> After a few tries: their server is vulnerable to the oldest HTTP hack in the book: ../../



Bingo!



HTTP servers are programmed to send files from the current directory. But what if you can craft a request to request files outside the current dir -- basically anywhere?

<time id="1508251398667874307">[09:15]</time> But crawling their entire filesystem will take a lot of time -- they might know we're doing this. So the first file we try to get is the `locatedb` file which is a cached index of all the files on a host.



And BOOM it works on the first try and we get all the files on the system.

<time id="1508251400379113472">[09:15]</time> Most important two files we see:



- bot.c: the source for the binary!

- server.js: the source for this shitty server



We request those files. Look at the source. The server is so clowny, it even opens a reverse shell on telnet. We have PWNed them. Easy.

<time id="1508251402060980225">[09:15]</time> But the question remains -- what the hell are they doing?



"bot.c" gives you a hint. They use Replit's infra as a massively distributed botnet. Yes our infra is that powerful.



This is bad, not only for us but for anyone they're attacking.

<time id="1508251403742982147">[09:15]</time> This is a big financial hit on us, it destabilizes our infrastructure, makes our service go down.



But worst of all?



Our software is being used for evil, to hurt other people, we can't have that happen.

<time id="1508251405420687362">[09:15]</time> Where is the CnC host hosted? It's DigitalOcean. We report the issue to them, but it will take them days maybe weeks to investigate (eventually with our help they would report them to the authorities).



For now, though, we have to fend for ourselves. How can we stop the attacks?

<time id="1508251407144534016">[09:15]</time> It's going to be a cat and mouse game. We're going to plug holes in our system that allows the programmatically starting repls. And they're going to try to find new holes.



Now that we have all their files, maybe we can find out more about them? Maybe we can even talk to them?

<time id="1508251408901935110">[09:15]</time> Most important thing we see is references to their website -- what is it?



It's a website that sells network attacks for bitcoin.



You pay them, give them an IP address, and they use their botnets to attack it. 



And they figured out how to use us as one of their botnets. Crazy.

<time id="1508251410642587652">[09:15]</time> We find a discord server linked. Time for some social engineering: we go in as customers. Idiots, they believe us. 



While in, we start getting useful info for fighting them.



When we plug a vulnerability, we see their customers complain, and we see them try to find another.

<time id="1508251412420984833">[09:15]</time> "we willl be back in 15 minutes"



Damn they must have found another hole. We quickly go and try to spoil their attack.



This goes on for days. Little sleep or food. Just days on the computer fighting.

<time id="1508251414207770629">[09:15]</time> A month goes by then suddenly... they give up. They shut everything down and move on.



We'd built an insane amount of software to observe, find, and stop attacks in a very short period of time.



We won. We couldn't believe it.

<time id="1508251416044859392">[09:15]</time> After all, was said and done they cost us a lot of money. But if you think about it, it's like hiring a consultancy to help us secure our systems.



Not a bad outcome. Replit is 1000x more secure.

<time id="1508251417844150273">[09:15]</time> One day I will tell you about how we fought and won the crypto kiddies.



For now, if you want in on some of the actions, we are hiring security engineers. It's not as insane as this story every day but there are always new challenges:



https://replit.com/site/careers

<time id="1508257103764344835">[09:38]</time> My brother reminds me that we managed to find time to go to the [@BloombergBeta](https://twitter.com/BloombergBeta/) startup holiday party during that period. It was a moment of calm in the storm and a good way to blow off some steam. No sleep the next few nights tho 

{{% quoted url="https://twitter.com/amasad/status/1071232311184654336/" label="amasad's tweet" %}}

.@replit ♥️ [@github](https://twitter.com/github/) 

{{% /quoted %}}

{{< photos 1508257103764344835 >}}

<time id="1508482175695425539">[2022-03-29 00:32] </time> Want to hear more about Replit, our challenges, product releases, and a secret announcement? Join us for our first online conference https://hopin.com/events/repl-con-22/registration

<time id="1508489965683978240">[2022-03-29 01:03] </time> To clarify for the reading comprehension challenged: we were never pwned here. They never gained access to user data. They just abused how the service *actually* works. You give us code and we run it. Tricky business to be sure.