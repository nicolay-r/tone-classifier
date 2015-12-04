#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from psycopg2 import connect
from vocs import TermVocabulary, DocVocabulary
from model_core import process_text
from pymystem3 import Mystem

if len(sys.argv) == 1:
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
mystem = Mystem()
for table in config['tables']:
    print table
    cursor.execute("""SELECT text FROM %s;"""%(table))
    row = cursor.fetchone()
    while (row is not None):
        terms, features = process_text(mystem, row[0])
        for t in terms + features.keys():
            term_voc.insert_term(t)
        row = cursor.fetchone()

term_voc.save(config['out'])
