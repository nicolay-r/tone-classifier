#!/usr/bin/python

import sys
from inspect import getsourcefile
from os.path import abspath, dirname
curr_dir = dirname(abspath(getsourcefile(lambda:0)))
sys.path.insert(0, curr_dir + '/../_aux')

from math import log

def to_unicode(terms):
    unicode_terms = []
    for term in terms:
        if (isinstance(term, str)):
            unicode_terms.append(unicode(term, 'utf-8'))
        else:
            unicode_terms.append(term)

    return unicode_terms

def to_unicode_term(term):
    if (isinstance(term, str)):
        return term.append(unicode(term, 'utf-8'))
    else:
        return term

def train_vector(tone, doc_voc, term_voc, ext_voc, terms, features):
    "build vector"
    vector = [tone, {}]
    for feature_name in features.keys():
        index = term_voc.get_term_index(feature_name)
        vector[1][index] = features[feature_name]

    unicode_terms = to_unicode(terms)
    for term in unicode_terms:
        index = term_voc.get_term_index(term)
        vector[1][index] = tf(term, unicode_terms) * idf(term,
            ext_voc, doc_voc, term_voc)
    return vector

def tf(term, doc_terms):
    "calculate tf measure for a doc"
    return doc_terms.count(term)*1.0/len(doc_terms)

def idf(term, ext_voc, doc_voc, term_voc):
    'calculate idf measure for tvoc'
    upper_term = to_unicode_term(term).upper()
    # concatenate dictionaries
    return log( (ext_voc.get_term_in_docs_count(upper_term) +
        doc_voc.get_term_in_docs_count(term)) * 1.0 /
        (ext_voc.get_docs_count() + doc_voc.get_docs_count()) )
