#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import MeCab
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a", "--test42", action = "store", type = "int", help = "kadai42 verb")
parser.add_option("-b", "--test43", action = "store", type = "int", help = "kadai43 verbbais")
parser.add_option("-c", "--test44", action = "store", type = "int", help = "kadai44 sahen")
parser.add_option("-d", "--test45", action = "store", type = "int", help = "kadai45 AnoB")
parser.add_option("-e", "--test46", action = "store", type = "int", help = "kadai46 nounchain")

(options, args) = parser.parse_args()

import sys
import MeCab

list = []
A45 = ""
B45 = 0
A46 = ""
B46 = 0

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
		# test42.pyの実装
			if options.test42 == 1:
				if list[1] == "動詞":
					print "   動詞" +'\t',
					print list[0]
		# test43.pyの実装
			if options.test43 == 1:
                        	if list[1] == "動詞":
					print "動詞の基本" + '\t',
                                	print list[7]
		# test44.pyの実装
			if options.test44 == 1:
                        	if list[1] == "名詞":
					if list[2] == "サ変接続":
						print "サ変名詞" + '\t',
                                		print list[0]
		# test45.pyの実装
			if options.test45 == 1:
	                        if list[1] == "名詞" and A45 == "":
					A45 += list[0]
				elif list[0] == "の" and A45 != "":
					A45 += list[0]
					B45 = 1
				elif list[1] == "名詞" and B45 == 1:
					A45 += list[0]
					print "AのB" + '\t',
					print A45
					B45 = 0
				else:
					A45 = ""
					B45 = 0
		# test46.pyの実装
			if options.test46 == 1:
                        	if list[1] == "名詞" and A46 == "":
					A46 += list[0]
				elif list[1] == "名詞" and A46 != "":
					A46 += list[0]
					B46 = 1
				elif list[1] != "名詞" and A46 != "" and B46 == 1:
					print "名詞の連接" + '\t',
					print A46
					A46 = ""
					B46 = 0
				else:
					A46 = ""
					B46 = 0
                        list = []
