$(document).ready(() => {
    // spoiler tags
    $(".spoiler_header").click(function () {
        $(this).next().toggle();
        console.log($(this));
        console.log($(this).next());
    });

    // load pocket rss feed
    if ($('.feed_container').length) {
        $(document).ready(function() {
            //feed to parse
            var feed = "/links.xml";
            $.ajax(feed, {
                accepts:{
                    xml:"application/rss+xml"
                },
                dataType:"xml",
                success:function(data) {
                    //Credit: http://stackoverflow.com/questions/10943544/how-to-parse-an-rss-feed-using-javascript
                    $('.feed_container').append("<ul></ul>");
                    $(data).find("item").each(function () { // or "item" or whatever suits your feed

                        var el = $(this);
                        let a  = document.createElement("a");
                        $(a).attr("href", el.find("link").text());
                        $(a).attr("target", "new");
                        $(a).html(el.find("title").text());
                        let li = document.createElement("li");
                        $(li).append(a);
                        $(li).append("&nbsp;<small>" + el.find("pubDate").text() + "</small>");
                        $('.feed_container ul').append(li);
                    });
                }	
            });
        });        
    }
});