#!/usr/bin/python

import sys

# Loop around the data
# It will be in the format key\tval
#

oldKey = None
out = []
suffix = []

for line in sys.stdin:
    data = line.strip().split("\t")

    thisKey = data[0]

    if oldKey and oldKey != thisKey:
        print ' '.join(out)
        oldKey = thisKey;
        out = []
        suffix = []

    oldKey = thisKey
    if len(data) == 6:
        suffix.append(data[0])
        suffix.extend(data[2:])
    else:
        out.append(data[0])
        out.extend(data[2:])
        out.extend(suffix)

if oldKey != None:
    print ' '.join(out)
