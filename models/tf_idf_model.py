#!/usr/bin/python
# -*- coding: utf-8 -*-

# global
import math

# this
import utils


def vectorizer(tone, term_voc, doc_voc, terms, features):
    """
    Vector builder

    Arguments:
    ---------
        tone -- sentiment score of terms list
        term_voc -- vocabulary of terms
        doc_voc -- vocabulary of documents

    Returns
    ------
        vector -- [tone, {index: value, ... }]
    """
    vector = [tone, {}]
    for feature_name in features.keys():
        index = term_voc.get_term_index(feature_name)
        vector[1][index] = features[feature_name]

    for term in terms:
        index = term_voc.get_term_index(term)
        vector[1][index] = tf(term, terms) * idf(term, term_voc, doc_voc)

    return vector


def tf(term, doc_terms):
    """
    Calculate tf measure for a document
    """
    return doc_terms.count(term)*1.0/len(doc_terms)


def idf(term, term_voc, doc_voc):
    """
    Calculate idf measure for vocabulary
    """
    return math.log(doc_voc.get_docs_count()*1.0 /
                    doc_voc.get_term_in_docs_count(term))

utils.vectorization_core(vectorizer)
