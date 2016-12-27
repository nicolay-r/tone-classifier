#!/usr/bin/python
# -*- coding: utf-8 -*-

# this
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
        vector -- {index1: value1, ... , indexN: valueN}
    """

    return feature_vectorizer(labeled_message['features'], term_voc)


def feature_vectorizer(features, term_voc):
    """
    Produces vector of features

    Returns
    ------
        vector -- {index1: value1, ..., indexN: valueN}
    """
    vector = {}

    for feature_name in features.keys():
        index = term_voc.get_term_index(feature_name)
        vector[index] = features[feature_name]

    return vector

utils.vectorization_core(vectorizer)
