from pathlib import Path
import shutil
cwd = Path.cwd() 
content_root = cwd / "collections" / "locations"

import os
import json

for mdfile in content_root.glob("**/_index.md"):
    print(mdfile)
    mdfile.rename(Path(mdfile.parent, "index.md"))