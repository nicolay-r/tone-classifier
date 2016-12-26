#!/usr/bin/python
# -*- coding: utf-8 -*-

# global
from gensim.models.word2vec import Word2Vec
import numpy as np

# this
import utils

WORD2VEC_BINARY_FILEPATH = 'bin/rubtsova_all.bin'

print 'Loading w2v: {}'.format(WORD2VEC_BINARY_FILEPATH)

w2v_model = Word2Vec.load(WORD2VEC_BINARY_FILEPATH)


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
    vector = {}

    terms = labeled_message['terms']
    w2v_vector = np.array([0] * w2v_model.vector_size, dtype=np.float32)
    for term in terms:
        if term in w2v_model:
            w2v_vector = w2v_vector + w2v_model[term]

    term_voc.insert_terms([index2term(index)
                           for index in range(0, w2v_vector.size)])

    for w2v_index, w2v_value in enumerate(w2v_vector):
        term = index2term(index)
        term_voc.insert_term(term)
        index = term_voc.get_term_index(term)
        vector[index] = w2v_value

    features = labeled_message['features']
    for feature_name in features.keys():
        index = term_voc.get_term_index(feature_name)
        vector[index] = features[feature_name]

    return vector


def index2term(index):
    return '$W2V_ITEM_' + str(index)

utils.vectorization_core(vectorizer)
