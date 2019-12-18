#!/bin/bash

export SRCDIR="tale-numtheory-jun03-crt/Pictures"
export DSTDIR="tale-numtheory-jun03-crt"

convert $SRCDIR/sequences.png -resize 800 $DSTDIR/sequences.png
convert $SRCDIR/crt-example.png -resize 400 $DSTDIR/crt-example.png
convert $SRCDIR/blankinship3.png -resize 440 $DSTDIR/blankinship3.png
convert $SRCDIR/torus-topology.png -resize 440 $DSTDIR/torus-topology.png
convert $SRCDIR/square-torus-topology.png -resize 350 $DSTDIR/square-torus-topology.png

