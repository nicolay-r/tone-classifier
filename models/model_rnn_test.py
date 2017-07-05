#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import logging
import zipfile
import pandas as pd
import numpy as np

import utils
import configs
from core.features import Features
from core.DocVocabulary import DocVocabulary
from core.TermVocabulary import TermVocabulary
from core.msg import TwitterMessageParser

from model_rnn import get_model_paths, get_problem, get_network, get_vectorizer


def predict(model, X, task_type, result_table):
    """
        model : networks.*
            neural network model
        X : np.ndarray
            represents test dataset
        task_type : str
        result_table : str
            output table which should be filled with the predicted result
    """
    logging.info("Predicting ...")
    y = model.forward_propagation(X)[0]

    # TODO: remove duplicated code at predict.py
    logging.info("Filling answers in {} ...".format(result_table))
    df = pd.read_csv(result_table, sep=',')
    sentiment_columns = utils.get_score_columns(task_type)
    for msg_index, row_index in enumerate(df.index):
        label = np.argmax(y[msg_index]) - 1
        for column in sentiment_columns:
            if not df[column].isnull()[row_index]:
                df.set_value(row_index, column, label)

    # Rewriting table with the filled results
    df.to_csv(result_table, sep=',')


def load_model(paths):
    logging.info("Reading: {} ...".format(paths['embedding_output']))

    with zipfile.ZipFile(paths['embedding_output'], "r") as zf:
        logging.info("Reading: {} ...".format(configs.FEATURES_FILENAME))
        features_settings = json.loads(
            zf.read(configs.FEATURES_FILENAME), encoding='utf-8')

        logging.info("Reading: {} ...".format(
            configs.TWITTER_MESSAGE_PARSER_FILENAME))
        message_settings = json.loads(
            zf.read(configs.TWITTER_MESSAGE_PARSER_FILENAME), encoding='utf-8')

    logging.info("Reading: {} ...".format(paths['model_output']))
    model = get_network(network_type).load(paths['model_output'])

    term_vocabulary = TermVocabulary.load(paths['term_vocabulary'])

    return (model,
            features_settings,
            message_settings,
            term_vocabulary)


def prepare_result_table(test_table, result_table):
    logging.info('Create a file for classifier results: {}'.format(
            result_table))
    result_df = pd.read_csv(test_table, sep=',')
    result_df.to_csv(result_table, sep=',')


if __name__ == "__main__":

    utils.init_logger()
    config = {'setting_name': sys.argv[1],
              'vectorizer_type': sys.argv[2],
              'network_type': sys.argv[3],
              'task_type': sys.argv[4],
              'test_table': sys.argv[5],
              'model_out': sys.argv[6]}

    task_type = config['task_type']
    network_type = config['network_type']
    paths = get_model_paths(task_type, network_type, config['setting_name'])

    # loading model
    model, features_settings, message_settings, term_vocabulary = \
        load_model(paths)

    features = Features(
        TwitterMessageParser(message_settings, task_type),
        features_settings)

    doc_vocabulary = DocVocabulary()

    problem = utils.create_problem(task_type,
                                   'test',
                                   config['test_table'],
                                   get_vectorizer(config['vectorizer_type']),
                                   features,
                                   term_vocabulary,
                                   doc_vocabulary,
                                   message_settings)

    # Preparing X dataset
    X = get_problem(problem, get_results=False)

    # Prepare
    prepare_result_table(config['test_table'], config['model_out'])
    predict(model, X, task_type, config['model_out'])
