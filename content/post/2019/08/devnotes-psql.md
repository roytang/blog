---
categories: []
date: 2019-08-08 00:00:00
tags:
- devnotes
- software development
title: "Devnotes: PostgreSQL on the command line"
type: post
---

I decided to start doing small "devnotes" on developer stuff I'm doing so I can refer to them later (and also because I feel like I could use more technical content on this blog)

Today is about PostgreSQL. I haven't used it much beyond standard ANSI sql stuff. You won't always have a graphical interface to access your database, sometimes you need to ssh to prod and query the database from the shell. 

The command line for PostgreSQL is `psql`. You can do:

`psql [database-user-name] -d [database-name]` and it should prompt you for your password.

But when I tried this today, I got:

`psql: FATAL:  Peer authentication failed for user "[database-user-name]"`

The problem had something to do with the permissions available to my ssh user. The workaround was to tell psql I was doing this from the local machine:

`psql: FATAL:  Peer authentication failed for user "[database-user-name]" -h 127.0.0.1`

Worked fine.

After connecting, you get a prompt that looks like this:

`[database-name]=# `

Now, when I connected today, I had to do some queries, but I wasn't superfamiliar with the project's schema, and would have to muck around to find table names and field names. The psql shell provides some handy shortcuts for that:

`\dt` - outputs a list of tables

`\d [table-name]` - describes a specific table, showing field names

You can also just directly run an SQL query, just make sure to end it with a semicolon.

If the command outputs a lot of records, it will show them to you in a page-able vim-like format. You can recognize it when it stops with a `:` after each page and you can hit spacebar to proceed, and at the end it shows `(END)`. And like vim, you might not know how to get out of this view. I had to google it myself, you just have to hit `q` to go back to the psql shell.

