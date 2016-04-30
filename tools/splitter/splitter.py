#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from psycopg2 import connect
from pymystem3 import Mystem
from inspect import getsourcefile
from os.path import abspath, dirname
import json
import io
from table import Table

sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) + '/../../models/aux')
from msg import Message
from features import Features

def show_progress(message, current, total):
    print "\rProcessing: %.2f%% [%d/%d] (%s)"%(float(current)*100/total,
        current, total, message),
    if (current == total):
        print ""

def msg2words(msg, splitter_config):
    if len(msg) < splitter_config['message_min_len']:
        # ignore all message if it's short
        return []
    words = msg.split(' ')
    if (len(words) > 0 and words[0] == 'RT'):
        # ignore retweets
        return []
    # ignore users and urls
    return [w for w in words
        if len(w) > 0 and w[0] != '@' and not('http://' in w)]

def get_message_rank(text, mystem, features, splitter_config):
    message = Message(text=text,
            mystem=mystem,
            configpath="msg.conf",
            task_type="none")

    message.process()
    terms = message.get_terms()

    scores = features.create(terms, message=text)

    mn = min(scores.values())
    mx = max(scores.values())
    if (mn > 0 and mx > 0):
        return 1
    elif (mn < 0 and mx < 0):
        return -1
    else:
        return 0


def process_message(text):
    text = text.replace('\'', '\'\'')
    if (text[0] == '\"'):
        text = text[1:]
    if (text[len(text)-1] == '\"'):
        text = text[:len(text)-1]
    return text.encode('utf-8')

if len(sys.argv) < 2:
    print """Usage: ./splitter.py <raw.csv>"""
    exit(0)

# Initialize Configuration Files
with open('splitter.conf') as config:
    splitter_config = json.load(config, encoding='utf8')
with open('conn.conf') as config:
    connection_config = json.load(config, encoding='utf8')
raw_filename = sys.argv[1]

# Create Connection
connection_settings = "dbname=%s user=%s password=%s host=%s"%(
    connection_config['database'], connection_config["user"],
    connection_config["password"], connection_config["host"])

# Prepare Tables
positive_table = Table(connection_settings, splitter_config['positive_table'])
positive_table.create()

negative_table = Table(connection_settings, splitter_config['negative_table'])
negative_table.create()

# Filter Messages
mystem = Mystem(entire_input=False)
features = Features("features.conf")
twits_processed = 0
positive_twits = 0
negative_twits = 0
line_index = 0
with io.open(raw_filename, 'rt', newline='\r\n') as f:
    lines = f.readlines()
    for line in lines:
        line_index += 1
        args = line.split(';')

        # check that line contains all information
        if (len(args) == 10):

            twitid = args[0]
            msg = process_message(args[3])
            rank = get_message_rank(msg, mystem, features, splitter_config)

            if (rank == 1):
                positive_table.add_message(twitid, msg.decode('utf-8'))
                positive_twits += 1
            elif (rank == -1):
                negative_table.add_message(twitid, msg.decode('utf-8'))
                negative_twits += 1

            twits_processed += 1

        show_progress("all: %d| \'+\': %d| \'-\': %d"%(twits_processed,
            positive_twits, negative_twits), line_index, len(lines))
        #conn.commit()

positive_table.close_connection()
negative_table.close_connection()
