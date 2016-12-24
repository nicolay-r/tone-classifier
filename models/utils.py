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
from core.msg import Message

import tweets
import prob


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
    argc = len(sys.argv)
    if (argc == 1):
        print "%s\n%s\n%s\n%s\n%s\n%s" % (
            "Usage: baseline_bank <database> <train_table> <output>",
            "<task> -- task type",
            "<database> -- database to connect for training data",
            "<train_table> -- table with training data",
            "<test_table> -- table with training data",
            "<vocabulary> -- vocabulary",
            "<train_output> -- file to save tonality vectors",
            "<test_output> -- file to save tonality vectors")
        exit(0)

    config = {'task_type': sys.argv[1],
              'database': sys.argv[2],
              'train_table': sys.argv[3],
              'test_table': sys.argv[4],
              'vocabulary_configpath': sys.argv[5],
              'train_output': sys.argv[6],
              'test_output': sys.argv[7]}
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
                                   config['train_table'],
                                   vectorizer,
                                   term_vocabulary,
                                   features_configpath,
                                   message_configpath)

    prob.save(train_problem, config['train_output'])

    # Test problem
    test_problem = create_problem(connection,
                                  config['task_type'],
                                  config['test_table'],
                                  vectorizer,
                                  term_vocabulary,
                                  features_configpath,
                                  message_configpath)

    prob.save(test_problem, config['test_output'])


def create_problem(connection, task_type, table, vectorizer, term_vocabulary,
                   features_configpath,
                   message_configpath):
    """
    Creates problem (vectors from messages with additional features)

    Arguments:
    ---------
        connection -- pgsql connection
        task_type
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
