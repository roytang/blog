---
date: 2009-01-04 07:22:20
tags:
- royondjango
- django
- python
- software development
title: Using Django Pingback
type: post
url: /2009/01/using-django-pingback/
---

I actually had some trouble using [django-pingback][1] on my custom blog engine; the [django-pingback documentation][2] is mostly fine, but there were some caveats that I had to discover myself through a bit of debugging:

  * The URL specified for the XML-RPC endpoint in the HTML head needs to be a full absolute url including domain, i.e. http://roytang.net/xmlrpc/, which gave me trouble when I was trying to test using localhost pinging to an online server. I eventually just decided to set it up, deploy on webfaction and test it online before I redirected the domain name.
  * The documentation mentioned that the pingback handler needs to have the same arguments as the detail view for the post, so I wrote it as follows: 
    {{< highlight python >}}
# exactly same arguments as 'details' view.
def pingback_blog_handler(catslug, year, month, slug, **kwargs):
    cat = Category.objects.get(slug=catslug)
    return Post.pub_objects.get(date__year=year, date__month=month, slug=slug, category=cat, published=True)
    {{< /highlight >}}
    
    But it wasn't exactly working for me, for some reason the function wasn't being called. After some debugging I found that I needed to use named parameters for catslug, year, month, slug in the URLConf for the post permalink in order for this to work. I'm not sure if this was because I was doing it wrong or it's some sort of undocumented requirement.</li> 
    
  * The pingback client was throwing a KeyError whenever a post I made would have anchor tags without an href attribute. Granted that there isn't much point in having an <a>anchor tag without the href</a>, but the code shouldn't just choke on it. I modified the following line in client.py: 
    {{< highlight python >}}
links = [a['href'] for a in soup.findAll('a') if is_external(a['href'], url)]
    {{< /highlight >}}
        
    Adding the check for the href attribute:

    {{< highlight python >}}
links = [a['href'] for a in soup.findAll('a') if a.has_key('href') and is_external(a['href'], url)]
    {{< /highlight >}}

    
    Those are all the changes I made to get pingbacks working. I hope they're still working now, as I haven't received any pingbacks since the django version of this blog went live >.

 [1]: http://code.google.com/p/django-pingback/
 [2]: http://hg.piranha.org.ua/django-pingback/file/6ca8eadcd22d/README.md#l1