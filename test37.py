#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
counts = defaultdict(lambda: 0)

for line in open(sys.argv[1]):
	counts[line] += 1

for foo, bar in sorted(counts.items(), key = lambda x:x[1], reverse=True):
	print "%r	%s" % (bar, foo),
