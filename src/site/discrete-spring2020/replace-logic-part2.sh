#!/bin/bash
echo "Converting images..."

export SRCDIR="tale-logic-part1/Pictures"
export DSTDIR="tale-logic-part1"

convert $SRCDIR/game-of-15.jpg -resize 400  $DSTDIR/game-of-15.jpg

