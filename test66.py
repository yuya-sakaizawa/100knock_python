#!/usr/bin/python
#-*-coding:utf-8

import sys, math
from collections import defaultdict

def noum(vector):
	sum = 0
	for k, v in vector.items():
		for s,t in v.items():
			sum += t * t
		sum = math.sqrt(sum)
		for s, t in v.items():
			vector[k][s] = float(t) / sum
		sum = 0

	return vector


def sent_vector(test_file):
	vector = defaultdict(lambda:defaultdict(int))

	for line in open(test_file):
		itemList = line.strip().split()
		vector[itemList[0]][itemList[1]+' '+itemList[2]] += 1

	vector = noum(vector)

	for k, v in vector.items():
		print k,
		for s, t in v.items():
			print s+":"+ str(t),
		print
		print
		print 

if __name__ == "__main__":
	sent_vector(sys.argv[1])
