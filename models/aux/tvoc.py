#/usr/bin/python

import operator

class TermVocabulary:
    def getTermIndex(self, term):
        return self.term_ind[term]

    def getTermInDocsCount(self, term):
        return self.doc_count[term]

    def getTermInVocCount(self, term):
        return self.voc_count[term]

    def getDocsCount(self):
        return self.documents

    def top(self, n):
        r = sorted(self.voc_count.items(),
            key=operator.itemgetter(1))[::-1]
        print "top %d:"%(n)
        for i in range(min(len(self.voc_count), n)):
            print r[i][0], ', ',

    def getIndexes(self, terms):
        indexes = []
        for term in terms:
            indexes.append(self.term_ind[term])
        return indexes

    def getNewIndex(self):
        result = self.index
        self.index += 1
        return result

    def add_feature(self, feature):
        if not(feature in self.term_ind):
            self.term_ind[feature] = self.getNewIndex()

    def add_doc(self, terms):
        used = []
        self.documents += 1
        for term in terms:
            # update voc_count
            if not(term in self.voc_count):
                self.voc_count[term] = 1
            else:
                self.voc_count[term] += 1
            # update term_ind
            if not(term in self.term_ind):
                self.term_ind[term] = self.getNewIndex()
            # update doc_count
            if not(term in used):
                if term in self.doc_count:
                    self.doc_count[term] += 1
                else:
                    self.doc_count[term] = 1
                used.append(term)

    def __init__(self):
        self.term_ind = {}
        self.voc_count = {}
        self.doc_count = {}
        self.documents = 0
        self.index = 1
