#!/usr/bin/python
#-*-coding:utf-8-*-
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
import sys, re, glob
from collections import defaultdict
from chunk import *

def test65(corpus, result_64):
	words = []
#	for text in corpus:
#		for sent in text:
#			for chunk in sent:
#				for morph in chunk.morphs:
#					print morph.surface, morph.base, morph.pos, morph.pos1, chunk.dst, chunk.srcs, chunk.ID 
	for line in open(result_64):
		words.append(line.strip())
#	print len(words)

	for text in corpus:
		for sent in text:
			for dst_chunk in sent:
				for src_chunk in sent:
					for word in words:
						if word in src_chunk.getsurface():
#							print 'word'
							if src_chunk.dst == dst_chunk.ID:
#								print 'ID'
								if dst_chunk.inPos("名詞") or dst_chunk.inPos('動詞') or dst_chunk.inPos('形容詞'):
#									print "aaa"
									print word +' -> '+str(dst_chunk.getsub())

						if word in dst_chunk.getsurface():
							#print 'bbb'
							if src_chunk.dst == dst_chunk.ID:
								#print 'bbb'
								if dst_chunk.inPos("名詞") or dst_chunk.inPos('動詞') or dst_chunk.inPos('形容詞'):
									#print 'bbb'
									print word +' <- '+str(src_chunk.getsub())

if __name__ == "__main__":
	corpus = []
	for name in glob.glob('japanese_*_cabocha.txt'):
		text  = make_Chunk(name)
		corpus.append(text)
	test65(corpus, sys.argv[1])
