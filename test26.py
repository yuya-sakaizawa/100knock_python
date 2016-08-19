#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

re_token = re.compile(r"ness$|ly$")

for line in open(sys.argv[1]):
	itemList = line.strip().split('\t')
	m = re_token.search(itemList[1])
	if m is None:
		pass
	else:
		print itemList[1]
