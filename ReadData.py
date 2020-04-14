# to run, use python ReadData.py <filename>
import sys
import re
import os.path as path
file = sys.argv[1]
f = open(file, "r")
name = ''
for line in f:

    pattern = re.compile('[a-zA-z]+ nmon:')
    l = pattern.findall(line)
    if l:
        x = l[0].split(' ')
        # print(x)
        if (path.exists('{}.dat'.format(x[0]))):

            data = open(x[0] + '.dat', 'a')
        else:
            data = open(x[0] + '.dat', 'w')
            data.write("# Name      Date      Time      User%      Sys%      Wait%      Idle%      Steal%      Busy      CPUs      memtotal      hightotal      lowtotal      swaptotal      memfree      highfree      lowfree      swapfree      memshared      cached      active      bigfree      buffers      swapcached      inactive\n")

    # Writes key as a comment for .dat file for gnuplot
    # gets CPU key first
    pattern = re.compile(
        'CPU_ALL,CPU Total [a-zA-Z]+,User%,Sys%,Wait%,Idle%,Steal%,Busy,CPUs')
    l = pattern.findall(line)
    if l:

        continue

    # gets MEM key after CPU key
    pattern = re.compile(
        'MEM,Memory MB [a-zA-Z]+,memtotal,hightotal,lowtotal,swaptotal,memfree,highfree,lowfree,swapfree,memshared,cached,active,bigfree,buffers,swapcached,inactive')
    l = pattern.findall(line)
    if l:

        continue

    # gets time, date, and name of sample
    pattern = re.compile('ZZZZ,(.*)')
    l = pattern.findall(line)
    if l:
        x = l[0].split(",")
        # print(x)
        name = x[0]
        time = x[1]
        date = x[2]

    # gets CPU sample data
    pattern = re.compile('CPU_ALL,{},(.*)'.format(name))
    l = pattern.findall(line)
    if l:
        x = l[0].split(',')
        # print(x)
        user = x[0]
        sys = x[1]
        wait = x[2]
        idle = x[3]
        steal = x[4]
        busy = x[5]
        if busy == '':
            busy = "0"
        cores = x[6]

    # GETS MEM sample data
    pattern = re.compile('MEM,{},(.*)'.format(name))
    l = pattern.findall(line)
    if l:
        x = l[0].split(',')
        # print(x)
        memtotal = x[0]
        hightotal = x[1]
        lowtotal = x[2]
        swaptotal = x[3]
        memfree = x[4]
        highfree = x[5]
        lowfree = x[6]
        swapfree = x[7]
        memshared = x[8]
        cached = x[9]
        active = x[10]
        bigfree = x[11]
        buffers = x[12]
        swapcached = x[13]
        inactive = x[14]

        # Writes all sample data in a form that gnuplot can read for graphing
        data.write("{}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}\n".format(name, date, time, user, sys, wait, idle, steal, busy, cores, memtotal, hightotal, lowtotal,
                                                                                                                                                                                                                                 swaptotal, memfree, highfree, lowfree, swapfree, memshared, cached, active, bigfree, buffers, swapcached, inactive))
f.close()
data.close()
print("Done with file")
