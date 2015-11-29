#!/usr/bin/python

from msg import Message
from tvoc import TermVocabulary
from math import log

urls_used = True
ht_used = True
users_used = True
retweet_used = True
print "urls:\t", urls_used
print "ht:\t", ht_used
print "users:\t", users_used
print "rt:\t", retweet_used

def process_text(mystem, text, tvoc):
    "process a text by Mystem analyzer"
    message = Message(text, mystem)
    message.normalize()

    terms = message.getLemmas()

    if (urls_used):
        terms += message.urls
    if (ht_used):
        terms += message.hash_tags
    if (users_used):
        terms += message.users
    if (retweet_used):
        terms += message.retweet

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
