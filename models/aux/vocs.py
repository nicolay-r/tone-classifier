#/usr/bin/python
# -*- coding: utf-8 -*-

import operator
import json
import io

# create WholeVocabulary
class TermVocabulary:

    def get_term_index(self, term):
        return self.term_index[term.decode('utf-8')]

    def get_term_in_voc_count(self, term):
        return self.term_in_voc_count[self.term_index[term]]

#    def top(self, n):
#        r = sorted(self.term_in_voc_count.items(),
#            key=operator.itemgetter(1))[::-1]
#        print "top %d:"%(n)
#        for i in range(min(len(self.term_in_voc_count), n)):
#            print r[i][0], ', ',

    def get_indexes(self, terms):
        return [self.term_index[term] for term in terms]

    def get_new_index(self):
        self.current_index += 1
        return self.current_index

    def insert_term(self, term):
        if not(term in self.term_index):
            self.term_index[term] = self.get_new_index()
            self.term_in_voc_count[self.term_index[term]] = 1
        else:
            self.term_in_voc_count[self.term_index[term]] += 1

    def __init__(self, filepath = ""):
        if (filepath == ""):
            self.term_index = {}
            self.term_in_voc_count = {}
            self.current_index = 0
        else:
            with io.open(filepath, 'r', encoding='utf-8') as f:
                voc = json.load(f, encoding='utf8')
            self.term_index = voc['term_index']
            self.current_index = voc['current_index']
            self.term_in_voc_count = voc['term_in_voc_count']
            print 'vocabulary loaded'
            print 'terms: %d'%(len(self.term_index))


    def save(self, filepath):
        with io.open(filepath, 'w', encoding='utf-8') as out:
            data = json.dumps( {
                'term_index': self.term_index,
                'current_index' : self.current_index,
                'term_in_voc_count' : self.term_in_voc_count
            }, ensure_ascii=False, encoding='utf8')
            out.write(unicode(data))

class DocVocabulary:
    def get_docs_count(self):
        return self.docs_count

    def add_doc(self, terms):
        used = []
        self.docs_count += 1
        for term in terms:
            # update docs_count
            if not(term in used):
                if term in self.term_in_docs_count:
                    self.term_in_docs_count[term] += 1
                else:
                    self.term_in_docs_count[term] = 1
                used.append(term)

    def get_term_in_docs_count(self, term):
        return self.term_in_docs_count[term]

    def __init__(self):
        self.term_in_docs_count = {}
        self.docs_count = 0
