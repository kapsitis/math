#!/bin/bash
if [ -z "$1" ]
then
  echo "Please specify directory"
else
#  cp $1/Pictures/*.svg $1
#  cp $1/Pictures/*.png $1

#  for file in $1/Pictures/*.svg
#  do 
#    convert $file -trim +repage $file
#  done
  for file in $1/Pictures/*.png
  do 
    convert $file -trim +repage $file
  done

fi
