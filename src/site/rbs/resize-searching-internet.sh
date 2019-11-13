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
convert $SRCDIR/venn-diagram1.png -resize 200 $DSTDIR/venn-diagram1.png
convert $SRCDIR/venn-diagram2.png -resize 200 $DSTDIR/venn-diagram2.png
convert $SRCDIR/venn-diagram3.png -resize 200 $DSTDIR/venn-diagram3.png
convert $SRCDIR/venn-diagram4.png -resize 200 $DSTDIR/venn-diagram4.png

convert $SRCDIR/caching.png -resize 400 $DSTDIR/caching.png


convert $SRCDIR/long-question.png  -resize 600 $DSTDIR/long-question.png
convert $SRCDIR/common-exceptions.png  -resize 600 $DSTDIR/common-exceptions.png

convert $SRCDIR/relevant-documents.png  -resize 350 $DSTDIR/relevant-documents.png

convert $SRCDIR/google-page-rank.png  -resize 400 $DSTDIR/google-page-rank.png
convert $SRCDIR/duckduckgo.png  -resize 400 $DSTDIR/duckduckgo.png
convert $SRCDIR/special-symbols.png  -resize 400 $DSTDIR/special-symbols.png

