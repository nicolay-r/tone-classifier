#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import walk
from os.path import join
import io
import sys
import json
import logging
import zipfile
import numpy as np

import utils
import configs
from core.features import Features
from core.DocVocabulary import DocVocabulary
from core.TermVocabulary import TermVocabulary
from core.msg import TwitterMessageParser

from model_w2v import vectorizer as w2v_vectorizer
from model_features_only import vectorizer as features_only

# RNN
from networks.theano.rnn import RNNTheano

# GRU
from networks.theano.gru import GRU2LTheano

# LSTM
from networks.theano.lstm.lstm_1l_vanilla import LSTM1lTheano
from networks.theano.lstm.lstm_1l_rmsprop import LSTM1lRmspropTheano
from networks.theano.lstm.lstm_1l_adam import LSTM1lAdamTheano
from networks.theano.lstm.lstm_2l_vanilla import LSTM2lTheano


def train_network(vectorizer, network_type, task_type, train_table,
                  setting_name):
    """
    Main function of vectorization for neural network

    network_type : str
        type of the network, which should be presented in NETWORKS dictionary.
    task_type : str
        TTK_TASK or BANK_TASK
    train_table : str
        Train table filepath

    returns : None
    """
    message_settings, features_settings = load_embeddings()

    features = Features(
            TwitterMessageParser(message_settings, task_type),
            features_settings)

    term_vocabulary = TermVocabulary()
    doc_vocabulary = DocVocabulary()

    problem = utils.create_problem(task_type,
                                   'train',
                                   train_table,
                                   vectorizer,
                                   features,
                                   term_vocabulary,
                                   doc_vocabulary,
                                   message_settings)

    assert(len(problem) > 0)

    X, y = get_problem(problem, get_results=True)

    embedding_size = X.shape[1]
    logging.info("embedding_size: {}".format(embedding_size))
    logging.info("Create RNN network model ...")

    # TODO:
    # Network setting should be presented in json configuration (apperently
    # rnn.conf)
    hidden_size = 400
    model = get_network(network_type, embedding_size, hidden_size)
    paths = get_model_paths(task_type, network_type, setting_name)

    logging.info("Pack embedding settings: {} ...".format(
        paths['embedding_output']))
    save_embeddings(paths['embedding_output'])

    logging.info("Save term vocabulary: {} ...".format(
        paths['term_vocabulary']))
    term_vocabulary.save(paths['term_vocabulary'])

    utils.train_network(model, X, y, paths['model_output'])


def get_problem(problem, get_results=True):
    """
    It parses problem and providing X, embedding size, and y (Optinal) as a
    result. Presence of lattest parameter depends on the 'get_results'
    argument. Thus, y will be returned in case of 'train' problem type,
    where we need a results, and will be ommitted in case of 'test' problem
    type, where we should predict results.

    get_results : bool
    """
    vector_index = 1
    embedding_size = len(problem[0][vector_index])
    for sentence in problem:
        if (len(sentence[vector_index]) != embedding_size):
            logging.error(
                'embedded vectors has different sizes.'
                'expected size of each element is {}'.format(embedding_size))

    X = np.ndarray((len(problem), embedding_size))

    y = np.ndarray(len(problem), dtype=np.int32)
    for index, sentence in enumerate(problem):
        if (get_results):
            # shift classes from {-1, 0, 1} -> {0, 1, 2}, that is why
            # incrementing value by 1
            y[index] = sentence[0] + 1
        for key, value in sentence[vector_index].iteritems():
            X[index][key-1] = value

    return (X, y) if get_results else X


def get_model_paths(task_type, network_type, setting_name):
    name = "{}_{}_{}".format(setting_name, task_type, network_type)
    e_out = join(configs.NETWORK_MODELS_ROOT, "{}_embedding.zip".format(name))
    m_out = join(configs.NETWORK_MODELS_ROOT, "{}_model.pkl".format(name))
    t_out = join(configs.NETWORK_MODELS_ROOT, "{}.tvoc".format(name))
    return {"model_output": m_out,
            "embedding_output": e_out,
            "term_vocabulary": t_out}


def save_embeddings(output):
    """
    Save embedding configurations.

    termVocabulary : TermVocabulary
    docVocabulary : DocVocabulary
    output : str
        represents a path to the .zip archive which stores all necessary data
        to vectorize test collection and test saved network 'model' in further.
    """
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
        for dirnames, folders, files in walk(configs.EMBEDINGS_ROOT):
            for f in files:
                zf.write(join(configs.EMBEDINGS_ROOT, f), arcname=f)


def load_embeddings():
    with io.open(configs.TWITTER_MESSAGE_PARSER_CONFIG, "r") as f:
        message_settings = json.load(f, encoding='utf-8')

    with io.open(configs.FEATURES_CONFIG, 'r') as f:
        features_settings = json.load(f, encoding='utf-8')

    return message_settings, features_settings


def get_vectorizer(vectorizer_type):
    if (vectorizer_type == 'w2v'):
        return w2v_vectorizer
    if (vectorizer_type == 'features_only'):
        return features_only
    raise "type {} doesn't supported".format(vectorizer_type)


def get_network(network_type, input_size, hidden_size):
    """
    network_type : str
    input_size : int
    hidden_size : int
    returns : networks.theano.*
        Initial model, based on the function arguments
    """
    if (network_type == 'rnn'):
        return RNNTheano(hidden_size, input_size)
    if (network_type == 'gru-2l'):
        return GRU2LTheano(input_size)
    if (network_type == 'lstm-1l'):
        return LSTM1lTheano(input_size)
    if (network_type == 'lstm-1l-rmsprop'):
        return LSTM1lRmspropTheano(input_size)
    if (network_type == 'lstm-1l-adam'):
        return LSTM1lAdamTheano(input_size)
    if (network_type == 'lstm-2l'):
        return LSTM2lTheano(input_size)
    raise "type {} doesn't supported".format(network_type)


if __name__ == "__main__":

    utils.init_logger()
    config = {'setting_name': sys.argv[1],
              'vectorizer_type': sys.argv[2],
              'network_type': sys.argv[3],
              'task_type': sys.argv[4],
              'train_table': sys.argv[5]}

    train_network(
            get_vectorizer(config['vectorizer_type']),
            config['network_type'],
            config['task_type'],
            config['train_table'],
            config['setting_name'])
