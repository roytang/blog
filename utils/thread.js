var articles = document.querySelectorAll("article");
var outText = [];
var firstUser = false;
var stopTheLoop = false;
articles.forEach(function(a) { 
    if (stopTheLoop) return;
    let t = "";
    let u = a.querySelector('div[data-testid="User-Name"] a')["href"];
    if (firstUser) {
        if (u != firstUser) {
            stopTheLoop = true;
            return;
        }
    } else {
        firstUser = u;
    }
    let s = a.querySelector('div[data-testid="tweetText"]'); 
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
console.log(outText.join("\n\n---\n\n"));