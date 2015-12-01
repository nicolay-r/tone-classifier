from math import log

import sys
from inspect import getsourcefile
from os.path import abspath, dirname
sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) + '/../aux')
from msg import Message
from tvoc import TermVocabulary

def train_vector(tone, tvoc, terms, features):
    "build vector"
    vector = [tone, {}]
    for feature_name in features.keys():
        index = tvoc.getTermIndex(feature_name)
        vector[1][index] = features[feature_name]
    for term in terms:
        index = tvoc.getTermIndex(term)
        vector[1][index] = tf(term, terms) * idf(term, tvoc)
    return vector

def tf(term, doc_terms):
    "calculate tf measure for a doc"
    return doc_terms.count(term)*1.0/len(doc_terms)

def idf(term, tvoc):
    'calculate idf measure for tvoc'
    return log(tvoc.getDocsCount()*1.0/tvoc.getTermInDocsCount(term))
