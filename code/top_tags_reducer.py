#!/usr/bin/python

import sys

# Loop around the data
# It will be in the format key\tval
#

topCount = [0] * 10
topTags = [0] * 10
oldKey = None
oldCount = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) < 2:
        continue

    thisKey, thisCount = data

    if oldKey and oldKey != thisKey:
        minCount = min(topCount)
        if oldCount >= minCount:
            index = topCount.index(minCount)
            topCount[index] = oldCount
            topTags[index] = oldKey
        oldCount = 0

    oldKey = thisKey
    oldCount += int(thisCount)

if oldKey != None:
    minCount = min(topCount)
    if oldCount >= minCount:
        index = topCount.index(minCount)
        topCount[index] = oldCount
        topTags[index] = oldKey

sort = sorted(range(10), key=lambda k: topCount[k], reverse=True)

for i in range(10):
    print topTags[sort[i]] + '\t' + str(topCount[sort[i]])
