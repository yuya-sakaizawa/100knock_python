#i/usr/bin/python
#-*-coding:utf-8-*-

import sys

for line in open(sys.argv[1]):
	itemList = line.split(' ')
	for i in range(len(itemList)):
		print itemList[i]
