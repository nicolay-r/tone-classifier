latexmk -pdf aidt.tex
latexmk -c
rm -rf aidt.bbl
xreader aidt.pdf
