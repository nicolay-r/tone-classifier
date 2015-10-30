#/usr/bin/python
class TermVocabulary:
    def getTermIndex(self, term):
        return self.term_ind[term]

    def getTermInDocsCount(self, term):
        return self.doc_count[term]

    def getTermInVocCount(self, term):
        return self.voc_count[term]

    def getDocsCount(self):
        return self.documents

    def getIndexes(self, terms):
        indexes = []
        for term in terms:
            indexes.append(self.term_ind[term])
        return indexes

    def df(self, term):
        'calculate df for a term'
        return self.getTermInDocsCount(term) *1.0 / self.getDocsCount()

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
                self.term_ind[term] = self.index
                self.index += 1
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
