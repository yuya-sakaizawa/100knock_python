#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
counts = defaultdict(lambda:0)
context_counts = defaultdict(lambda:0)

for line in open(sys.argv[1]):
	itemList = line.strip().split('\t')
	counts[itemList[1] +' ' + itemList[2]] = itemList[0]
	context_counts[itemList[1]] += int(itemList[0])

for sen, count in counts.items():
	words = sen.strip().split()
	context = ''.join(words[0])
	prob = float(counts[sen]) / context_counts[context]
	print str(prob) +'\t'+ words[0] +'\t'+ words[1]
