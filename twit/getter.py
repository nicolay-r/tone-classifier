#!/usr/bin/python

import tweepy
import sys
import json
import csv
import os
import time

if (len(sys.argv) == 1):
    print "usage: ./getter.py <keys_file> <path_prefix>"
    exit(0)

keys_filename = sys.argv[1]
prefix = sys.argv[2]

with open(keys_filename) as data:
    keys = json.load(data)

print "Get auth object ..."
auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
print "Set access tokens ..."
auth.set_access_token(keys['access_token'], keys['access_secret'])
print "Getting API ..."
api = tweepy.API(auth)

out_folder = os.path.join(prefix, 'log')
if not os.path.exists(out_folder):
    os.mkdir(out_folder)

out_filepath = os.path.join(out_folder,
    str(time.ctime()).replace(' ', '_'))

with open(out_filepath, 'w') as out:

    csv_writer = csv.writer(out, delimiter=';', quoting=csv.QUOTE_MINIMAL)

    for t in tweepy.Cursor(api.search, q="test", lang="ru", count=4).items():
        csv_writer.writerow([t.id, t.created_at,
            t.user.screen_name.encode('utf-8'), t.text.encode('utf-8'),
            t.retweet_count, t.user.favourites_count, t.user.statuses_count,
            t.user.followers_count, t.user.friends_count, t.user.listed_count])
