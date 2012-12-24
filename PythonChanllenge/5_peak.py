#! /usr/bin/env python3
# Filename: peak.py

import pickle as p
import urllib.request

ans = p.load((urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')))

#print (ans)
for line in ans:
    print (''.join(t[0]*t[1] for t in line))

for line in ans:
    print (''.join(map(lambda p: p[0]*p[1], line)))
#print (ans)
