#!/usr/bin/python
# -*- coding: utf-8 -*-
# global
import sys
import logging
import numpy as np

# local
import utils
import utils_keras as uk
import model_w2v
import eval as ev

# networks
from networks.keras import lstm_1l


def vectorizer(labeled_message, term_voc, doc_voc):
    """
    Vector builder

    Arguments:
    ---------
        labeled_message -- dictionary with the following fields:
                           {score, id, terms, features}
        term_voc -- vocabulary of terms
        doc_voc -- vocabulary of documents

    Returns
    ------
        vector: np.array
    """
    # features = labeled_message['features']
    # vector = model_features_only.feature_vectorizer(features, term_voc)

    terms = labeled_message['terms']
    vector = np.zeros(MAX_SEQUENCE_LENGTH)

    for i in range(min(len(terms), MAX_SEQUENCE_LENGTH)):
        term = terms[i]
        if (term in W2V_MODEL.vocab):
            vector[i] = W2V_MODEL.vocab.get(term).index

    return vector


W2V_MODEL = model_w2v.W2V_MODELS[0]

if __name__ == "__main__":
    utils.init_logger()
    config = {'task_type': sys.argv[1],
              'test_table': sys.argv[2],
              'train_table': sys.argv[3],
              'etalon_table': sys.argv[4]}

    MAX_SEQUENCE_LENGTH = 40
    EPOCHS = 3
    BATCH_SIZE = 8

    # prepare
    train_problem, test_problem = uk.prepare_problem(
        vectorizer,
        config['task_type'],
        config['train_table'],
        config['test_table'],
        config['etalon_table'])

    x_train, y_train = uk.process_problem(train_problem, 'train')
    x_test, ids = uk.process_problem(test_problem, 'test')

    # create model
    model = lstm_1l.build(W2V_MODEL, MAX_SEQUENCE_LENGTH)

    # fit
    model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE)

    # predict
    logging.info("Predicting results ...")
    y_test = model.predict(x_test, batch_size=BATCH_SIZE)

    # check
    result_table = config['test_table'] + '.result.csv'
    uk.prepare_result_table(config['test_table'], result_table)
    uk.fill_test_results(y_test, config['task_type'], result_table)

    logging.info("Check results ...")
    result = ev.check(
            config['task_type'],
            result_table,
            config['etalon_table'])
    ev.show(result)
