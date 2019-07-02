#!/usr/bin/python

import sys

maxKey = None
maxHits = -1
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
        if maxHits < totalHits:
            maxHits = totalHits
            maxKey = oldKey

        oldKey = thisKey;
        totalHits = 0

    oldKey = thisKey
    totalHits += float(thisHit)

print maxKey, "\t", maxHits

