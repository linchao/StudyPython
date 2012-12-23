#! /usr/bin/env python3
# Filename: map.py

import string

trans_table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
origin = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq\
glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.\
lmu ynnjw ml rfc spj."

change = origin.translate(trans_table)

ans = "map"
final = ans.translate(trans_table)
print (change)
print (final)
