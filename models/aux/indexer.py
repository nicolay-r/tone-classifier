#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
from psycopg2 import connect
from vocs import TermVocabulary, DocVocabulary
from msg import Message
from pymystem3 import Mystem

if len(sys.argv) < 4:
    print "usage: indexer.py <database> <out> <tablelist>"
    exit(0)

config = {'database':sys.argv[1], 'out':sys.argv[2], 'tables':sys.argv[3:]}

# Init configuration files
with open("conn.conf", "r") as f:
    conn_config = json.load(f, encoding='utf-8')
with open("indexer.conf", "r") as f:
    indexer_config = json.load(f, encoding='utf-8')

# Connect to a database
settings = """dbname=%s user=%s password=%s host=%s"""%(config['database'],
    conn_config["user"], conn_config["password"], conn_config["host"])
connection = connect(settings)
cursor = connection.cursor()

# Add all possible words terms
term_voc = TermVocabulary()
mystem = Mystem(entire_input=False)
for table in config['tables']:
    print table
    cursor.execute("""SELECT text FROM %s;"""%(table))
    row = cursor.fetchone()
    count = 0
    while (row is not None):
        message = Message(text=row[0], mystem=mystem, configpath="msg.conf")
        message.process()
        terms = message.get_terms()
        for t in terms:
            term_voc.insert_term(t)
        row = cursor.fetchone()
        count += 1
    print "messages count: ", count

# Add all possible features
print "features: %s"%(indexer_config['feature_names'])
for feature_name in indexer_config['feature_names']:
    term_voc.insert_term(feature_name)

# Show and save result
term_voc.top(50)
term_voc.save(config['out'])
