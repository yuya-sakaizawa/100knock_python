#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import json
import pymongo
from pymongo import *

#コネクション作成
con = Connection('127.0.0.1', 27017)

#コネクションからtestデータベースを取得
db = con.nlp100_sakaizawa

#testデータベースからfooコレクションを取得
col = db.tweets

query = unicode(sys.argv[1], 'utf-8')

for i in col.find({"bigram":query}):
	print i

#for i in col.find():
#	if unicode("無料", "utf-8") in i["bigram"]:
#		print i

con.disconnect()

