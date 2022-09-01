---
title: "Initial Thoughts on AI-generated Art (and Code)"
date: 2022-09-01T23:14:24+08:00
tags:
- tech-life
- software-development
dontinlinephotos: true
resources:
- src: artist_dalle.png
  title: '"realistic photo of a starving artist who lost his job because of ai image generation tools  standing despondently on a street corner , golden hour" - DALL-E'
- src: artist_midjourney.png
  title: '"realistic photo of a starving artist who lost his job because of ai image generation tools  standing despondently on a street corner , golden hour" - Midjourney'
- src: ch_dalle.png
  title: '"black and white 4 panel comic strip about a small boy wearing a red striped shirt and his anthromorphic pet tiger who leaps at him as he comes home from school" - DALL-E'
- src: ch_midjourney.png
  title: '"black and white 4 panel comic strip about a small boy wearing a red striped shirt and his anthromorphic pet tiger who leaps at him as he comes home from school" - Midjourney'
- src: superhero_dalle.png
  title: '"a superhero in a green and black costume flying in to stop a helicopter from crashing into a tall building in the middle of a bustling metropolis, dragon in the background" - DALL-E'
- src: superhero_midjourney.png
  title: '"a superhero in a green and black costume flying in to stop a helicopter from crashing into a tall building in the middle of a bustling metropolis, dragon in the background" - Midjourney'
---

A couple of months ago I got access to the [DALL-E](https://en.wikipedia.org/wiki/DALL-E), an AI/machine learning model that lets you generate images from natural language descriptions. Basically they have a server they run and you get some limited number of credits per month (?) to generate images. I only got around to trying it last week and posted some of my samples in [the most recent weeknotes](/2022/08/weeknotes-08-28/).

Since then, I feel like there's a spike in the number of AI image generation-related news and articles I encounter. (More likely than not, I just notice them more now that I've actually played with it a bit.) There are other such tools available like [Midjourney](https://www.midjourney.com/home/) (similar to DALL-E, running on its own server) and the recently-released [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion), which is open source and you can run it on those PC. Admittedly I don't have a lot of experience with these tools yet, but I thought I'd write down some initial thoughts so that I can maybe look back at them down the line.

#### How are artists affected?

I guess the first thing to ask is: should artists be threatened by this sort of tech? Will it take away their livelihoods? (I must note that even though I consider [sketching](/tags/albums) a hobby, I don't really consider myself an artist; not one with any level of skill at least.)

Here's one artist who isn't worried: [Why Dall-E will not steal my job as an illustrator](https://emmanuel6.medium.com/why-dall-e-will-not-steal-my-job-6a1e2943cb82). 

He also makes some excellent points about how even in various fields where automation can do what humans do, there is still some space for the field to survive. Although the problem is that economics around art may start to change. There will always be a space for people to create art themselves and to enjoy art created by humans, but for commercial purposes, why pay an artist so much if the AI-assisted tools become good enough or cheap enough as an alternative? There may still be a demand for hand-made ("artisanal"?) art, but for many commercial endeavors the demand for human artists may lessen. 

{{% photos artist_ %}}

On the other hand, these tools seem like they might end up enabling new kinds of artists as well. An interesting article related to this is: [4.2 Gigabytes, or: How to Draw Anything](https://andys.page/posts/how-to-draw/). It describes a process where even with very little drawing skill, you can layout an image using simple tools like MSPaint, and use the AI tools to enhance it into a much more detailed or realistic drawing. While a professional artist probably still has an advantage in this regard (since he would know more about things like lighting and composition, etc), these tools can democratize the space a bit, allowing people who previously would not have been able to generate such types of art to do so. 

I think the closest analogy is to photography, which was also mentioned in the post from Emmanuel above: even though phone cameras have made it so that anyone can take pictures anywhere, there is still a demand for professional photographers, since their skill means they know how to take better shots, find better angles etc.

One thing to note is that these tools require a great deal of specificity - if you have a certain concept or idea of the art already in your head, you need to be very specific in your descriptions/prompts to get something close to that, and that may not always be possible. And the less you speak the language of art, the more difficult it may be for you.

{{% photos ch_ %}}

The tools may also forever be limited in terms of imagination - since they are limited to what their training data set contains, it will be difficult to get something entirely new from these tools, aside from blending styles we have already seen. Although perhaps the same could be said of human artists, given each human artist has their own influences.

A likely future may be that artists and illustrators integrate these tools into the profession,to make stages like prototyping and iteration easier/faster, while still requiring their skill for final touchups or adjustments and such. 

Some more interesting articles: 

- [AI wins state fair art contest, annoys humans](https://arstechnica.com/information-technology/2022/08/ai-wins-state-fair-art-contest-annoys-humans/)
- [So, I think it's a complete myth that AI can't generate assets for an entire game with a consistent style.](https://www.reddit.com/r/gamedev/comments/x00s3h/so_i_think_its_a_complete_myth_that_ai_cant/)

#### Concerns

Another big question right now about these AI content generation tools is the ethics behind using other people's works as part of the training data set. Andy Baio gave a quick overview of the ethics concerns here: [Opening the Pandora’s Box of AI Art](https://waxy.org/2022/08/opening-the-pandoras-box-of-ai-art/). It's certainly a complex question both legally and ethically.

One thing to note is that the AI learns from the training data much the same way a human artist does - the human artist looks at and studies lots and lots of images over the course of his life/career and he mimics and learns from them and blends them all into what his own personal style becomes. If I had the discipline to draw a comic book, doubtless the style would be some combination of the many comic artists whose works I have enjoyed through the years. We all learn from those who come before us; these tools simply make that process happen a whole lot faster. 

{{% photos superhero_ %}}

Aside from the already mentioned issues, there's also the possibility that of large-scale adoption of AI-generated images could be used for purposes such as targeted propaganda.

> 'AI'-generated art at scale risks becoming DOS attack on that discourse. It's fairly easy, for example, to imagine an authoritarian government using these methods to daily bombard every citizen with personalised pro-government propaganda. - [Baldur Bjarnason](https://toot.cafe/@baldur/108912031406992695) 

We already know how targeted algorithmic content streams on social media platforms are generating a negative effect on society - it's definitely a possibility that this technology might have similar negative effects if/when they become widespread.

#### What about code?

AI-generated software code is another interesting thing for me. The biggest advancement in this space is of course Github's Copilot which can generate working code from a natural language description. It has the same controversial problem with the source material as it was trained on largely open source code which may have usage restrictions. While currently, Github Copilot is limited to writing functions in a single file (I only tried the Beta, maybe this has changed?) I can imagine future AI-assisted coding tools to allow generation of more complex boilerplate code for entire projects like a React frontend or a Django/rails backend with a natural language request perhaps somewhat similar to the one made [in this joke meme](/2018/01/10156317519613912/):

{{< photo "2018/01/10156317519613912/" >}}

Of course it's not going to be that simple. The same caveats about specificity apply, perhaps even more so compared to images. There is a lot to be specified in a software project, most likely you would need to define screens using descriptions like:

- "a CRUD maintenance screen with the following fields: aaaa, bbbb (use an autocomplete dropdown from [some url]), cccc (numeric). Use standard button set."
- "add a standard checkout screen with the following options: ..."
- "an image gallery in a carousel loading the images from [source url] with the schema [this url]; clicking each image should zoom in and provide the following details: (...)"

It's not unlike writing a technical spec! So it would definitely still be technical work just with a more natural language and not some kind of "no code" solution. The prompt engineering in this case could act as an additional layer of abstraction over the generated code. The same way we have a compiler as a tool to translate our programming languages into lower level languages, the AI code-generation tools would help translate our natural language prompts into code. Most likely the generated code would be boilerplate/template code that would most still need to review and tweaks by an experienced (human) developer, although perhaps as the tools mature the generated code gets better and better and the human developer can get to focus more on higher-value tasks like performance optimization or developing algorithms for new processes that the AI doesn't know yet.

This is all just a fantasy right now of course, but something that might be possible down the line. It will be interesting to see whether our industry adapts to wide usage of this kind of tool or whether developers will still insist on the old ways.

#### The future

The whole "content generation using AI" trend started with text generation using tools like [GPT-3](https://en.wikipedia.org/wiki/GPT-3). Currently the biggest strides are being made in static image generation, but one can imagine in the future it could be extended to other sort of media - videos, animation, music, and software as mentioned above etc. You can even mix tools to do something like [gamedev prototyping maybe](https://twitter.com/simonw/status/1555626060384911360)? 

If we don't get some kind of resolution on the ethical and copyright issues before then, we certainly will by the time the RIAA or MPAA get into it!

AI/machine learning may very well turn out to be one of the more crucial advancements of the next few years, certainly more interesting and a larger possible impact than the whole blockchain thing. It will be interesting to see how it all shakes out and whether we can overcome all the raised concerns. 

As for me, I've just about run out of free Midjourney credits. I might take the time to try to install Stable Diffusion later on (not sure if my PC can handle it) and try it out as well.