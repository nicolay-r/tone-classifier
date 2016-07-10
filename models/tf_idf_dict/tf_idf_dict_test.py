#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from psycopg2 import connect
from pymystem3 import Mystem
from inspect import getsourcefile
from os.path import abspath, dirname
from etvoc import ExtendedTermVocabulary

curr_dir = dirname(abspath(getsourcefile(lambda:0)))
sys.path.insert(0, curr_dir + '/../_aux')
from vocs import TermVocabulary, DocVocabulary
from msg import Message
from features import Features
import pconf
import twits
import prob
import test
import json
import vec

argc = len(sys.argv)
if (argc == 1):
    print """%s\n%s\n%s\n%s\n%s\n%s"""%(
        "Usage: baseline_bank_test <database> <train_table> <output> <pconf_output>",
        "<task_type> -- type of task",
        "<database> -- database to connect for training data",
        "<test_table> -- table with testing data for bank",
        "<vocabulary> -- terms vocabulary",
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

# Initialize config files
with open("conn.conf", "r") as f:
    conn_config = json.load(f, encoding='utf-8')

features = Features("features.conf")

# Connect to a database
connSettings = """dbname=%s user=%s password=%s host=%s"""%(config['database'],
    conn_config["user"], conn_config["password"], conn_config["host"])
conn = connect(connSettings)
cursor = conn.cursor()

# create new etalon table
new_etalon_table = 'tf_idf_dict_' + config['task_type'] + '_new_etalon'
result_table =  'tf_idf_dict_' + config['task_type'] + '_results'
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
    print "class:\t%s"%(score)
    # getting twits with the same score
    twits.get(config['task_type'], cursor, etalon_table, score, limit)
    # processing twits
    row = twits.next_row(cursor, score, 'test')
    processed_rows = 0
    total_rows = cursor.rowcount
    while row is not None:
        text = row[0]
        index = row[1]
        message = Message(text=text, mystem=mystem, configpath="msg.conf",
            task_type=config["task_type"])
        message.process()
        terms = message.get_terms()
        #test.add_row(conn, new_etalon_table, columns, row[2:])
        doc_voc.add_doc(terms)
        vectors.append({'id': index, 'terms' : terms,
            'features' : features.create(terms, message=text) })
        # next row
        row = twits.next_row(cursor, score, 'test')
        processed_rows += 1

        print "\rProgress: %.2f%% [%d/%d]"%(float(processed_rows)*100/total_rows,
            processed_rows, total_rows),
    print ""
# make problem
print "build extended term vocabulary"
ext_voc = ExtendedTermVocabulary(curr_dir + "/russian.tsv")
for vector in vectors:
    problem.append(vec.train_vector(vector['id'], doc_voc,
        term_voc, ext_voc, vector['terms'], vector['features']))

#save problem
prob.save(problem, config['output'])

#save .pconf
pconf.save(config['task_type'], new_etalon_table,
    result_table, config['pconf_output'])
