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

convert $SRCDIR/16-divisors-var1.png -resize 100 $DSTDIR/16-divisors-var1.png
convert $SRCDIR/16-divisors-var2.png -resize 300 $DSTDIR/16-divisors-var2.png
convert $SRCDIR/16-divisors-var3.png -resize 400 $DSTDIR/16-divisors-var3.png
convert $SRCDIR/16-divisors-var4.png -resize 600 $DSTDIR/16-divisors-var4.png
convert $SRCDIR/16-divisors-var5.png -resize 400 $DSTDIR/16-divisors-var5.png

convert $SRCDIR/divisors-of-60-seq.png -resize 400 $DSTDIR/divisors-of-60-seq.png
convert $SRCDIR/divisors-of-60-hasse.png -resize 400 $DSTDIR/divisors-of-60-hasse.png
convert $SRCDIR/divisors-of-36-seq.png -resize 300 $DSTDIR/divisors-of-36-seq.png
convert $SRCDIR/divisors-of-36-hasse.png -resize 300 $DSTDIR/divisors-of-36-hasse.png


convert $SRCDIR/hasse-1-to-15.png -resize 400 $DSTDIR/hasse-1-to-15.png
convert $SRCDIR/hasse-larger.png -resize 840 $DSTDIR/hasse-larger.png
convert $SRCDIR/factoring-12.png -resize 400 $DSTDIR/factoring-12.png
convert $SRCDIR/factoring-90.png -resize 700 $DSTDIR/factoring-90.png


convert $SRCDIR/venn-for-divisors.png -resize 500 $DSTDIR/venn-for-divisors.png
convert $SRCDIR/lcm-2-3-4-5-7.png -resize 600 $DSTDIR/lcm-2-3-4-5-7.png
convert $SRCDIR/lattice-10-14.png -resize 300 $DSTDIR/lattice-10-14.png
convert $SRCDIR/meet-and-join.png -resize 800 $DSTDIR/meet-and-join.png







