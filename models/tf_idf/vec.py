from math import log

import sys
from inspect import getsourcefile
from os.path import abspath, dirname
sys.path.insert(0, dirname(abspath(getsourcefile(lambda:0))) + '/../aux')
from msg import Message
from vocs import TermVocabulary

def train_vector(tone, term_voc, doc_voc, terms, features):
    "build vector"
    vector = [tone, {}]
    for feature_name in features.keys():
        index = term_voc.get_term_index(feature_name)
        vector[1][index] = features[feature_name]
    for term in terms:
        index = term_voc.get_term_index(term)
        vector[1][index] = tf(term, terms) * idf(term, term_voc, doc_voc)
    return vector

def tf(term, doc_terms):
    "calculate tf measure for a doc"
    return doc_terms.count(term)*1.0/len(doc_terms)

def idf(term, term_voc, doc_voc):
    'calculate idf measure for voc'
    return log(doc_voc.get_docs_count()*1.0/
        doc_voc.get_term_in_docs_count(term))
