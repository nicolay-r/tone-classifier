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

sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) + '/../../models/_aux')
from msg import Message
from features import Features


def show_progress(message, current, total):
    print "\rProcessing: %.2f%% [%d/%d] (%s)"%(float(current)*100/total,
        current, total, message),
    if (current == total):
        print ""

if len(sys.argv) < 2:
    print """Usage: ./splitter.py <raw.csv> [--clean]"""
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
negative_table = Table(connection_settings, splitter_config['negative_table'])

positive_table.create()
negative_table.create()
if len(sys.argv) == 3 and sys.argv[2] == '--clean':
    positive_table.clean()
    negative_table.clean()

# Filter Messages
mystem = Mystem(entire_input=False)
features = Features("features.conf")
twits_processed = 0
positive_twits = 0
negative_twits = 0
with io.open(raw_filename, 'rt', newline='\r\n', encoding='utf-8') as f:
    lines = f.readlines()
    for line_index, line in enumerate(lines):
        args = line.split(';')
        twitid = args[0]
        # merge parts of message
        msg = ";".join(args[3:len(args)-8]).replace('\'', '\'\'')
        # remove quotes
        if (len(msg) > 0 and msg[0] == '"' and msg[-1] == '"'):
            msg = msg[1:-1]
        rank = int(args[-2])

        if (rank > 0):
            positive_table.add_message(twitid, msg)
            positive_twits += 1
        elif (rank < 0):
            negative_table.add_message(twitid, msg)
            negative_twits += 1

        twits_processed += 1

        show_progress("all: %d| \'+\': %d| \'-\': %d" % (
                       twits_processed, positive_twits, negative_twits),
                       line_index, len(lines))

        line_index += 1

positive_table.close_connection()
negative_table.close_connection()
