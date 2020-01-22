---
date: 2010-01-09 04:47:32
reply_to:
  label: '''ValueError in Django'' on stackoverflow'
  name: Wally
  type: stackexchange
  url: https://stackoverflow.com/questions/2032360/valueerror-in-django
source: stackexchange
syndicated:
- type: stackexchange
  url: https://stackoverflow.com/questions/2032360/valueerror-in-django/2032378#2032378
tags:
- python
- django
---

    urlpatterns = patterns('',     
        (r'^salaries/employee/$', list_detail.object_list, 'employee_info'),
    )

The third item in the tuple needs to be a dictionary, not a string. Try removing the single quotes around employee_info:

    urlpatterns = patterns('',     
        (r'^salaries/employee/$', list_detail.object_list, employee_info),
    )