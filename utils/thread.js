var articleSelector = "article";
var usernameSelector = 'div[data-testid="User-Name"] a';
var textSelector = 'div[data-testid="tweetText"]';

// wayback version
articleSelector = "div.ThreadedConversation-tweet";
usernameSelector = "a.js-user-profile-link";
textSelector = "p.tweet-text";

var articles = document.querySelectorAll(articleSelector);
var outText = [];
var firstUser = false;
var stopTheLoop = false;
articles.forEach(function(a) { 
    console.log(a);
    if (stopTheLoop) return;
    let t = "";
    let u = a.querySelector(usernameSelector)["href"];
    if (firstUser) {
        if (u != firstUser) {
            stopTheLoop = true;
            return;
        }
    } else {
        firstUser = u;
    }
    let s = a.querySelector(textSelector); 
    if (s) {
        t = s.innerText.replaceAll("\n", "\n\n");
    }
    let p = a.querySelector('div[data-testid="tweetPhoto"]'); 
    if (p) {
        t = t + "\n\n[image]"
    }
    let v = a.querySelector('div[data-testid="videoComponent"]'); 
    if (v) {
        t = t + "\n\n[video or gif]"
    }
    outText.push(t);
})
outText = outText.join("\n\n---\n\n");
console.log(outText);
outText;