from math import log, exp

import sys
from inspect import getsourcefile
from os.path import abspath, dirname
sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) + '/../_aux')
from msg import Message
from vocs import TermVocabulary

def to_unicode(terms):
    unicode_terms = []
    for term in terms:
        if (isinstance(term, str)):
            unicode_terms.append(unicode(term, 'utf-8'))
        else:
            unicode_terms.append(term)

    return unicode_terms

def train_vector(tone, term_voc, doc_voc, terms, features):
    "build vector"
    vector = [tone, {}]
    for feature_name in features.keys():
        index = term_voc.get_term_index(feature_name)
        vector[1][index] = features[feature_name]

    unicode_terms = to_unicode(terms)
    for term in unicode_terms:
        index = term_voc.get_term_index(term)
        vector[1][index] = bag_of_words(term, unicode_terms)
    return vector

def bag_of_words(term, doc_terms):
    "calculate bag_of_words measure for a doc"
    return doc_terms.count(term)*1.0

def norm(count, k):
    if (count >= 0):
        return 1.0 - exp(-abs(count/k))
    else:
        return - (1.0 - exp(-abs(count/k)))
