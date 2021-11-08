---
date: 2021-11-08 11:49:07
syndicated:
- type: mastodon
  url: https://mastodon.technology/users/roytang/statuses/107241331374399672
- type: twitter
  url: https://twitter.com/roytang/status/1457679520991903748/
tags:
- tech life
- software development
- python
- mastodon
title: Posting via the Mastodon API using Python
---

Some notes on posting to Mastodon via their HTTP API using Python. The backend of this site uses similar code to enable automated syndication to [my Mastodon account](https://mastodon.technology/@roytang).

### Creating an access token

- Go to your mastodon preferences (it's the gear icon above the search bar in the web interface) and click Development. (Or go to `[yourservername]/settings/applications`) 
- Click "New Application". Specify application name. Default permissions should be fine. Save.
- Click your application name in the grid on the Development page. Your access token will be in the top part of the screen.

### Posting a status (or as they call it, a "toot")

Just need to send one HTTP request. I recommend using [the `requests` library for Python.](https://docs.python-requests.org/en/latest/)

Use the token you got above as the "Bearer" in the authorization header. Post the toot contents as a "status" field to the `/api/v1/statuses` endpoint of your Mastodon server.

```python
data = { "status": "The content of your toot goes here!"}

url = "%s/api/v1/statuses" % (MASTODON_HOST)
r = requests.post(url, 
        data=data, 
        headers={'Authorization': 'Bearer %s' % (MASTODON_TOKEN)})
json_data = r.json() # you can inspect the json response to check for problems
```

### Attaching images to a toot

Fine, I'll use "toot"!

Upload your images via the `/api/v1/media` endpoint. 

The post payload should be a "file" field with `(filename, fileobject, mimetype)`. Pass the file data via the `files` parameter of `requests.post`.

For alt-text, pass a `description` field via the `data` parameter.

Get the `id` field from the json response, you'll need them when posting the toot.

You can upload up to 4 images for a single toot. You can pass the id fields as an array via the `media_ids[]` parameter when posting the toot.

```python
import requests
from pathlib import Path

# upload test files to /api/v1/media
TEST_FILES = [
    "test1.jpg",
    "test2.jpg",
    "test3.jpg",
    "test4.jpg",
]
files_root = Path("d:\\temp\\masto")
media_ids = []
for file in TEST_FILES:
    test_file = files_root / file
    data = {
        'description': 'Test file ' + file
    }
    files = {
        'file': (file, test_file.open('rb'), 'application/octet-stream')
    }
    url = "%s/api/v1/media" % (MASTODON_HOST)
    r = requests.post(url, 
        files=files, 
        headers={'Authorization': 'Bearer %s' % (MASTODON_TOKEN)})
    json_data = r.json()

    media_id = json_data['id']
    media_ids.append(media_id)

# after collecting the media ids, include them in the toot payload
data = { 
    "status": "This should be a status with multiple attached images!", 
    "media_ids[]": media_ids
}

url = "%s/api/v1/statuses" % (MASTODON_HOST)
r = requests.post(url, 
        data=data, 
        headers={'Authorization': 'Bearer %s' % (MASTODON_TOKEN)})
json_data = r.json()
```

That should be it! The [API documentation for Mastodon](https://docs.joinmastodon.org/methods/statuses/) is actually pretty straightforward so it's easy to figure out.