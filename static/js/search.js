/**
 * Run event after DOM is ready
 * @param  {Function} fn Callback function
 */
var ready = function ( fn ) {

    // Sanity check
    if ( typeof fn !== 'function' ) return;

    // If document is already loaded, run method
    if ( document.readyState === 'interactive' || document.readyState === 'complete' ) {
        return fn();
    }

    // Otherwise, wait until document is loaded
    document.addEventListener( 'DOMContentLoaded', fn, false );

};

ready(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const q = urlParams.get('q');
    let searchUrl = "https://apps.roytang.net/search/?q="+q;
    let parentNode = document.getElementById("search-results");

    fetch(searchUrl)
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonResponse) {
            for (let i in jsonResponse) {
                let r = jsonResponse[i];
                let article = document.createElement("article");
                article.className = 'list_item';
                article.innerHTML = '<div class="title">' +
                    '<a class="u-url post-title" href="' + r['url'] + '"><h2 class="p-name">' + r['title'] + '</h2></a>' + 
                    '</div><div class="content">' +
                    r['highlights'] + 
                    '<p><a href="' + r['url'] + '">READ MORE</a></p></div>' +
                    '<div class="meta"><div class="meta1">' + 
                    '<p class="meta_item"><time class="dt-published">' + r['date'] + '</time></p></div></div>' 
                    ;
                parentNode.appendChild(article);
            }
        });
});