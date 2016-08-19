#!/usr/bin/python
#-*-coding:utf-8-*-

#[0-9a-zA-Z_]{1,15} がツイッターのアカウントの正規表現

import sys
import re

san  = re.compile(u"([一-龠ぁ-んァ-ヴ]{,5})(さん|氏|ちゃん)")
#si   = re.compile(r"([一-龠]{1,20}|[ぁ-ん]{1,20}|[ァ-ヴ]{1,20})(氏)")
#chan = re.compile(r"([一-龠]{1,20}|[ぁ-ん]{1,20}|[ァ-ヴ]{1,20})(ちゃん)")

for line in open(sys.argv[1]):
	line = line.decode("utf-8")
	m =  san.search(line)
#       m =   si.search(line)
#       m = chan.search(line)
	if m is None:
		pass
	else:
		print m.group()		#.encode("utf-8")

