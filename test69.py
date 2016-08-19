#!/usr/bin/python
#-*-coding:utf-8-*-
import sys

print "graph knock60 {"
for line in open(sys.argv[1]):
	line = line.replace('\"', r'\"')
	List = line.strip().split('\t')
	itemList = List[1].split()
	print "\t\""+itemList[0]+"\" -- \""+itemList[1]+"\";"
print "}"
