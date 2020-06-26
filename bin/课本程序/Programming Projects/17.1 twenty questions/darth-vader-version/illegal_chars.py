#!/usr/bin/python
from sys import *

i = 0
if len(argv) > 1:
    for line in open(argv[1]):
        i += 1
        line = line.strip()

        # look for illegal characters
        for c in line:
            if ord(c) < 32 or ord(c) >= 128:
                print("line %5d: %d '%s'" % (i, ord(c), c))

else:
    print("Usage: %s FILENAME" % argv[0])
