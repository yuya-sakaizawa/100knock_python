#!/usr/bin/python
#-*-coding;utf-8-*-

import sys
list1 = []
list2 = []
for line in open(sys.argv[1]):
	itemList = line[:-1].split('\t')
	list1.append(itemList[0])
list1.sort()

for i in range(len(list1)):
	list2.append(list1[i])

count = 1
k = 0;
for i in range(len(list1)):
	if list1[k] == list2[i]:
		pass
	else:
		count+=1
		k = i

print count
