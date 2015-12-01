#!/usr/bin/python

import sys
from inspect import getsourcefile
from os.path import abspath, dirname
curr_dir = dirname(abspath(getsourcefile(lambda:0)))
sys.path.insert(0, curr_dir + '/../aux')

from math import log
from msg import Message
from tvoc import TermVocabulary

def train_vector(tone, tvoc, etvoc, terms, features):
    "build vector"
    vector = [tone, {}]
    for feature_name in features.keys():
        index = tvoc.getTermIndex(feature_name)
        vector[1][index] = features[feature_name]
    for term in terms:
        index = tvoc.getTermIndex(term)
        vector[1][index] = tf(term, terms) * idf(term, etvoc, tvoc)
    return vector

def tf(term, doc_terms):
    "calculate tf measure for a doc"
    return doc_terms.count(term)*1.0/len(doc_terms)

def idf(term, etvoc, tvoc):
    'calculate idf measure for tvoc'
    tterm = term.decode('utf-8').upper().encode('utf-8')
    # concatenate dictionaries
    return log( (etvoc.getTermInDocsCount(tterm) +
        tvoc.getTermInDocsCount(term)) * 1.0 /
        (etvoc.getDocsCount() + tvoc.getDocsCount()) )
