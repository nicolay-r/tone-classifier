#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from psycopg2 import connect
from vocs import TermVocabulary, DocVocabulary
from msg import Message
from pymystem3 import Mystem

if len(sys.argv) == 0:
    print "usage: indexer.py <database> <out> <tablelist>"
    exit(0)

config = {
    'database' : sys.argv[1],
    'out' : sys.argv[2],
    'tables' : sys.argv[3:]
}

# Connect to a database
settings = """dbname=%s user=%s password=%s host=%s"""%(
    config['database'], "postgres", "postgres", "localhost")
connection = connect(settings)
cursor = connection.cursor()

term_voc = TermVocabulary()
mystem = Mystem(entire_input=False)
for table in config['tables']:
    print table
    cursor.execute("""SELECT text FROM %s;"""%(table))
    row = cursor.fetchone()
    count = 0
    while (row is not None):
        message = Message(row[0], mystem)
        message.process()
        terms, features = message.get_terms_and_features()
        for t in terms + features.keys():
            term_voc.insert_term(t)
        row = cursor.fetchone()
        count += 1
    print "messages count: ", count
term_voc.top(50)
term_voc.save(config['out'])
