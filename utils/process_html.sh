#!/bin/bash
# Author: Sachin Yadav
for filepath in ./_notebooks/*.ipynb; do
    # echo $filepath
    filename=$(basename ${filepath})
    # echo $filename
    basename=${filename%.ipynb}
    # echo $basename
    python3 utils/style_html.py ./_html/$basename.html ./_html/$basename.html
done
