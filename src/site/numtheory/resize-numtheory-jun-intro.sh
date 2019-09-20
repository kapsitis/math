#!/bin/bash

export SRCDIR="tale-numtheory-jun-intro/Pictures"
export DSTDIR="tale-numtheory-jun-intro"

convert $SRCDIR/number-sets.png -resize 600 $DSTDIR/number-sets.png
convert $SRCDIR/white-table.png -resize 900 $DSTDIR/white-table.png
convert $SRCDIR/color-table.png -resize 900 $DSTDIR/color-table.png
convert $SRCDIR/build-pentagon.jpg -resize 450 $DSTDIR/build-pentagon.jpg
convert $SRCDIR/inclusion-exclusion.png -resize 800 $DSTDIR/inclusion-exclusion.png

convert $SRCDIR/induction-deduction.png -resize 400 $DSTDIR/induction-deduction.png

convert $SRCDIR/necklace-proof.png -resize 300 $DSTDIR/necklace-proof.png
convert $SRCDIR/vo_1985_9_5_01.png -resize 500 $DSTDIR/vo_1985_9_5_01.png
