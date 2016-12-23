#!/usr/bin/python
# -*- coding: utf-8 -*-


# TODO:
# Реализовать функцию получения словаря индексированных слов, вместо
# сохранения.

"""
Text indexing, presented as 'text' field in tablelist
"""

import sys
import json
from psycopg2 import connect
from pymystem3 import Mystem

# core
import utils
from vocs import TermVocabulary
from msg import Message

if len(sys.argv) < 4:
    print "usage: {} <database> <out> <tablelist>".format(sys.argv[0])
    exit(0)

config = {'database': sys.argv[1],
          'out': sys.argv[2],
          'tables': sys.argv[3:]}
message_configpath = "msg.conf"

# Init configuration files
with open("indexer.conf", "r") as f:
    indexer_config = json.load(f, encoding='utf-8')

# Connect to a database
settings = "dbname=%s user=%s password=%s host=%s" % (config['database'],
                                                      utils.PGSQL_USER,
                                                      utils.PGSQL_PWD,
                                                      utils.PGSQL_HOST)

connection = connect(settings)
cursor = connection.cursor()

# Add all possible words terms
term_voc = TermVocabulary()
mystem = Mystem(entire_input=False)
for table in config['tables']:

    print "Extracting terms from messages of '%s' table ..." % (table)

    for row in utils.table_iterate(connection,
                                   "SELECT text FROM %s;" % (table)):

        message = Message(text=row[0],
                          mystem=mystem,
                          configpath=message_configpath)
        message.process()
        terms = message.get_terms()
        for t in terms:
            term_voc.insert_term(t)

# Add all possible features
print "features: %s" % (indexer_config['feature_names'])
for feature_name in indexer_config['feature_names']:
    term_voc.insert_term(feature_name)

# Show and save result
# term_voc.top(50)
term_voc.save(config['out'])
