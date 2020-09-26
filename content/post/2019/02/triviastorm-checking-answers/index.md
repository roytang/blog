---
author: roy
categories: []
date: 2019-02-03 05:56:56
tags:
- projects
- python
- triviastorm
- testing
- Software Development
title: 'TriviaStorm: Text and Answer parsing'
type: post
---

A while back I started a [Twitter trivia bot as a weekend project](/2017/02/weekend-project-twitter-trivia-bot/). That bot is still [up and running on Twitter](https://twitter.com/triviastorm), you can check it out there!

But today, I thought I'd write about the answer-checking mechanism used by the bot. It was a bit interesting to me because it was the first nontrivial use I had for [Django's unit testing framework](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/). I'm not too keen on unit testing web functionality (something I still have to learn), but this seemed an appropriate first use of a unit test framework for several reasons:

- the bot had to be able to handle a wide variety of answers
- there were a lot of test cases to check and a single checking function handling everything - I couldn't risk breaking previous working tests
- inputs were discrete and outputs were easily checkable
- I needed to be able to add new test scenarios all the time as more problematic answers were provided

The project currently isn't open source, but I did make a gist of the `tests.py` I used [here](https://gist.github.com/roytang/9199962097bdf3ca2aa8ec9c43bd7ef8).

The `check` function basically accepts three parameters: 

- a checking mode (currently only supports EXACT and ALL_ANYORDER)
- the answer phrase provided by the player
- a set of valid answers accepted for the question

There's a number of test cases already handled:

- checking should be case-insensitive
- articles should be ignored if they're at the start of the answer phrase
- numbers should be acceptable for the spelled-out versions i.e. "7" should be accepted for "seven", and vice versa
- some minor soundex (phonetic matching) support (via [Python Jellyfish](https://github.com/jamesturk/jellyfish))
- handling of questions that support multiple answers. This is what ALL_ANYORDER is for - it means that all the given answers must be provided, but they can be in any order. i.e. if the valid answer set is `"Huey"`, `"Dewey"` and `"Louie"`, then `"Louie Huey Dewey"` should be accepted as an answer
- nonalphanumeric characters should be treated as whitespace, except in some special cases
- special case: abbreviations like `"don't"` or `"can't"` should be treated as if they were a single term like `"dont"` or `"cant"` instead of `"don t"` or `"can t"`

The answer checking definitely still isn't perfect, but I'm pretty happy with where it's at right now. There is also definitely an element of subjectivity as to which answers should be accepted. One time a player complained that his answer `"Batman vs Superman Dawn of Justice"` should count for `"Batman v Superman: Dawn of Justice"`, but for this particular question I had chosen not to allow "vs" for "v" because that was the actual movie title, which might be unreasonable now that I think about it!

I do know that I need to implement a better "synonym" handling, i.e. mapping of `"v"<->"vs"` and other terms like `"mr"<->"mister"` or `"natl"<->"national"`. The problem with handling things like that is that is the possible combinations of phrases expands when multiple such terms are found in the same answer, so it can't scale too well. I suppose I need to normalize the answer sets at the time the question is defined. What do you know, I figured out how to do something just by writing a blog post!

I do have a bunch of other enhancements planned for the trivia bot, including support for slack and discord, and a longer time frame roadmap, but I'm not sure when I can commit more time to it. Still, it's turned out to be a pretty fun endeavor, I'm hoping it leads to something cool!