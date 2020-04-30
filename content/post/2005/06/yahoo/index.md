---
categories: []
date: 2005-06-16 16:21:00
source: roywantsmeat
syndicated:
- type: blogger
  url: https://roywantsmeat.blogspot.com/2005/06/yahoo.html
tags:
- Software Development
title: Yahoo!
type: post
url: /2005/06/yahoo/
---

Some comments on the Yahoo webapps.

  * The next/previous links on top of Yahoo mail messages are confusing. I'm not sure if they take me up or down the mail-list. Gmail is better, since it explicitly says "older" and "newer"; With Yahoo, I'm always wrong when I guess. After some experimenting, I figure it out. "Next" and "Previous" are based on the sort order in the list of messages. Since the default is sorted by date descending (newest first), "Next" corresponds to Yahoo's "older" by default. Which is kind of hard to figure intuitively. 
  * In the grid that lists mail messages, I wanted to test if the columns would wrap any words that were too long. Multiple observations here:
      * As part of this experiment, I wanted to create an email address with a very long name. Apparently, the Yahoo ID "abcdefghijklmnopqrstuvwxyz012345" was already taken. I settled on "solongandthanksforallthefish2005@yahoo.com". You can send the account mail if you like. 
      * There's a UI bug in the password verification screen if the Yahoo ID is too long. The gray box on the left has its right border broken. 
      * Bummer. I didn't realize the value in the sender column was the name in the Yahoo profile instead of the actual email address. I update the account name to `AllTheThingsSheKeepsInsideAreTheThingsThatReallyMatterTheFacePutsOnItsBestDisguiseAndAllIsWellUntilT heHeartBetraysLordBringOutTheLightWrapItAllAroundMeLetItHoldMeTightSoakUpAllThatIBleedLordBringOutTh eLightWrapItAllAroundMeLetItHoldMeTightSoakUpAllThatIBleedIBleedWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWX`
  
        which breaks even more layouts, including this one (mental note: fix that tomorrow). 
      * Doh! I actually had to change the Outgoing name, which was set to the original account name. Why doesn't it update the mail setting when I change the (global) Yahoo account setting? Updated it to "AllTheThingsSheKeepsInsideAreT" 
      * I sent some mail messages with the long name and a long subject line. As I suspected... Yahoo compensates for the unwrappable words by expanding the grid cell, breaking the layout. This was a problem I encountered before in the webapps at workand I still don't have a solution that would work in all browsers. 
  * I'm also interested in how popular webapps handle timestamping, so I try this out as well. For the uninformed, timestamping means handling the case where two people both try to edit the same record at roughly the same time. If there's no handling, the person who updates first usually has his changes lost, without any notification.</p> 
      * I try it out first with Yahoo Address Book and Notepad. Both experiments fail... there's no timestamping. I tested it by opening a record (Address Book entry/Notepad note) for updating in two separate Firefox tabs. I update one tab and save, then update the second tab and save. Changes made in the first tab are lost. 
      * Well, I guess that's okay, since technically, only one person at a time is expected to access these webapps. So I do something else. I create [a Yahoo Group][1] . I get two moderators, me and a dummy email account. I login with both accounts, using Firefox for one and IE for the other. I try to update the group description with one account, then the other. Bam! First guy's changes are lost, without notification! If this were some sort of mission-critical webapp, that would be a dangerous bug. 

I'm sleepy. More later.

 [1]: http://groups.yahoo.com/group/roytang/