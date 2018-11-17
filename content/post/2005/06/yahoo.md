---
categories:
- Software Development
date: 2005-06-16 16:21:00
title: Yahoo!
type: post
url: /2005/06/yahoo/
---

Some comments on the Yahoo webapps.

  * The next/previous links on top of Yahoo mail messages are confusing. I'm not sure if they take me up or down the mail-list. Gmail is better, since it explicitly says "older&#8221; and "newer&#8221;; With Yahoo, I'm always wrong when I guess. After some experimenting, I figure it out. "Next&#8221; and "Previous&#8221; are based on the sort order in the list of messages. Since the default is sorted by date descending (newest first), "Next&#8221; corresponds to Yahoo's "older&#8221; by default. Which is kind of hard to figure intuitively. 
  * In the grid that lists mail messages, I wanted to test if the columns would wrap any words that were too long. Multiple observations here:</p> 
      * As part of this experiment, I wanted to create an email address with a very long name. Apparently, the Yahoo ID "abcdefghijklmnopqrstuvwxyz012345&#8221; was already taken. I settled on "solongandthanksforallthefish2005@yahoo.com&#8221;. You can send the account mail if you like. 
      * There's a UI bug in the password verification screen if the Yahoo ID is too long. The gray box on the left has its right border broken. 
      * Bummer. I didn't realize the value in the sender column was the name in the Yahoo profile instead of the actual email address. I update the account name to
  
        "AllTheThingsSheKeepsInsideAreTheThingsThatReallyMatterTheFacePutsOnItsBestDisguiseAndAllIsWellUntilT heHeartBetraysLordBringOutTheLightWrapItAllAroundMeLetItHoldMeTightSoakUpAllThatIBleedLordBringOutTh eLightWrapItAllAroundMeLetItHoldMeTightSoakUpAllThatIBleedIBleedWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX&#8221;,
  
        which breaks even more layouts, including this one (mental note: fix that tomorrow). 
      * Doh! I actually had to change the Outgoing name, which was set to the original account name. Why doesn't it update the mail setting when I change the (global) Yahoo account setting? Updated it to "AllTheThingsSheKeepsInsideAreT&#8221; 
      * I sent some mail messages with the long name and a long subject line. As I suspected&#8230;Yahoo compensates for the unwrappable words by expanding the grid cell, breaking the layout. This was a problem I encountered before in the webapps at workand I still don't have a solution that would work in all browsers. 
  * I'm also interested in how popular webapps handle timestamping, so I try this out as well. For the uninformed, timestamping means handling the case where two people both try to edit the same record at roughly the same time. If there's no handling, the person who updates first usually has his changes lost, without any notification.</p> 
      * I try it out first with Yahoo Address Book and Notepad. Both experiments fail&#8230;there's no timestamping. I tested it by opening a record (Address Book entry/Notepad note) for updating in two separate Firefox tabs. I update one tab and save, then update the second tab and save. Changes made in the first tab are lost. 
      * Well, I guess that's okay, since technically, only one person at a time is expected to access these webapps. So I do something else. I create
      
        [
       
        a Yahoo Group
      
][1] 
      
        . I get two moderators, me and a dummy email account. I login with both accounts, using Firefox for one and IE for the other. I try to update the group description with one account, then the other. Bam! First guy's changes are lost, without notification! If this were some sort of mission-critical webapp, that would be a dangerous bug. 

I'm sleepy. More later.

 [1]: http://groups.yahoo.com/group/roytang/

## Comments

### Comment by [eClair](http://www.blogger.com/profile/3338893) on 2005-06-17 14:55:00 +0000
I have stopped using my Yahoo!mail account except for Yahoo!groups. I really
  
like Gmail better &#8211; not just the amount of inbox space but also labels and
  
what not.

Whoa! You really are playing around with Yahoo!

### Comment by [Roy](http://www.blogger.com/profile/1694272) on 2005-06-19 16:48:00 +0000
I actually don't use my Yahoo mail account either. Only for stuff life account
  
registrations, and experiments like these.

GMail is incredible of course. I don't even use Thunderbird anymore because of
  
it.

I want more industrial-strength webapps to toy around with!