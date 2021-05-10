import platform
from pathlib import Path

CALIBRE_LOCATION = '/Applications/calibre.app/Contents/MacOS/ebook-convert' if platform.system() == 'Darwin' \
    else Path("C:/Program Files/calibre2/ebook-convert")
