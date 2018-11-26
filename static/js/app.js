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

    let elements = document.querySelectorAll(".spoiler_header");
    Array.prototype.forEach.call(elements, function(el, i) {
        el.addEventListener( 'click', function( event ) {
            let nextEl = el.nextElementSibling;
            let display = getComputedStyle(nextEl)['display'];
            if (display == 'none') {
                nextEl.style.display = 'block';
            } else {
                nextEl.style.display = 'none';
            }
        }, false);        
    });

    // load pocket rss feed
    let container = document.querySelector('.feed_container');
    if (container) {
        //feed to parse
        let feed = "/links.xml";

        // vanillaJS ajax example: http://youmightnotneedjquery.com/
        var request = new XMLHttpRequest();
        request.open('GET', feed, true);
        request.onload = function() {
          if (request.status >= 200 && request.status < 400) {
            // dom parser example: https://www.hongkiat.com/blog/rss-reader-in-javascript/
            var domParser = new DOMParser();
            let doc = domParser.parseFromString(request.responseText, 'text/xml');
            doc.querySelectorAll('item').forEach( (item) => {
                let a  = document.createElement("a");
                a.setAttribute("href", item.querySelector('link').textContent);
                a.setAttribute("target", "new");
                a.innerHTML = item.querySelector('title').textContent;
                let li = document.createElement("li");
                li.appendChild(a);
                li.innerHTML = li.innerHTML + "&nbsp;<small>" + item.querySelector('pubDate').textContent + "</small>";
                container.appendChild(li);
            });
          } else {
              console.log("Error parsing the XML file.");
          }
        };
        
        request.onerror = function() {
          console.log("Error parsing the XML file: There was a connection error of some sort");
        };
        
        request.send();
        
        
        // $.ajax(feed, {
        //     accepts:{
        //         xml:"application/rss+xml"
        //     },
        //     dataType:"xml",
        //     success:function(data) {
        //         //Credit: http://stackoverflow.com/questions/10943544/how-to-parse-an-rss-feed-using-javascript
        //         $('.feed_container').append("<ul></ul>");
        //         $(data).find("item").each(function () { // or "item" or whatever suits your feed

        //             var el = $(this);
        //             let a  = document.createElement("a");
        //             $(a).attr("href", el.find("link").text());
        //             $(a).attr("target", "new");
        //             $(a).html(el.find("title").text());
        //             let li = document.createElement("li");
        //             $(li).append(a);
        //             $(li).append("&nbsp;<small>" + el.find("pubDate").text() + "</small>");
        //             $('.feed_container ul').append(li);
        //         });
        //     }	
        // });
    }
});