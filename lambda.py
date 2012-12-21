#! /usr/bin/env python3
# Filename: lambda.py

def make_repeater(n):
    return lambda s: s*n

twice = make_repeater(2)

print (twice('word'))
print (twice(5))

print (eval('2*3'))
exec ('print ("Hello World")')
