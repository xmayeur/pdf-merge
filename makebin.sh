#!/bin/sh
rm -fr ./dist ./build
# create the .app file
pyinstaller  --onedir \
 --noconfirm \
 --icon icon.png \
 pdf-merge.py

sudo rm /usr/local/bin/pdf-merge
sudo ln -s /Users/xavier/PycharmProjects/pdf-zip/dist/pdf-merge/pdf-merge /usr/local/bin/pdf-merge