 #!/usr/bin/python
#-*-coding:utf-8-*-

#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

import sys

class Morph:
	def  __init__(self, surface, base, pos, pos1):
		self.surface=surface
		self.base=base
		self.pos=pos
		self.pos1=pos1

text = []
sent = []
for line in open(sys.argv[1]):
	line = line.strip()
	if '* ' in line:
		pass
	else:
		if line != "EOS":
			itemList = line.strip().split('\t')
			list = itemList[1].split(',')
			Cabo = Morph(itemList[0], list[6], list[0], list[1])
			sent.append(Cabo)
		else:
			text.append(sent)
			sent = []
for line in text:
	for sent in line:
		print sent.surface, sent.base, sent.pos, sent.pos1
	print '\n'
