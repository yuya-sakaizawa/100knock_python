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

for i in col.find():
	prev = "<s>"
	bigram_list = []
	for uni in i['body']:
		bigram = prev + uni
		bigram_list.append(bigram)
		prev = uni
	i["bigram"]=bigram_list
	col.save(i)

col.create_index([("bigram", ASCENDING)])

con.disconnect()

