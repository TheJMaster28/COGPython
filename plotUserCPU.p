stats 'dat_files/dijkstra.dat' using 4
set xdata time
set timefmt "%d-%b-%Y %H:%M:%S"
set format x "%d-%b-%Y %H:%M:%S"
set xlabel 'Time'
set ylabel 'User%'
plot 'dat_files/dijkstra.dat' u 2:4 w linespoints ls 1 t 'dijkstra', '' u 2:(STATS_mean) w l lt 4 lw 4 t 'Avg User%'
pause -1
