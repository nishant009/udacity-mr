#!/usr/bin/python

# Format of each line is a tsv. Fields are in the header
#
# We want the element 2 (body)
# We need to write them out to standard output, separated by a tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

reader.next()

for line in reader:
    if len(line) >= 6:
        if line[5] == 'question':
            print line[0] + '\t' + line[3]
        else:
            print line[6] + '\t' + line[3]
       
