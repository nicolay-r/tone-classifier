#!/usr/bin/python

from msg import Message

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
    for index in tvoc.getIndexes(terms):
        vector[1][index] = 1
    return vector


