#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Text indexing, presented as 'text' field in tablelist
"""

import sys
import utils

from tweets import tweets_filter_sql_request
from TermVocabulary import TermVocabulary
from msg import TwitterMessageParser


def create_term_vocabulary(connection, tables, task_type, message_configpath):
    """
    connection : psycopg2
        psycopg2 connection object
    task_type: str
        possible values are 'bank' or 'tkk' task types.
    tables : str[]
    message_configpath : str
    returns: TermVocabulary
        vocabulary of all terms, presented in 'tables'
    """

    # TODO: Guarantee that we don't have different sentiment labels for
    # for the same message.
    term_vocabulary = TermVocabulary()
    message_parser = TwitterMessageParser(message_configpath)
    for table in tables:
        print "Extracting terms from messages of '%s' table ..." % (table)
        for sentiment in [-1, 0, 1]:
            sql_request = tweets_filter_sql_request(
                task_type, table, sentiment, sys.maxint)
            for row in utils.table_iterate(connection, sql_request):
                message_parser.parse(row[0])
                for t in message_parser.get_terms():
                    term_vocabulary.insert_term(t, sentiment)

    return term_vocabulary
