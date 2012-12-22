#! /usr/bin/env python3
# Filename: using_sys.py

import sys

print ('The command line arguments are:')
for i in sys.argv:
    print (i)

for i in sys.path:
    print (i)

