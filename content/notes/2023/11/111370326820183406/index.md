---
date: 2023-11-07 16:58:44+00:00
dontinlinephotos: true
reply_to:
  label: www.jvt.me's toot
  name: www.jvt.me
  type: mastodon
  url: https://fed.brid.gy/r/https://www.jvt.me/mf2/2023/11/imcyu/
source: mastodon
syndicated:
- type: mastodon
  url: https://indieweb.social/users/roytang/statuses/111370326820183406
tags:
- www.jvt.me
- wwwjvtme
- replies
---

<p><span class="h-card" translate="no"><a href="https://fed.brid.gy/r/https://www.jvt.me" class="u-url mention">@<span>www.jvt.me</span></a></span> dont have time to test it or anything, but something like this would probably work:</p>

```sql
select repo, 
  sum(case when advisory_type="SECURITY" then total_advisories else 0 end) as total_security,
  sum(case when advisory_type="DEPRECATED" then total_advisories else 0 end) as total_deprecated,
  sum(case when advisory_type="UNMAINTAINED" then total_advisories else 0 end) as total_unmaintained
from (
  your original big query
)
group by repo
```