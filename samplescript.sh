#!/bin/bash
>&2 echo "stderr stream..."
echo "stdout stream..."
pandoc -t revealjs -s -o content.html content.md --slide-level=2 \
    -V revealjs-url=../../reveal.js --metadata pagetitle="Uzdevumi" \
    --mathjax="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" \
    -V theme="white"