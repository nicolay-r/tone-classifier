#!/usr/bin/python
# -*- coding: utf-8 -*-

# global
import math

# this
import utils
import model_features_only


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
    vector = model_features_only.feature_vectorizer(features, term_voc)

    terms = labeled_message['terms']
    for term in terms:
        index = term_voc.get_term_index(term)
        vector[index] = tf(term, terms) * idf(term, doc_voc, '1') - \
            tf(term, terms) * idf(term, doc_voc,  '-1')

    return vector


def tf(term, terms):
    """
    Boolean tf
    """
    return 1 if terms.count(term) > 0 else 0


def idf(term, doc_voc, sentiment):
    """
    sentiment idf measure
    """
    return math.log(doc_voc.get_docs_count(sentiment)*1.0 + 0.5 /
                    (doc_voc.get_term_in_docs_count(term, sentiment) + 0.5))


if __name__ == "__main__":
    utils.vectorization_core(vectorizer, merge_doc_vocabularies=True)
