#! /usr/bin/env python3
# Filename：pickling.py

import pickle as p

shoplistfile = 'shoplist.data'
# the name of the file where we will store he object

shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')
p.dump(shoplist, f) # dump the object to a file
f.close()

del shoplist        # remove the shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
storedlist = p.load(f)
print (storedlist)
