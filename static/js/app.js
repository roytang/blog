$(document).ready(() => {
    // spoiler tags
    $(".spoiler_header").click(function () {
        $(this).next().toggle();
        console.log($(this));
        console.log($(this).next());
    });
});