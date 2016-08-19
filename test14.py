#!/usr/bin/python
#-*-coding:utf-8-*-

#[0-9a-zA-Z_]{1,15} がツイッターのアカウントの正規表現

import sys
import re

com = re.compile(r"(@[0-9a-zA-Z_]{1,15})")

for line in open(sys.argv[1]):
        m = com.search(line)
        if m is None:
                pass
        else:
                print m.group()

