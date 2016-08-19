#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import Counter
dict = {}
tap = ()
cnt = Counter()

for line in open(sys.argv[1]):
	word = line.strip().split('|')
	tap = (word[1], word[3], word[6])
	if word[0] in dict:
		cnt[word[0]] += 1
		w = word[0] + "(" + str(cnt[word[0]]+1) + ")"
		dict[w] = tap
	else:
		dict[word[0]] = tap

print 'end'
print dict[raw_input()]
