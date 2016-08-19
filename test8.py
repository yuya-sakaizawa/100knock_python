#!/usr/bin/python
#-*-cording;utf-8-*-

import sys

d = []

for line in open(sys.argv[1]):
	itemList = line[:-1].split('\t')
	d.append(itemList)

for i in sorted(d, key = lambda x:x[1]):
	print i[0], i[1]
