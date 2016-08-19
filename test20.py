#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

e = re.compile(r"\([^一-龠ぁ-んァ-ヴ]{3,6}\)")

for line in open(sys.argv[1]):
	emoji = e.search(line)
	if emoji is None:
		pass
	else:
		print emoji.group(0)
