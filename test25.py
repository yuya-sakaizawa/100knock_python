#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

re_token = re.compile(r"\.+$|\,+$")

for line in open(sys.argv[1]):
	itemList = line.strip().split(' ')
	for i in itemList:
		m = re_token.search(i)
		if m is None:
			print i + '\t' + i.lower()
		else:
			print i[:-1] + '\t' + i[:-1].lower()
			print m.group() + '\t' + m.group().lower()
	print ''
