#!/usr/bin/python
# -*- coding: utf-8 -*-

# this
import utils
import model_features_only


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
    for term in terms:
        index = term_voc.get_term_index(term)
        vector[index] = bag_of_words(term, terms)

    return vector


def bag_of_words(term, doc_terms):
    """
    calculate bag_of_words measure for a doc
    """
    return doc_terms.count(term) * 1.0


utils.vectorization_core(vectorizer)
