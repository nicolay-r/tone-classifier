#!/usr/bin/python
# -*- coding: utf-8 -*-

# global
import math

# this
import utils
from model_features_only import feature_vectorizer
from model_tf_idf_delta import tf


def vectorizer(labeled_message, term_voc, doc_voc):
    """
    labeled_message: dict
        donary with the following fields: {score, id, terms, features}
    term_voc : core.TermVocabulary
    doc_voc : core.DocVocabulary
    returns : dict
        vector {index1: value1, ... , indexN: valueN}
    """
    features = labeled_message['features']
    vector = feature_vectorizer(features, term_voc)

    terms = labeled_message['terms']
    for term in terms:
        index = term_voc.get_term_index(term)
        vector[index] = tf(term, terms) * idf(term, doc_voc, '1', '-1')

    return vector


def idf(term, doc_voc, s1, s2):
    """
    Delta smoothed prop idf
    doc_voc : core.DocVocabulary
    s1 : str
        first sentiment class
    s2 : str
        second sentiment class
    """
    N1 = doc_voc.get_docs_count(s1)
    N2 = doc_voc.get_docs_count(s2)
    df1 = doc_voc.get_term_in_docs_count(term, s1)
    df2 = doc_voc.get_term_in_docs_count(term, s2)
    return math.log(((N1 - df1)*(df2 + 0.5)) / ((N2 - df2)*(df1 + 0.5)))

if __name__ == "__main__":
    utils.vectorization_core(vectorizer, merge_doc_vocabularies=True)
