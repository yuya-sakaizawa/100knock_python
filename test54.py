#!/usr/bin/python
#-*-coding:utf-8-*-

#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

import sys
from collections import defaultdict

class Chunk:
	def  __init__(self, morphs, dst, srcs, ID):
		self.morphs = morphs
		self.dst    = dst
		self.srcs   = srcs
		self.ID	    = ID
	def __str__(self):
		return "".join([morph.surface for morph in self.morphs])
	def inPos(self, str_pos):
		for morph in self.morphs:
			if morph.pos == str_pos:
				return True
		return False
	def inPos1(self, str_pos1):
		for morph in self.morphs:
			if morph.pos1 == str_pos1:
				return True
		return False
	def withoutPos(self, str_pos):
		new_morphs=[]
		for morph in self.morphs:
			if not morph.pos == str_pos:	
				new_morphs.append(morph)
		return Chunk(new_morphs, self.dst, self.srcs, self.ID)
	def getsurface(self):
		all_surface = ''
		for morph in self.morphs:
			all_surface += morph.surface
		return all_surface


class Morph:
	def  __init__(self, surface, base, pos, pos1):
		self.surface=surface
		self.base=base
		self.pos=pos
		self.pos1=pos1

def make_Chunk(test_file):
	SAKI = []
	text = []
	sent = []
	srcdict = defaultdict(list)
	for line in open(test_file):
		line = line.strip()
		if line != 'EOS':
			SAKI.append(line)
		else:
			for line in SAKI:
				if '* ' in line:
					itemList = line.split()
					Chu = Chunk([], int(itemList[2][:-1]), [], int(itemList[1]))
					srcdict[int(itemList[2][:-1])].append(int(itemList[1]))
					sent.append(Chu)
				else:
					itemList = line.split('\t')
					List   	 = itemList[1].split(',')
					Chu.morphs.append(Morph(itemList[0], List[6], List[0], List[1]))
			text.append(sent)
			for Chu in sent:
				Chu.srcs = srcdict[Chu.ID]
			srcdict = defaultdict(list)
			sent = []
			SAKI = []
			

#	for line in text:
#		for sent in line:
#			for morph in sent.morphs:
#				print morph.surface, morph.base, morph.pos, morph.pos1, sent.dst, sent.srcs, sent.ID
#		print '\n'
	return text

if __name__ == "__main__":
	make_Chunk(sys.argv[1])
