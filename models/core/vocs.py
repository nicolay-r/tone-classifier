# -*- coding: utf-8 -*-

import operator
import json
import io


class TermVocabulary:

    def __init__(self, filepath=""):
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
            print 'terms: %d' % (len(self.term_index))

    @staticmethod
    def to_unicode(s):
        if isinstance(s, str):
            return unicode(s, 'utf-8')
        elif isinstance(s, unicode):
            return s

    def get_terms(self):
        return self.term_index.keys()

    def get_term_index(self, term):
        unicode_term = TermVocabulary.to_unicode(term)
        return self.term_index[unicode_term]

    def get_term_in_voc_count(self, term):
        unicode_term = TermVocabulary.to_unicode(term)
        return self.term_in_voc_count[self.get_term_index(unicode_term)]

    def top(self, n):
        r = sorted(self.term_in_voc_count.items(),
                   key=operator.itemgetter(1))[::-1]
        print "top %d:" % (n)
        for i in range(min(len(self.term_in_voc_count), n)):
            for w, index in self.term_index.iteritems():
                if (index == r[i][0]):
                    print w, ', ',

    def get_indexes(self, terms):
        return [self.get_term_index(term) for term in terms]

    def get_new_index(self):
        self.current_index += 1
        return self.current_index

    def insert_term(self, term):
        unicode_term = TermVocabulary.to_unicode(term)
        if not(unicode_term in self.term_index):
            self.term_index[unicode_term] = self.get_new_index()
            self.term_in_voc_count[self.get_term_index(unicode_term)] = 1
        else:
            self.term_in_voc_count[self.get_term_index(unicode_term)] += 1

    def save(self, filepath):
        with io.open(filepath, 'w', encoding='utf-8') as out:
            data = json.dumps({
                              'term_index': self.term_index,
                              'current_index': self.current_index,
                              'term_in_voc_count': self.term_in_voc_count
                              }, ensure_ascii=False, encoding='utf8')
            out.write(unicode(data))


class DocVocabulary:

    def __init__(self):
        self.term_in_docs_count = {}
        self.docs_count = 0

    @staticmethod
    def to_unicode(s):
        if isinstance(s, str):
            return unicode(s, 'utf-8')
        elif isinstance(s, unicode):
            return s

    def get_docs_count(self):
        return self.docs_count

    def get_terms_in_docs_count(self):
        return self.term_in_docs_count

    def add_doc(self, terms):
        used = []
        self.docs_count += 1
        for term in terms:
            unicode_term = DocVocabulary.to_unicode(term)
            # update docs_count
            if not(unicode_term in used):
                if unicode_term in self.term_in_docs_count:
                    self.term_in_docs_count[unicode_term] += 1
                else:
                    self.term_in_docs_count[unicode_term] = 1
                used.append(unicode_term)

    def get_term_in_docs_count(self, term):
        unicode_term = DocVocabulary.to_unicode(term)
        return self.term_in_docs_count[unicode_term]

    def get_term_in_docs_count_safe(self, term):
        unicode_term = DocVocabulary.to_unicode(term)
        if (unicode_term in self.term_in_docs_count):
            return self.get_term_in_docs_count(unicode_term)
        else:
            return 0
