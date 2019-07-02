#!/usr/bin/python

# Format of each line is a tsv. Fields are in the header
#
# We want the element 2 (body)
# We need to write them out to standard output, separated by a tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

reader.next()

mem = {}

for line in reader:
    if len(line) >= 2:
        tags = line[2].strip().split(' ')
        for tag in tags:
            if tag in mem:
                mem[tag] += 1
            else:
                mem[tag] = 1

for key, value in mem.items():
    print key + '\t' + str(value)
       
