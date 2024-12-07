from pathlib import Path
# Proper exif rotation with PIL. Handles all the cases in https://github.com/recurser/exif-orientation-examples
from PIL import Image

cwd = Path.cwd() 
p = cwd / "collections" / "albums" / "albums" / "japan2024"
print(p)
for mdfile in p.glob("**/*.jpg"):
    filename = str(mdfile)
    image = Image.open(filename)
    exif = image._getexif()
    ORIENTATION = 274
    if exif is not None and ORIENTATION in exif:
        orientation = exif[ORIENTATION]
        method = {2: Image.FLIP_LEFT_RIGHT, 4: Image.FLIP_TOP_BOTTOM, 8: Image.ROTATE_90, 3: Image.ROTATE_180, 6: Image.ROTATE_270, 5: Image.TRANSPOSE, 7: Image.TRANSVERSE}
        if orientation in method:
            image = image.transpose(method[orientation])
    image.save(filename)
    print(filename)

if False:

    filename = "C:\\repos\\blog\\collections\\albums\\albums\\japan2024\\misdo_pikachu.jpg"
    image = Image.open(filename)
    exif = image._getexif()
    ORIENTATION = 274
    if exif is not None and ORIENTATION in exif:
        orientation = exif[ORIENTATION]
        method = {2: Image.FLIP_LEFT_RIGHT, 4: Image.FLIP_TOP_BOTTOM, 8: Image.ROTATE_90, 3: Image.ROTATE_180, 6: Image.ROTATE_270, 5: Image.TRANSPOSE, 7: Image.TRANSVERSE}
        if orientation in method:
            image = image.transpose(method[orientation])
    image.save(filename)