---
date: 2009-02-14 14:17:32
tags:
- royondjango
- django
- python
- software development
title: Stylesheet Switcher using Django
type: post
url: /2009/02/stylesheet-switcher-using-django/
---

You may have noticed the new color scheme and new "Theme Switcher" widget in the sidebar. I had done some CSS work during the past month in the office and it made me want to tweak the stylesheets on this site a bit. I figured I might as well make it easy to switch stylesheets, so I wrote a small Theme Switcher django app. (Well, it's more of a stylesheet switcher I guess)

The model is simple:

{{< highlight python >}}
class Theme(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=250)
    css_path = models.CharField(max_length=500)

    def __str__(self):
        return self.title
{{< /highlight >}}        

I only needed one view -- to switch the current theme.

Added the ff to urls.py:

{{< highlight python >}}
(r'^theme/([a-zA-Z0-9\-]+)/', 'themer.views.switch'),
{{< /highlight >}}        

The view code simply stores the selected theme as a cookie:

{{< highlight python >}}
def switch(request, theme_slug):
  """ Sets a cookie to specify the new theme, then redirects to the referer or root url """
  theme = get_object_or_404(Theme, slug=theme_slug)
  referer = "/"
  if "HTTP_REFERER" in request.META:
    referer = request.META["HTTP_REFERER"]
  resp = HttpResponseRedirect(referer)
  resp.set_cookie("theme", theme_slug, 100000)
  return resp
{{< /highlight >}}

To load the stylesheet, I set up a [context processor][1] to pass both the current theme and the list of themes to the context. I wanted to do this using template tags, but I couldn't figure out how to extract a cookie from within a template tag.

{{< highlight python >}}
from themer.models import Theme
def context_processor(request):
    theme_list = Theme.objects.all()
    if "theme" in request.COOKIES:
        slug = request.COOKIES["theme"]
        try:
            theme = Theme.objects.get(slug=slug)
        except Theme.DoesNotExist:
            theme = None
    else:
        if theme_list.count() > 0:
            theme = theme_list[0]
        else:
            theme = None
    return {"current_theme" : theme, "theme_list" : theme_list}
{{< /highlight >}}

Then in my base template file, I add the following to the head section:

{{< highlight html >}}
<link rel="stylesheet" href="{{ current_theme.css_path }}" type="text/css" />
{{< /highlight >}}

And add the list of themes into the sidebar.

{{< highlight html >}}
<h2>Theme Switcher</h2>
<ul>
            {% for theme in theme_list %}
            <li>
            {% ifequal theme.slug current_theme.slug %}
            {{ theme.title }} <span class="note">(current)</span>
            {% else %}
            <a href="{% url themer.views.switch theme.slug %}" title="Switch to {{ theme.title }} theme">{{ theme.title }}</a>
            {% endifequal %}
            </li>
            {% endfor %}
            </ul>
{{< /highlight >}}

And we're done!

Of course, I'm still not particularly strong in web design, so the two current "themes" really just switch around the color scheme. The light blue theme is named Azorius, while the old black and green theme is named Golgari, both named after the respective color guilds in Magic: The Gathering's Ravnica block.

Hopefully this gives me a chance to whip up more interesting themes and polish the old CSS skills some more. Enjoy!

 [1]: http://www.b-list.org/weblog/2006/jun/14/django-tips-template-context-processors/ "Django tips: Template context processors by James Bennet"