#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, glob
from test72_1 import *
if __name__ == "__main__":
	text = []
	NPs_list = None
#	for name in glob.glob('english_*_line_genia.txt'):
#		create_token(name)
	text = create_token(sys.argv[1])
	NPs_list = create_NPs_list(text)
#	print len(NPs_list)
		
	for NPs in NPs_list:
		print "#",
		print str(NPs)
		print_feature(NPs)

