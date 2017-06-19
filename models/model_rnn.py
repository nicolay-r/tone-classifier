#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import walk
from os.path import join
import sys
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

from networks.theano.rnn import RNNTheano


def train_network(vectorizer, network_type, task_type, train_table):
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
    message_configpath = configs.TWITTER_MESSAGE_PARSER_CONFIG
    features_configpath = configs.FEATURES_CONFIG

    features = Features(
            TwitterMessageParser(message_configpath, task_type),
            features_configpath)

    term_vocabulary = TermVocabulary()
    doc_vocabulary = DocVocabulary()

    problem = utils.create_problem(task_type,
                                   'train',
                                   train_table,
                                   vectorizer,
                                   features,
                                   term_vocabulary,
                                   doc_vocabulary,
                                   features_configpath,
                                   message_configpath)

    assert(len(problem) > 0)

    vector_index = 1
    embedding_size = len(problem[0][vector_index])
    for sentence in problem:
        if (len(sentence[vector_index]) != embedding_size):
            logging.error(
                'embedded vectors has different sizes.'
                'expected size of each element is {}'.format(embedding_size))

    logging.info("embedding_size: {}".format(embedding_size))

    X = np.ndarray((len(problem), embedding_size))
    y = np.ndarray(len(problem), dtype=np.int32)
    for index, sentence in enumerate(problem):
        y[index] = sentence[0]
        for key, value in sentence[vector_index].iteritems():
            X[index][key-1] = value

    logging.info("Create RNN network model ...")

    # TODO:
    # Network setting should be presented in json configuration (apperently
    # rnn.conf)
    hidden_layer_size = 400
    model = NETWORKS[network_type](hidden_layer_size, embedding_size)
    paths = get_model_paths(task_type, network_type)

    logging.info("Pack embedding settings: {} ...".format(
        paths['embedding_output']))
    save_embeddings(paths['embedding_output'])

    utils.train_network(model, X, y, paths['model_output'])


def test_network(network_type, task_type, test_table):
    # TODO:
    # apply network
    pass


def get_model_paths(task_type, network_type):
    name = "{}_{}_{}".format(SETTING_NAME, task_type, network_type)
    e_out = join(configs.NETWORK_MODELS_ROOT, "{}_embedding.zip".format(name))
    m_out = join(configs.NETWORK_MODELS_ROOT, "{}_model.pkl".format(name))
    return {"model_output": m_out, "embedding_output": e_out}


def save_embeddings(output):
    """
    Save embedding configurations.
    output : str
        represents a path to the .zip archive which stores all necessary data
        to vectorize test collection and test saved network 'model' in further.
    """
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
        for dirnames, folders, files in walk(configs.EMBEDINGS_ROOT):
            for f in files:
                zf.write(join(configs.EMBEDINGS_ROOT, f), arcname=f)


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
              'train_table': sys.argv[5]}

    SETTING_NAME = config['setting_name']

    train_network(
            VECTORIZERS[config['vectorizer_type']],
            config['network_type'],
            config['task_type'],
            config['train_table'])
