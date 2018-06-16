#!/bin/bash

# Containing directory of this file
DIR=$( dirname ${BASH_SOURCE[0]})

# Input markdown
in=$1
if [ $# -lt 1 ]; then
        echo "You need to pass the source markdown file."
        read -p "Enter markdown file: "
fi

# The output hmlt file
filename=${in##*/}
filename=${filename%.*}
out=$filename.html
if [ $# -gt 1 ]; then
        out=$2
fi

filters="--filter $DIR/minted.py"

echo "Running: pandoc $in -o $out --toc $filters --template=$DIR/html/template.html -s --smart"
pandoc $in -o $out --toc --filter $DIR/prism_highlight.py --template=$DIR/template.html -s --smart

echo ""
echo "All Done. HTML file written to: $out"

# chromimum $out