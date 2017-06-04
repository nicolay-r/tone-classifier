# -*- coding: utf-8 -*-

"""
Text indexing, presented as 'text' field in tablelist
"""

import pandas as pd
from TermVocabulary import TermVocabulary
from msg import TwitterMessageParser


def create_term_vocabulary(table_filepaths, message_configpath):
    """
    task_type: str
        possible values are 'bank' or 'tkk' task types.
    table_filepaths : str[]
        filepaths of tables, described in 'csv' format.
    message_configpath : str
    returns: TermVocabulary
        vocabulary of all terms, presented in 'table_filepaths'
    """

    term_vocabulary = TermVocabulary()
    message_parser = TwitterMessageParser(message_configpath)
    for table in table_filepaths:
        df = pd.read_csv(table, sep=',')
        print "Extracting terms from '%s' file ..." % (table)
        for row in df.index:
            msg = df['text'][row]
            message_parser.parse(msg)
            for t in message_parser.get_terms():
                term_vocabulary.insert_term(t)

    return term_vocabulary
