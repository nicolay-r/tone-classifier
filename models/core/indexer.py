# -*- coding: utf-8 -*-

"""
Text indexing, presented as 'text' field in tablelist
"""

import utils
from TermVocabulary import TermVocabulary
from msg import TwitterMessageParser


def create_term_vocabulary(connection, tables, message_configpath):
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

    term_vocabulary = TermVocabulary()
    message_parser = TwitterMessageParser(message_configpath)
    for table in tables:
        print "Extracting terms from messages of '%s' table ..." % (table)
        sql_request = "SELECT text FROM %s;" % (table)
        for row in utils.table_iterate(connection, sql_request):
            message_parser.parse(row[0])
            for t in message_parser.get_terms():
                term_vocabulary.insert_term(t)

    return term_vocabulary
