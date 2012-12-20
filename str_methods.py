#! /usr/bin/env python3
# Filename: str_methods.py

name = 'Swaroop' # This is a string objecct

if name.startswith('Swa'):
    print ('Yes, the string starts with "Swa"')

if 'a' in name:
    print ('Yes, it contains the string "a"')

if name.find('war') != -1:
    print ('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
delimiter = delimiter.join(mylist)
print (delimiter)
