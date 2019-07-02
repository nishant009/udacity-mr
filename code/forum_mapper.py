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
    if len(line) >= 4:
        body = line[4]
        if body:
            content = re.split("[\s\.,!?:;\"\(\)<>\[\]#\$=\-/]+", body.lower())
            if 'fantastic' in content:
                count = content.count('fantastic') 
                print "fantastic\t",count
