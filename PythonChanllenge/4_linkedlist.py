#! /usr/bin/env python3
# Filename: linkedlist

import urllib.request

base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

current = '63579'

num = 1
while True:
    response = urllib.request.urlopen(base_url+current)
    text = str(response.read())
    print (text)
    if text.startswith("b'and the next nothing is"):
        current = ''.join(d for d in text if str.isdigit(d))
        print ("%d %s" %(num, current))
        num += 1
    else:
        break
    
print (base_url+current)
