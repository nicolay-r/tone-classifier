#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from psycopg2 import connect
from pymystem3 import Mystem
from inspect import getsourcefile
from os.path import abspath, dirname
import model_core

sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) + '/..')
from tvoc import TermVocabulary
from msg import Message
import pconf
import twits

argc = len(sys.argv)
if (argc == 1):
    print """%s\n%s\n%s\n%s\n%s"""%(
        "Usage: baseline_bank <database> <train_table> <output>",
        "<database> -- database to connect for training data",
        "<train_table> -- table with training data for bank",
        "<output> -- file to save tonality vectors",
        "<pconf_output> -- file to save configuration for predict.py")
    exit(0)

testVectors = False
if (argc > 4):
    testVectors = True

# Connect to a database
connSettings = """dbname=%s user=%s password=%s host=%s"""%(
    sys.argv[1], "postgres", "postgres", "localhost")

conn = connect(connSettings)
cursor = conn.cursor()

if (testVectors):
    # taking all results
    limit = sys.maxint
else:
    limit = 350

# make problem
m = Mystem(entire_input=False)
tvoc = TermVocabulary()
problem = []
for score in [-1, 0, 1]:
    # getting twits with the same score
    twits.get("bank", cursor, sys.argv[2], score, limit)
    # processing twits
    row = cursor.fetchone()
    while row is not None:
        text = row[0]
        index = row[1]
        terms = model_core.process_text(m, text, tvoc)

        if (argc > 4): # in case of test collection
            problem.append(model_core.train_vector(index, tvoc, terms))
        else: # in case of train collection
            problem.append(model_core.train_vector(score, tvoc, terms))
        # next row
        row = cursor.fetchone()

#save problem
with open(sys.argv[3], "w") as f:
    for pv in problem:
        f.write("%s "%(pv[0]))
        for index, value in sorted(pv[1].iteritems()):
            f.write("%s:%s "%(index, value))
        f.write("\n");

#save .pconf
if (argc > 4):
    pconf.save("bank", sys.argv[2],
        "baseline_bank_results", sys.argv[4])
