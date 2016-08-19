#!/usr/bin/python
#-*-coding:utf-8-*-

import sys, glob
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

def main():
	list = []
	A = ""
	B = 0


	for words in open(sys.argv[1]):
		if '* ' in words:
			if A != "":
				print A
				A = ""
		else:
	       	        if "\t" in words:
				#print words
        	                w = words.strip().split('\t')
        	                list.append(w[0])
        	                m = w[1].split(",")
        	                for i in m:
        	                        list.append(i)
        	                if list[1] == "名詞":
					A += list[0]
				if list[1] != "名詞" and A != "":
					print A
					A = ""
				list = []
	

if __name__ == '__main__':
	main()
