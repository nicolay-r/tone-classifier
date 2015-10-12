#!/usr/bin/python
class TermVocabulary:

        def getIndex(term):
                return d[term]

        def getIndexes(self, terms):
                indexes = []
                for term in terms:
                        indexes.append(self.d[term])
                return indexes

        def addTerms(self, terms):
                for term in terms:
                        if not(term in self.d):
                                self.d[term] = self.index
                                self.index += 1

        def __init__(self):
                self.d = {}
                self.index = 1
