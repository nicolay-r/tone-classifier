#!/usr/bin/python

import tweepy
import json
import sys
import time
import os
import csv

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        t = json.loads(data)

        with open(self.filepath, 'a') as out:
            # how to save
            self.csv_writer = csv.writer(out, delimiter=';',
                quoting=csv.QUOTE_MINIMAL)

            self.csv_writer.writerow([t['id'], t['created_at'],
                t['user']['screen_name'].encode('utf-8'),
                t['text'].encode('utf-8'), t['retweet_count'],
                t['user']['favourites_count'], t['user']['statuses_count'],
                t['user']['followers_count'], t['user']['friends_count'],
                t['user']['listed_count']])

        return True

    def on_error(self, status):
        print status

    def __init__(self, filepath):
        # where to save
        self.filepath = filepath


if (len(sys.argv) == 1):
    print "usage: ./getter.py <keys_file> <out_folder>"
    exit(0)

keys_filename = sys.argv[1]
out_folder = sys.argv[2]
out_filepath = os.path.join(out_folder, str(time.ctime()).replace(' ', '_'))
with open(keys_filename) as data:
    keys = json.load(data)

# Create listener object
listener = StdOutListener(out_filepath)

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_secret'])

# https://dev.twitter.com/docs/streaming-apis
stream = tweepy.Stream(auth, listener)

# Setting up streamer
while (True):
    print "Reconnect ..."
    try:
        stream.filter(track=['twitter'], languages=['ru'])
    except Exception as e:
        print "Exception: ", str(e)

