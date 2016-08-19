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

for i in col.find({"url":"https://twitter.com/___licht/status/485830082703790081"}):
	print i


con.disconnect()

