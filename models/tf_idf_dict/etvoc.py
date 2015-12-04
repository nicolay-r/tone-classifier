#/usr/bin/python
# -*- coding: utf-8 -*-

class ExtendedTermVocabulary:

    def get_docs_count(self):
        return self.docs_count

    def get_term_in_docs_count(self, term):
        if (term in self.doc_freq):
            return self.doc_freq[term]
        else:
            return 0

    def __init__(self, filename):
        self.doc_freq = {}
        with open(filename) as f:
            lines = f.readlines()
            self.docs_count = int(lines[0])
            print "edict count: ", len(lines[1:])
            for row in lines[1:]:
                word, count = row.split()
                self.doc_freq[word] = int(count)
