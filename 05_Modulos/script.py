#!/usr/bin/env python3
import sys

print(sys.argv)

for i in sys.argv:
    print(i)

for j in range(1,len(sys.argv)):
    print(sys.argv[j])
