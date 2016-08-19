#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

re_word = re.compile(r"[a-zA-Z]+|\.")
from collections import defaultdict
counts = defaultdict(lambda: 0)
rank  = 1

for line in open(sys.argv[1]):
	itemList = line.strip().split('\t')
	counts[itemList[1]] += 1

for foo, bar in sorted(counts.items(), key = lambda x:x[1], reverse=True):
	word  = re_word.search(foo)
	if word is None:
		pass
	elif rank <= 100:
		print "[%d] %s %r" % (rank, foo, bar)
		rank += 1

