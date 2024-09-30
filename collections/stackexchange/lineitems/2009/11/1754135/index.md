---
date: 2009-11-18 06:58:03
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/1754135/applet-with-jdialog-not-hiding-correctly-in-mac-osx
tags:
- java
- macos
- applet
- questions
- stackoverflow
- software development
title: Applet with JDialog not hiding correctly in Mac OSX
---

I have an applet that calls a JDialog that contains a JProgressBar component. I subclass the JDialog to expose a method to update the JProgressBar, something like:

    public class ProgressDialog extends javax.swing.JDialog {
        public void setProgress(double progress) {
            jProgressBar1.setValue(jProgressBar1.getMinimum() + (int) (progress * jProgressBar1.getMaximum()));
        }
        ...
    }

I use this dialog in the following manner:

    public void test() throws Exception {
        progressDialog = new ProgressDialog(null, true);

        try {
            progressDialog.setLocationRelativeTo(null);

            // show the dialog
            EventQueue.invokeLater(new Runnable() {
                public void run() {
                    progressDialog.setVisible(true);
                }
            });

            // business logic code that calls progressDialog.setProgress along the way
            doStuff();
            
        } finally {
            progressDialog.setVisible(false);
            progressDialog.dispose();
        }
    }

It works fine on Windows/any browser. However, when invoking the above function on Firefox 2/3/3.5 on a Mac, the progressDialog is displayed indefinitely, i.e. it doesn't close.

I suspected that calling setVisible(true) inside the EventQueue was causing the problem, since it's a blocking call and might block the queue completely, so I tried changing it to:

            // show the dialog
            new Thread() {
                public void run() {
                    progressDialog.setVisible(true);
                }
            }.start();

With this change, the progressDialog now closes correctly, but a new problem emerged - the contents of the dialog (which included the progressbar, an icon and a JLabel used to show a message string) were no longer shown inside the dialog. It was still a problem only on Mac Firefox.

Any ideas? I realize it's probably some AWT threading issue, but I've been at this for a couple of days and can't find a good solution. Wrapping the doStuff() business logic in a separate new Thread seems to work, but it's not easy to refactor the actual business logic code into a separate thread, so I'm hoping there's a simpler solution.

The envt is:
Mac OSX 10.5
Java 1.5
Firefox 2/3/3.5