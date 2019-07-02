#!/usr/bin/python

import sys

totalHits = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
#

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", totalHits
        oldKey = thisKey;
        totalHits = 0

    oldKey = thisKey
    totalHits += float(thisHit)

if oldKey != None:
    print oldKey, "\t", totalHits

