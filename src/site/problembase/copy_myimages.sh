#!/bin/bash

# scp myimages/*.png kalvis@18.193.16.199:/var/www/html/static/eliozo/images
rm -fr /Users/kapsitis/workspace-public/qualification-project/eliozoapp/eliozo/static/eliozo/images/*
cp myimages/*.png /Users/kapsitis/workspace-public/qualification-project/eliozoapp/eliozo/static/eliozo/images
