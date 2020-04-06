# to run, use python ReadData.py <filename>
import sys
import re
file = sys.argv[1]
f = open(file, "r")
data = open(file + '.dat', 'w')
for line in f:

    # Writes key as a comment for .dat file for gnuplot
    # gets CPU key first
    pattern = re.compile('CPU_ALL,CPU Total [a-zA-Z]*,(.*)')
    l = pattern.findall(line)
    if l:
        x = l[0].split(',')
        # print(x)
        data.write("# Name      Date      Time      {}      {}      {}      {}      {}      {}      {}      ".format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
        # move on to next line to avoid overlap with other regex
        continue

    # gets MEM key after CPU key
    pattern = re.compile('MEM,Memory MB [a-zA-Z]*,(.*)')
    l = pattern.findall(line)
    if l:
        x = l[0].split(',')
        # print(x)
        data.write("{}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}\n".format(
            x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14]))
        # move on to next line to avoid overlap with other regex
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
