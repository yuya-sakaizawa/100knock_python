#!/usr/bin/python
#-*-coding:utf-8-*-

 #表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
import sys
import MeCab


text = []
word = {}
"""
for line in open(sys.argv[1]):
	tagger = MeCab.Tagger('mecab')
	result = tagger.parse(line.strip())
	print result,

"""
for line in open(sys.argv[1]):
	tagger  = MeCab.Tagger('mecab')
	result  = tagger.parse(line.strip())
	result3 = result.split('\n')
	sent = []
	for result2 in result3:
		if '\t' in result2:
			itemList = result2.split('\t')
			List     = itemList[1].split(',')
			word = {"surface":itemList[0], "base":List[6], "pos":List[0], "pos1": List[1]}		
			sent.append(word)
	text.append(sent)

print text[2][0]
"""		
for sent in text:
	for d in sent:
		for i, j in d.items():
			if i == "surface":
				print j,
"""
