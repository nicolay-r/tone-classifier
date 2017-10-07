#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import logging
from os.path import join, exists

import utils
import configs
from core.features import Features
from core.DocVocabulary import DocVocabulary
from core.TermVocabulary import TermVocabulary
from core.msg import TwitterMessageParser

from eval import check
from model_theano import get_model_paths, get_problem, save_embeddings, \
                         get_vectorizer, get_network
from model_theano_test import predict, prepare_result_table
from networks.theano import optimizer


def train_network(vectorizer, network_type, task_type, train_table,
                  test_table, etalon_table, setting_name):
    """
    Main function of vectorization for neural network
    """
    message_settings, features_settings = utils.load_embeddings()

    features = Features(
            TwitterMessageParser(message_settings, task_type),
            features_settings)

    term_vocabulary = TermVocabulary()
    doc_vocabulary = DocVocabulary()

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

    assert(X_test.shape[1] == X_train.shape[1])

    embedding_size = X_test.shape[1]
    logging.info("embedding_size: {}".format(embedding_size))
    logging.info("Create {} network model ...".format(network_type))

    # TODO:
    # Network setting should be presented in json configuration (apperently
    # rnn.conf)
    hidden_layer_size = 400
    model = get_network(network_type, embedding_size, hidden_layer_size)
    paths = get_model_paths(task_type, network_type, setting_name)

    diagnostic_output = join(configs.NETWORK_MODELS_ROOT,
                             "{}.diag".format(setting_name))

    logging.info("Pack embedding settings: {} ...".format(
        paths['embedding_output']))
    save_embeddings(paths['embedding_output'])

    def callback(model, X_test, X_train, Y, task_type, result_table,
                 etalon_table, diagnostic_output):
        """
        Test model
        """
        logging.info("Testing model ...")
        loss = model.calculate_loss(X_train, Y)
        predict(model, X_test, task_type, result_table)
        result = check(task_type, result_table, etalon_table)
        logging.info("Appending results: {} ...".format(diagnostic_output))
        with open(diagnostic_output, 'a') as output:
            output.writelines("{} {} {}\n".format(
                loss, result["F_macro"], result["F_micro"]))

    model_output = paths['model_output']
    if (exists(model_output)):
        logging.info("Loading existed model: {} ...".format(model_output))
        model.load(model_output)

    output_table = test_table + '.result.csv'
    prepare_result_table(test_table, output_table)

    test = lambda: callback(model, X_test, X_train, Y, task_type,
                            output_table, etalon_table, diagnostic_output)

    optimizer.train_network(model, X_train, Y, model_output, callback=test)

    with open(diagnostic_output, 'a') as output:
        output.writelines("-----")


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
