latexmk -pdf diploma.tex
latexmk -c
rm diploma.bbl
evince diploma.pdf
