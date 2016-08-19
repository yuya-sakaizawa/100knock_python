#!/usr/bin/python
#-*-coding:utf-8-*-

#[0-9a-zA-Z_]{1,15} がツイッターのアカウントの正規表現
# 日本語トークンを切り出すための正規表現。
#JP_TOKEN = re.compile(u"[一-龠]+|[ぁ-ん]+|[ァ-ヴ]+|[a-zA-Z0-9]+")

import sys
import re

JP_TOKEN = re.compile(r"([一-龠]+)\(([A-Z]+)\)")

for line in open(sys.argv[1]):
        m = JP_TOKEN.search(line)
        if m is None:
                pass
        else:
		print m.group(0)
#                print m.group(1) + '\t' + m.group(2) 
