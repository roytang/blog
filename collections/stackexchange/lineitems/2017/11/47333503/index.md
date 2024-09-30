---
date: 2017-11-16 15:31:08
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/47333503/marklogic-roxy-calling-a-javascript-module-from-app-specific-rb
tags:
- marklogic
- roxy
- questions
- stackoverflow
- software development
title: 'Marklogic Roxy: Calling a javascript module from app_specific.rb'
---

I have a Marklogic 9 project that I'm configuring with Roxy. 
I've been following these examples: https://github.com/marklogic-community/roxy/wiki/Adding-Custom-Build-Steps

Basically, I have a server-side JS function that I want to call after deploy content. I have something like this:

  # then you would define your new method

      def deploy_content
        # you can optionally call the original
        original_deploy_content
    
        # do your stuff here
        execute_query(%Q{
          xquery version "1.0-ml";
          xdmp:javascript-eval('var process = require("/ingestion/process.sjs"); process.postDeployContent();')
        },
        :db_name => @properties["ml.app-name"] + "-content")
    
      end

The xquery being called here evaluates fine when executed via query console. But when I call ml local deploy content, I get the following error:


    ERROR: 500 "Internal Server Error"
    ERROR: <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
        <title>500 Internal Server Error</title>
        <meta name="robots" content="noindex,nofollow"/>
        <link rel="stylesheet" href="/error.css"/>
      </head>
      <body>
        <span class="error">
          <h1>500 Internal Server Error</h1>
          <dl>
            <dt>XDMP-MODNOTFOUND: var process = require("/ingestion/process.sjs"); process.postDeployContent(); -- Module /ingestion/process.sjs not found</dt>
            <dd></dd>
            <dt>in [anonymous], at 1:14 [javascript]</dt>
            <dd></dd>
            <dt>at 3:6,
    in xdmp:eval("var process = require(&amp;quot;/ingestion/process.sjs&amp;quot;); proce...") [javascript]</dt>
            <dd></dd>
            <dt>in /eval, at 3:6 [1.0-ml]</dt>
            <dd></dd>
          </dl>
        </span>
      </body>
    </html>

Why is the module not found when running via xquery from app_specific.rb?

Or... is there a better way to call a JS module function from here. Sorry, I'm not too familiar with the xquery side, so I just called a JS function instead.