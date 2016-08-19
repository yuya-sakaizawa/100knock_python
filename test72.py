#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, glob

class Token:
	def  __init__(self, w, lem, pos, chunk):
		self.w=w
		self.lem=lem
		self.pos=pos
		self.chunk=chunk
	def __str__(self):
		return self.w

class NPs:
	def __init__(self, f_Token, NP, b_Token):
		self.f_Token = f_Token
		self.NP = NP
		self.b_Token = b_Token
	def __str__(self):
		return " ".join([str(token) for token in self.NP])
def print_feature(self):
	if len(self.NP) == 1:
		fw      = self.NP[0].w		#先頭の単語
		fpos    = self.NP[0].pos	#先頭の品詞
		fw_fpos = fw+'|'+fpos		#先頭の単語品詞
		w_term  = self.NP[0].w	#名詞句の単語列
	else:
		fw      = self.NP[1].w		#先頭の単語
		fpos    = self.NP[1].pos	#先頭の品詞
		fw_fpos = fw+'|'+fpos		#先頭の単語品詞	
		w_term  = "	".join([str(token) for token in self.NP[1:]])
	w1      = self.b_Token.lem	#名詞句の一語後の単語
	pos1    = self.b_Token.pos	#名詞句の一語後の品詞
	w_1     = self.f_Token.lem	#名詞句の一語前の単語
	pos_1   = self.f_Token.pos	#名詞句の一語前の品詞
	hw      = self.NP[-1].w		#末尾の単語
	hpos    = self.NP[-1].pos	#末尾の品詞
	hw_hpos = hw+'|'+hpos		#末尾の単語品詞
	if self.NP[0].w == "A" or self.NP[0].w == "a" or self.NP[0].w == "An" or self.NP[0].w == "an":
		print "A"+' '+'w[-1]='+w_1+' '+'fw='+fw+' '+'fpos='+fpos+' '+'w[0]='+w_term+' '+'fw|fpos='+fw_fpos \
			+' '+'hw='+hw+' '+'hw|hpos='+hw_hpos+' '+'pos[+1]='+pos1+' '+'hpos='+hpos \
				+' '+'hpos='+hpos+' '+'w[+1]='+w1
	elif self.NP[0].w == "The" or self.NP[0].w == "the":
		print "THE"+' '+'w[-1]='+w_1+' '+'fw='+fw+' '+'fpos='+fpos+' '+'w[0]='+w_term+' '+'fw|fpos='+fw_fpos \
			+' '+'hw='+hw+' '+'hw|hpos='+hw_hpos+' '+'pos[+1]='+pos1+' '+'hpos='+hpos \
				+' '+'hpos='+hpos+' '+'w[+1]='+w1	
	else:
		w_term = str(self.NP[0].w) + '\t' + w_term
		print "NONE"+' '+'w[-1]='+w_1+' '+'fw='+fw+' '+'fpos='+fpos+' '+'w[0]='+w_term+' '+'fw|fpos='+fw_fpos \
			+' '+'hw='+hw+' '+'hw|hpos='+hw_hpos+' '+'pos[+1]='+pos1+' '+'hpos='+hpos \
				+' '+'hpos='+hpos+' '+'w[+1]='+w1

def create_token(test_file):
	text = []
	sent = []

	for line in open(test_file):
		if line == '\n':
			text.append(sent)
			sent = []
		else:
			itemList = line.strip().split('\t')
			token = Token(itemList[0], itemList[1], itemList[2], itemList[3])
			sent.append(token)

#	for line in text:
#		for sent in line:
#			print sent.w, sent.lem, sent.pos, sent.chunk
#		print '\n'
	return text

def create_NPs_list(text):
	k = -1
	all_term = []
	f_Token = None
        NPs_list = []
	b_Token = None
	part_NP = []
        for sent in text:
                for Token in sent:
			all_term.append(Token)

	for sent in text:
		for Token in sent:
			k+= 1
                        if part_NP == [] and Token.chunk == 'B-NP':
                                part_NP.append(Token)
                        elif Token.chunk == 'B-NP':
                                f_Token = all_term[k-(len(part_NP))-1]
				b_Token = all_term[k]
				NPs_list.append(NPs(f_Token, part_NP, b_Token))
                                part_NP = []
				part_NP.append(Token)
                        elif part_NP != [] and Token.chunk != 'I-NP':
                                f_Token = all_term[k-(len(part_NP))-1]
				b_Token = all_term[k]
				NPs_list.append(NPs(f_Token, part_NP, b_Token))
                                part_NP = []
                        if part_NP != [] and Token.chunk == 'I-NP': 
                                part_NP.append(Token)

	return NPs_list

if __name__ == "__main__":
	text = []
	NPs_list = None
#	for name in glob.glob('english_*_line_genia.txt'):
#		create_token(name)
	text = create_token(sys.argv[1])
	NPs_list = create_NPs_list(text)
	
	for NPs in NPs_list:
		print "#",
		print str(NPs)

