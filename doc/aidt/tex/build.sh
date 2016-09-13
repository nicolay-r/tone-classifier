gnuplot plots/cost_measurment.plt
latexmk -pdf aidt.tex
latexmk -c
rm -rf aidt.bbl
evince aidt.pdf
