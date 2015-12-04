#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from psycopg2 import connect
from pymystem3 import Mystem
from inspect import getsourcefile
from os.path import abspath, dirname
from etvoc import ExtendedTermVocabulary
import vec

curr_dir = dirname(abspath(getsourcefile(lambda:0)))
sys.path.insert(0, curr_dir + '/../aux')
from vocs import TermVocabulary, DocVocabulary
from msg import Message
import model_core
import pconf
import twits
import prob

argc = len(sys.argv)
if (argc == 1):
    print """%s\n%s\n%s\n%s\n%s\n%s"""%(
        "Usage: baseline_bank <database> <train_table> <output>",
        '<task_type> -- type of task',
        "<database> -- database to connect for training data",
        "<train_table> -- table with training data for bank",
        '<vocabulary> -- term vocabulary',
        "<output> -- file to save tonality vectors")
    exit(0)

config = {
    'task_type' : sys.argv[1],
    'database' : sys.argv[2],
    'train_table' : sys.argv[3],
    'vocabulary' : sys.argv[4],
    'output' : sys.argv[5]
}

# Connect to a database
connSettings = """dbname=%s user=%s password=%s host=%s"""%(
    config['database'], "postgres", "postgres", "localhost")
conn = connect(connSettings)
cursor = conn.cursor()

# make a term vocabulary
m = Mystem(entire_input=False)
term_voc = TermVocabulary(config['vocabulary'])
doc_voc = DocVocabulary()
problem = []
limit = sys.maxint
vectors = []
for score in [-1, 0, 1]:
    # getting twits with the same score
    twits.get(config['task_type'], cursor, config['train_table'], score, limit)
    # processing twits
    row = twits.next_row(cursor, score, 'train')
    count = 0
    while row is not None:
        text = row[0]
        index = row[1]
        terms, features = model_core.process_text(m, text)
        doc_voc.add_doc(terms)
        vectors.append({'score': score, 'terms' : terms, 'features' : features})
        # next row
        row = twits.next_row(cursor, score, 'train')
        count += 1
    print "class %s;\tvectors:%s"%(score, count)

# make problem
print "build extended term vocabulary"
ext_voc = ExtendedTermVocabulary(curr_dir + "/russian.tsv")
for vector in vectors:
    problem.append(vec.train_vector(vector['score'], doc_voc,
        term_voc, ext_voc, vector['terms'], vector['features']))

#save problem
prob.save(problem, config['output'])
