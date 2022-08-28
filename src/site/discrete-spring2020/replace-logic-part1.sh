#!/bin/bash
echo "Converting images..."


export SRCDIR="tale-logic-part1/Pictures"
export DSTDIR="tale-logic-part1"

convert $SRCDIR/willy-pogany-mephistopheles-and-student.png -resize 300 $DSTDIR/willy-pogany-mephistopheles-and-student.png

convert $SRCDIR/broccoli.png -resize 300 $DSTDIR/broccoli.png


