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
    $('.pxgallery').photobox('a',{ thumbs: true, time:0 });

    // populate collections gallery
    $('.collections_list li').each(function() {
        let thisElement = $(this);
        let dataUrl = thisElement.find("a").attr("href") + "data.json";
        console.log(dataUrl);

        $.getJSON( dataUrl, function( data ) {
            thisElement.append(" (" + data["count"] + ")")
        });
    })
});