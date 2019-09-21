#!/bin/bash

export SRCDIR="tale-numtheory-jun01-divisibility/Pictures"
export DSTDIR="tale-numtheory-jun01-divisibility"

convert $SRCDIR/lattice-of-divisors.png -resize 400 $DSTDIR/lattice-of-divisors.png
convert $SRCDIR/remainders-in-python.png -resize 400 $DSTDIR/remainders-in-python.png
convert $SRCDIR/divisors-of-60.png -resize 400 $DSTDIR/divisors-of-60.png

convert $SRCDIR/pi-counting-function.png -resize 400 $DSTDIR/pi-counting-function.png
convert $SRCDIR/natural-logarithm.png -resize 400 $DSTDIR/natural-logarithm.png
convert $SRCDIR/marcis-bendiks.png -resize 500 $DSTDIR/marcis-bendiks.png

convert $SRCDIR/ulam-spiral.png -resize 400 $DSTDIR/ulam-spiral.png
convert $SRCDIR/eratosthenes.png -resize 400 $DSTDIR/eratosthenes.png


