#!/usr/bin/python

import sys

# Loop around the data
# It will be in the format key\tval
#

oldKey = None
idList = []

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) < 2:
        continue

    thisKey, thisId = data

    if oldKey and oldKey != thisKey:
        print oldKey + '\t' + ','.join(idList)
        idList = []

    oldKey = thisKey
    idList.append(thisId)

if oldKey != None:
    print oldKey + '\t' + ','.join(idList)
