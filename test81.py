#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import json
from pymongo import Connection

f = open(sys.argv[1])

data = json.load(f)

#for dict in data:
#	for key, value in dict.items():
#		print key, value
#	print


#コネクション作成
con = Connection('127.0.0.1', 27017)

#コネクションからtestデータベースを取得
db = con.nlp100_sakaizawa

# 以下のように記載することも可能
# db = con['test']

#testデータベースからfooコレクションを取得
col = db.tweets

# 以下のように記載することも可能
# col = db['foo']

for i in data:
	screen_name = i["user"]["screen_name"]
	id = i["id_str"]
	specific_url  = 'https://twitter.com/%s/status/%s' % (screen_name, id)

	if "retweeted_status" in i:
		re_url = 'https://twitter.com/%s/status/%s' % \
				(i["retweeted_status"]["user"]["screen_name"],\
					i["retweeted_status"]["id_str"])
	else:
		re_url = None

	if i["in_reply_to_screen_name"] is None:
		reply_url = None
	else:
		reply_url = 'https://twitter.com/%s/status/%s' % \
				(i["in_reply_to_screen_name"],\
					i["in_reply_to_user_id_str"])
#		print reply_url

	col.insert({"url":specific_url , "data":i["created_at"], \
			"user":i["id"],  "nickname":i["user"]["name"], \
			"body":i["text"], "freq_rted":i["retweet_count"], \
			"re_url":re_url, "reply_url":reply_url})


"""
print "========find_one========"
print col.find_one()

print "========find========"
for data in col.find():
    print data

print "========find_query========"
for data in col.find({u'a':10}):
    print data
"""

