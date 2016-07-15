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

filters="--filter $DIR/prism_highlight.py"

echo "Running: pandoc $in -o $out $filters --template=$DIR/html/simple.html -s --smart"
pandoc $in -o $out --filter $DIR/prism_highlight.py --filter $DIR/magic_headers.py --template=$DIR/html/simple.html -s --smart

echo ""
echo "All Done. HTML file written to: $out"

chromium $out
