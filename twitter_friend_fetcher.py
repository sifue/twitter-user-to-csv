#coding: UTF-8

import os
import csv
import twitter
import sys

args = sys.argv

print("Started args:")
print(args)

if len(args) < 4:
    print("起動引数を[実行スクリプト名 対象者名 出力ファイル名 ラベル名]としてください。")
    sys.exit(1)

# 取得したキーとアクセストークンを設定する
auth = twitter.OAuth(consumer_key=os.environ["CONSUMER_KEY"],
                     consumer_secret=os.environ["CONSUMER_SECRET"],
                     token=os.environ["TOKEN"],
                     token_secret=os.environ["TOKEN_SECRET"])

t = twitter.Twitter(auth=auth)

cursor = -1

while cursor != 0:
    r = t.friends.list(screen_name=args[1], count=200, cursor=cursor)

    contexts = {}
    for user in r["users"]:
        contexts[user["id_str"]] = {
            "name" : user["name"],
            "screen_name": user["screen_name"],
            "location" : user["location"],
            "description": user["description"]
            }

    with open(args[2], "a") as f:
        writer = csv.writer(f)
        for context in contexts.values():
            writer.writerow([str(context), args[3]])
    
    print("next_cursor:")
    print(r["next_cursor"])
    cursor = r["next_cursor"]

print("Finished.")