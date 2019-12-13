#!/bin/bash

export SRCDIR="tale-numtheory-jun03-crt/Pictures"
export DSTDIR="tale-numtheory-jun03-crt"

convert $SRCDIR/sequences.png -resize 800 $DSTDIR/sequences.png
convert $SRCDIR/crt-example.png -resize 400 $DSTDIR/crt-example.png



