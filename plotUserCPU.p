String1 =  sprintf('dat_files/%s.dat', file)
stats String1 using 4
set xdata time
set timefmt "%d-%b-%Y %H:%M:%S"
set format x "%d-%b-%Y %H:%M:%S"
set logscale y
set xlabel 'Time'
set ylabel 'User%'

plot String1 u 2:4 w linespoints ls 1 t file 
pause -1
