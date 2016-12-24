# -*- coding: utf-8 -*-

import sys
from pymystem3 import Mystem

# core
import core
from core.vocs import DocVocabulary
from core.features import Features
from core.msg import Message

import tweets


def create_problem(connection, task_type, table, vectorizer, term_vocabulary,
                   features_configpath,
                   message_configpath):
    """
    Creates problem (vectors from messages with additional features)

    Arguments:
    ---------
        connection
        task_type
        table -- table name
        vectorizer -- function for producing vector from terms
        term_vocabulary -- vocabulary of terms
        features_configpath
        messsage_configpath

    Returns:
    --------
        prob
    """
    mystem = Mystem(entire_input=False)
    features = Features(features_configpath)
    doc_vocabulary = DocVocabulary()
    limit = sys.maxint
    vectors = []

    for score in [-1, 0, 1]:
        print "Class:\t%s" % (score)
        # getting tweets with the same score
        cursor = connection.cursor()
        request = tweets.tweets_filter_sql_request(task_type, cursor, table,
                                                   score, limit)
        for row in core.utils.table_iterate(connection, request):
            # row = tweets.next_row(cursor, score, 'test')
            text = row[0]
            index = row[1]

            message = Message(text, mystem, message_configpath, task_type)
            message.process()
            terms = message.get_terms()
            # test.add_row(connection, new_etalon_table, columns, row[2:])
            # feature: name: value
            doc_vocabulary.add_doc(terms)
            unicode_terms = to_unicode(terms)
            vectors.append({'id': index,
                            'terms': unicode_terms,
                            'features': features.create(unicode_terms,
                                                        message=text)})
            # next row
            # row = tweets.next_row(cursor, score, 'test')

    # Create problem
    problem = []
    for vector in vectors:
        problem.append(vectorizer(vector['id'],
                                  term_vocabulary,
                                  doc_vocabulary,
                                  vector['terms'],
                                  vector['features']))
    return problem


def to_unicode(terms):
    unicode_terms = []
    for term in terms:
        if (isinstance(term, str)):
            unicode_terms.append(unicode(term, 'utf-8'))
        else:
            unicode_terms.append(term)

    return unicode_terms
