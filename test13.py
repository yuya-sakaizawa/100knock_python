#!/usr/bin/python
#-*-coding:utf-8-*-

#[0-9a-zA-Z_]{1,15} がツイッターのアカウントの正規表現

import sys
import re
from collections import defaultdict

re_acount = re.compile(r"([0-9a-zA-Z_]{1,15}) : ")
re_RT     = re.compile(r"RT @[0-9a-zA-Z_]{1,15}: ")

acount = ""
tweet  = ""

acount_dict = defaultdict(list)

for line in open(sys.argv[1]):
	txt_acount = re_acount.match(line)
	if txt_acount is None:
		tweet = tweet + line
	else:
		if acount == "":
			pass
		else:
			tweet = tweet[:-1]
			acount_dict[acount].append(tweet)
		acount = txt_acount.group(1)
		tweet = line[len(txt_acount.group()):]

for key, value in acount_dict.items():
	for tweet in value:
		RT = re_RT.match(tweet)
		if RT is None:
			RT = re_RT.search(tweet)
			if RT is None:
				pass
			else:
				print "----"
				print tweet[:RT.start()]

