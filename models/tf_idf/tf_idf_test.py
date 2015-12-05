#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from psycopg2 import connect
from pymystem3 import Mystem
from inspect import getsourcefile
from os.path import abspath, dirname
import vec

sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) + '/../aux')
from vocs import TermVocabulary, DocVocabulary
from msg import Message
import pconf
import twits
import prob
import test

argc = len(sys.argv)
if (argc == 1):
    print """%s\n%s\n%s\n%s\n%s"""%(
        "Usage: baseline_bank_test <database> <train_table> <output> <pconf_output>",
        "<task_type> -- type of task",
        "<database> -- database to connect for training data",
        "<test_table> -- table with testing data for bank",
        "<vocabulary> -- vocabulary",
        "<output> -- file to save tonality vectors",
        "<pconf_output> -- file to save configuration for predict.py")
    exit(0)

config = {
    'task_type' : sys.argv[1],
    'database' : sys.argv[2],
    'test_table' : sys.argv[3],
    'vocabulary' : sys.argv[4],
    'output' : sys.argv[5],
    'pconf_output' : sys.argv[6]
}

etalon_table = config['test_table']

# Connect to a database
connSettings = """dbname=%s user=%s password=%s host=%s"""%(
    config['database'], "postgres", "postgres", "localhost")
conn = connect(connSettings)
cursor = conn.cursor()

# create new etalon table
new_etalon_table = 'tf_idf_' + config['task_type'] + '_new_etalon'
out_table = 'tf_idf_' + config['task_type'] + '_results'
print "create_table:", new_etalon_table
test.create_table_as(conn, new_etalon_table, etalon_table)
columns = twits.get_score_columns(config['task_type'])

# make problem
mystem = Mystem(entire_input=False)
term_voc = TermVocabulary(config['vocabulary'])
doc_voc = DocVocabulary()
problem = []
limit = sys.maxint
vectors = []
for score in [-1, 0, 1]:
    # getting twits with the same score
    twits.get(config['task_type'], cursor, etalon_table, score, limit)
    # processing twits
    row = twits.next_row(cursor, score, 'test')
    count = 0
    while row is not None:
        text = row[0]
        index = row[1]
        message = Message(text, mystem)
        message.process()
        terms, features = message.get_terms_and_features()
        test.add_row(conn, new_etalon_table, columns, row[2:])
        # feature: name: value
        doc_voc.add_doc(terms)
        vectors.append({'id': index, 'terms' : terms, 'features' : features})
        # next row
        row = twits.next_row(cursor, score, 'test')
        count += 1
    print "class:\t%s; %s"%(score, count)

# make problem
for vector in vectors:
    problem.append(vec.train_vector(vector['id'],
        term_voc, doc_voc, vector['terms'], vector['features']))

#save problem
prob.save(problem, config['output'])

#save .pconf
pconf.save(config['task_type'], new_etalon_table,
    out_table, config['pconf_output'])
