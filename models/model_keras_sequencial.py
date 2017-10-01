#!/usr/bin/python
# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Embedding, Input, Dense
from keras.layers.recurrent import LSTM

import sys
import numpy as np
import utils
import model_w2v
from model_rnn import load_embeddings

from core.features import Features
from core.DocVocabulary import DocVocabulary
from core.TermVocabulary import TermVocabulary
from core.msg import TwitterMessageParser

MAX_SEQUENCE_LENGTH = 40
EPOCHS = 20
BATCH_SIZE = 8


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


def train_network(vectorizer, task_type, train_table, test_table,
                  etalon_table):
    """
    Main function of vectorization for neural network
    """
    message_settings, features_settings = load_embeddings()

    features = Features(
            TwitterMessageParser(message_settings, task_type),
            features_settings)

    term_vocabulary = TermVocabulary()
    doc_vocabulary = DocVocabulary()

    train_problem = utils.create_problem(task_type, 'train', train_table,
                                         vectorizer, features, term_vocabulary,
                                         doc_vocabulary, message_settings)

    # test_problem = utils.create_problem(task_type, 'test', test_table,
    #                                     vectorizer, features, term_vocabulary,
    #                                     doc_vocabulary, message_settings)

    process_problem(train_problem, 'train')


def process_problem(problem, collection_type):
    """
    problem: list [{label, vector}, ... ]
        List of vectorized messages. Each message presented as list where
        first element is a 'score' or 'id' (depending on the 'train' or 'score'
        dataset accordingly) and the secont (latter) is a vector -- embedded
        sentence (obtained by vectorizer)
    collection_type: str
        'test' or 'train'
    """
    for message in problem:
        if (collection_type == 'train'):
            y = np.zeros(3)
            y[message[0] + 1] = 1
            Y_TRAIN.append(y)
            X_TRAIN.append(message[1])


def build_keras_model(w2v_model):
    """
    w2v_model : gensim.models.word2vec.Word2Vec
        word2vec model

    returns : keras.models.Model
        compiled model
    """
    # TODO: support multiple w2v models
    # case for only 1 model
    # without features
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

    model = build_keras_model(W2V_MODEL)

    X_TRAIN = []
    Y_TRAIN = []

    train_network(
            vectorizer,
            config['task_type'],
            config['train_table'],
            config['test_table'],
            config['etalon_table'])

    model.fit(np.vstack(X_TRAIN),
              np.vstack(Y_TRAIN),
              epochs=EPOCHS, batch_size=BATCH_SIZE)

    # model.predict(X_TEST, batch_size=BATCH_SIZE)
