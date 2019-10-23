---
date: 2013-04-15 07:01:21
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/16009411/ckeditor-inline-editing-content-isnt-editable
tags:
- ckeditor
- questions
- stackoverflow
- software development
title: CKEditor inline editing - content isnt editable?
---

I downloaded the latest CKEditor and tried the following:

    <html>
    <head>
    <script src="ckeditor/ckeditor.js">
    </script>
    </head>
    <body>
    <div id="editor">
    Some test text
    </div>
    <script>
    CKEDITOR.disableAutoInline = true;
    
    var editor = CKEDITOR.inline( 'editor' );
    </script>
    </body>

It worked in the sense that I can click the div to make the editor toolbar appear, but aside from that I can't seem to edit the content! Most of the toolbar buttons are disabled, and typing into the field does nothing. (See screenshot below)

![enter image description here][1]


According to http://nightly.ckeditor.com/13-04-14-07-42/standard/samples/inlinebycode.html this should be all the JS I need. Is there some other config setting I need to be doing?


  [1]: http://i.stack.imgur.com/koQbY.png