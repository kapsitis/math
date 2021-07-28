#!/bin/bash
if [ -z "$1" ]
then
  echo "Please specify directory"
else  

#  if [ "$(ls -A $1/Pictures)" ]; then
  if ls $1/Pictures/*.png &>/dev/null; then
    for file in $1/Pictures/*.png
    do 
      convert $file -trim +repage $file
    done
  fi

  murr=$(echo "${1/tale/replace}"|sed 's#/##g')
  if test -f "${murr}.sh"; then
    source ${murr}.sh
  fi

  cd $1
  pandoc -t revealjs -s -o content.html content.md --slide-level=2 \
    -V revealjs-url=../../reveal.js --metadata pagetitle="Uzdevumi" \
    --mathjax="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" \
    -V theme="white"
fi



