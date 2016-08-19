#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from lxml import etree

xml = open(sys.argv[1])
doc = etree.parse(xml)

#print(etree.tostring(root, pretty_print=True))		#入力のファイル全表示

#for sent in sentences:
#	if sent.get('id') == '1':
#		for sen in sent:
#			if sen.tag == 'dependencies':
#				for dep in sen:
#					for depend in dep:
#						if depend.get('idx') == '4':
#							print depend.text
#						if token.tag == 'word':
#							print token.text + ' ',

#print


pr = 0
for dep in doc.xpath('//sentence[@id = "1"]/\
			dependencies[@type = "basic-dependencies"]/dep'):
	for item in dep:
		if pr == 1:
			print item.text
			pr = 0
		if item.tag == 'governor' and item.get('idx') == '4':
			pr = 1

#for token in doc.xpath('//token'):
#	print token[0].text + ' ',

#for element in root.iter():
#	print element.tag, element.text


