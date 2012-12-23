#! /usr/bin/env python3
# Filename: equality

#!/usr/bin/env python
import re
mess = open("equality.txt").read()
print (''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',  mess)))

# learn the regular expression
p = re.compile('[a-z]+')
m = p.match("abd4234")

print (m.group())
print ("span: %d %d" %(m.span()))

s = p.search('12sdf3')
print (s.group())
print ("span: %d %d" %(s.span()))

#re.findall('(^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}([^A-Z]|$)', text)

