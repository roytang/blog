---
date: 2010-07-22 12:06:37
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/3308615/proper-way-to-contain-floating-elements-using-html-css
tags:
- html
- css
- questions
- stackoverflow
- software development
- container
title: Proper way to contain floating elements using HTML/CSS?
---

Say I have the following HTML:

    <head>
        <style>
            #container {
                border: 1px red solid;
            }
            .floaty {
                width: 200px;
                float: left;
                border: 1px green solid;
            }
        </style>
    </head>
    <body>
    <div id='container'>
        Text inside the container
        <div class='floaty'>
        Floaty block 1<br/>
        Floaty block 1<br/>
        Floaty block 1<br/>
        </div>
        <div class='floaty'>
        Floaty block 2<br/>
        Floaty block 2<br/>
        Floaty block 2<br/>
        </div>
        <div class='floaty'>
        Floaty block 3<br/>
        Floaty block 3<br/>
        Floaty block 3<br/>
        </div>
    </div>
    </body>

This renders as: ![floaty divs][1]


What's the proper CSS way to have the container (red-bordered box) completely surround the floaty green-bordered boxes?


  [1]: https://i.stack.imgur.com/Ci22u.png