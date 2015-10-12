#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from pymystem3 import Mystem
from TermVocabulary import TermVocabulary

argc = len(sys.argv)

# Build Problem Vector
def probVector(tone, indexes):
        v = [tone, {}]
        for index in tvoc.getIndexes(terms):
                v[1][index] = 1
        return v

if (argc == 1):
        print """%s\n%s\n%s\n%s"""%(
                "Usage: baseline_bank <database> <train_table> <output>",
                "<database> -- database to connect for training data",
                "<train_table> -- table with training data for bank",
                "<output> -- file to save tonality vectors")
        exit(0)


m = Mystem(entire_input=False)

# Text Processing
terms = m.lemmatize("Мама мыла")


print " ".join(terms)
tvoc = TermVocabulary()
tvoc.addTerms(terms)

# Make Vector
tone = -1
print probVector(tone, tvoc.getIndexes(terms))


