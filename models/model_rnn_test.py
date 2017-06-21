#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import logging
import zipfile
import pandas as pd

import utils
import configs
from core.features import Features
from core.DocVocabulary import DocVocabulary
from core.TermVocabulary import TermVocabulary
from core.msg import TwitterMessageParser

from model_rnn import get_model_paths, get_X_y_embedding

from model_w2v import vectorizer as w2v_vectorizer
from model_features_only import vectorizer as features_only

from networks.theano.rnn import RNNTheano


def predict():
    # TODO
    pass


def test_network(vectorizer, network_type, task_type, test_table):

    paths = get_model_paths(task_type, network_type, SETTING_NAME)
    logging.info("Reading: {} ...".format(paths['embedding_output']))

    with zipfile.ZipFile(paths['embedding_output'], "r") as zf:
        logging.info("Reading: {} ...".format(configs.FEATURES_FILENAME))
        features_settings = json.loads(
            zf.read(configs.FEATURES_FILENAME), encoding='utf-8')

        logging.info("Reading: {} ...".format(
            configs.TWITTER_MESSAGE_PARSER_FILENAME))
        message_settings = json.loads(
            zf.read(configs.TWITTER_MESSAGE_PARSER_FILENAME), encoding='utf-8')

    features = Features(
        TwitterMessageParser(message_settings, task_type),
        features_settings)

    term_vocabulary = TermVocabulary()
    doc_vocabulary = DocVocabulary()

    problem = utils.create_problem(task_type,
                                   'test',
                                   test_table,
                                   vectorizer,
                                   features,
                                   term_vocabulary,
                                   doc_vocabulary,
                                   message_settings)

    X, y, embedding_size = get_X_y_embedding(problem)

    result_table = '{}_{}_{}.csv.out'.format(SETTING_NAME, task_type,
                                             network_type)
    logging.info('Create a file for classifier results: {}'.format(
            result_table))
    result_df = pd.read_csv(test_table, sep=',')
    result_df.to_csv(result_table, sep=',')
    loggin.info('done')


if __name__ == "__main__":

    VECTORIZERS = {
            'w2v': w2v_vectorizer,
            'features_only': features_only
        }

    NETWORKS = {
            'rnn': RNNTheano,
            'lstm': None,
            'gru': None
        }

    utils.init_logger()
    config = {'setting_name': sys.argv[1],
              'vectorizer_type': sys.argv[2],
              'network_type': sys.argv[3],
              'task_type': sys.argv[4],
              'test_table': sys.argv[5]}

    SETTING_NAME = config['setting_name']

    test_network(
            VECTORIZERS[config['vectorizer_type']],
            config['network_type'],
            config['task_type'],
            config['test_table'])
