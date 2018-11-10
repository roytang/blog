from pathlib import Path
import urllib.request

remote_url = "https://getpocket.com/users/hungryroy/feed/all"

# imports a feed into a local xml, so it can be parsed by JS without CORS issues
# (I realize I could just generate the links page directly via md here, but I didn't want to add a feedparser dependency)
def import_feed():
    mystr = ""
    with urllib.request.urlopen(remote_url) as fp:
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

    cwd = Path.cwd() 
    p = cwd / "content" / "links.xml"
    with p.open("w", encoding="utf8") as f:
        f.write(mystr)

import_feed()