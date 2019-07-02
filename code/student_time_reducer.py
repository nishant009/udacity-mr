#!/usr/bin/python

import sys

# Loop around the data
# It will be in the format key\tval
#

oldKey = None
hourDict = {}

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) < 2:
        continue

    thisKey, thisHour = data

    if oldKey and oldKey != thisKey:
        max = -1
        for count in hourDict.values():
            if count > max:
                max = count
        for hour, count in hourDict.items():
            if count == max:
                print oldKey + '\t' + hour
        oldKey = thisKey;
        hourDict = {}

    oldKey = thisKey
    if thisHour in hourDict:
        hourDict[thisHour] += 1
    else:
        hourDict[thisHour] = 1 

if oldKey != None:
    max = -1
    for count in hourDict.values():
        if count > max:
            max = count
    for hour, count in hourDict.items():
        if count == max:
            print oldKey + '\t' + hour

