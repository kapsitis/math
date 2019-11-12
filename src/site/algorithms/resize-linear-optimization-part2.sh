#!/bin/bash

export SRCDIR="tale-linear-optimization-part2/Pictures"
export DSTDIR="tale-linear-optimization-part2"

convert $SRCDIR/max-flow-graph.png -resize 500 $DSTDIR/max-flow-graph.png
convert $SRCDIR/hamiltonian_path_3d.png -resize 350 $DSTDIR/hamiltonian_path_3d.png
convert $SRCDIR/flow-preservation.png -resize 350 $DSTDIR/flow-preservation.png
convert $SRCDIR/elipsoid-algorithm.png -resize 400 $DSTDIR/elipsoid-algorithm.png


