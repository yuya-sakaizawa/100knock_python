#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from stemming.porter2 import stem

for line in open(sys.argv[1]):
	itemList = line.strip().split('\t')
	stm = stem(itemList[1])
	print itemList[0] +'\t'+ itemList[1] +'\t'+ stm

