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
});