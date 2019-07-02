#!/usr/bin/python

import sys

# Loop around the data
# It will be in the format key\tval
#

oldKey = None
qLength = 0
aLength = 0
aCount = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) < 3:
        continue

    thisKey, thisType, thisLength = data

    if oldKey and oldKey != thisKey:
        if aCount == 0:
            print oldKey + '\t' + str(qLength) + '\t0'
        else:
            print oldKey + '\t' + str(qLength) + '\t' + str(aLength/float(aCount))
        oldKey = thisKey;
        qLength = 0
        aLength = 0
        aCount = 0

    oldKey = thisKey
    if int(thisType) == 0:
        qLength = int(thisLength)
    else:
        aLength += int(thisLength)
        aCount += 1

if oldKey != None:
    if aCount == 0:
        print oldKey + '\t' + str(qLength) + '\t0'
    else:
        print oldKey + '\t' + str(qLength) + '\t' + str(float(aLength/aCount))

