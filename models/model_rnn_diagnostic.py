#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import logging

import utils
from core.features import Features
from core.DocVocabulary import DocVocabulary
from core.TermVocabulary import TermVocabulary
from core.msg import TwitterMessageParser

from eval import check
from model_rnn import get_model_paths, get_problem, save_embeddings, \
                      get_vectorizer, get_network, load_embeddings
from model_rnn_test import predict, prepare_result_table


def train_network(vectorizer, network_type, task_type, train_table,
                  test_table, etalon_table, setting_name):
    """
    Main function of vectorization for neural network
    """
    message_settings, features_settings = load_embeddings()

    features = Features(
            TwitterMessageParser(message_settings, task_type),
            features_settings)

    term_vocabulary = TermVocabulary()
    doc_vocabulary = DocVocabulary()

    # Get problems
    train_problem = utils.create_problem(task_type, 'train', train_table,
                                         vectorizer, features, term_vocabulary,
                                         doc_vocabulary, message_settings)

    test_problem = utils.create_problem(task_type, 'test', test_table,
                                        vectorizer, features, term_vocabulary,
                                        doc_vocabulary, message_settings)

    assert(len(train_problem) > 0 and len(test_problem) > 0)

    # Transform into appliable for neural network collections
    X_test = get_problem(test_problem, get_results=False)
    X_train, Y = get_problem(train_problem, get_results=True)

    import ipdb; ipdb.set_trace() # BREAKPOINT

    assert(X_test.shape[1] == X_train.shape[1])

    embedding_size = X_test.shape[1]
    logging.info("embedding_size: {}".format(embedding_size))
    logging.info("Create {} network model ...".format(network_type))

    # TODO:
    # Network setting should be presented in json configuration (apperently
    # rnn.conf)
    hidden_layer_size = 400
    model = get_network(network_type)(hidden_layer_size, embedding_size)
    paths = get_model_paths(task_type, network_type, setting_name)

    logging.info("Pack embedding settings: {} ...".format(
        paths['embedding_output']))
    save_embeddings(paths['embedding_output'])

    def callback(model, X_test, task_type, result_table, etalon_table):
        predict(model, X_test, task_type, result_table)
        check(task_type, result_table, etalon_table)

    model_output = paths['model_output']

    output_table = test_table + 'result.csv'
    prepare_result_table(test_table, output_table)
    utils.train_network(model, X_train, Y, model_output,
                        lambda: callback(model, X_test, task_type,
                                         output_table, etalon_table))


if __name__ == "__main__":

    utils.init_logger()
    config = {'setting_name': sys.argv[1],
              'vectorizer_type': sys.argv[2],
              'network_type': sys.argv[3],
              'task_type': sys.argv[4],
              'test_table': sys.argv[5],
              'train_table': sys.argv[6],
              'etalon_table': sys.argv[7]}

    train_network(
            get_vectorizer(config['vectorizer_type']),
            config['network_type'],
            config['task_type'],
            config['train_table'],
            config['test_table'],
            config['etalon_table'],
            config['setting_name'])
