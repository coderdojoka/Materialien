#!/bin/bash

# Containing directory of this file
DIR=$( dirname ${BASH_SOURCE[0]})

# Input markdown
in=$1
if [ $# -lt 1 ]; then
        echo "You need pass the source markdown file."
        read -p "Enter markdown file: "
fi

# The output tex file
filename=${in##*/}
filename=${filename%.*}
out=$filename.tex
if [ $# -gt 1 ]; then
        out=$2
fi

# we save all the output here
output=tmp_latex
if [ $# -gt 2 ]; then
        output=$3
fi

mkdir $output


echo "Running: pandoc $in --filter $DIR/magic_headers.py --filter $DIR/minted.py -o $output/$out --template=$DIR/pandoc_template.tex --variable vorlagen_pfad=$DIR/.. -s --smart"
pandoc $in --filter $DIR/magic_headers.py --filter $DIR/minted.py -o $output/$out --template=$DIR/pandoc_template.tex --variable vorlagen_pfad=$DIR/.. -s --smart

echo "Running: pdflatex -output-dir=$output -interaction=nonstopmode -shell-escape $output/$out > $output/compile.log"
pdflatex -interaction=nonstopmode -output-dir=$output -shell-escape $output/$out > $output/compile.log



# Get the pdfs from the output dir
mv $output/$filename.pdf .

echo ""
echo "Done. Your temp files have been written to: $output"

# evince $filename.pdf & > /dev/null