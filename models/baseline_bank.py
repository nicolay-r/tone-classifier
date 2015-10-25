#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from psycopg2 import connect
from pymystem3 import Mystem
from TermVocabulary import TermVocabulary
from twit import Twit
import pconf
import sys

# Text Processing
def textProcessing(mystem, text, tvoc):
        twit = Twit(text, mystem)
        twit.normalize()
        terms = twit.getLemmas()

        terms += twit.getIgnored()

        tvoc.addTerms(terms)
        return terms

# Build Problem Vector
def trainVector(tone, indexes):
        v = [tone, {}]
        for index in tvoc.getIndexes(terms):
                v[1][index] = 1
        return v

def getTwits(cursor, table, score, limit):
    cursor.execute("""SELECT text, sberbank, vtb, gazprom, alfabank,
        bankmoskvy, raiffeisen, uralsib, rshb FROM %s WHERE
        (sberbank=\'%d\' OR vtb=\'%d\' OR gazprom=\'%d\' OR alfabank=\'%d\' OR bankmoskvy=\'%d\'
        OR raiffeisen=\'%d\' OR uralsib=\'%d\' OR rshb=\'%d\') LIMIT(\'%d\');"""%(sys.argv[2],
        score, score, score, score, score, score, score, score, limit))

argc = len(sys.argv)

if (argc == 1):
        print """%s\n%s\n%s\n%s\n%s"""%(
                "Usage: baseline_bank <database> <train_table> <output>",
                "<database> -- database to connect for training data",
                "<train_table> -- table with training data for bank",
                "<output> -- file to save tonality vectors"
                "<pconf_output> -- file to save configuration for predict.py")
        exit(0)
testVectors = False
if (argc > 4):
        testVectors = True
#make problem
m = Mystem(entire_input=False)
tvoc = TermVocabulary()
problem = []

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

for score in [-1, 0, 1]:
    # getting twits with the same score
    getTwits(cursor, sys.argv[2], score, limit)
    # processing twits
    row = cursor.fetchone()
    while row is not None:
            text = row[0]
            terms = textProcessing(m, text, tvoc)
            # change to getTrainVector() method
            problem.append(trainVector(score, tvoc.getIndexes(terms)))

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

