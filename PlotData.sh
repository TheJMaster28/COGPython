#!/bin/bash

#echo 'plotting User% Data'
#gnuplot -e "set xdata time; set timefmt '%d-%b-%Y %H:%M:%S'"
#gnuplot  -e "plot '$1.dat' using 2:4 w line; pause -1"

# set xdata time
# set timefmt "%d-%b-%Y %H:%M:%S"
# plot '.dat' using 2:4 w line
# pause -1

file_name=$1
command_name=$2
echo $command_name
if [[ "$command_name" = "user" ]]; then
	gnuplot -e "file='$file_name'" plotUserCPU.p	
fi 


