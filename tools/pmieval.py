#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from inspect import getsourcefile
from os.path import abspath, dirname
sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) + '/../models/aux')

from pymystem3 import Mystem
from psycopg2 import connect
from vocs import TermVocabulary, DocVocabulary
from math import log
from msg import Message
import operator
import json
import io

def build_vocabularies(mystem, cursor, table_with_text):
    print 'Processing datata for \'%s\' vocabulary'%(table_with_text)
    cursor.execute('SELECT text from %s'%( table_with_text));

    term_voc = TermVocabulary()
    doc_voc = DocVocabulary()

    row = cursor.fetchone()
    rows = 0
    while (row is not None):
        message = Message(row[0], mystem)
        message.process()

        terms, features = message.get_terms_and_features()
        for t in terms:
            term_voc.insert_term(t)

        doc_voc.add_doc(terms)

        row = cursor.fetchone()
        rows = rows + 1

    print rows
    return (term_voc, doc_voc)

def merge_two_lists(x, y):
    return list(set(x).union(y))

def p(docs_with_term, total_docs):
    return float(docs_with_term) / total_docs

def PMI(term, dv1, dv2):
    t1 = dv1.get_term_in_docs_count_safe(term) + 1
    t2 = dv2.get_term_in_docs_count_safe(term) + 1
    N1 = dv1.get_docs_count()
    N2 = dv2.get_docs_count()

    #if (term.decode('utf-8') == 'на'.decode('utf-8')):
    #    print t1, ' ', t2

    return log(p(t1, N1 + N2) * float(N1 + N2) /
        (p(t1 + t2, N1 + N2) * p(N1, N1 + N2)), 2)

def SO(tv1, dv1, tv2, dv2):
    N = dv1.get_docs_count() + dv2.get_docs_count()

    result = {}

    all_terms = merge_two_lists(tv1.get_terms(), tv2.get_terms())
    for term in all_terms:
        result[term] = PMI(term, dv1, dv2) - PMI(term, dv2, dv1)

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

tv1, dv1 = build_vocabularies(mystem, cursor, original_table)
tv2, dv2 = build_vocabularies(mystem, cursor, opposite_table)

scores = SO(tv1, dv1, tv2, dv2)

with io.open(out_filepath, 'w', encoding='utf-8') as out:
    for pair in scores:
        out.write(("\'%s\' = %f\n"%(pair[0], pair[1])).decode('utf-8'))

