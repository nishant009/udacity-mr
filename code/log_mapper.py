#!/usr/bin/python

# Format of each line is in common log format:
# %h %l %u %t \"%r\" %>s %b
#
# We need to write them out to standard output, separated by a tab

import sys
import re

from urlparse import urlparse

regex = '([\d\.]+)\s(.*)\s(.*)\s\[(.*)\]\s"(.*)"\s(\d+)\s(.*)'
pattern = re.compile(regex)

for line in sys.stdin:
    match = pattern.match(line.strip())
    if match:
        data = match.groups()
        if len(data) == 7:
            ip, identity, userName, timeStamp, request, status, bytes = data
            url = request.split(' ')[1]
            parseRes = urlparse(url)
            toRemove = parseRes.scheme + '://' + parseRes.netloc
            path = url.replace(toRemove, '')
            print "{0}\t{1}".format(path, 1)

