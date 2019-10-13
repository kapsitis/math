#!/bin/bash

export SRCDIR="knitr-intro/Pictures"
export DSTDIR="knitr-intro"


convert $SRCDIR/excel-data-set.png -resize 600 $DSTDIR/excel-data-set.png

