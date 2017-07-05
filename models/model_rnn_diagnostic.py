#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
import sys
import json
import logging

import utils
import configs
from core.features import Features
from core.DocVocabulary import DocVocabulary
from core.TermVocabulary import TermVocabulary
from core.msg import TwitterMessageParser

from model_rnn import get_model_paths, get_problem, save_embeddings, \
                      get_vectorizer, get_network
from model_rnn_test import test_network


def train_network(vectorizer, network_type, task_type, train_table,
                  test_table, etalon_table, setting_name):
    """
    Main function of vectorization for neural network
    """
    with io.open(configs.TWITTER_MESSAGE_PARSER_CONFIG, "r") as f:
        message_settings = json.load(f, encoding='utf-8')

    with io.open(configs.FEATURES_CONFIG, 'r') as f:
        features_settings = json.load(f, encoding='utf-8')

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
    X_test, embedding_size = get_problem(test_problem, get_results=False)
    X_train, Y, _ = get_problem(train_problem, get_results=True)

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

    # TODO: combine test_network with eval script
    test_callback = lambda: test_network(paths, vectorizer, network_type,
                                         task_type, test_table,
                                         paths['model_output'])

    utils.train_network(model, X_train, Y, paths['model_output'],
                        callback=test_callback)


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
