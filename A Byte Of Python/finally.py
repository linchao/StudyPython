#! /usr/bin/env python3
# Filename: finally.py

import time

try:
    f = open('poem.txt')
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print (line,)
finally:
    f.close()
    print ('Cleaning up...closed the file')
