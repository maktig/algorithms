#!/usr/bin/env python

file = 'IntegerArray2.txt'

f = open(file,'w')

for i in range(100000,0,-1):
    line = str(i) + "\n"
    f.write(line)

f.close()
