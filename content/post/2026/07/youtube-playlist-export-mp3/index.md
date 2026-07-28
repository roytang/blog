---
title: "Exporting a Youtube Playlist to MP3s"
date: 2026-07-28T20:51:51+08:00
tags:
- youtube
---

Writing this post mostly so I can refer to it again later if needed.

A while back I taught my dad how to save YT videos he watches on TV to a playlist and he watches a lot of music and recently he asked me if I could export his playlist to mp3s and put them on a flash drive so he can play them in his car. (Do not suggest that I teach him how to use an app like Spotify instead, he is very tech unsavvy, its basically impossible.)

I was like okay, that should be easy, I can just use `yt-dlp`. When I checked the actual playlist to be exported, it turns out the playlist has SEVEN HUNDRED ENTRIES!! Lol okay, I tried `yt-dlp` anyway, but it turns out there's [a bug where it can only process the first 100 items of a playlist](https://github.com/yt-dlp/yt-dlp/issues/11130). This is regardless of any other filtering or offset parameters, there was no way around it. 

It does support exporting from a list of URLs in a file though, so second option: scrape the individual URLs from the playlist page using JavaScript:

```javascript
// load the playlist screen and scroll to the end then run this in console
var myList = document.querySelectorAll("a.ytLockupMetadataViewModelTitle");

var output = "";
for (var i=0; i<myList.length; i++) {
  var item = myList[i];
  output = output + item.href.split("&list")[0];
  output = output + "\n";
}

console.log(output);
```

Then I just place the logged list into a file, and ran `yt-dlp` with the following parameters:

`yt-dlp -a list.txt --audio-format mp3 --no-overwrites -t sleep -x`

A breakdown:

- `-a list.txt`: specify the list of URLs to download
- `--audio-format mp3`: specify the output audio format
- `--no-overwrites`: skip already downloaded files (makes resuming a partial run easier)
- `-t sleep`: needed to minimize the chance of hitting YT rate limits
- `-x`: download audio only. In this case, the entire video will still be downloaded then extracted to audio then the video file will be deleted. So it still uses up bandwidth, but less disk space in the end.

That's it! It took me a few tries to download the entire list and it took quite a while, but eventually I got all 700+ items. Hopefully they fix that bug linked to above so that I can just skip the whole scraping part of this.
