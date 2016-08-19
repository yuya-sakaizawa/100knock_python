#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

com = re.compile(r"なう$")

for line in open(sys.argv[1]):
        m = com.search(line)
        if m is None:
                pass
        else:
                print line,

