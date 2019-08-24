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
    if (q) {
        let searchUrl = "https://apps.roytang.net/blog/search/?q="+q;
        let parentNode = document.getElementById("search-results");
        document.getElementById("search-criteria").innerText = q;

        fetch(searchUrl)
            .then(function(response) {
                return response.json();
            })
            .then(function(jsonResponse) {
                let h = "";
                if (jsonResponse.length == 0) {
                    h += "Sorry, your search got no results!";
                }
                parentNode.innerText = h;
                for (let i in jsonResponse) {
                    let r = jsonResponse[i];
                    let article = document.createElement("article");
                    article.className = 'list_item';
                    let html = "";
                    if (r['title'] && r['title'] != 'None') {
                        html = html + '<div class="title">' +
                        '<a class="u-url post-title" href="' + r['url'] + '"><h2 class="p-name">' + r['title'] + '</h2></a>' + 
                        '</div>';
                    }
                    html = html + '<div class="content">' +
                        r['highlights'] + 
                        '<p><a href="' + r['url'] + '">View ' + r['content_type'] + '</a></p></div>' +
                        '<div class="meta"><div class="meta1">' + 
                        '<p class="meta_item"><time class="dt-published">' + r['date'] + '</time></p></div></div>' 
                        ;
                    article.innerHTML = html;
                    parentNode.appendChild(article);
                }
            });
    } else {
        document.getElementById("search-container").innerHTML = "How did you get here? Type your search into the text box above!";
    }
});