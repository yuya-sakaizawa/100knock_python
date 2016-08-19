#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, glob

class Token:
	def  __init__(self, w, lem, pos, chunk):
		self.w=w
		self.lem=lem
		self.pos=pos
		self.chunk=chunk

def create_token(test_file):

	text = []
	sent = []

	for line in open(test_file):
		if line == '\n':
			text.append(sent)
		else:
			itemList = line.strip().split('\t')
			token = Token(itemList[0], itemList[1], itemList[2], itemList[3])
			sent.append(token)
	return text

#	for line in text:
#		for sent in line:
#			print sent.w, sent.lem, sent.pos, sent.chunk
#		print '\n'

def create_NP(text):
	NP = ""
	for sent in text:
		for Token in sent:
			if NP == "" and Token.chunk == 'B-NP':
				NP += Token.w
#				print NP
#				NP = ""
			elif Token.chunk == 'B-NP':
				print "# " + NP
				NP = ""
			elif NP != "" and Token.chunk != 'I-NP':
				print "# " + NP
				NP = ""
			if NP != "" and Token.chunk == 'I-NP':
				NP += " "
				NP += Token.w
#				print NP
#				NP = ""

if __name__ == "__main__":
	text = []
#	for name in glob.glob('english_*_line_genia.txt'):
#		text = create_token(name)
	text = create_token(sys.argv[1])
	create_NP(text)
