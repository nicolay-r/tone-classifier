#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import logging
import numpy as np

import utils
import configs
from core import indexer
from core.features import Features
from core.DocVocabulary import DocVocabulary
from core.TermVocabulary import TermVocabulary
from core.msg import TwitterMessageParser

from model_w2v import vectorizer as w2v_vectorizer
from model_features_only import vectorizer as features_only


def vectorization_core_rnn_train(vectorizer, task_type, train_table,
                                 train_output):
    """
    Main function of vectorization for rnn

    task_type : str
        TTK_TASK or BANK_TASK
    train_table : str
        Train table filepath
    train_output : str
        Output filepath

    returns : None
    """
    message_configpath = configs.TWITTER_MESSAGE_PARSER_CONFIG
    features_configpath = configs.FEATURES_CONFIG

    term_vocabulary = indexer.create_term_vocabulary([train_table],
                                                     message_configpath)

    features = Features(
            TwitterMessageParser(message_configpath, task_type),
            features_configpath)

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

    print "embedding_size: {}".format(embedding_size)

    # X = np.ndarray((len(problem), embedding_size))
    # y = np.ndarray(len(problem))
    # for index, sentence in enumerate(problem):
    #     X[index] = sentence[vector_index]

    # print X
    # print y

    print problem


if __name__ == "__main__":

    VECTORIZERS = {
        'w2v': w2v_vectorizer,
        'features_only': features_only}

    utils.init_logger()
    config = {'vectorizer_type': sys.argv[1],
              'task_type': sys.argv[2],
              'train_table': sys.argv[3],
              'train_output': sys.argv[4]}

    vectorization_core_rnn_train(
            VECTORIZERS[config['vectorizer_type']],
            config['task_type'],
            config['train_table'],
            config['train_output'])
