reset
set key outside
set key right top
set grid
set xrange [0.1:1]
set xtics 0.1,0.1,1
set yrange [0.34:0.48]
set ytics 0.34,0.01,0.48
set xlabel "SVM 'Cost' Parameter Value"
set ylabel "Fmacro(neg, pos)"

plot "sentirueval_2015_balanced.dat" using 1:2 with linespoints title "BANK_01", \
    "sentirueval_2015_balanced.dat" using 1:3 with linespoints title "BANK_02", \
    "sentirueval_2015_balanced.dat" using 1:4 with linespoints title "BANK_03", \
    "sentirueval_2015_balanced.dat" using 1:5 with linespoints title "BANK_04", \
    "sentirueval_2015_balanced.dat" using 1:6 with linespoints title "BANK_05"
pause -1

set term png
set output "sentirueval_2015_bank_balanced.png"
replot
