#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from inspect import getsourcefile
from os.path import abspath, dirname
sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) +
    '/../../models/aux')

from pymystem3 import Mystem
from psycopg2 import connect
from vocs import TermVocabulary, DocVocabulary
from math import log
from msg import Message
import operator
import json
import io

def show_progress(message, current, total):
    print "\r%s: %.2f%% [%d/%d]"%(message, float(current)*100/total, current,
        total),
    # Going to the next line in case of Finish
    if (current == total):
        print ""

def build_vocabularies(mystem, cursor, table_with_text, msg_config_path):
    print 'Processing data for \'%s\' vocabulary'%(table_with_text)
    cursor.execute('SELECT text from %s'%( table_with_text));

    term_voc = TermVocabulary()
    doc_voc = DocVocabulary()

    row = cursor.fetchone()
    total_rows = cursor.rowcount
    processed_rows = 0
    while (row is not None):
        message = Message(text=row[0], mystem=mystem, configpath=msg_config_path)
        message.process()

        terms = message.get_terms()
        for t in terms:
            term_voc.insert_term(t)

        doc_voc.add_doc(terms)
        row = cursor.fetchone()
        processed_rows += 1
        show_progress("Building vocabulary", processed_rows, total_rows)

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

def to_unicode(term):
    if isinstance(term, str):
        return unicode(term, 'utf-8')
    elif isinstance(term, unicode):
        return term

def SO(tv1, dv1, tv2, dv2):
    N = dv1.get_docs_count() + dv2.get_docs_count()

    r1 = {}

    all_terms = merge_two_lists(tv1.get_terms(), tv2.get_terms())
    processed_terms = 0
    for term in all_terms:
        r1[to_unicode(term)] = PMI(term, dv1, dv2) - PMI(term, dv2, dv1)
        processed_terms += 1
        show_progress("Calculating SO", processed_terms, len(all_terms))

    r1 = sorted(r1.items(), key=operator.itemgetter(1), reverse=True)

    return r1

def save(connection, out_table, r):
    cursor = connection.cursor()
    max_term_length = 50
    cursor.execute("""CREATE TABLE IF NOT EXISTS {table}(
                            term VARCHAR({max_length}),
                            tone REAL)""".format(table = out_table, max_length =
        max_term_length));
    cursor.execute("DELETE FROM {table}".format(table = out_table));
    connection.commit()

    for pair in r:
        if (len(pair[0]) < max_term_length):
            cursor.execute("""INSERT INTO {table} ({term}, {value})
                VALUES (\'{t}\', {v})""".format(term="term", value='tone',
                table=out_table, t=pair[0].encode('utf-8').replace("'", "''"), v=pair[1]));

        connection.commit()

if (len(sys.argv) < 3):
    print 'usage ./pmieval.py <original_table> <opposite_table> <result_table>'
    exit(0)

original_table = sys.argv[1]
opposite_table = sys.argv[2]
result_table = sys.argv[3]
msg_config_path = "msg.conf"

with open(".conn", "r") as connection:
    conn = json.load(connection, encoding='utf8')

# Connect to a database
settings = """dbname=%s user=%s password=%s host=%s"""%(
    conn['database'], conn["user"], conn["password"], conn["host"])
connection = connect(settings)
cursor = connection.cursor()

mystem = Mystem()

tv1, dv1 = build_vocabularies(mystem, cursor, original_table, msg_config_path)
tv2, dv2 = build_vocabularies(mystem, cursor, opposite_table, msg_config_path)

r1 = SO(tv1, dv1, tv2, dv2)

# save results
save(connection, result_table, r1)
