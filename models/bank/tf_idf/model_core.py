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

    tvoc.add_doc(terms)
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
    return doc_terms.count(term)*1.0/len(doc_terms)

def idf(term, tvoc):
    'calculate idf measure for tvoc'
    return log(tvoc.getDocsCount()*1.0/tvoc.getTermInDocsCount(term))
