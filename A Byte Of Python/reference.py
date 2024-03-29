#! /usr/bin/env python3
# Filename: reference.py

print ('Simple assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!

del shoplist[1]

print ('shoplist is', shoplist)
print ('mylist is', mylist)
# notice that both shoplist and mylist both print the same list without
# the 'mango' confirming that they point to the same object

print ('Copy by making a full slice')
mylist = shoplist[:] # make a copy by doing a full slice
del mylist[0] # remove the first item

print ('shoplist is', shoplist)
print ('mylist is', mylist)
# notice that now the two lists are different
