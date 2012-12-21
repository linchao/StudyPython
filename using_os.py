#! /usr/bin/env python3
# Filename: using_os.py

import os

print (os.name)
print (os.getcwd())

folds = os.listdir()
for filename in folds:
    print (filename)
    
