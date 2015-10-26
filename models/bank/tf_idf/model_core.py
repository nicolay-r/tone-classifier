#!/usr/bin/python

from msg import Message
from tvoc import TermVocabulary
from math import log

def process_text(mystem, text, tvoc):
    "process a text by Mystem analyzer"
    message = Message(text, mystem)
    message.normalize()

    terms = message.getLemmas()
    terms += message.getIgnored()

    tvoc.addTerms(terms)
    return terms

def train_vector(tone, tvoc, terms):
    "build vector"
    vector = [tone, {}]
    for term in terms:
        index = tvoc.getTermIndex(term)
        vector[1][index] = tf(term, terms) * idf(term, tvoc)
    return vector

def tf(term, doc_terms):
    "calculate tf measure for a doc"
    in_doc = 0.0
    for d_term in doc_terms:
        if (term == d_term):
            in_doc += 1

    return in_doc/len(doc_terms)

def idf(term, tvoc):
    'calculate idf measure for tvoc'
    return log(float(tvoc.getDocsCount())/tvoc.getTermInDocsCount(term))
