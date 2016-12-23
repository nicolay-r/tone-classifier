#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
from psycopg2 import connect
from pymystem3 import Mystem

# core
import core.utils
from core.vocs import TermVocabulary, DocVocabulary
from core.msg import Message
from core.features import Features

import tweets
import pconf
import prob
import vec


if len(sys.argv) == 1:
    print """%s\n%s\n%s\n%s\n%s""" % (
        "Usage: ./{} <database> <train_table> <output> <pconf_output>".format(
            sys.argv[0]),
        "<task_type> -- type of task",
        "<database> -- database to connect for training data",
        "<test_table> -- table with testing data for bank",
        "<vocabulary> -- vocabulary",
        "<output> -- file to save tonality vectors",
        "<pconf_output> -- file to save configuration for predict.py")
    exit(0)

config = {
    'task_type': sys.argv[1],
    'database': sys.argv[2],
    'test_table': sys.argv[3],
    'vocabulary': sys.argv[4],
    'output': sys.argv[5],
    'pconf_output': sys.argv[6]
}
message_configpath = "msg.conf"

etalon_table = config['test_table']

# Initialize config files
with open("msg.conf", "r") as f:
    msg_config = json.load(f, encoding='utf-8')

features = Features("features.conf")

# Connect to a database
connectionSettings = """dbname=%s user=%s
                        password=%s host=%s""" % (config['database'],
                                                  core.utils.PGSQL_USER,
                                                  core.utils.PGSQL_PWD,
                                                  core.utils.PGSQL_HOST)
connection = connect(connectionSettings)
cursor = connection.cursor()

# Create new etalon table
new_etalon_table = 'tf_idf_{}_new_etalon'.format(config['task_type'])
out_table = 'tf_idf_{}_results'.format(config['task_type'])

print "Create table:", new_etalon_table
core.utils.create_table_as(connection, new_etalon_table, etalon_table)
columns = tweets.get_score_columns(config['task_type'])

# Make problem
mystem = Mystem(entire_input=False)
term_vocabulary = TermVocabulary(config['vocabulary'])
doc_vocabulary = DocVocabulary()
problem = []
limit = sys.maxint
vectors = []

for score in [-1, 0, 1]:
    print "Class:\t%s" % (score)
    # getting tweets with the same score
    request = tweets.tweets_filter_sql_request(config['task_type'], cursor,
                                               etalon_table, score, limit)
    for row in core.utils.table_iterate(connection, request):
        # row = tweets.next_row(cursor, score, 'test')
        text = row[0]
        index = row[1]

        message = Message(text, mystem, message_configpath,
                          config['task_type'])
        message.process()
        terms = message.get_terms()
        # test.add_row(connection, new_etalon_table, columns, row[2:])
        # feature: name: value
        doc_vocabulary.add_doc(terms)
        vectors.append({'id': index,
                        'terms': terms,
                        'features': features.create(terms, message=text)})
        # next row
        # row = tweets.next_row(cursor, score, 'test')

# Create problem (SVM notation)
for vector in vectors:
    problem.append(vec.train_vector(vector['id'],
                                    term_vocabulary,
                                    doc_vocabulary,
                                    vector['terms'],
                                    vector['features']))

# Save problem
prob.save(problem, config['output'])

# Save .pconf
pconf.save(config['database'],
           config['task_type'],
           new_etalon_table,
           out_table,
           config['pconf_output'])
