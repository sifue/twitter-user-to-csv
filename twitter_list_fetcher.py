#coding: UTF-8

import os
import csv
import twitter
import sys

args = sys.argv

print("Started args:")
print(args)

if len(args) < 5:
    print("起動引数を[実行スクリプト名 リスト所有者名 リスト名 出力ファイル名 ラベル名]としてください。")
    sys.exit(1)

# 取得したキーとアクセストークンを設定する
auth = twitter.OAuth(consumer_key=os.environ["CONSUMER_KEY"],
                     consumer_secret=os.environ["CONSUMER_SECRET"],
                     token=os.environ["TOKEN"],
                     token_secret=os.environ["TOKEN_SECRET"])

t = twitter.Twitter(auth=auth)

# Get the members of tamtar's list "Things That Are Rad"
r = t.lists.members(owner_screen_name=args[1], slug=args[2], count=5000)

contexts = {}

for user in r["users"]:
    contexts[user["id_str"]] = {
        "name" : user["name"],
        "screen_name": user["screen_name"],
        "location" : user["location"],
        "description": user["description"]
        }

with open(args[3], "a") as f:
    writer = csv.writer(f)
    for context in contexts.values():
        writer.writerow([str(context), args[4]])

print("Finished.")