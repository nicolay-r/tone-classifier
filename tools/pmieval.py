#!/usr/bin/python

import os
import sys
from inspect import getsourcefile
from os.path import abspath, dirname
sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) + '/../models/aux')

from pymystem3 import Mystem
from psycopg2 import connect
from vocs import TermVocabulary
from math import log10
from msg import Message
import operator
import json
import io

def build_vocabulary(mystem, cursor, table_with_text):
    print 'Processing datata for \'%s\' vocabulary'%(table_with_text)
    cursor.execute('SELECT text from %s'%( table_with_text));
    vocabulary = TermVocabulary()
    row = cursor.fetchone()
    while (row is not None):
        message = Message(row[0], mystem)
        message.process()
        terms, features = message.get_terms_and_features()
        for t in terms:
            vocabulary.insert_term(t)
        row = cursor.fetchone()

    return vocabulary

def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

def PMI(original_voc, opposite_voc):
    corpus_size = len(merge_two_dicts(original_voc.term_in_voc_count,
        opposite_voc.term_in_voc_count))
    result = {}
    eps = 10 ** (-3)
    for term in original_voc.get_terms():
        fa = original_voc.get_term_in_voc_count(term)

        if (term in opposite_voc.term_in_voc_count):
            fb = opposite_voc.get_term_in_voc_count(term)
        else:
            fb = 0
        pmi = log10((fa+fb)*corpus_size*1.0/(fa * fb + eps))

        result[term] = pmi

    result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)

    return result

if (len(sys.argv) < 4):
    print 'usage ./pmieval.py <original_table> <opposite_table> <out>'
    exit(0)

original_table = sys.argv[1]
opposite_table = sys.argv[2]
out_filepath = sys.argv[3]

with open(".conn", "r") as connection:
    conn = json.load(connection, encoding='utf8')

# Connect to a database
settings = """dbname=%s user=%s password=%s host=%s"""%(
    conn['database'], conn["user"], conn["password"], conn["host"])
connection = connect(settings)
cursor = connection.cursor()

mystem = Mystem(entire_input=False)

v1 = build_vocabulary(mystem, cursor, original_table)
v2 = build_vocabulary(mystem, cursor, opposite_table)

scores = PMI(v1, v2)

with io.open(out_filepath, 'w', encoding='utf-8') as out:
    for pair in scores:
        out.write(("\'%s\' = %f\n"%(pair[0], pair[1])).decode('utf-8'))

