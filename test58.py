#!/usr/bin/python
#-*-coding:utf-8-*-

#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

import sys, re
from collections import defaultdict
from test54 import *

def Moto_saki(text):
#	for sent in text:
#		for chunk in sent:
#			for morph in chunk.morphs:
#				print morph.surface, morph.base, morph.pos, morph.pos1, chunk.dst, chunk.srcs, chunk.ID


	for sent in text:
		for dst_chunk in sent:
			if len(dst_chunk.srcs) >= 2:
				for src_chunk in sent:
					if dst_chunk.ID == src_chunk.dst:					
						print src_chunk, "\t", dst_chunk

if __name__ == "__main__":
	text  = make_Chunk(sys.argv[1])
	Moto_saki(text)
