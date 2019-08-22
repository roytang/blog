---
categories: []
date: 2019-08-24 00:00:00
tags:
- software development
- tech life
- devnotes
title: "Devnotes: Migrating Mercurial to Git"
type: post
---

Big news in online repositories this week is that [Bitbucket is sunsetting support for Mercurial](https://bitbucket.org/blog/sunsetting-mercurial-support-in-bitbucket)! This might be the death knell for Mercurial, although Git was already the super popular choice before. Back when I started using online source control for my personal coding projects I started out with Bitbucket over Github because they offered unlimited private repos and Mercurial (which I had already tried out before at work, so at first I preferred it over git). Now that Gitlab and Github both offer unlimited private repos, there's no reason to stick with Bitbucket either. I had already migrated most of my private Git repos to Gitlab before, but hadn't realized until now that I also had a couple of Mercurial repos there that needed to be migrated as well. I hadn't touched those repos in so long that I didn't even have Mercurial installed locally anymore! (Although I'm still using the code locally!)

Luckily, converting a mercurial repo to git turned out to be straightforward thanks to a project called [fast-export](https://repo.or.cz/fast-export.git). Modified instructions from a convenient [stackoverflow post](https://stackoverflow.com/questions/10710250/converting-mercurial-folder-to-a-git-repository#):

{{< highlight bash >}}
brew install hg # install hg on my mac first
cd ~
hg clone https://user@bitbucket.org/user/reponame
git clone git://repo.or.cz/fast-export.git
git init git_repo
cd git_repo
~/fast-export/hg-fast-export.sh -r ~/reponame
git checkout HEAD
{{< / highlight >}}

The process was fairly quick, and the commit history from the Mercurial side was even retained, I would have been happy just retaining HEAD! After that, I just create a new private repo on Gitlab, set that as the remote, then push to Gitlab as usual. 

It's a good thing I remembered to check my Bitbucket account, as apparently they will be deleting the old Mercurial repos when time is up!

