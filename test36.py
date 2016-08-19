#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from collections import defaultdict
word = defaultdict(lambda:0)
sen2 = ""

for line in open(sys.argv[1]):
        words = line[:-1].split()
	sen1 = words[1]
	if sen2 is "":
		sen2 = sen1
	else:
		print sen2 +'\t'+ sen1
		sen2 = sen1

