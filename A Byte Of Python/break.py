#! /usr/bin/env python3
# Filename: break.py

while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    print ('Length of the string is', len(s))
print ('Done')
