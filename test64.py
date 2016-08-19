#!/usr/bin/python
#-*-coding:utf-8

import sys, glob, math, re
from collections import defaultdict

def main(test_file):
	re_number = re.compile(r"([0-9])")
	tf_idf = defaultdict(lambda:0)
	rank = 1

	for line in open(test_file):
		itemList = line.strip().split('\t')
		m = re_number.search(itemList[0])
		if m is None:
			tf_idf[itemList[0]] = float(itemList[1])

	for k, v in sorted(tf_idf.items(), key = lambda x:-x[1]):
		if rank <= 100:
			print k
			rank += 1
		else:
			break


if __name__ == '__main__':
	main(sys.argv[1])
