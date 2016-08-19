#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import matplotlib.pyplot as plt
from collections import defaultdict
word = defaultdict(lambda:0)
data = []

for line in open(sys.argv[1]):
	itemList = line.strip().split()
#	word[itemList[1]] += 1
	data.append(int(itemList[1]))

#for i, j in word.items():
#	print i +'\t'+ str(j)

fig = plt.figure(1)
plt.hist(data, bins=50, range=(1, 50))
plt.title(r"test49", fontsize=20)
#plt.xlim(0, 300)
plt.xlabel(r"Hind", fontsize=15)
#plt.ylim(0, 300)
plt.ylabel(r"Type", fontsize=15)
plt.savefig("test49.eps")
plt.show()

