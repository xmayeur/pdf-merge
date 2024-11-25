 #!/bin/sh
 rm -fr ./dist ./build
# create the .app file
 pyinstaller -F \
 --noconfirm \
 --icon icon.png \
 pdf-merge.py

