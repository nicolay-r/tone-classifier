#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
from psycopg2 import connect
import json
import io

def show_progress(message, current, total):
    print "\rProcessing: %.2f%% [%d/%d] (%s)"%(float(current)*100/total,
        current, total, message),
    if (current == total):
        print ""

def msg2words(msg):
    # ignore all message if it's short
    if len(msg) < 40:
        return []
    # ignore users and urls
    return [w for w in msg.split(' ')
        if len(w) > 0 and w[0] != '@' and not('http://' in w)]

def get_message_rank(msg, positive_keywords, negative_keywords):
    positive = 0
    negative = 0
    words = msg2words(msg)

    for keyword in positive_keywords:
        for word in words:
            if (keyword in word):
                #print keyword, ' IN ', msg
                positive += 1

    for keyword in negative_keywords:
        for word in words:
            if (keyword in word):
                #print keyword, ' IN ', msg
                negative += 1

    if (positive > 0 and negative == 0):
        return 1
    elif (negative > 0 and positive == 0):
        return -1
    else:
        return 0

def create_table(conn, table_name):
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS %s (
        twitid BIGINT PRIMARY KEY,
        text VARCHAR(256) DEFAULT NULL)"""%(table_name))
    cursor.execute("DELETE FROM %s"%(table_name))

    cursor.close()
    conn.commit()

def add_msg(twitid, text, table, cursor):
    cursor.execute("""INSERT INTO %s(twitid, text) SELECT \'%s\', \'%s\'
        WHERE NOT EXISTS(SELECT twitid FROM %s WHERE twitid=%s)"""%(
        table, twitid, text, table, twitid))

if len(argv) < 2:
    print """Usage: ./splitter.py <raw.csv>"""
    exit(0)

# Initialize Configuration File
with open('splitter.conf') as config:
    splitter_config = json.load(config, encoding='utf8')
connection_config = splitter_config['connection']
raw_filename = argv[1]

# Create Connection
connection_settings = "dbname=%s user=%s password=%s host=%s"%(
    connection_config['database'], connection_config["user"],
    connection_config["password"], connection_config["host"])
conn = connect(connection_settings)

# Prepare Tables
positive_table_name = splitter_config['positive_table']
create_table(conn, positive_table_name)
negative_table_name = splitter_config['negative_table']
create_table(conn, negative_table_name)

# Filter Messages
cursor = conn.cursor()
twits_processed = 0
positive_twits = 0
negative_twits = 0
line_index = 0
with io.open(raw_filename, 'rt', newline='\r\n') as f:
    lines = f.readlines()
    for line in lines:
        line_index += 1
        args = line.split(';')
        if (len(args) == 10):

            twitid = args[0]
            msg = args[3]
            rank = get_message_rank(msg, splitter_config['positive_keywords'],
                splitter_config['negative_keywords'])

            if (rank == 1):
                add_msg(twitid, msg, positive_table_name, cursor)
                positive_twits += 1
            elif (rank == -1):
                add_msg(twitid, msg, negative_table_name, cursor)
                negative_twits += 1

            twits_processed += 1

        show_progress("all: %d| \'+\': %d| \'-\': %d"%(twits_processed,
            positive_twits, negative_twits), line_index, len(lines))
        conn.commit()

cursor.close()
conn.close()
