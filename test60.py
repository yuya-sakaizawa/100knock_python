#!/usr/bin/python
#-*-coding:utf-8-*-
import sys

print "digraph knock60 {"
for line in open(sys.argv[1]):
	line = line.replace('\"', r'\"')
	List = line.strip().split('\t')
	print "\t\""+List[0]+"\" -> \""+List[1]+"\";"
print "}"
