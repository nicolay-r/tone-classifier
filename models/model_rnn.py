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
    with io.open(configs.TWITTER_MESSAGE_PARSER_CONFIG, "r") as f:
        message_settings = json.load(f, encoding='utf-8')

    with io.open(configs.FEATURES_CONFIG, 'r') as f:
        features_settings = json.load(f, encoding='utf-8')

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

    X, y, embedding_size = get_problem(problem, 'train')

    logging.info("embedding_size: {}".format(embedding_size))
    logging.info("Create RNN network model ...")

    # TODO:
    # Network setting should be presented in json configuration (apperently
    # rnn.conf)
    hidden_layer_size = 400
    model = NETWORKS[network_type](hidden_layer_size, embedding_size)
    paths = get_model_paths(task_type, network_type, SETTING_NAME)

    logging.info("Pack embedding settings: {} ...".format(
        paths['embedding_output']))
    save_embeddings(paths['embedding_output'])

    utils.train_network(model, X, y, paths['model_output'])


def get_problem(problem, problem_type):
    """
        It parses problem and providing X, embedding size, and y (Optinal) as a
        result. Presence of lattest parameter depends on the 'problem_type'
        argument. Thus, y will be returned in case of 'train' problem type,
        and will be ommitted in case of 'task' problem type.

        problem_type : str
            'train' or 'test'
    """
    if problem_type not in ['train', 'test']:
        logging.error("problem_type '{}' doesn't support".format(problem_type))

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
        if (problem_type == 'train'):
            y[index] = sentence[0]
        for key, value in sentence[vector_index].iteritems():
            X[index][key-1] = value

    return (X, y, embedding_size) if problem_type == 'train' else \
           (X, embedding_size)


def get_model_paths(task_type, network_type, setting_name):
    name = "{}_{}_{}".format(setting_name, task_type, network_type)
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
