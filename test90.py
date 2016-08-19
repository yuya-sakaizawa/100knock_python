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

#for tweets in col.find({"$query":{"body":query}, "$orderby":{"freq_rt":-1}}).limit(10):
#	print tweets

freq_rt = []
for tweets in col.find():
	if query in tweets["body"]:
		freq_rt.append(tweets)

for tweet in sorted(freq_rt, key = lambda x:-x['freq_rted']):
	print tweet['body']
