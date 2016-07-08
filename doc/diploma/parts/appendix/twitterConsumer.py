#!/usr/bin/python
import tweepy, json, sys, time, os, csv

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        t = json.loads(data)
        with open(self.filepath, 'a') as out: # how to save
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
    def __init__(self, filepath): # where to save
        self.filepath = filepath

# Create listener object
listener = StdOutListener(data_filepath)
auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_secret'])
# https://dev.twitter.com/docs/streaming-apis
stream = tweepy.Stream(auth, listener)
# Setting up streamer
with open(log_file, 'w') as log:
    while (True):
        log.write("Reconnect ...")
        try:
            stream.filter(track=['twitter'], languages=['ru'])
        except Exception as e:
            log.write("Exception: %s"%(str(e)))
