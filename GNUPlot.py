import PyGnuplot as gp
import numpy as np
import sys
name = sys.argv[1]
gp.c('set xdata time')
gp.c('set timefmt "%d-%b-%Y %H:%M:%S"')
gp.c('plot "{}.dat" using 2:4 w line'.format(name))
