#!/usr/bin/python
#-*-coding:utf-8-*-

#太郎が花子に本を借りた
#* 0 3D 0/1 -1.467645
#太郎	名詞,固有名詞,人名,名,*,*,太郎,タロウ,タロー
#が	助詞,格助詞,一般,*,*,*,が,ガ,ガ
#* 1 3D 0/1 -1.467645
#花子	名詞,固有名詞,人名,名,*,*,花子,ハナコ,ハナコ
#に	助詞,格助詞,一般,*,*,*,に,ニ,ニ
#* 2 3D 0/1 -1.467645
#本	名詞,一般,*,*,*,*,本,ホン,ホン
#を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
#* 3 -1D 0/1 0.000000
#借り	動詞,自立,*,*,一段,連用形,借りる,カリ,カリ
#た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
#EOS

import sys
from collections import defaultdict

class Chunk:
	def  __init__(self, morphs, dst, srcs, ID, sub, fun):		#subject:sub function:fun
		self.morphs = morphs
		self.dst    = dst
		self.srcs   = srcs
		self.ID	    = ID
		self.sub    = sub
		self.fun    = fun
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
		return Chunk(new_morphs, self.dst, self.srcs, self.ID, self.sub, self.fun)
	def getsurface(self):
		all_surface = ''
		for morph in self.morphs:
			all_surface += morph.surface
		return all_surface
	def getsub(self):
		if "*" == self.morphs[self.sub].base:
			return self.morphs[self.sub].surface
		else:
			return self.morphs[self.sub].base

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
					kinou =  itemList[3].split('/')
					Chu = Chunk([], int(itemList[2][:-1]), [], int(itemList[1]), int(kinou[0]), int(kinou[1]))
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
#				print morph.surface, morph.base, morph.pos, morph.pos1, sent.dst, sent.srcs, sent.ID, sent.sub, sent.fun
#		print '\n'
	return text

if __name__ == "__main__":
	make_Chunk(sys.argv[1])
