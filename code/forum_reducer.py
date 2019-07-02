#!/usr/bin/python

import sys

totalHits = 0

# Loop around the data
# It will be in the format key\tval
#

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    _, thisHit = data_mapped

    totalHits += float(thisHit)

print "fantastic\t", totalHits

