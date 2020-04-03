import sys
import re
file = sys.argv[1]
f = open(file, "r")
data = open(file + '.dat', 'w')
for line in f:
    # line = f.readline()

    pattern = re.compile('(User%)')
    l = pattern.findall(line)
    if l:
        continue

    pattern = re.compile('(memtotal)')
    l = pattern.findall(line)
    if l:
        continue

    pattern = re.compile('ZZZZ,(.*)')
    l = pattern.findall(line)
    if l:
        x = l[0].split(",")
        print(x)
        name = x[0]
        time = x[1]
        date = x[2]
        # pattern = re.compile('[0-9]+:[0-9]+:[0-9]+')
        # time = pattern.findall(l[0])
        # print(time)

        # pattern = re.compile('[00-31]+-[A-Z]+-[0-9]+')
        # date = pattern.findall(l[0])
        # print(date)

    pattern = re.compile('CPU_ALL,{},(.*)'.format(name))
    l = pattern.findall(line)
    if l:
        x = l[0].split(',')
        print(x)
        user = x[0]
        sys = x[1]
        wait = x[2]
        idle = x[3]
        steal = x[4]
        busy = x[5]
        if busy == '':
            busy = "0"
        cores = x[6]

    pattern = re.compile('MEM,{},(.*)'.format(name))
    l = pattern.findall(line)
    if l:
        x = l[0].split(',')
        print(x)
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
        data.write("{}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}      {}\n".format(name, date, time, user, sys, wait, idle, steal, busy, cores, memtotal, hightotal, lowtotal,
                                                                                                                                                                                                                                 swaptotal, memfree, highfree, lowfree, swapfree, memshared, cached, active, bigfree, buffers, swapcached, inactive))

    print('done with line')
f.close()
data.close()
