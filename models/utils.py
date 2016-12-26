# -*- coding: utf-8 -*-

# global
import sys
import psycopg2
from pymystem3 import Mystem

# core
import core
import core.utils
import core.indexer
from core.vocs import DocVocabulary
from core.features import Features
from core.msg import TwitterMessage

import tweets
import prob
import pconf


def vectorization_core(vectorizer):
    """
    Main function of collection vectorization

    Argument
    --------
        vectorizer -- message vectorization function

    Returns
    -------
        None
    """
    if (sys.argv < 8):
        exit(0)

    config = {'task_type': sys.argv[1],
              'database': sys.argv[2],
              'train_table': sys.argv[3],
              'test_table': sys.argv[4],
              'train_output': sys.argv[5],
              'test_output': sys.argv[6],
              'pconf_output': sys.argv[7]}
    message_configpath = "msg.conf"
    features_configpath = "features.conf"

    # Connect to a database
    connectionSettings = """dbname=%s user=%s
                            password=%s host=%s""" % (config['database'],
                                                      core.utils.PGSQL_USER,
                                                      core.utils.PGSQL_PWD,
                                                      core.utils.PGSQL_HOST)
    connection = psycopg2.connect(connectionSettings)

    # Create vocabulary of terms
    term_vocabulary = core.indexer.create_term_vocabulary(
                                connection,
                                [config['train_table'], config['test_table']],
                                message_configpath)

    # Train problem
    train_problem = create_problem(connection,
                                   config['task_type'],
                                   'train',
                                   config['train_table'],
                                   vectorizer,
                                   term_vocabulary,
                                   features_configpath,
                                   message_configpath)

    # Test problem
    test_problem = create_problem(connection,
                                  config['task_type'],
                                  'test',
                                  config['test_table'],
                                  vectorizer,
                                  term_vocabulary,
                                  features_configpath,
                                  message_configpath)

    result_table = config['test_table'] + '_problem'
    core.utils.drop_table(connection, result_table)
    core.utils.create_table_as(connection, config['test_table'], result_table)

    # Save
    prob.save(train_problem, config['train_output'])
    prob.save(test_problem, config['test_output'])
    pconf.save(config['database'],
               tweets.get_score_columns(config['task_type']),
               result_table,
               config['pconf_output'])


def create_problem(connection, task_type, collection_type, table, vectorizer,
                   term_vocabulary, features_configpath, message_configpath):
    """
    Creates problem (vectors from messages with additional features)

    Arguments:
    ---------
        connection -- pgsql connection
        task_type
        collection_type -- could be 'train' or 'test', it affects on the
                           generated vector prefixes (tone score for 'train'
                           task, and 'id' for 'test' task respectively)
        table -- table name
        vectorizer -- function for producing vector from terms
        term_vocabulary -- vocabulary of terms
        features_configpath
        messsage_configpath

    Returns:
    --------
        problem -- list of vectorized messages
    """
    mystem = Mystem(entire_input=False)
    features = Features(connection, features_configpath)
    doc_vocabulary = DocVocabulary()
    limit = sys.maxint
    labeled_messages = []

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

            message = TwitterMessage(text,
                                     mystem,
                                     message_configpath,
                                     task_type)
            terms = message.get_terms()
            # test.add_row(connection, new_etalon_table, columns, row[2:])
            # feature: name: value
            doc_vocabulary.add_doc(terms)
            unicode_terms = to_unicode(terms)
            labeled_message = {'score': score,
                               'id': index,
                               'terms': unicode_terms,
                               'features': features.vectorize(unicode_terms,
                                                              text)}
            labeled_messages.append(labeled_message)

            term_vocabulary.insert_terms(
                    labeled_message['features'].iterkeys())
            # next row
            # row = tweets.next_row(cursor, score, 'test')

    # Create vectors
    problem = []
    for labeled_message in labeled_messages:
        vector = vectorizer(labeled_message, term_vocabulary, doc_vocabulary)
        if (collection_type == 'train'):
            problem.append([labeled_message['score'], vector])
        elif (collection_type == 'test'):
            problem.append([labeled_message['id'], vector])
        else:
            raise ValueError(
                    'Unexpected collection_type={}'.format(collection_type))

    return problem


def to_unicode(terms):
    """
    Converts list of 'str' into list of 'unicode' strings
    """
    unicode_terms = []
    for term in terms:
        if (isinstance(term, str)):
            unicode_terms.append(unicode(term, 'utf-8'))
        else:
            unicode_terms.append(term)

    return unicode_terms
