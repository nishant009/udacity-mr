#!/usr/bin/python

# Format of each line is a tsv. Fields are in the header
#
# We want the element 2 (body)
# We need to write them out to standard output, separated by a tab

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

reader.next()

for line in reader:
    if len(line) >= 6:
        if line[5] == 'question':
            print line[0] + '\t0\t' + str(len(line[4]))
        elif line[5] == 'answer':
            print line[6] + '\t1\t' + str(len(line[4]))
        else:
            continue

