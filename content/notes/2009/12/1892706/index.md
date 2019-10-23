---
date: 2009-12-12 07:46:48
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1892706/word-doc-document-printout-wont-print-to-a-particular-printer
tags:
- ms-word
- word-vba
- questions
- stackoverflow
- software development
title: Word doc document.PrintOut won't print to a particular printer
---

I have the following .js file being run using cscript on Windows Vista with Office 2007:

    var err = 0;
    var app = WScript.CreateObject("Word.Application");
    try {
      var filename = WScript.StdIn.ReadLine();
      var enc = filename.toLowerCase().indexOf(".txt") >= 0 ? 65001 : 1252;
      var objDoc = app.Documents.Open(filename, false, true, false, " ", " ", false, " ", " ", 0, enc, true, false, 0, true);
      objDoc.PrintOut(false, false, 0, " ", " ", " ", 0);
    } catch (e) {
      err = 1;
    } finally {
      app.Quit(0);
    }
    WScript.Quit(err);

The point of the code is that it will accept a filename from stdin and print that document using Word. My problem is that for a particular printer we are testing with, the document doesn't get printed. I can trace that it executes .PrintOut properly and without any errors, and that the WINWORD process is started and terminated as expected (I can see it in the TaskManager). For our other test printer, the script works correctly.

I'm a bit new to this type of scripting (the guy who wrote it is on vacation...), any advice as to how I can resolve this problem?

Edit: I've isolated the PrintOut call, the rest of the script is irrelevant, even calling ActiveDocument.PrintOut from inside a Word document has the same problems with the printer.