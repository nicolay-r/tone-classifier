#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from psycopg2 import connect
from pymystem3 import Mystem
from inspect import getsourcefile
from os.path import abspath, dirname
import model_core
from etvoc import ExtendedTermVocabulary

curr_dir = dirname(abspath(getsourcefile(lambda:0)))
sys.path.insert(0, curr_dir + '/../aux')
from tvoc import TermVocabulary
from msg import Message
import pconf
import twits
import prob

argc = len(sys.argv)
if (argc == 1):
    print """%s\n%s\n%s\n%s\n%s"""%(
        "Usage: baseline_bank <database> <train_table> <output>",
        "<database> -- database to connect for training data",
        "<train_table> -- table with training data for bank",
        "<output> -- file to save tonality vectors")
    exit(0)

# Connect to a database
connSettings = """dbname=%s user=%s password=%s host=%s"""%(
    sys.argv[1], "postgres", "postgres", "localhost")
conn = connect(connSettings)
cursor = conn.cursor()

# make a term vocabulary
m = Mystem(entire_input=False)
tvoc = TermVocabulary()
problem = []
limit = sys.maxint
vectors = []
for score in [-1, 0, 1]:
    # getting twits with the same score
    twits.get("bank", cursor, sys.argv[2], score, limit)
    # processing twits
    row = cursor.fetchone()
    count = 0
    while row is not None:
        text = row[0]
        index = row[1]
        terms = model_core.process_text(m, text, tvoc)
        vectors.append({'score': score, 'terms' : terms})
        # next row
        row = cursor.fetchone()
        count += 1
    print "class %s;\tvectors:%s"%(score, count)

# make problem
print "build extended term vocabulary"
etvoc = ExtendedTermVocabulary(curr_dir + "/russian.tsv")
for vector in vectors:
    problem.append(model_core.train_vector(
        vector['score'], tvoc, etvoc, vector['terms']))

#save problem
prob.save(problem, sys.argv[3])
