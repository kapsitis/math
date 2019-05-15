#!/bin/bash
if [ -z "$1" ]
then
  echo "Please specify directory"
else
  cp $1/Pictures/*.svg $1
  for file in $1/*.svg
  do 
    convert $file -trim +repage $file
  done
fi
