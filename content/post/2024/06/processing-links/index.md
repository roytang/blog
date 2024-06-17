---
title: "How I Process Links"
date: 2024-06-17T21:09:45+08:00
toc: true
tags:
- blogging
- meta
---

I have recently been wading through hundreds of backlogged links and reading items to "process" them and that got me thinking that maybe I should document how this whole "link processing" thing works, if only for me to think through why the workflow is how it is, and to get a better handle of what I want out of it. I guess this is a "thinking in public" kind of post.

### Inputs

Typically, "links" come from one of the following sources:

- my feed reader
- social media: mostly Mastodon and sometimes Reddit these days
- nonpublic group chats

I may encounter these links via either desktop web browsing or on mobile (Android) / tablet (iPadOS), using web or apps. So this workflow needs to support processing links from any of those systems.

### Holding area

Once I come across a "link of interest", I will save it to an interim holding area. Currently I use an app called [SimpleNote](https://simplenote.com/). I am not 100% happy with this app's features (perhaps a topic meant for a different blog post), but it works for what I am doing now.

History: I was previously using Google Keep, but migrated off that as another step in de-googling. Before using google keep, I had been using bookmarking services like the long-defunct [Delicious](https://en.wikipedia.org/wiki/Delicious_(website)) (classic!) and [Pocket](https://getpocket.com/), but those never really fit too well with what I wanted to do.

Okay, so when I find a "link of interest", I add it to a new note in SimpleNote. On desktop, that's copy and paste. On mobile/tablet, that's using the "share target" functionality of whatever app I'm using. Usually on mobile/tablet I'm either lying down or in a queue somewhere passing time and it needs to be as quick and easy as possible. The note will contain whatever info the source app wants to include.

Note: most sources will have some way for me to have a "holding area" inside each app. For example, my feed reader lets me "star" items to revisit later. Mastodon lets me "favorite" toots and Reddit lets me "save" links. I sometimes use these features (in Mastodon for example it's super easy to just click the favorite icon instead of multiple clicks to save to a share target), but the downside to these is that I would have multiple different holding areas to go through later. I prefer using an app like SimpleNote because it makes future processing easier.

### Processing

Periodically, I will open the SimpleNote webapp and do a round of "processing" any new/unprocessed links. I almost always do this on my desktop, because often I will need to do things like open multiple tabs, switch between them, copy-paste excerpts, and that's just too difficult on mobile. Plus I like seeing how websites look in a full-width browser instead of the tiny screen space provided by mobile.

What does it mean to "process" the links? This depends on the link in question and why I saved it in the first place.

1. Articles/longer posts I read that I think other people (not necessarily people I know) would find interesting: For these I create a post in my [link blog](/links/) which would sometimes include a short comment from me and/or one or more excerpts from the article in question. Any posts to the link blog automatically get pushed out to [Mastodon](https://indieweb.social/@roytang) and will appear in the next [weeknotes](/tags/weeknotes/)
2. Memes/videos I think friends would enjoy: Usually get shared to nonpublic group chats. Used to be I would share this sort of thing on Facebook/Twitter, but for some reason I don't do that anymore. Sometimes something fits in both #1 and #2.
3. Articles/longer posts that I found interesting and want to comment more on: Typically this means I want more space to excerpt and comment than what I typically share via the link blog in #1. In this case, I will write a blog post about it. I may group related topics/links into a blog post as needed. It may take a while for me to have the bandwidth to write the post, so they stay on the list until I do.
4. Articles/longer posts/videos that looked interesting but I did not have bandwidth to go read/watch at the time: if I have bandwidth at processing time I'll try to read/watch them immediately. If not, they stay in the list and I'll revisit them in a future pass
5. Books/comics/TV shows/movies/music/software mentioned by other people that I might want to check out: I used to process these like #4 above, but now I've started making "buckets" - basically longer notes where I group all related items. These are basically separate backlog lists! Each entry is not necessarily one book/TV show/movie/whatever, but often it will be articles/posts like "My Favorite Books from 2023". Having them grouped together in buckets makes it easier for me for example if I'm looking for a book to read, I just look in the "books" bucket. In theory I could use SimpleNote's tags feature for this, but I prefer this way for some reason.
6. Articles / posts that I saved because they contain trivia that I thought I could add to the [trivia bot](https://botsin.space/@triviastorm): I add them to the trivia bot! Typically I add questions to the bot in larger batches, so I tend to not process such links until I have enough for a decent-sized batch. I don't have a "bucket" for this yet, I probably should.
7. Things that seemed interesting and I might want to get into: These are basically aspirational "to do someday" items. Of a different scale than #4, basically these are new hobbies or projects I might want to undertake. I tend to leave them there in the list until I get around to them, which is often never. I plan to post about this topic soon.
8. Blogs / personal websites: I love checking out other people's blogs and personal websites, but I am very bad at going through these items in a timely manner. I have also created a "bucket" for them. Processing these can be a bit involved - I'll check out the contents, see what the site layout/design is like (maybe I'll steal something!), check the archives, check the about page, etc. When I find a blog or personal website that I think the content is generally interesting to me and it has an RSS feed, I will subscribe to it in a "tentative" folder in my feed reader. (I described this process in [a previous blogroll update post](/2022/06/blogroll-updates/)). Sometimes I will find an interesting blog or website that doesn't have an RSS feed or that I don't think fits in my feed reader but I might want to check it out again later. For such items, I don't know what to do and they stay there until I figure something out. Also, these days I typically don't share such blogs/personal website via the linkblog, not sure if that should change.
9. Things I might want to implement for this website: They stay on the list until I either get around to them or I lose interest. Again, should probably be in a bucket.
10. Other to-dos: Surprisingly, I already have a "to do" bucket, but it is not very well-maintained. Same as above: they stay on the list until I get around to them or lose interest.
11. Others / Misc: Mostly things I found interesting but unsure what to do with the information. They stay on the list until I figure them out. Sometimes I will group them into topical lists. For example, I have a list that is about "Drawing", but I'm not sure what I'll do with that list yet.

### Problems with the current workflow

1. I am very bad at maintaining the SimpleNote holding area. I tend to process old links less often and add new ones more frequently, so the number of notes tends to be growing most of the time. The "buckets" thing was a recent practice I started to help me get a better handle of how many unprocessed notes there are
2. I have a lot of links saved where I am unsure what to do with them
3. I am unsure about what the distinction should be between the link blog and the main blog. In my head it's just "the main blog is for longer posts" and "the link blog is for links to share", but that doesn't always work cleanly. Sometimes I will make a "link dump" post to help with the backlog of unprocessed links, basically a group of related links all together in a single post. I wouldn't want to post them individually to the link blog, because it feels a bit spammy to share so many at once, so they go into a blog post that can be shared in one go
4. I am unsure if the link blog is good as a browsable list. I kind of want to have something like a curated directory of links in categories, built out of the links shared to the link blog, but this is something I need to have a good think about. (i.e. How I want to do it, how I want it to look, etc). Having such a thing would help with the problems above

### Action items

1. Process the holding area more often?
2. More buckets! Identified above: Trivia posts, website to-dos.
3. Figure out how I want to handle "interesting blog or website that doesn't have an RSS feed or that I don't think fits in my feed reader but I might want to check it out again later"
4. Think about the "curated directory of links" idea and what kind of links I want shared to the link blog