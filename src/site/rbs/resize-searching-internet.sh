#!/bin/bash

export SRCDIR="searching-internet/Pictures"
export DSTDIR="searching-internet"


convert $SRCDIR/incognito-mode.png -resize 700 $DSTDIR/incognito-mode.png
convert $SRCDIR/browser-history.png -resize 600 $DSTDIR/browser-history.png

convert $SRCDIR/youtube-search-filters.png -resize 640 $DSTDIR/youtube-search-filters.png
convert $SRCDIR/regex-char-groups.png -resize 400 $DSTDIR/regex-char-groups.png
convert $SRCDIR/char-groups-result.png -resize 100 $DSTDIR/char-groups-result.png

convert $SRCDIR/mountain-line1.png -resize 400 $DSTDIR/mountain-line1.png
convert $SRCDIR/mountain-line2.png -resize 400 $DSTDIR/mountain-line2.png

convert $SRCDIR/prestotuneup.jpg -resize 400 $DSTDIR/prestotuneup.jpg


convert $SRCDIR/caching.png -resize 400 $DSTDIR/caching.png



