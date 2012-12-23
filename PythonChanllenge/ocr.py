#! /usr/bin/env python3
# Filename: ocr.py

import string
input_file = open ('ocr.txt')

mess = ''.join([line.rstrip() for line in input_file])
ans = ''.join(char for char in mess if str.isalpha(char))

# count the number
#occurrences = {}
#for c in mess:
#    occurrences[c] = occurrences.get(c, 0) + 1

#for i in occurrences:
#    print ("%s %d" %(i, occurrences[i]))

# you can use collections.OrderedDict()

# you can just use the read()
# however, it includes the '\n'
#all_the_text = input_file.read()
#print (all_the_text)

# although you can use filter
# it is too slow
#ans = list(filter(lambda x: str.isalpha(x), mess))

print (ans)
