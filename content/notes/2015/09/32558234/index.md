---
date: 2015-09-14 06:06:45
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/32558234/invalid-ssl-certificate-in-apache
tags:
- apache
- ssl
- questions
- stackoverflow
- software development
title: Invalid SSL certificate in Apache
---

I have installed an SSL certificate on my Apache server, but when I access the site via URL from a different machine, an HTTPS error is shown and viewing the certificate details says "this certificate has an invalid digital signature"

If I view the same URL from within the server itself, the certificate is fine and there is no HTTPS error. 

I'm not sure what to look for in httpd.conf. Any advice?

Thanks!