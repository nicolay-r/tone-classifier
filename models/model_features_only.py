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

    return utils.feature_vectorizer(labeled_message['features'], term_voc)


utils.vectorization_core(vectorizer, init_term_vocabulary=False)
