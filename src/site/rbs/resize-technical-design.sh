#!/bin/bash

export SRCDIR="technical-design/Pictures"
export DSTDIR="technical-design"

convert $SRCDIR/desert-picture.jpeg -resize 440 $DSTDIR/desert-picture.jpeg


