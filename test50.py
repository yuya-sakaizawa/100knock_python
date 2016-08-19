#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import matplotlib.pyplot as plt
w = 0
listx = []
listy = []

for line in open(sys.argv[1]):
	itemList = line.strip().split()
	w += 1
	listx.append(w)
	listy.append(itemList[1])

fig = plt.figure(1)
plt.plot(listx, listy)
plt.title(r"test50", fontsize=20)
plt.xlim(0, 100)
plt.xlabel(r"Juni", fontsize=15)
plt.ylim(0, 800)
plt.ylabel(r"Hind", fontsize=15)
plt.savefig("test50.eps")
plt.show()
