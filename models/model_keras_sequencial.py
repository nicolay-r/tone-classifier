#!/usr/bin/python
# -*- coding: utf-8 -*-
from keras.models import Model
from keras.layers import Embedding, Input, Dense
from keras.layers.recurrent import LSTM

import numpy as np

import utils

import model_features_only
import model_w2v


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
        vector -- {index1: value1, ... , indexN: valueN}
    """
    features = labeled_message['features']
    vector = model_features_only.feature_vectorizer(features, term_voc)

    terms = labeled_message['terms']

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


MAX_SEQUENCE_LENGTH = 40
EPOCHS = 20
BATCH_SIZE = 8

# case for only 1 model
# without features
w2v_model = model_w2v.W2V_MODELS[0]

input_layer = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
embedding_layer = Embedding(len(w2v_model.vocab),
                            w2v_model.vector_size,
                            weights=[create_embedding_matrix(w2v_model)],
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=False)
lstm_layer = LSTM(200, activation='tanh', recurrent_activation='hard_sigmoid')
dense_layer = Dense(3, activation='softmax')


es = embedding_layer(input_layer)
x = lstm_layer(es)
preds = dense_layer(x)

model = Model(es, preds)

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

if __name__ == "__main__":
    x_train = []
    y_train = []
    utils.vectorization_core(vectorizer, init_term_vocabulary=False)
    model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE)
