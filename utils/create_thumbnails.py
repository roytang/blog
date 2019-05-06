from PIL import Image
from pathlib import Path
cwd = Path.cwd() 
p = cwd / "static" / "gallery"
extensions = [".png", ".jpg"]
THUMB_SUFFIX = "-thumb"
THUMB_WIDTH = 300

for ext in extensions:
    for file in p.glob("**/*" + ext):
        im = Image.open(file)
        width, height = im.size
        im.thumbnail((300, 300*height/width))
        im.save(str(file).replace(ext, THUMB_SUFFIX+ext))
        

