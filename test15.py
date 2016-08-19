import sys
import re

com = re.compile(r"@([0-9a-zA-Z_]{1,15})")
acount = ""
src = ""

for line in open(sys.argv[1]):
        m   = com.search(line)
        if m is None:
                print line,
        else:
		src = str(line)
		acount = m.group(1)
		dst = src.replace(acount, "<a href=\"https://twitter.com/#!/"+acount+"\">@"+acount+"</a>") 
                print dst
