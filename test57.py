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
		for src_chunk in sent:
			for dst_chunk in sent:
				if dst_chunk.ID == src_chunk.dst:
					if src_chunk.inPos('名詞') and dst_chunk.inPos('動詞') and not dst_chunk.inPos1('非自立') and not src_chunk.inPos1('非自立'):
						print src_chunk.withoutPos('記号'), "\t", dst_chunk.withoutPos('記号')

if __name__ == "__main__":
	text  = make_Chunk(sys.argv[1])
	Moto_saki(text)
