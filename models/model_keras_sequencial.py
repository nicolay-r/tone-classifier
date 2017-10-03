#!/usr/bin/python
# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Embedding, Dense
from keras.layers.recurrent import LSTM

import sys
import utils_keras as uk
import numpy as np
import eval as ev
import model_w2v
import utils


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


def create_embedding_matrix(w2v_model):
    """
    creates matrix (words_count, embedding_size) based on 'w2v_model'

    w2v_model: gensim.models.word2vec.Word2Vec
        word2vec model

    returns: np.ndarray
        shape (words_count, embedding_size)
    """
    words_count = len(w2v_model.vocab)
    matrix = np.zeros((words_count, w2v_model.vector_size))

    for word, info in w2v_model.vocab.items():
        index = info.index
        matrix[index] = w2v_model.syn0[index]

    return matrix


def build_keras_model(w2v_model):
    """
    w2v_model : gensim.models.word2vec.Word2Vec
        word2vec model

    returns : keras.models.Model
        compiled model
    """
    # TODO: support multiple w2v models
    # input_layer = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
    embedding_layer = Embedding(len(w2v_model.vocab),
                                w2v_model.vector_size,
                                weights=[create_embedding_matrix(w2v_model)],
                                input_length=MAX_SEQUENCE_LENGTH,
                                trainable=False)
    lstm_layer = LSTM(200)
    dense_layer = Dense(3, activation='softmax')

    model = Sequential()
    model.add(embedding_layer)
    model.add(lstm_layer)
    model.add(dense_layer)

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    print model.summary()

    return model


W2V_MODEL = model_w2v.W2V_MODELS[0]

if __name__ == "__main__":
    utils.init_logger()
    config = {'task_type': sys.argv[1],
              'test_table': sys.argv[2],
              'train_table': sys.argv[3],
              'etalon_table': sys.argv[4]}

    MAX_SEQUENCE_LENGTH = 40
    EPOCHS = 1
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
    model = build_keras_model(W2V_MODEL)

    # fit
    model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE)

    # predict
    y_test = model.predict(x_test, batch_size=BATCH_SIZE)

    # check
    result_table = config['test_table'] + '.result.csv'
    uk.prepare_result_table(config['test_table'], result_table)
    result = ev.check(config['task_type'], result_table)
    ev.show(result)
