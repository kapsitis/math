#!/bin/bash

export SRCDIR="project-processes/Pictures"
export DSTDIR="project-processes"

convert $SRCDIR/chart-on-injuries.png -resize 640 $DSTDIR/chart-on-injuries.png
convert $SRCDIR/question-on-gdp.png -resize 900 $DSTDIR/question-on-gdp.png

convert $SRCDIR/interests.png -resize 840 $DSTDIR/interests.png

convert $SRCDIR/skill-self-evaluations.png -resize 840 $DSTDIR/skill-self-evaluations.png
