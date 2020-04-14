# COGPython

Gets data from sample file and organizes to a .dat file for gnuplot to read

to run, use `python ReadData.py <filename>`

GNUPlot commands to plot:

```set xdata time
set timefmt "%d-%b-%Y %H:%M:%S"
plot 'dijkstra.dat' using 2:4 w line
```
