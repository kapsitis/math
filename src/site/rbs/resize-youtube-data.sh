#!/bin/bash

export SRCDIR="youtube-data/Pictures"
export DSTDIR="youtube-data"

convert $SRCDIR/analytics-demography.png -resize 700 $DSTDIR/analytics-demography.png

convert $SRCDIR/analytics-devices.png -resize 700 $DSTDIR/analytics-devices.png
convert $SRCDIR/analytics-piechart.png -resize 400 $DSTDIR/analytics-piechart.png

convert $SRCDIR/analytics-timeline.png -resize 700 $DSTDIR/analytics-timeline.png


convert $SRCDIR/beata-jonite.png -resize 400 $DSTDIR/beata-jonite.png
convert $SRCDIR/lv-tv-ratings.png -resize 450 $DSTDIR/lv-tv-ratings.png


convert $SRCDIR/minutes-spent-per-day.png -resize 600 $DSTDIR/minutes-spent-per-day.png

convert $SRCDIR/poster.png -resize 400 $DSTDIR/poster.png

convert $SRCDIR/remarketing.jpg -resize 500 $DSTDIR/remarketing.jpg


convert $SRCDIR/youtube-go-to-studio.png -resize 250 $DSTDIR/youtube-go-to-studio.png
convert $SRCDIR/youtube-analytics-page.png -resize 400 $DSTDIR/youtube-analytics-page.png

convert $SRCDIR/lab01-screenshot01.png -resize 300 $DSTDIR/lab01-screenshot01.png
convert $SRCDIR/lab01-screenshot02.png -resize 300 $DSTDIR/lab01-screenshot02.png
convert $SRCDIR/lab01-screenshot03.png -resize 300 $DSTDIR/lab01-screenshot03.png
convert $SRCDIR/lab01-screenshot04.png -resize 300 $DSTDIR/lab01-screenshot04.png



