"""
By default, FreeType supports the following font formats.

TrueType fonts (TTF) and TrueType collections (TTC)
CFF fonts
WOFF fonts
OpenType fonts (OTF, both TrueType and CFF variants) and OpenType collections (OTC)
Type 1 fonts (PFA and PFB)
CID-keyed Type 1 fonts
SFNT-based bitmap fonts, including color Emoji
X11 PCF fonts
Windows FNT fonts
BDF fonts (including anti-aliased ones)
PFR fonts
Type 42 fonts (limited support)
"""

import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(cur_dir)
sys.path.append(cur_dir)

os.environ["PATH"] = os.path.join(cur_dir, "dll") + os.pathsep + os.environ["PATH"]

# ./python.exe -m virtualenv freetype_env
# ./freetype_env/Scripts/activate.bat
# ./python.exe -m pip install freetype-py
# ./python.exe -m pip install pillow

import freetype
from PIL import Image, ImageOps

face = freetype.Face("./test/1.ttf")

face.set_char_size(48 * 64)
face.load_char("S")


bitmap = face.glyph.bitmap
image = Image.frombytes("L", (bitmap.width, bitmap.rows), bytes(bitmap.buffer))
image = ImageOps.invert(image)
image = image.convert("RGBA")
print(image.save("S.png"))
