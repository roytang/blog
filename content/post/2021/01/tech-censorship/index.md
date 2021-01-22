---
title: "Thoughts on Tech Censorship and Social Media"
date: 2021-01-22
tags:
- current events
- tech life
slug: tech-censorship
---

Discussions on tech censorship came to the forefront in recent weeks due to the aftermath of the Jan 6 capitol insurrection in the US. I've been writing down a bunch of thoughts about the complicated issue, let's see if I can hammer them into a blog post. (I also wanted to defer posting about it until after the Biden inauguration, in case more things of interest happen.) Here's where I am now:

#### Trump

Ok, so first Trump (or anyone) getting kicked off Twitter (or any service) for TOS violations (inciting violence etc). it's kind of a free speech issue, except the censorship is being done by a private entity, so it specifically doesn't violate the US first amendment. I think that without question, I agree that social media platforms have a right to pick and choose what they allow on their platforms (except those that they aren't allowed to discriminate against, by law, like race, religion, etc). And Trump absolutely violated ToS by inciting the Jan 6 riots. 

People are thinking this is a free speech issue because being deplatformed feels similar to being escorted off and banned from a public square. Of course, if you were on a public square goading people to raid govt buildings and kill elected officials, a lot of people would you want you dragged away from there anyway. That being said, I think the bigger issue is why have we these tech companies/platforms that are being treated as de facto public squares in the first place. It feels like we shouldn't have allowed them to grow to this size/amount of influence in the first place.

If you're on the fence as to whether this was a correct decision, there is [research that says misinformation dropped drastically after Twitter kicked off Trump](https://www.msn.com/en-us/news/politics/misinformation-dropped-dramatically-the-week-after-twitter-banned-trump/ar-BB1cOqVP), so that as you will.

I'll circle back to social media platforms/public square stuff in a bit.

#### Parler

Now, Parler. In theory, Parler could have become a competing public square, in fact that's one of the things it's doing. But Parler itself has been deplatformed, not just by Google/Apple, but by the webhost, AWS. I don't have any opinions either way about the app stores kicking them out (although I will say Apple is more egregious, since there's no alternative to Apple's app store on iOS), but AWS kicking them out seems more problematic. It is a bit analogous to a landlord kicking out a tenant from their building because they are doing illegal things, like maybe running a meth lab? So by that analogy it can be justified. Technically, the discussions on Parler aren't directly violent, but they are planning violence. So, can a landlord evict a tenant because his space was being used to plot violence? 

Following the landlord analogy, they could always just find another landlord, but few compare in scale and capability to Amazon. So this may be another case of monopolies being problematic. They could also just host the content themselves, build their own datacenter etc. It's akin to saying you can just buy/build your own house if no one is willing to let you rent one. It's true, but not very pragmatic in many cases.

My gut is that AWS kicking Parler off was justified, because Parler wasn't making a good-faith effort to manage harmful content on their platform, but it still leaves a worse taste in the mouth than the Trump/Twitter. scenario

Anyway, it's super dumb to be planning these things in public anyway! Why don't they get private forums, those are still things right? Or even a private FB group. Can FB ban them for discussions in a private group? Maybe. Or why don't they all join those QAnon forums or whatever?

#### How should social media platforms change?

Circling back to my earlier assertion, I don't think social media platforms should be liable for what their users post. To me, this seems sensible on its face, otherwise no one would bother hosting content posted by other people (which I don't mind, I have a website.) I also think platforms are well within their rights to filter what is or is not allowed to be posted on their platforms. (See above.)

(There's a whole side discussion about section 230 of the US CDA where conservatives are thinking repealing platform protections provided by that law would step them from censoring people, but that seems completely wrong. I'm not an American though, so I don't particularly care.)

I do think however, that platforms should be held responsible for promoting, recommending or otherwise broadcasting harmful content via their algorithmic "timelines", as that is more of an editorial decision than anything else. Think of it in terms of, if I was a content curator who recommended stuff to my followers, and I started recommending or promoting things illegal things like child porn or criminal stuff, I should absolutely be held accountable. The less that platforms promote harmful material, the less likely they are to gather steam and influece. Don't give harmful people megaphones! [Related twitter thread I read recently talking about this very same thing.](https://twitter.com/hankgreen/status/1351736509095792640) 

If the platforms aren't allowed to use recommendation engines, what then? I would suggest that strictly chronological timelines should be fine, with no judgment made by the platform as to whether individual posts should be seen outside of that order or by people who aren't subscribed to those sources. 

For ads, I think platforms should be liable for what ads they allow to run. And information should be publicly available for whoever paid for the ad. If someone advertises something illegal in real life, law enforcement needs to be able to track them down. And probably we should avoid targeted advertising as well. I think showing ads depending on what topics the user follows might be ok, assuming the topics aren't super specific. For example, if the user follows a lot of politics, showing political ads might be ok, as long as the user is exposed to all flavors of political ads (i.e. ads from all sides). Definitely something that can still be refined. (And it goes without saying, if the platforms can't do targeted advertising, they would be less inclined to siphon off all your personal data? Or is that too naive?)

I think stuff like Twitter's "trending topics" section is fine, as long as it's not super localized, i.e. you get a sense of what everyone is talking about, not just people in your bubble or whatever.

Side note: I will agree not all algorithmic recommendations are bad. I've been watching a lot of British TV show clips on Youtube recently, and YT keeps recommending more, so I watch more, and it's fine, it's entertaining. That said, I would willingly give up those recommendations in exchange for the above. After all, people can always curate and provide recommendations manually (and they can be held liable or banned if needed!)

#### Regulation and Monopolies

Unfortunately social media platforms aren't likely to do the above changes on their own, as avoiding algorithmic recommendations cuts into their "engagement" or whatever BS metric they choose to use. So it would have to be enforced by some kind of government regulation.

There is a lot of talk about regulating big tech in the US government, but most of it centers on splitting up larger companies like Facebook and Google. I think that while this is not necessarily a wrong approach, it won't be super useful. The monopoly power these large companies have doesn't come directly from the services they offer but rather from the size of their userbase. (Which admittedly, is influenced by the services they offer.)

What I would suggest instead is to cut into that userbase monopoly by requiring the platforms to implement open standards for external services to subscribe/follow publicly-available content published on their platform. It can be something simple like RSS or something a bit more complicated like how Mastodon implements ActivityPub. Private comms/DMs can be via open protocols too like XMPP. (Or email! Remember email?)

The idea is, if I want to follow someone on Facebook, I shouldn't have to be required to have a Facebook account. This is part of the reason why so many people find it hard to leave Facebook - a lot of the people they follow and want to keep in touch with are there.

I don't believe it would be necessary to require platforms to do the opposite thing - allow their users to follow users on other platforms - because users would just naturally prefer any platform that does implement such a feature.

Requiring open protocols would remove the whole "public square" problem because now instead of having 1 or 2 de facto public squares, we can have as many as we want. Official government feeds could be hosted on their own servers instead of being forced to publish via Facebook or Twitter, and the public could still follow them from the platform of their choice. Same goes for influencers, brands, companies, whatever.

One might think this would make it easier to distribute harmful content and harder to censor it, but as we can see on the open web, the opposite is true: harmful content is difficult to stumble upon normally (you have to be specifically looking for it) and can easily be punished, which is why we don't see a lot of openly operating child porn websites. 

#### In conclusion

That's a whole lot of words, but I don't have a conclusion. Like I said, complicated issue. (And I'm sure there are some easy flaws in my assertions above, I haven't spent more than an hour thinking these through.) But these are discussions we should be having, and at least some of what I've outlined are above are options that are worth considering, given how harmful and divisive we have found the current social media paradigm to be. I still believe in the promise of the internet in bringing people and the world together - but we need to be doing it in a smart and responsible way.

#### RRL

Some other articles I've read lately, relevant to this topic:

- [What Social Networks Could Learn](https://www.platformer.news/p/what-social-networks-could-learn)
- [How to Start Fixing Social Media](https://onezero.medium.com/how-to-start-fixing-social-media-196297eb6b71) (Warning: Medium)
- [Online Speech and Publishing](https://www.ben-evans.com/benedictevans/2021/1/17/speech-and-publishing)
