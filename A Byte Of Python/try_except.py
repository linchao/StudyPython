#! /usr/bin/env python3
# Filename: try_except.py

import sys

try:
    s = input('Enter something -->')
except EOFError:
    print ('\nWhy did you do an EOF on me?')
    sys.exit(0)  # exit the program
except:
    print ('\nSome error/exception occurred.')
    # here, we are not exiting the program

print ('Done')
