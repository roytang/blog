import json
from pathlib import Path
from datetime import datetime
import frontmatter
import re
import string
from urllib.parse import urlparse, parse_qs, urldefrag
from urllib.error import HTTPError
import urllib.request

with Path("d:\\temp\\anchors.json").open() as f:
    anchors = json.loads(f.read())
with Path("d:\\temp\\anchors-map.json").open() as f:
    anchors_map = json.loads(f.read())

idx = 0
for anchor in anchors:
    try:
        headers = {'cookie': ''} # paste the cookie here
        print(anchor)
        if anchor in anchors_map:
            print("skip")
            continue
        req = urllib.request.Request(anchor, headers=headers)
        response = urllib.request.urlopen(req)
        # print(response.geturl())
        anchors_map[anchor] = response.geturl()
        idx = idx + 1
        # if idx > 5:
        #     break
    except:
        break

print(idx)

with Path("d:\\temp\\anchors-map.json").open("w") as f:
    f.write(json.dumps(anchors_map, indent=2))

def replaces_values(name, listValues, index)
  if index = 0:
      return name
  if (name = '${' + index + '}'):
    newvalue = listValues[0]
  else
    // slice returns the list minus the first N elemments
    replaces_values(name, listValues.slice(1), index+1) 
  end
  return 'newvalue'
end