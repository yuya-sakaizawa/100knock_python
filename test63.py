#!/usr/bin/python
#-*-coding:utf-8

import sys, glob, math
from collections import defaultdict

def main():
	freq = defaultdict(lambda:0)
	df   = defaultdict(lambda:0)
	N = float(len(glob.glob('japanese_*_cabocha_n.txt')))
	docid = 1
#	print N

	for name in glob.glob('japanese_*_cabocha_n.txt'):
		for word in open(name):
			word = word.strip()
			freq[word]+=1
			if df[word] == 0:
				df[word] += 1
				df[word+' '+str(docid)] += 1
			if df[word] > 0 and df[word+' '+str(docid)] == 0:
				df[word] += 1
				df[word+' '+str(docid)] += 1
		docid += 1

	for k, v in sorted(freq.items(), key=lambda x:x[-1]):
		print ("%s	%f	%f	%f") % \
				 (k, v*math.log(N/df[k], 2), v, df[k] )

if __name__ == '__main__':
	main()
