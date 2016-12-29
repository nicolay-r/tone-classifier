#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Text indexing, presented as 'text' field in tablelist
"""

# core
import utils
import vocs
from msg import TwitterMessageParser


def create_term_vocabulary(connection, tables, message_configpath):
    """
    Arguments
    ---------
        connection
        tables
        message_configpath

    Returns
    -------
        term_vocabulary -- vocabulary of all terms, presented in 'tables'
    """

    # Init configuration files
    # with open("indexer.conf", "r") as f:
    #    indexer_config = json.load(f, encoding='utf-8')

    # Add all possible words terms
    term_vocabulary = vocs.TermVocabulary()
    message_parser = TwitterMessageParser(message_configpath)
    for table in tables:
        print "Extracting terms from messages of '%s' table ..." % (table)
        sql_request = "SELECT text FROM %s;" % (table)
        for row in utils.table_iterate(connection, sql_request):
            message_parser.parse(row[0])
            terms = message_parser.get_terms()
            for t in terms:
                term_vocabulary.insert_term(t)

    # Add all possible features
    # print "Features: %s" % (indexer_config['feature_names'])
    # for feature_name in indexer_config['feature_names']:
    #     term_voc.insert_term(feature_name)

    return term_vocabulary
