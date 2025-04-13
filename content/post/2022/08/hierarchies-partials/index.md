---
date: 2022-08-16 15:12:33
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/108833384619013588
- type: twitter
  url: https://twitter.com/roytang/status/1559570927691902976/
tags:
- meta
- blogging
- tech-life
title: Content Hierarchies and Partials in SSGs and this site
---

Via [Kev Quirk](https://kevq.uk/static-site-generators-are-easy-to-useright/): this [great article by Florens Verschelde about SSGs](https://fvsch.com/static-site-generators) 

(Aside: I already shared this via the [links](/links) page, but I had more to say, so now there's a blog post about it too.)

I agree with a lot of things mentioned in this article, but what really hit home for me was the complaint about limitations in how content hierarchies and partial content are handled in SSGs.

> "...But the nail in the coffin was always that it’s either impossible or way too hard to build a single page from several pieces of content."

This relates to something that was very unintuitive to me when [I started using Hugo in 2018](/2018/11/site-migration-to-hugo/). Basically, Hugo doesn't do well if you have multiple markdown files in the same page bundle or have additional markdown files in subfolders. For example, if you had a file hierarchy like this:

```
:::IRC logs 
posts
└─ my-post
   ├─ index.md
   ├─ other.md
   ├─ resource1.png
   ├─ resource2.png
   └─ otherchildren
      ├─ child1.md
      ├─ child2.md
      └─ child3
         └─ index.md
```

I would have expected to be able to convert all of these markdown files into HTML that I could link to from the root index page. Instead, Hugo only generates the root `my-post/index.html` from `posts/my-post/index.md`. (I had to run Hugo first to test this.)

*Note: I use [Hugo's page bundles feature](https://gohugo.io/content-management/page-bundles/) to group the markdown files and associated resources (images, etc) together, which means the root file for each post must be `index.md`. I initially tried having all my attachments in the static folder, with the path mirroring the content, but because of the sheer number of posts/size of the repository, it was very unwieldy to be jumping between two sets of folders when trying to look at the attachments for a specific post.*


I can understand the frustration with not being able to handle this sort of scenario, as there are some use cases that hierarchical organization of the markdown files can address quite well. 

One example would be: In the early stages of my migration to Hugo, I had comments as a separate post type under the content root, i.e. I had folders for `content/post` and `content/comment`. But I needed a way to relate the comment to the related post, so I added a "reply-to" to the metadata with the URL path of the parent post and in the Hugo theme, when listing out comments for a post I would need to iterate through all the comments and filter only those comments that matched the URL path of the current post. This approach had the advantage of the comment being a markdown file similar to a regular post which I liked. But it had two disadvantages: (a) the comment generation logic added a nontrivial amount of time to the Hugo build; and more importantly (b) I couldn't intuitively go over the comments for a post just by looking at the file tree.

What I would have preferred was a structure like this (similar to above):


```
:::IRC logs 
posts
└─ my-post
   ├─ index.md
   ├─ resource1.png
   ├─ resource2.png
   ├─ comment1.md
   ├─ comment2.md
   └─ comment3
      ├─ index.md
      └─ attachment.png
```

Or even:

```
:::IRC logs 
posts
└─ my-post
   ├─ index.md
   ├─ resource1.png
   ├─ resource2.png
   └─ comments
      ├─ comment1.md
      ├─ comment2.md
      └─ comment3
         ├─ index.md
         └─ attachment.png
```

I wasn't able to get this to work with Hugo because there's no way to access those "child" markdown files. (Or maybe there is; this was very early in my implementation, so maybe I just couldn't figure it out.) I ended up implementing comments as JSON files with a similar file structure as above. (This works because Hugo [has functionality for me to fetch data from JSON resources](https://gohugo.io/functions/transform.unmarshal/))

Another use case: In my current site, I often want to be able to handle "partial" posts, i.e. shorter posts that are individually addressable but are also part of larger posts. 

For example: I often write reviews of movies, tv shows, books, games I've recently consumed, and I have [some media pages that index the reviews](/reviews/movies) and link to the individual review pages. But sometimes like in my [weeknotes](/blog/tags/weeknotes) I'll have a bunch of short reviews at once. When that happens, the index points to the review in the larger weeknotes page, but it's a bit weird to be loading the entire page, when I could just be loading the part of the content that contains the specific review.

I also often want to be able to view partial content by tags: for example, if I wanted to view all posts tagged "movies", it would include many of the weeknotes (since many of them have movie reviews), but that increases the amount of text I need to look at and not all of it is relevant to the search. If I wanted to say, tag all the book posts by a specific author, I risk including in the tag other reviews in the same file.

Ideally, I would be able to arrange my content hierarchically, like this for example:

```
:::IRC logs 
posts
└─ weeknotes-08-07-2022
   ├─ index.md
   ├─ resource1.png
   ├─ resource2.png
   └─ reviews
      ├─ movie1.md
      ├─ book1.md
      └─ movie2
         ├─ index.md
         └─ moviestill.png
```

...where each item under reviews would be individually addressable (have their own URL) and taggable but still be part of the larger parent page. Now, there are certainly workarounds to achieve this; I could just have each review be a separate note and embed it in the weeknotes post as needed, but that has the same problem of not being able to view the organization in the file hierarchy. 

I have a few other use cases like similar to this that I had found problematic implementing under the Hugo paradigm, which is why I really liked the linked article. That being said, the linked article's statement that "static site generators are terrible at handling content" is probably a dramatic exaggeration. 

For the record, I think the current crop of SSGs are fine, especially for very simple sites that don't have a lot of content and aren't very particular about how organization. I will admit that my concerns are mostly because I like being able to do different kinds of queries and whatnot on my data, and that doesn't work without a finer level of detail in tagging and organizational structure. 

### The Current Site

The current site is no longer running on an SSG; [I migrated to a Django-based backend almost 2 years ago](/2020/10/site-migration-to-django/). But I'm still bound by the limitations and conventions I had back when I was running on Hugo, because the backing data (markdown files, etc) are still the same ones from the Hugo version. In fact, [the source project for this blog](https://github.com/roytang/blog) is still a valid Hugo project, although running the build will probably take a very long time. Until last year I was even maintaining [a mirror that was generated using Hugo](https://mirror.roytang.net/). (I stopped updating it because I had added some custom shortcodes that I hadn't had the energy to backport over.) When I want to write a new post, often I still use `hugo new`!

(I've written more about this blog's custom backend [here](/2021/11/cypress/) if you'd like to know more about these decisions and the weird architecture.)

Despite having foundations in an SSG, in theory I could surpass the above limitations now by rewriting a lot of my backend to support those use cases. Reading the above article is making me consider that.

Adding support for partials (and probably rewriting to support comments as described above). It would introduce some downsides: mainly a more complicated hierarchy and writing composite posts would be more difficult. And I would need to go back in time and update relevant posts, etc. I would need to think about how to minimize friction when writing composite posts. It might allow me to introduce a simpler data model (since comments and reviews can now be post types?). Overall, a lot of tradeoffs to think about. It would be a non-trivial effort, but something to consider. (This isn't really a problem as I enjoy working on the backend code and honestly the code could use a good once-over...)