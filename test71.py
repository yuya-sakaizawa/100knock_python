#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re
re_sentence = re.compile(r"(\.) ([A-Z])|(\[[0-9]+\]+) ([A-Z])")
#re_sentence = re.compile(r"(\.) ([A-Z])|(\.\[[0-9]+\]) ([A-Z])")
sentence = ""
t=0

for line in open(sys.argv[1]):
	line = line.strip()
	m1 = re_sentence.search(line.strip())
	if m1 is None:
		print line
	else:
		m = re_sentence.split(line.strip())
		t = m.count(None)
		for i in range(t):
			m.remove(None)
		for i in range(len(m)):
			if i == 0:
				sentence = m[i]
			elif i == 1:
				sentence += m[i]
				print sentence
			elif i == len(m)-2:
				sentence = m[i]
			elif i == len(m)-1:
				sentence += m[i]
				print sentence
			elif (i+1) % 3 == 0:
				sentence = m[i]
			elif (i+1) % 3 == 1:
				sentence += m[i]
			else:
				sentence += m[i]
				print sentence

