latexmk -pdf aidt.tex
latexmk -c
rm aidt.bbl
evince aidt.pdf
