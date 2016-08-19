#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from lxml import etree

xml = open(sys.argv[1])
doc = etree.parse(xml)

#print(etree.tostring(root, pretty_print=True))		#入力のファイル全表示
#sentences = doc.xpath('//sentence')


#for sent in sentences:
#	if sent.get('id') == '2':
#		for token in sent.xpath('./token'):
#			print 'in_for'
#			if token.get('id') == '5':
#				print token[0].text

#print

#k = 0

#for token in doc.xpath('//token'):
#	if token.get('id') == '5':
#		k += 1
#		if k == 2:
#			print token[0].text

#for element in root.iter():
#	print element.tag, element.text


for item in doc.xpath('//sentence[@id = "2"]/tokens/token[@id = "5"]/word'):
	print item.text

