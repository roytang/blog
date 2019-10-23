---
date: 2013-03-25 09:37:29
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/15611653/implementing-http-basic-authentication-in-a-servlet
tags:
- java
- servlets
- basic-authentication
- questions
- stackoverflow
- software development
title: Implementing HTTP Basic Authentication in a servlet
---

I want to write a servlet that wraps around a set of resources and needs to protect them with basic HTTP auth; the submitted username/pass will be checked against the backend database before serving the file. 

Does anyone have any working examples of this? I tried the sample at http://www.coderanch.com/t/352345/Servlets/java/HTTP-basic-authentication-Web-Applications but it kept returning an `IllegalStateException` in the `sendError` call.