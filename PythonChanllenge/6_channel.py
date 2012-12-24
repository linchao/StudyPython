#! /usr/bin/env python3
# Filename: channel.py

import re
import zipfile

textpath = 'channel\\'

#regular = re.compile('Next nothing is \d?')

#current = '90052'
#num = 1
#while True:
#    f = open(textpath + current + '.txt')
#    line = f.readline()
#    f.close()
#    #print (line)
#    current = ''.join(re.findall('Next nothing is (\d+)', line))
#    if len(current) == 0:
#        print (current)
#        break
#    print ('%d %s' %(num, current))
#    num += 1

#testfile = os.listdir(textpath)
#for filename in testfile:
#    if filename[:-4] in occurrences:
#        pass
#    else:
#        print (filename)
#        check(filename[:-4])
   
zip_file = zipfile.ZipFile("channel.zip", "r")

current = '90052'
collect = ''
while True:
    temp = (zip_file.getinfo("%s.txt" %current).comment)
    t1 = str(temp)[2:-1]
    print (t1)
    collect += t1
    line = zip_file.open('%s.txt' % current)
    f = open(textpath + current + '.txt')
    line = f.readline()
    current = ''.join(re.findall('Next nothing is (\d+)', line))
    #print (current)
    if len(current) == 0:
        print (collect)
        break

print ('')
ls = '\n'
cure = 'abc'
print (cure+ls)
print ('heh')
    
