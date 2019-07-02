#!/usr/bin/python

# Format of each line is a tsv. Fields are in the header
#
# We want the element 2 (body)
# We need to write them out to standard output, separated by a tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    write_line = []
    if len(line) == 5:
        write_line.append(line[0])
        write_line.append('A')
        write_line.extend(line[1:])
    else:
        write_line.append(line[3])
        write_line.append('B')
        write_line.extend(line[:3])
        write_line.extend(line[5:10])

    writer.writerow(write_line)
