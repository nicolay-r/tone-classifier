#!/usr/bin/python
# -*- coding: utf-8 -*-

# global
import sys
import math
import psycopg2

# core
import core.utils

# this
import utils
import prob


def vectorizer(tone, term_voc, doc_voc, terms, features):
    """
    Vector builder

    Arguments:
    ---------
        tone -- sentiment score of terms list
        term_voc -- vocabulary of terms
        doc_voc -- vocabulary of documents

    """
    vector = [tone, {}]
    for feature_name in features.keys():
        index = term_voc.get_term_index(feature_name)
        vector[1][index] = features[feature_name]

    for term in terms:
        index = term_voc.get_term_index(term)
        vector[1][index] = tf(term, terms)*idf(term, term_voc, doc_voc)

    return vector


def tf(term, doc_terms):
    """
    Calculate tf measure for a document
    """
    return doc_terms.count(term)*1.0/len(doc_terms)


def idf(term, term_voc, doc_voc):
    """
    Calculate idf measure for vocabulary
    """
    return math.log(doc_voc.get_docs_count()*1.0 /
                    doc_voc.get_term_in_docs_count(term))


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

# Train problem
train_problem = utils.create_problem(connection,
                                     config['task_type'],
                                     config['train_table'],
                                     vectorizer,
                                     features_configpath,
                                     config['vocabulary_configpath'],
                                     message_configpath)

prob.save(train_problem, config['train_output'])

# Test problem
test_problem = utils.create_problem(connection,
                                    config['task_type'],
                                    config['test_table'],
                                    vectorizer,
                                    features_configpath,
                                    config['vocabulary_configpath'],
                                    message_configpath)

prob.save(test_problem, config['test_output'])
