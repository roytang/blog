---
date: 2020-11-05 06:59:41
slug: server-setup-notes
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/105156709394792329
- type: twitter
  url: https://twitter.com/roytang/statuses/1324263713411538945/
tags:
- tech life
- software development
title: 'Server Setup Notes: Ubuntu, Nginx, Django, MySQL'
---

I recently did [a server migration](/2020/10/site-migration-to-django/) since I moved to new hosting, The move was from managed/shared hosting to a VPS, these are some notes I took during the process, which I figure might be helpful if I ever tried to  do this again. (And maybe someone else finds it helpful too). Links and references to helpeful resources are included.

### Setting up a webserver and WSGI container

I already knew I wanted to use Nginx (managed hosting on the old server always used Apache), that meant needing to choose a WSGI container for the Django apps. The choices were either gunicorn or uwsgi. Readings suggest minimal performance difference between the two. I did try setting up both, and found uwsgi's setup much more straightforward and with more helpful step-by-step documentation: https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html

Nginx itself was pretty straightforward to set up. This "common pitfalls" article was helpful in resolving issues: https://origin-www.wp.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/.

One thing I will note that's not in the article above is that for static files to be served by Nginx, it was easier to just have everything be under /var/www, for permission purposes. I initially had static files in a different folder in my user root, but really there's no reason for that since you're going to serve them statically anyway. 

### Setting up PHP on Nginx

I needed PHP since I had a few minor scripts/pages and a Wordpress install that needed PHP. For the setup on Nginx, I found this guide from askubuntu super helpful: https://askubuntu.com/questions/134666/what-is-the-easiest-way-to-enable-php-on-nginx

This guide from DigitalOcean was also helpful: https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-in-ubuntu-16-04

I was encountering some issues with fastcgi not mapping requests to the correct PHP script if the Nginx location block was aliased. This was with me using the default `snippets/fastcgi-php.conf` that was provided with the fastcgi install. I resolved the issue by adding an additional fastcgi_param to the php location block like so:

```
    location /sample-path {
        alias /var/www/sample-path;
        # autoindex on;

        location ~ \.php$ {
                include snippets/fastcgi-php.conf;
                fastcgi_param  SCRIPT_FILENAME    $request_filename;
                fastcgi_pass unix:/run/php/php7.4-fpm.sock;
        }
    }
```

The solution for this came from the Nginx common pitfalls article listed above.

### Choosing a database

I initially wanted to use PostgreSQL (since that's what I was using locally) and set that up first. Then I realized I had a Wordpress install I wanted to carry over, and apparently Wordpress needs MySQL, so oops. I didn't want to have two databases running, so that was out. Plan out your database usage boys. 

### Setting up MySQL for Django

I created the initial MySQL database with character set `utf8`, which apparently had the dumb implementation of only supporting 3 bytes for multibyte characters. This led to errors when I tried importing records into Django that had emojis and the like in text. Apparently the "correct" character set to use is `utf8mb4` (mb4 -> "multibyte 4" I guess?). It's kinda dumb that they had to invent a "more utf8 character set" because of their initial dumb implementation. It's also dumb that I didn't realize this when apparently the MySQL databases on the old server were already using `utf8mb4`! On the Django side, you need to specify the charset in the database settings. Helpful for resolving this issue was donturner's answer on this SO question: https://stackoverflow.com/questions/2108824/

After some initial testing, I also encountered a "MySQL has gone away" every so often. Turns out Django was holding on to connections for too long, so a timeout had to be set in the database settings as well. SO reference: https://stackoverflow.com/questions/26958592/

### Misc stuff

I used cron to set up most of the batch jobs I usually run (like the Twitter bots, etc). Initially I had problems where it seemed like cron wasn't running the jobs, even though syslog showed me the cron daemon was actually running. I don't have notes on how I resolved this, but mentioning it here so that if this happens again in the future, I know to actuall take notes!

Setting up log files for my cron jobs: I did it this way: `0 * * * * /path-to-batch/hourly.sh >> /var/log/cron/my-log-file.log 2>&1`. The "2>&1" at the end is necessary so that stderr is redirected to the same file (otherwise you'd only get stdout).

Log rotation: these is the kind of thing you don't realize you need to do when you're managing your own server. Anyway, I found this guide helpful: https://linoxide.com/linux-how-to/setup-log-rotation-logrotate-ubuntu/

I needed to set up AWStats on the new server (and migrate data from the old server). This guide was helpful: https://larsee.com/blog/2020/06/awstats-on-ubuntu-20-04-with-nginx/

When migrating the old AWStats data files, the filename format from the oldserver was slightly different (new install needed to end with `*.roytang.net.txt`), so I learned a bit of bash scripting to do the batch rename:

`for i in /path-to-tmp/awstats/*.txt ; do cp "$i" "/path-to-tmp/awstats/out/$(basename "$i" .txt).roytang.net.txt" ; done`

Setting up Let's Encrypt SSL on Nginx: https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/

### Lessons learned

One thing I didn't expect from the migration from shared hosting to a VPS is how much memory I'd need. My old hosting plan was only on 512MB ram, and the lowest DigitalOcean droplet had 1GB RAM, so I figured that was fine! But MySQL occasionally had out of memory errors on startup even at 1GB ram, so I bumped up to the next level (2GB RAM). I guess the database RAM usage didn't count against my limits on the shared hosting! The next tier isn't much more expensive and is still manageable for my casual/hobby hosting purposes, but I will probably try to look into more detail into the memory situation at some point to see what I can optimize.