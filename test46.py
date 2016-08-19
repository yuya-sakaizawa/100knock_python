#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
list = []
A = ""
B = 0

for line in open(sys.argv[1]):
        tagger = MeCab.Tagger('mecabrc')
        sen = tagger.parse(line)
        words = sen.strip().split('\n')
        for word in words:
                if "\t" in word:
                        w = word.strip().split('\t')
                        list.append(w[0])
                        m = w[1].split(",")
                        for i in m:
                                list.append(i)
                        if list[1] == "名詞" and A == "":
				A += list[0]
			elif list[1] == "名詞" and A != "":
				A += list[0]
				B = 1
			elif list[1] != "名詞" and A != "" and B == 1:
				print A
				A = ""
				B = 0
			else:
				A = ""
				B = 0
                        list = []

