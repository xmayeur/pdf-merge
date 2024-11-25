#!/bin/sh
 rm -fr ./dist ./build
# create the .app file
pyinstaller --onedir --windowed \
--noconfirm \
--icon icon.png \
pdf-merge.py

sudo rm /usr/local/bin/pdf-merge/pdf-merge
sudo ln -s /Users/xavier/PycharmProjects/pdf-zip/dist/pdf-merge.app/Contents/MacOS/pdf-merge /usr/local/bin/pdf-merge

exit (0)
# --collect-submodules  './pdf-merge.py' \
# --collect-submodules  './get_secrets.py' \
# --hidden-import='tkinter' \
# --hidden-import='PIL._tkinter_finder' \

# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r dist/pdfmerge.app dist/dmg
# If the DMG already exists, delete it.
test -f "dist/pdfmerge.dmg" && rm "dist/pdfmerge.dmg"
create-dmg \
  --volname "pdfmerge" \
  --volicon "icon.icns" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --hide-extension "pdfmerge.app" \
  --app-drop-link 425 120 \
  --icon "pdfmerge.app" 120 120 \
  "dist/pdfmerge.dmg" \
  "dist/dmg/"

#   --icon "pdfmerge" 120 120 \
