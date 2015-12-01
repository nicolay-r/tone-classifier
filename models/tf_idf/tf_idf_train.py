#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from psycopg2 import connect
from pymystem3 import Mystem
from inspect import getsourcefile
from os.path import abspath, dirname
import model_core

sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) + '/../aux')
from tvoc import TermVocabulary
from msg import Message
import pconf
import twits
import prob

argc = len(sys.argv)
if (argc == 1):
    print """%s\n%s\n%s\n%s\n%s"""%(
        "Usage: baseline_bank <database> <train_table> <output>",
        "<task> -- task type",
        "<database> -- database to connect for training data",
        "<train_table> -- table with training data for bank",
        "<output> -- file to save tonality vectors")
    exit(0)

config = {
    'task_type' : sys.argv[1],
    'database' : sys.argv[2],
    'train_table' : sys.argv[3],
    'output' : sys.argv[4]
}

# Connect to a database
connSettings = """dbname=%s user=%s password=%s host=%s"""%(
    config['database'], "postgres", "postgres", "localhost")
conn = connect(connSettings)
cursor = conn.cursor()

# make a term vocabulary
m = Mystem(entire_input=False)
tvoc = TermVocabulary()
problem = []
limit = sys.maxint # no limits
vectors = []
for score in [-1, 0, 1]:
    tmpvoc = TermVocabulary()
    # getting twits with the same score
    twits.get(config['task_type'], cursor, config['train_table'], score, limit)
    # processing twits
    row = twits.next_row(cursor, score, 'train')
    count = 0
    while row is not None:
        text = row[0]
        index = row[1]
        terms = model_core.process_text(m, text, tvoc)
        model_core.process_text(m, text, tmpvoc)
        vectors.append({'score': score, 'terms' : terms})
        # next row
        row = twits.next_row(cursor, score, 'train')
        count += 1
    tmpvoc.top(30)
    print "class %s;\tvectors:%s"%(score, count)

# make problem
for vector in vectors:
    problem.append(model_core.train_vector(
        vector['score'], tvoc, vector['terms']))

#save problem
prob.save(problem, config['output'])
