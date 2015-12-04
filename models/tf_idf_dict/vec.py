#!/usr/bin/python

import sys
from inspect import getsourcefile
from os.path import abspath, dirname
curr_dir = dirname(abspath(getsourcefile(lambda:0)))
sys.path.insert(0, curr_dir + '/../aux')

from math import log

def train_vector(tone, doc_voc, term_voc, ext_voc, terms, features):
    "build vector"
    vector = [tone, {}]
    for feature_name in features.keys():
        index = term_voc.get_term_index(feature_name)
        vector[1][index] = features[feature_name]
    for term in terms:
        index = term_voc.get_term_index(term)
        vector[1][index] = tf(term, terms) * idf(term,
            ext_voc, doc_voc, term_voc)
    return vector

def tf(term, doc_terms):
    "calculate tf measure for a doc"
    return doc_terms.count(term)*1.0/len(doc_terms)

def idf(term, ext_voc, doc_voc, term_voc):
    'calculate idf measure for tvoc'
    tterm = term.decode('utf-8').upper().encode('utf-8')
    # concatenate dictionaries
    return log( (ext_voc.get_term_in_docs_count(tterm) +
        doc_voc.get_term_in_docs_count(term)) * 1.0 /
        (ext_voc.get_docs_count() + doc_voc.get_docs_count()) )
