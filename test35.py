#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import marshal
word = []

f = open(sys.argv[1], 'rb')

for line in marshal.load(f):
	word.append(line)

words = sorted(word)

for line in open(sys.argv[2]):
	itemList = line.strip().split('\t')
	sen = itemList[1] + "(3)"
	if sen in words:
		print itemList[1] + "	3~"
	else:
		pass	
