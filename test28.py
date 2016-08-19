#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
counts = defaultdict(lambda: 0)
rank = 1

sen2 = ""

for line in open(sys.argv[1]):
	itemList = line.strip().split('\t')
	sen1 = itemList[1]
	if sen2 is "":
		sen2 = sen1
	else:
		sen = sen2 + ' ' + sen1
		print sen
		sen2 = sen1
		counts[sen] += 1

print ""

for foo, bar in sorted(counts.items(), key = lambda x:x[1], reverse=True):
	if rank <= 100:
		print "[%d] %s %r" % (rank, foo, bar)
		rank += 1

