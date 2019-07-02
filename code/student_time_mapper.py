#!/usr/bin/python

# Format of each line is a tsv. Fields are in the header
#
# We want the element 2 (body)
# We need to write them out to standard output, separated by a tab

import sys
import csv
import re

from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

reader.next()

for line in reader:
    if len(line) >= 8:
        date_added = line[8]
        hour = datetime.strptime(date_added[:-3], "%Y-%m-%d %H:%M:%S.%f").hour
        print line[3] + '\t' + str(hour)

